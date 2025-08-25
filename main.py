from config_manager import SheetManager
from browser_handler import launch_browser
from actions import run_bing_rewards


def main():
    """Entry point for running Bing Rewards automation."""
    manager = SheetManager("credentials.json", "BingRewards")
    accounts = manager.read_accounts()

    for _, acc in accounts.iterrows():
        try:
            playwright, context, page = launch_browser(
                profile_path=f"chrome_profiles/{acc['profile_name']}",
                extension_path="path/to/RewardsSearchAutomator"
            )
            status, message = run_bing_rewards(page, acc)
            manager.log_run(acc["account_id"], status, message)
        except Exception as e:
            manager.log_run(acc["account_id"], "failed", str(e))
        finally:
            context.close()
            playwright.stop()


if __name__ == "__main__":
    main()
