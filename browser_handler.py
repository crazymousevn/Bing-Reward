from playwright.sync_api import sync_playwright


def launch_browser(profile_path: str, extension_path: str):
    playwright = sync_playwright().start()
    context = playwright.chromium.launch_persistent_context(
        user_data_dir=profile_path,
        headless=False,
        args=[
            f"--disable-extensions-except={extension_path}",
            f"--load-extension={extension_path}"
        ]
    )
    page = context.new_page()
    return playwright, context, page
