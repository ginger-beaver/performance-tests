from clients.grpc.gateway.client_factory import GRPCClientFactory, build_gateway_grpc_client
from clients.grpc.gateway import (
    AccountsGatewayGRPCClient,
    CardsGatewayGRPCClient,
    OperationsGatewayGRPCClient,
    UsersGatewayGRPCClient
)

from clients.http.gateway.client_factory import HTTPClientFactory, build_gateway_http_client
from clients.http.gateway import (
    AccountsGatewayHTTPClient,
    CardsGatewayHTTPClient,
    OperationsGatewayHTTPClient,
    UsersGatewayHTTPClient
)

from seeds.schema.plan import (
    SeedsPlan,
    SeedUsersPlan,
    SeedAccountsPlan,
)
from seeds.schema.result import (
    SeedsResult,
    SeedUserResult,
    SeedCardResult,
    SeedAccountResult,
    SeedOperationResult
)


class SeedsBuilder:
    def __init__(
            self,
            users_gateway_client: UsersGatewayGRPCClient | UsersGatewayHTTPClient,
            cards_gateway_client: CardsGatewayGRPCClient | CardsGatewayHTTPClient,
            accounts_gateway_client: AccountsGatewayGRPCClient | AccountsGatewayHTTPClient,
            operations_gateway_client: OperationsGatewayGRPCClient | OperationsGatewayHTTPClient
    ):
        self.users_gateway_client = users_gateway_client
        self.cards_gateway_client = cards_gateway_client
        self.accounts_gateway_client = accounts_gateway_client
        self.operations_gateway_client = operations_gateway_client

    def build_physical_card_result(self, user_id: str, account_id: str) -> SeedCardResult:
        response = self.cards_gateway_client.issue_physical_card(
            user_id=user_id,
            account_id=account_id
        )
        return SeedCardResult(card_id=response.card.id)

    def build_top_up_operation_result(self, card_id: str, account_id: str) -> SeedOperationResult:
        response = self.operations_gateway_client.make_top_up_operation(
            card_id=card_id,
            account_id=account_id
        )
        return SeedOperationResult(operation_id=response.operation.id)

    def build_purchase_operation_result(self, card_id: str, account_id: str) -> SeedOperationResult:
        response = self.operations_gateway_client.make_purchase_operation(
            card_id=card_id,
            account_id=account_id
        )
        return SeedOperationResult(operation_id=response.operation.id)

    def build_savings_account_result(self, user_id: str) -> SeedAccountResult:
        response = self.accounts_gateway_client.open_savings_account(user_id=user_id)
        return SeedAccountResult(account_id=response.account.id)

    def build_deposit_account_result(self, user_id: str) -> SeedAccountResult:
        response = self.accounts_gateway_client.open_deposit_account(user_id=user_id)
        return SeedAccountResult(account_id=response.account.id)

    def build_debit_card_account_result(self, plan: SeedAccountsPlan, user_id: str) -> SeedAccountResult:
        response = self.accounts_gateway_client.open_debit_card_account(user_id=user_id)
        card_id = response.account.cards[0].id
        account_id = response.account.id

        return SeedAccountResult(
            account_id=response.account.id,
            physical_cards=[
                self.build_physical_card_result(user_id=user_id, account_id=response.account.id)
                for _ in range(plan.physical_cards.count)
            ],
            top_up_operations=[
                self.build_top_up_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.top_up_operations.count)
            ],
            purchase_operations=[
                self.build_purchase_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.purchase_operations.count)
            ]
        )

    def build_credit_card_account_result(self, plan: SeedAccountsPlan, user_id: str) -> SeedAccountResult:
        response = self.accounts_gateway_client.open_credit_card_account(user_id=user_id)
        card_id = response.account.cards[0].id
        account_id = response.account.id

        return SeedAccountResult(
            account_id=response.account.id,
            physical_cards=[
                self.build_physical_card_result(user_id=user_id, account_id=account_id)
                for _ in range(plan.physical_cards.count)
            ],
            top_up_operations=[
                self.build_top_up_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.top_up_operations.count)
            ],
            purchase_operations=[
                self.build_purchase_operation_result(card_id=card_id, account_id=account_id)
                for _ in range(plan.purchase_operations.count)
            ]
        )

    def build_user(self, plan: SeedUsersPlan) -> SeedUserResult:
        response = self.users_gateway_client.create_user()

        return SeedUserResult(
            user_id=response.user.id,
            savings_accounts=[
                self.build_savings_account_result(user_id=response.user.id)
                for _ in range(plan.savings_accounts.count)
            ],
            deposit_accounts=[
                self.build_deposit_account_result(user_id=response.user.id)
                for _ in range(plan.deposit_accounts.count)
            ],
            debit_card_accounts=[
                self.build_debit_card_account_result(plan=plan.debit_card_accounts, user_id=response.user.id)
                for _ in range(plan.debit_card_accounts.count)
            ],
            credit_card_accounts=[
                self.build_credit_card_account_result(plan=plan.credit_card_accounts, user_id=response.user.id)
                for _ in range(plan.credit_card_accounts.count)
            ]
        )

    def build(self, plan: SeedsPlan) -> SeedsResult:
        return SeedsResult(users=[self.build_user(plan=plan.users) for _ in range(plan.users.count)])


def build_grpc_seeds_builder() -> SeedsBuilder:
    grpc_factory = GRPCClientFactory(lambda: build_gateway_grpc_client())

    return SeedsBuilder(
        users_gateway_client=grpc_factory.create(UsersGatewayGRPCClient),
        cards_gateway_client=grpc_factory.create(CardsGatewayGRPCClient),
        accounts_gateway_client=grpc_factory.create(AccountsGatewayGRPCClient),
        operations_gateway_client=grpc_factory.create(OperationsGatewayGRPCClient)
    )


def build_http_seeds_builder():
    http_factory = HTTPClientFactory(lambda: build_gateway_http_client())

    return SeedsBuilder(
        users_gateway_client=http_factory.create(UsersGatewayHTTPClient),
        cards_gateway_client=http_factory.create(CardsGatewayHTTPClient),
        accounts_gateway_client=http_factory.create(AccountsGatewayHTTPClient),
        operations_gateway_client=http_factory.create(OperationsGatewayHTTPClient)
    )
