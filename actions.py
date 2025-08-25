import time


def run_bing_rewards(page, account):
    """Navigate to Bing and let the Rewards extension run for the given account.

    Args:
        page: Playwright page object for the browser.
        account: A dictionary or object containing account details.

    Returns:
        tuple: (status, message) summarizing the run.
    """
    # Navigate to Bing home page
    page.goto("https://www.bing.com/")
    # Wait for a few seconds to allow the extension to perform searches
    time.sleep(5)
    # TODO: Add additional checks/logging if needed
    return "success", "Extension executed"
