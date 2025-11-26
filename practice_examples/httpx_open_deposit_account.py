import time

import httpx

client = httpx.Client(base_url="http://localhost:8003")

payload = {
    "email": f"{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

create_user_response = client.post("/api/v1/users", json=payload)
create_user_response_data = create_user_response.json()

user_id = create_user_response_data["user"]["id"]

open_deposit_account_response = client.post("/api/v1/accounts/open-deposit-account", json={"userId": user_id})
open_deposit_account_response_data = open_deposit_account_response.json()

print(open_deposit_account_response.status_code)
print(open_deposit_account_response_data)
