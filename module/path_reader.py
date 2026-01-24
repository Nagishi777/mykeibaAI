# ---------------------
# Path Reader Module
# This module reads file paths from a JSON configuration file.
# ---------------------

import json
from pathlib import Path

class PathReader:
    def __init__(self, config_file: str):
        self.config_file = Path(config_file)
        with open(self.config_file, "r", encoding="utf-8") as f:
            self.paths = json.load(f)

    def get_path(self, key: str) -> str:
        return self.paths.get(key, None)

# --- Example Usage ---
# インスタンスの実体化
# 引数にはfile_pathをまとめているjsonファイルのパスを指定する
# reader = PathReader("C:\\Users\\yasak\\デスクトップ\\Keiba_App\\mykeibaAI_ver1p0\\file_path.json")
# "Desktop_features"キーに対応するパスを取得
# desktop_features_path = reader.get_path("Desktop_features")

# print(desktop_features_path)
# ---------------------