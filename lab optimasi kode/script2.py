import subprocess
import time
import requests
from playwright.sync_api import sync_playwright

EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

EDGE_ARGS = [
    EDGE_PATH,
    "--remote-debugging-port=9222",
    "--new-window"
]

print("Menjalankan Microsoft Edge...")

subprocess.Popen(EDGE_ARGS)

# Menunggu sampai CDP aktif
for i in range(30):
    try:
        requests.get("http://127.0.0.1:9222/json/version", timeout=1)
        print("CDP siap.")
        break
    except:
        time.sleep(1)
else:
    raise RuntimeError("Microsoft Edge gagal membuka Remote Debugging.")

with sync_playwright() as p:

    browser = p.chromium.connect_over_cdp(
        "http://127.0.0.1:9222"
    )

    context = browser.contexts[0]

    page = context.new_page()

    page.goto(
        "https://chatgpt.com",
        wait_until="networkidle"
    )

    print("ChatGPT siap.")

    input("Tekan ENTER...")