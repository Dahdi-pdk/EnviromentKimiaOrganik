from playwright.sync_api import sync_playwright
from datetime import datetime

WEBSITES = [
    "https://chatgpt.com",
    "https://claude.ai",
    "https://notebooklm.google.com",
    "https://github.com"
]

def log(message):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] {message}")

with sync_playwright() as p:

    log("Menjalankan Microsoft Edge...")

    browser = p.chromium.launch(
        channel="msedge",
        headless=False
    )

    context = browser.new_context()

    for i, url in enumerate(WEBSITES, start=1):

        log(f"[{i}/{len(WEBSITES)}] Membuka {url}")

        page = context.new_page()

        try:

            page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=60000
            )

            log("DOM selesai dibuat")

            page.wait_for_load_state("load")
            log("Semua resource utama selesai")

            page.wait_for_load_state("networkidle")
            log("Network Idle")

            title = page.title()

            log(f"Judul halaman : {title}")
            log("-" * 60)

        except Exception as e:

            log(f"Gagal membuka {url}")
            log(str(e))
            log("-" * 60)

    log("Semua website telah siap.")

    input("\nTekan ENTER untuk menutup browser...")

    browser.close()