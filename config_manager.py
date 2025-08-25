import gspread
import pandas as pd
from google.oauth2.service_account import Credentials


class SheetManager:
    def __init__(self, creds_path: str, sheet_name: str):
        scopes = ["https://www.googleapis.com/auth/spreadsheets", 
                  "https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_file(creds_path, scopes=scopes)
        client = gspread.authorize(creds)
        self.sheet = client.open(sheet_name)

    def read_accounts(self):
        ws = self.sheet.worksheet("Accounts_Config")
        data = ws.get_all_records()
        return pd.DataFrame(data)

    def log_run(self, account_id, status, message):
        ws = self.sheet.worksheet("Run_Logs")
        ws.append_row([pd.Timestamp.now().isoformat(), account_id, status, message])
