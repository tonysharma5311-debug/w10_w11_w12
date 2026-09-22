#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Miner Automation - W10, W11, W12 (Terminals 271-360 Only)
W10: 271-300 | W11: 301-330 | W12: 331-360
"""

import os
import sys
import subprocess
import time
import argparse
import psutil
from datetime import datetime
from typing import Optional

def auto_install_dependencies():
    required = ['requests', 'psutil', 'pillow']
    for package in required:
        try:
            if package == 'pillow':
                __import__('PIL')
            else:
                __import__(package)
            print(f"[OK] {package} already installed")
        except ImportError:
            print(f"[*] Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
            print(f"[OK] {package} installed")

auto_install_dependencies()

import requests
from PIL import ImageGrab

# ==================== TELEGRAM ====================
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "8670890083:AAFdQaEiC67jmk6l8jxxdG01NTEN4JxvPUc")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "6955911349")

class TelegramLogger:
    def __init__(self):
        self.base_url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"
    def send_message(self, message: str):
        try:
            requests.post(f"{self.base_url}/sendMessage", json={"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "HTML"}, timeout=10)
        except:
            pass
    def send_photo(self, image_path: str, caption: str):
        try:
            with open(image_path, 'rb') as f:
                requests.post(f"{self.base_url}/sendPhoto", files={'photo': f}, data={'chat_id': TELEGRAM_CHAT_ID, 'caption': caption, 'parse_mode': 'HTML'}, timeout=30)
            os.remove(image_path)
        except:
            pass

telegram = TelegramLogger()

# ==================== CONFIG ====================
FIREFOX_PATH = r"C:\Program Files\Mozilla Firefox\firefox.exe"
API_BASE = "https://api.unmineable.com/v5"
WALLET_ADDRESS = "nano_1g97x3h6wxd4h577p6dricapigs78ccc7tcowjfm67hewsmg7qob4xwc8jak"
COIN = "NANO"
BATCH_SIZE = 3
GAP_BETWEEN_BATCHES = 60
CHECK_INTERVAL = 360

# ==================== W10: TERMINALS 271-300 ====================
W10_TERMINALS = [
    [271, "Terminal 271", "rcpjfbr2y2gl3h23wut3uq", "https://ais-pre-rcpjfbr2y2gl3h23wut3uq-319779192587.asia-southeast1.run.app"],
    [272, "Terminal 272", "h57r6v62rz5eqbr25ai4nt", "https://ais-pre-h57r6v62rz5eqbr25ai4nt-319779192587.asia-southeast1.run.app"],
    [273, "Terminal 273", "vpu46qauhykc2ukb6eplvd", "https://ais-pre-vpu46qauhykc2ukb6eplvd-319779192587.asia-southeast1.run.app"],
    [274, "Terminal 274", "dak7unleyqf7egd6evvzpz", "https://ais-pre-dak7unleyqf7egd6evvzpz-319779192587.asia-southeast1.run.app"],
    [275, "Terminal 275", "umliugf4g2bu45jhls5sva", "https://ais-pre-umliugf4g2bu45jhls5sva-319779192587.asia-southeast1.run.app"],
    [276, "Terminal 276", "mkfaxxuj2jgelcj73o7lmq", "https://ais-pre-mkfaxxuj2jgelcj73o7lmq-319779192587.asia-southeast1.run.app"],
    [277, "Terminal 277", "js56tmupdot76ujdopivh3", "https://ais-pre-js56tmupdot76ujdopivh3-319779192587.asia-southeast1.run.app"],
    [278, "Terminal 278", "qhul27vggsrikcxgl7gcd5", "https://ais-pre-qhul27vggsrikcxgl7gcd5-319779192587.asia-southeast1.run.app"],
    [279, "Terminal 279", "ry6cvkg6velruipbkmexdd", "https://ais-pre-ry6cvkg6velruipbkmexdd-319779192587.asia-southeast1.run.app"],
    [280, "Terminal 280", "hokxijhycvcuftksoejo6x", "https://ais-pre-hokxijhycvcuftksoejo6x-319779192587.asia-southeast1.run.app"],
    [281, "Terminal 281", "4x2l7ndgqoaak2gnin6t4u", "https://ais-pre-4x2l7ndgqoaak2gnin6t4u-319779192587.asia-southeast1.run.app"],
    [282, "Terminal 282", "vhmz3cvbnekqy55s6jcokz", "https://ais-pre-vhmz3cvbnekqy55s6jcokz-319779192587.asia-southeast1.run.app"],
    [283, "Terminal 283", "ec6iili2e57tsbenl33kdk", "https://ais-pre-ec6iili2e57tsbenl33kdk-319779192587.asia-southeast1.run.app"],
    [284, "Terminal 284", "vizuuraeim2kuh7klp5ls6", "https://ais-pre-vizuuraeim2kuh7klp5ls6-319779192587.asia-southeast1.run.app"],
    [285, "Terminal 285", "6jvgsg6pn6qtcdktlc4p6u", "https://ais-pre-6jvgsg6pn6qtcdktlc4p6u-319779192587.asia-southeast1.run.app"],
    [286, "Terminal 286", "qhsgmcl5b3x65xwusvbtf6", "https://ais-pre-qhsgmcl5b3x65xwusvbtf6-319779192587.asia-southeast1.run.app"],
    [287, "Terminal 287", "ei4mb6vjxa3vtwelfwg2ik", "https://ais-pre-ei4mb6vjxa3vtwelfwg2ik-319779192587.asia-southeast1.run.app"],
    [288, "Terminal 288", "7l35eufacj63f5yuimxkh6", "https://ais-pre-7l35eufacj63f5yuimxkh6-319779192587.asia-southeast1.run.app"],
    [289, "Terminal 289", "m5d6cnqegyzjxthaqmug6n", "https://ais-pre-m5d6cnqegyzjxthaqmug6n-319779192587.asia-southeast1.run.app"],
    [290, "Terminal 290", "cvnwlugfvdk3dcdvfbfziy", "https://ais-pre-cvnwlugfvdk3dcdvfbfziy-319779192587.asia-southeast1.run.app"],
    [291, "Terminal 291", "z42g7z4utkd4shhqrsdt6g", "https://ais-pre-z42g7z4utkd4shhqrsdt6g-319779192587.asia-southeast1.run.app"],
    [292, "Terminal 292", "fsg2qwfwwh6ilofvlqe2vu", "https://ais-pre-fsg2qwfwwh6ilofvlqe2vu-319779192587.asia-southeast1.run.app"],
    [293, "Terminal 293", "sdsv5e65mjoqsxictszoiy", "https://ais-pre-sdsv5e65mjoqsxictszoiy-319779192587.asia-southeast1.run.app"],
    [294, "Terminal 294", "nbymjj6pcet2h5lvpi4xqe", "https://ais-pre-nbymjj6pcet2h5lvpi4xqe-319779192587.asia-southeast1.run.app"],
    [295, "Terminal 295", "ummt6pctyjbfuphitk6hpa", "https://ais-pre-ummt6pctyjbfuphitk6hpa-319779192587.asia-southeast1.run.app"],
    [296, "Terminal 296", "evsjqxf5mrmghgvbkbfojo", "https://ais-pre-evsjqxf5mrmghgvbkbfojo-319779192587.asia-southeast1.run.app"],
    [297, "Terminal 297", "255xkdk6gwsqgusmfegcfz", "https://ais-pre-255xkdk6gwsqgusmfegcfz-319779192587.asia-southeast1.run.app"],
    [298, "Terminal 298", "7nyf3gzhgjrovqbdndsqk2", "https://ais-pre-7nyf3gzhgjrovqbdndsqk2-319779192587.asia-southeast1.run.app"],
    [299, "Terminal 299", "wuvuaadtdklvcelau2l24a", "https://ais-pre-wuvuaadtdklvcelau2l24a-319779192587.asia-southeast1.run.app"],
    [300, "Terminal 300", "4f4qrks3kt5oefjjiylgyf", "https://ais-pre-4f4qrks3kt5oefjjiylgyf-319779192587.asia-southeast1.run.app"],
]

# ==================== W11: TERMINALS 301-330 (UPDATED) ====================
W11_TERMINALS = [
    [301, "Terminal 301", "gg7gsr6654phfifhphp3oq", "https://ais-pre-gg7gsr6654phfifhphp3oq-738426852972.asia-east1.run.app"],
    [302, "Terminal 302", "ha7y537pkrqqf6eicboc6m", "https://ais-pre-ha7y537pkrqqf6eicboc6m-738426852972.asia-east1.run.app"],
    [303, "Terminal 303", "r5yu5giaeco5aaygo4ihlg", "https://ais-pre-r5yu5giaeco5aaygo4ihlg-738426852972.asia-east1.run.app"],
    [304, "Terminal 304", "bgx5scxvanjtj7uo2b6bhd", "https://ais-pre-bgx5scxvanjtj7uo2b6bhd-738426852972.asia-east1.run.app"],
    [305, "Terminal 305", "enp4zhu2pvuoe2u6k6c2ft", "https://ais-pre-enp4zhu2pvuoe2u6k6c2ft-738426852972.asia-east1.run.app"],
    [306, "Terminal 306", "ksjcktdujxticlqntffhjc", "https://ais-pre-ksjcktdujxticlqntffhjc-738426852972.asia-east1.run.app"],
    [307, "Terminal 307", "7xlxx3iabilr62g3y67i7b", "https://ais-pre-7xlxx3iabilr62g3y67i7b-738426852972.asia-east1.run.app"],
    [308, "Terminal 308", "25mqlmiydevu45xi2mkkki", "https://ais-pre-25mqlmiydevu45xi2mkkki-738426852972.asia-east1.run.app"],
    [309, "Terminal 309", "blsjqzuucm22rrbzlyabuz", "https://ais-pre-blsjqzuucm22rrbzlyabuz-738426852972.asia-east1.run.app"],
    [310, "Terminal 310", "iuig5fslnlkpjkikapl4nk", "https://ais-pre-iuig5fslnlkpjkikapl4nk-738426852972.asia-east1.run.app"],
    [311, "Terminal 311", "4lwmmasa5fuooeu6bxvaka", "https://ais-pre-4lwmmasa5fuooeu6bxvaka-738426852972.asia-east1.run.app"],
    [312, "Terminal 312", "37al5iieskmst6tq24lbjd", "https://ais-pre-37al5iieskmst6tq24lbjd-738426852972.asia-east1.run.app"],
    [313, "Terminal 313", "c2jv6xvdgt6oqlsjrvuduf", "https://ais-pre-c2jv6xvdgt6oqlsjrvuduf-738426852972.asia-east1.run.app"],
    [314, "Terminal 314", "bk3l5d23jimwzwkpdeqibe", "https://ais-pre-bk3l5d23jimwzwkpdeqibe-738426852972.asia-east1.run.app"],
    [315, "Terminal 315", "u4bvkixs4e5knzfqzkctdp", "https://ais-pre-u4bvkixs4e5knzfqzkctdp-738426852972.asia-east1.run.app"],
    [316, "Terminal 316", "d6sorr5ccuplr4sjkolynp", "https://ais-pre-d6sorr5ccuplr4sjkolynp-738426852972.asia-east1.run.app"],
    [317, "Terminal 317", "6unl3myd3qrkjwibavbhzf", "https://ais-pre-6unl3myd3qrkjwibavbhzf-738426852972.asia-east1.run.app"],
    [318, "Terminal 318", "jq5gkd7xwnnzg3khnem7nv", "https://ais-pre-jq5gkd7xwnnzg3khnem7nv-738426852972.asia-east1.run.app"],
    [319, "Terminal 319", "ko43jvcjhit3yjkdun4rod", "https://ais-pre-ko43jvcjhit3yjkdun4rod-738426852972.asia-east1.run.app"],
    [320, "Terminal 320", "u36wkcrj3rnifxwsmgyksz", "https://ais-pre-u36wkcrj3rnifxwsmgyksz-738426852972.asia-east1.run.app"],
    [321, "Terminal 321", "wt4lgu7mr64fwae562vets", "https://ais-pre-wt4lgu7mr64fwae562vets-738426852972.asia-east1.run.app"],
    [322, "Terminal 322", "i5qeafkmqtow4mwuzaqjwg", "https://ais-pre-i5qeafkmqtow4mwuzaqjwg-738426852972.asia-east1.run.app"],
    [323, "Terminal 323", "tzpqk4t3eu72cspqnx5qzm", "https://ais-pre-tzpqk4t3eu72cspqnx5qzm-738426852972.asia-east1.run.app"],
    [324, "Terminal 324", "7dngksona4643bvjxcl57l", "https://ais-pre-7dngksona4643bvjxcl57l-738426852972.asia-east1.run.app"],
    [325, "Terminal 325", "rdo366vltmt22mg6f67bb6", "https://ais-pre-rdo366vltmt22mg6f67bb6-738426852972.asia-east1.run.app"],
    [326, "Terminal 326", "bctrrkfw7tcnbgeuyhenhh", "https://ais-pre-bctrrkfw7tcnbgeuyhenhh-738426852972.asia-east1.run.app"],
    [327, "Terminal 327", "rnyxzwqhf2rhb3ltdwjxqz", "https://ais-pre-rnyxzwqhf2rhb3ltdwjxqz-738426852972.asia-east1.run.app"],
    [328, "Terminal 328", "col4ym3srrgcid2veausnl", "https://ais-pre-col4ym3srrgcid2veausnl-738426852972.asia-east1.run.app"],
    [329, "Terminal 329", "up6tzhjwlyw3q2z3q6qvk5", "https://ais-pre-up6tzhjwlyw3q2z3q6qvk5-738426852972.asia-east1.run.app"],
    [330, "Terminal 330", "2okzaqxndkxiggpuysdah6", "https://ais-pre-2okzaqxndkxiggpuysdah6-738426852972.asia-east1.run.app"],
]

# ==================== W12: TERMINALS 331-360 ====================
W12_TERMINALS = [
    [331, "Terminal 331", "dago4fy4mff4z5ec33tg7z", "https://ais-pre-dago4fy4mff4z5ec33tg7z-305664602043.asia-east1.run.app"],
    [332, "Terminal 332", "ni4aimv7vx6x2ksfvthwy6", "https://ais-pre-ni4aimv7vx6x2ksfvthwy6-305664602043.asia-east1.run.app"],
    [333, "Terminal 333", "w5ks7423b46kofplrxbrqj", "https://ais-pre-w5ks7423b46kofplrxbrqj-305664602043.asia-east1.run.app"],
    [334, "Terminal 334", "akvndtcjkbeq6rjxufcwha", "https://ais-pre-akvndtcjkbeq6rjxufcwha-305664602043.asia-east1.run.app"],
    [335, "Terminal 335", "472zevyb44xb4xjxmyn66l", "https://ais-pre-472zevyb44xb4xjxmyn66l-305664602043.asia-east1.run.app"],
    [336, "Terminal 336", "rrnycef7owjusdee4ltrvj", "https://ais-pre-rrnycef7owjusdee4ltrvj-305664602043.asia-east1.run.app"],
    [337, "Terminal 337", "l2v2iipoejrm7c6xnqms3i", "https://ais-pre-l2v2iipoejrm7c6xnqms3i-305664602043.asia-east1.run.app"],
    [338, "Terminal 338", "tid3gc65bdhe43c6s3susd", "https://ais-pre-tid3gc65bdhe43c6s3susd-305664602043.asia-east1.run.app"],
    [339, "Terminal 339", "f3wocmcthuk2gtb2rk3b35", "https://ais-pre-f3wocmcthuk2gtb2rk3b35-305664602043.asia-east1.run.app"],
    [340, "Terminal 340", "s3fxdd2ykgyqxdq6haxpk5", "https://ais-pre-s3fxdd2ykgyqxdq6haxpk5-305664602043.asia-east1.run.app"],
    [341, "Terminal 341", "rinytgpmago6tg3coj2xon", "https://ais-pre-rinytgpmago6tg3coj2xon-305664602043.asia-east1.run.app"],
    [342, "Terminal 342", "f2o33wtxy4xbap5logpkbb", "https://ais-pre-f2o33wtxy4xbap5logpkbb-305664602043.asia-east1.run.app"],
    [343, "Terminal 343", "qrsbyzdwfpmmhg6q3vgiyx", "https://ais-pre-qrsbyzdwfpmmhg6q3vgiyx-305664602043.asia-east1.run.app"],
    [344, "Terminal 344", "dvwg4bndbyvmacixp4a5fi", "https://ais-pre-dvwg4bndbyvmacixp4a5fi-305664602043.asia-east1.run.app"],
    [345, "Terminal 345", "yjkbtstf5rb4l7irmumy2w", "https://ais-pre-yjkbtstf5rb4l7irmumy2w-305664602043.asia-east1.run.app"],
    [346, "Terminal 346", "pim3tdt42oem553e7ji6od", "https://ais-pre-pim3tdt42oem553e7ji6od-305664602043.asia-east1.run.app"],
    [347, "Terminal 347", "mmnsvjeawb57t27iwca2go", "https://ais-pre-mmnsvjeawb57t27iwca2go-305664602043.asia-east1.run.app"],
    [348, "Terminal 348", "klkks7noxv42ybyugjldhu", "https://ais-pre-klkks7noxv42ybyugjldhu-305664602043.asia-east1.run.app"],
    [349, "Terminal 349", "f25mjco5npw3j2tz3zn5e5", "https://ais-pre-f25mjco5npw3j2tz3zn5e5-305664602043.asia-east1.run.app"],
    [350, "Terminal 350", "fahzmtptfbgtdzdm5auyuj", "https://ais-pre-fahzmtptfbgtdzdm5auyuj-305664602043.asia-east1.run.app"],
    [351, "Terminal 351", "cvaccsale7kbacmpzqywbb", "https://ais-pre-cvaccsale7kbacmpzqywbb-305664602043.asia-east1.run.app"],
    [352, "Terminal 352", "kith4hfpulio2bfabobk6n", "https://ais-pre-kith4hfpulio2bfabobk6n-305664602043.asia-east1.run.app"],
    [353, "Terminal 353", "v5xhkx3rtct4t5zvu6a3w5", "https://ais-pre-v5xhkx3rtct4t5zvu6a3w5-305664602043.asia-east1.run.app"],
    [354, "Terminal 354", "y6d4rood5taanh4wsi6yl4", "https://ais-pre-y6d4rood5taanh4wsi6yl4-305664602043.asia-east1.run.app"],
    [355, "Terminal 355", "em55fzdwtnord5xin5oa5b", "https://ais-pre-em55fzdwtnord5xin5oa5b-305664602043.asia-east1.run.app"],
    [356, "Terminal 356", "ilay2rkju7mcox2kayyllp", "https://ais-pre-ilay2rkju7mcox2kayyllp-305664602043.asia-east1.run.app"],
    [357, "Terminal 357", "bvdt3cq4dyhcwbgrjk5xtx", "https://ais-pre-bvdt3cq4dyhcwbgrjk5xtx-305664602043.asia-east1.run.app"],
    [358, "Terminal 358", "la3n6ywdoyu5tab26smmay", "https://ais-pre-la3n6ywdoyu5tab26smmay-305664602043.asia-east1.run.app"],
    [359, "Terminal 359", "25mjexdkf6auqgggbtjo7f", "https://ais-pre-25mjexdkf6auqgggbtjo7f-305664602043.asia-east1.run.app"],
    [360, "Terminal 360", "yycbv4rptoqq2jcwa7verh", "https://ais-pre-yycbv4rptoqq2jcwa7verh-305664602043.asia-east1.run.app"],
]

# ==================== FUNCTIONS ====================
def log(msg): print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")
def send_tg(title, msg, emoji="📘"): telegram.send_message(f"{emoji} <b>{title}</b>\n{msg}")
def get_system_info():
    try:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        return f"CPU: {cpu}% | RAM: {ram.used/(1024**3):.1f}/{ram.total/(1024**3):.1f}GB ({ram.percent}%)"
    except:
        return "N/A"

def take_screenshot(filename="screenshot.png"):
    try:
        screenshot = ImageGrab.grab()
        screenshot.save(filename)
        return filename
    except:
        return None

def get_uuid():
    try:
        r = requests.get(f"{API_BASE}/address/{WALLET_ADDRESS}?coin={COIN}", headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
        return r.json().get('data', {}).get('uuid')
    except:
        return None

def check_status(miner_name, uuid):
    try:
        r = requests.get(f"{API_BASE}/account/{uuid}/workers", headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
        workers = r.json().get('data', {}).get('randomx', {}).get('workers', [])
        for w in workers:
            if w.get('name') == miner_name:
                return w.get('online', False)
        return False
    except:
        return False

def open_window(url, name):
    try:
        subprocess.Popen([FIREFOX_PATH, "-new-window", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except:
        return False

def close_window(miner_name):
    try:
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            if proc.info['name'] == 'firefox.exe' and miner_name in str(proc.info['cmdline']):
                proc.terminate()
                return True
    except:
        pass
    return False

def run_workflow(terminals, workflow_name):
    if not os.path.exists(FIREFOX_PATH):
        send_tg("ERROR", "Firefox not found!", "❌")
        return
    
    total = len(terminals)
    batches = (total + BATCH_SIZE - 1) // BATCH_SIZE
    
    log(f"{workflow_name} Started | Total: {total}")
    send_tg("WORKFLOW STARTED", f"{workflow_name}\nTotal: {total}\n{get_system_info()}", "🚀")
    
    uuid = get_uuid()
    if not uuid:
        send_tg("ERROR", "Failed to get UUID!", "❌")
        return
    
    # Open first batch (for screenshot)
    log("Opening BATCH 1...")
    first_batch = terminals[0:BATCH_SIZE]
    for m in first_batch:
        open_window(m[3], m[1])
        time.sleep(2)
    
    time.sleep(30)
    ss = take_screenshot(f"screenshot_{workflow_name.replace(' ', '_')}.png")
    if ss:
        caption = f"📸 BATCH 1 SCREENSHOT\n{workflow_name}\n{get_system_info()}"
        telegram.send_photo(ss, caption)
    
    time.sleep(GAP_BETWEEN_BATCHES)
    
    # Open remaining batches
    for b in range(1, batches):
        start = b * BATCH_SIZE
        end = min(start + BATCH_SIZE, total)
        for m in terminals[start:end]:
            open_window(m[3], m[1])
            time.sleep(2)
        if end < total:
            time.sleep(GAP_BETWEEN_BATCHES)
    
    log("All terminals opened!")
    send_tg("ALL OPENED", f"All {total} terminals opened!\n{get_system_info()}", "✅")
    
    # Monitoring loop
    while True:
        time.sleep(CHECK_INTERVAL)
        offline, online = [], 0
        for m in terminals:
            if check_status(m[2], uuid):
                online += 1
            else:
                offline.append(m)
        
        if offline:
            send_tg(f"STATUS - {len(offline)} OFFLINE", f"{workflow_name}: {online}/{total} ONLINE\n{get_system_info()}", "⚠️")
            for m in offline:
                close_window(m[2])
                time.sleep(2)
                open_window(m[3], m[1])
                time.sleep(3)
            send_tg("RESTART COMPLETE", f"Restarted {len(offline)} miners", "✅")
        else:
            send_tg("STATUS - ALL ONLINE", f"{workflow_name}: {online}/{total} ONLINE (100%)\n{get_system_info()}", "✅")

# ==================== MAIN ====================
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--workflow', type=str, default='W10')
    args = parser.parse_args()
    
    if args.workflow == 'W10':
        run_workflow(W10_TERMINALS, "W10 (271-300)")
    elif args.workflow == 'W11':
        run_workflow(W11_TERMINALS, "W11 (301-330)")
    elif args.workflow == 'W12':
        run_workflow(W12_TERMINALS, "W12 (331-360)")
    else:
        print("Use --workflow W10, W11, or W12")
