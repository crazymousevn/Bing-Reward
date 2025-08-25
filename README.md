# Bing-Reward Automation

This project automates earning Microsoft Rewards points via Bing search using Playwright and optionally the Rewards Search Automator extension.

## Features

- Reads account information from a Google Sheet using the Sheets API.
- Launches Chrome with persistent profiles and the Rewards Search Automator extension for each account.
- Performs Bing searches to earn daily points.
- Logs status and messages back to Google Sheets for tracking.
- Modular architecture with separate modules for configuration, browser handling, actions, and the main orchestrator.
- Phase 1 uses the Rewards Search Automator extension; Phase 2 will implement custom search logic.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/crazymousevn/Bing-Reward.git
   cd Bing-Reward
   ```
2. Install the dependencies:
   ```
   pip install -r requirements.txt
   playwright install
   ```
3. Set up the Google Sheets API:
   - Create a Google Cloud project and enable Google Drive & Sheets API.
   - Create a service account and download the `credentials.json` file. Place it in the project root.
   - Share your Google Sheet with the service account email.
   - Prepare two sheets in your spreadsheet: `Accounts_Config` for account configuration and `Run_Logs` for logs.
4. Prepare Chrome profiles and extension:
   - Create a directory `chrome_profiles/` and a sub-directory for each account.
   - Install the Rewards Search Automator extension in each profile.

## Usage

1. Populate the `Accounts_Config` sheet with the following columns:
   - `account_id`: a unique identifier for the account.
   - `email`: the Microsoft account email address.
   - `password`: the account password (optional if using saved credentials in the profile).
   - `proxy`: proxy configuration (optional).
   - `profile_name`: the name of the Chrome profile directory inside `chrome_profiles/`.
   - `status`: initial status (e.g., `active`).
2. Update `main.py` to set the correct path to your extension in `launch_browser()`.
3. Run the script:
   ```
   python main.py
   ```
   The script will iterate through the accounts, open the browser with the extension, perform the Bing Reward searches, and log results to the `Run_Logs` sheet.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
