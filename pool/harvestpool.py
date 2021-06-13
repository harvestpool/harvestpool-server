import aiohttp
import json
from typing import Dict


class HarvestpoolClient():
    def __init__(self) -> None:
        pass

    async def handle_partial_submitted(self, partial: Dict, msg: Dict):
        harvestpool_msg = {"parital": partial, "msg": msg}
        json_data = json.dumps(harvestpool_msg)
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(f"https://harvestpool.farm/api/v1/submit/partial", data=json_data) as resp:
                    if resp.ok:
                        server_response: Dict = json.loads(await resp.text())
                        #self.farmer.log.info(f"Pool response: {pool_response}")
                        # if "error_code" in pool_response:
                        #     self.farmer.log.error(
                        #         f"Error in pooling: {pool_response['error_code'], pool_response['error_message']}"
                        #     )
                        #     pool_state_dict["pool_errors_24"].append(pool_response)
                        # else:
                        #     pool_state_dict["points_acknowledged_since_start"] += pool_state_dict[
                        #         "current_difficulty"
                        #     ]
                        #     pool_state_dict["points_acknowledged_24h"].append(
                        #         (time.time(), pool_state_dict["current_difficulty"])
                        #     )
                        #     pool_state_dict["current_difficulty"] = pool_response["current_difficulty"]
                        #     pool_state_dict["current_points_balance"] = pool_response["points_balance"]

                    else:
                        pass
                        # self.farmer.log.error(f"Error sending partial to {pool_url}, {resp.status}")
        except Exception as e:
            # self.farmer.log.error(f"Error connecting to pool: {e}")
            pass
