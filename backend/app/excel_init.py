import pandas as pd
import os

def init_excel(path: str, columns: list):
    # Ensure parent directory exists
    os.makedirs(os.path.dirname(path), exist_ok=True)

    if not os.path.exists(path):
        df = pd.DataFrame(columns=columns)
        df.to_excel(path, index=False)
    else:
        try:
            pd.read_excel(path)
        except Exception:
            df = pd.DataFrame(columns=columns)
            df.to_excel(path, index=False)
