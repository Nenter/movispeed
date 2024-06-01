from playwright.sync_api import sync_playwright
"""
Se necesita playwright libreria:
!#/bin/bash
sudo apt install python3
sudo pip3 install playwright
"""
def run(playwright):
    browser = playwright.chromium.launch(
        headless=False, #False muestra ventana. True oculta.
        args =['--ignore-certificate-errors'],
    )
    context = browser.new_context()
    page = context.new_page()

    try:
        page.goto('https://movispeed.es/movispeed/', wait_until="domcontentloaded")
    except playwright._impl._errors.TimeoutError:
        pass
    page.evaluate('iniciarTest()')

    limit_loops=30

    for i in range(limit_loops):
        print(f"Esperant...{i}/{limit_loops}")

        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(1000)

        total_download_mbps=page.locator('#textoIzquierda').inner_html()
        total_upload_mbps=page.locator('#textoDerecha').inner_html()
        
        if float(total_download_mbps) > 0 and float (total_upload_mbps)>0:
            break
    else:
        print ("No s'ha pogut obtindre la velocitat.")
        return False, None, None

    context.close()
    browser.close()

    return True, total_download_mbps,total_upload_mbps

with sync_playwright() as playwright:
    success, total_download_mbps,total_upload_mbps = run (playwright)

    print("success: ", success)
    print("Download: ", total_download_mbps," Mbps")
    print("Upload ", total_upload_mbps," Mbps")
