from abc import ABC, abstractmethod
from typing import Callable

from seeds.builder import SeedsBuilder
from seeds.dumps import save_seeds_result, load_seeds_result
from seeds.schema.plan import SeedsPlan
from seeds.schema.result import SeedsResult


class SeedsScenario(ABC):

    def __init__(self, seeder_builder_func):
        self.seeder_builder_func: Callable[[], SeedsBuilder] = seeder_builder_func

    @property
    @abstractmethod
    def plan(self) -> SeedsPlan:
        ...

    @property
    @abstractmethod
    def scenario(self) -> str:
        ...

    def save(self, result: SeedsResult) -> None:
        save_seeds_result(result=result, scenario=self.scenario)

    def load(self) -> SeedsResult:
        return load_seeds_result(scenario=self.scenario)

    def build(self) -> None:
        seeder_builder = self.seeder_builder_func()
        result = seeder_builder.build(self.plan)
        self.save(result)
