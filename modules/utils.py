import os
import json


def format_page_number(page_num):
    """將頁數轉為三位數字串（如 12 -> 012）"""
    return f"{page_num:d}"


def ensure_dir(path):
    """確保資料夾存在"""
    if not os.path.exists(path):
        os.makedirs(path)


def load_env(env_path='.env'):
    """讀取 .env 檔取得圖片網址模板"""
    with open(env_path, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                return line.strip()
    raise ValueError('.env 檔案格式錯誤')


def load_cookies(cookie_path='cookie.json'):
    """讀取 cookie.json 並轉成 dict"""
    with open(cookie_path, 'r', encoding='utf-8') as f:
        cookies_list = json.load(f)
    return {cookie['name']: cookie['value'] for cookie in cookies_list}
