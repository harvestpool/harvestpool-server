from typing import Any, Dict, List, Optional, Tuple

from chia.util.default_root import DEFAULT_ROOT_PATH
from chia.util.config import (
    create_default_chia_config,
    initial_config_file,
    load_config,
    save_config,
    unflatten_properties,
)


def init():
    config: Dict = load_config(DEFAULT_ROOT_PATH, "config.yaml")

    config['pool_server']['pool_url'] = 'http://pool.harvestpool.farm'

    config["pool_server"]['pool_target_puzzle_hash'] = "txch1478upmu9hex8asj773agz4qc7apmrt34dcj38t6am8qva096w35q38a4pm"
    config["pool_server"]["pool_target_fingerprint"] = 1150743361
    config["pool_server"]["wallet_id"] = "1"

    config["pool_server"]["pool_fee_puzzle_hash"] = "txch1qmevcjz9hjmxw5sm9pmy79d5x6l9clc0g7le4dpjxk6f6508v5wsk8j4uf"

    save_config(DEFAULT_ROOT_PATH, "config.yaml", config)


if __name__ == "__main__":
    init()
