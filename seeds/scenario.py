import logging
from abc import ABC, abstractmethod
from typing import Callable

from seeds.builder import SeedsBuilder
from seeds.dumps import save_seeds_result, load_seeds_result
from seeds.schema.plan import SeedsPlan
from seeds.schema.result import SeedsResult

logger = logging.getLogger("SEEDS_SCENARIO")


class SeedsScenario(ABC):

    def __init__(self, seeder_builder_func: Callable[[], SeedsBuilder]):
        self.seeder_builder: SeedsBuilder = seeder_builder_func()

    @property
    @abstractmethod
    def plan(self) -> SeedsPlan:
        ...

    @property
    @abstractmethod
    def scenario(self) -> str:
        ...

    def save(self, result: SeedsResult) -> None:
        logger.info(f"[{self.scenario}] Saving seeding result to file.")
        save_seeds_result(result=result, scenario=self.scenario)
        logger.info(f"[{self.scenario}] Seeding result saved successfully.")

    def load(self) -> SeedsResult:
        logger.info(f"[{self.scenario}] Loading seeding result from file.")
        result = load_seeds_result(scenario=self.scenario)
        logger.info(f"[{self.scenario}] Seeding result loaded successfully.")
        return result

    def build(self) -> None:
        plan_json = self.plan.model_dump_json(indent=2, exclude_defaults=True)
        logger.info(f"[{self.scenario}] Starting seeding data generation for plan: {plan_json}")
        result = self.seeder_builder.build(self.plan)
        logger.info(f"[{self.scenario}] Seeding data generation completed.")
        self.save(result)
