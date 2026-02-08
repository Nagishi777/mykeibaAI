# ---------------------
# Get HTML Module
# This module gets html code from netkeiba.com.
# ---------------------

import os
import time
import random
import requests
from module.random_agent import RandomUserAgent

class GetHTML:
    def __init__(self, timeout: int = 10, min_sleep: float = 0.8, max_sleep: float = 2.0, ua: RandomUserAgent = RandomUserAgent()):
        self.timeout = timeout
        self.min_sleep = min_sleep
        self.max_sleep = max_sleep
        self.ua = RandomUserAgent()

    def get_and_save(self, url: str, save_path: str):
        """
        指定URLからHTMLを取得し、指定パスに保存する
        url: 取得先URL
        save_path: 保存先ファイルパス(.bin形式)
        """
        if os.path.exists(save_path):
            print(f"[Skip] Existing bin file: {save_path}")
            return # 既にそのURLが取得済みならスキップ
        else:
            try:
                res = requests.get(url, headers={"User-Agent": self.ua.get_user_agent()}, timeout=self.timeout)
                res.raise_for_status()  # エラーがあれば例外を発生

                # HTMLをバイナリで保存
                with open(save_path, "wb") as f:
                    f.write(res.content)

                # アクセス間隔を少し空ける（サーバー負荷対策）
                time.sleep(random.uniform(self.min_sleep, self.max_sleep))

            except Exception as e:
                print(f"[ERROR] Failed to fetch {url}: {e}")