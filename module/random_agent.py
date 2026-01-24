# ---------------------
# User Agent Module
# This module generates user agent randomly.
# ---------------------

import random

class RandomUserAgent:
    def __init__(self):
        # 利用可能なUserAgent一覧
        self.user_agents = [
            # Windows Chrome 系
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edg/121.0.2277.83 Safari/537.36",
            # macOS Chrome 系
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        ]
        # インスタンス化時点でランダムに選択
        self.user_agent = random.choice(self.user_agents)

    def get_user_agent(self) -> str:
        """選ばれたUserAgentを返す"""
        return self.user_agent