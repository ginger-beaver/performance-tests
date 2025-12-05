import logging
import os

from seeds.schema.result import SeedsResult

logger = logging.getLogger("SEEDS_DUMPS")


def save_seeds_result(result: SeedsResult, scenario: str):
    if not os.path.exists("dumps"):
        os.mkdir("dumps")

    file_path = f"./dumps/{scenario}_seeds.json"
    with open(file_path, "w+", encoding="utf-8") as file:
        file.write(result.model_dump_json())

    logger.info(f"Seeding result saved to file: {file_path}")


def load_seeds_result(scenario: str) -> SeedsResult:
    file_path = f"./dumps/{scenario}_seeds.json"
    with open(file_path, "r", encoding="utf-8") as file:
        result = SeedsResult.model_validate_json(file.read())

    logger.info(f"Seeding result loaded from file: {file_path}")
    return result
