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

    config["pool_server"]["pool_info"]["default_res"] = "Harvestpool.farm"
    config["pool_server"]["pool_info"]["name"] = "Harvestpool.farm"
    config["pool_server"]["pool_info"]["logo_url"] = "https://harvestpool.farm/img/Canada.png"
    config["pool_server"]["pool_info"]["description"] = "Canadian Chia farming pool with 1% fee and advanced user interface."
    config["pool_server"]["pool_fee"] = 0.01
    config["pool_server"]["min_difficulty"] = 10
    config["pool_server"]["default_difficulty"] = 10

    config['pool_server']['pool_url'] = 'http://pool.harvestpool.farm'
    config["pool_server"]['pool_target_puzzle_hash'] = "txch1478upmu9hex8asj773agz4qc7apmrt34dcj38t6am8qva096w35q38a4pm"
    config["pool_server"]["pool_target_fingerprint"] = 1150743361
    config["pool_server"]["wallet_id"] = "1"
    config["pool_server"]["pool_fee_puzzle_hash"] = "txch1qmevcjz9hjmxw5sm9pmy79d5x6l9clc0g7le4dpjxk6f6508v5wsk8j4uf"

    config["pool_server"]["partial_time_limit"] = 25
    config["pool_server"]["partial_confirmation_delay"] = 30
    config["pool_server"]["scan_start_height"] = 1000
    config["pool_server"]["collect_pool_rewards_interval"] = 600
    config["pool_server"]["confirmation_security_threshold"] = 6
    config["pool_server"]["payment_interval"] = 600
    config["pool_server"]["max_additions_per_transaction"] = 400
    config["pool_server"]["number_of_partials_target"] = 100

    save_config(DEFAULT_ROOT_PATH, "config.yaml", config)


if __name__ == "__main__":
    init()
