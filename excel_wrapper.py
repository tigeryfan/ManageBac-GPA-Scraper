import pandas as pd
from datetime import datetime
import os

def insert(data, file_name):
    df = pd.DataFrame(list(data.items()), columns=['Class', 'Score'])
    date_str = datetime.now().strftime("%Y-%m-%d")

    with pd.ExcelWriter(file_name, engine='openpyxl', mode='a' if os.path.exists(file_name) else 'w') as writer:
        df.to_excel(writer, sheet_name=date_str, index=False)

    return True

if __name__ == "__main__":
    data = {
        'GPA': 3.93,
        'Class 1': 3.00,
        'Class 2': 2.00,
        'Class 3': 3.00,
        'Class 4': 3.00,
        'Class 5': 3.00,
        'Class 6': 2.00,
        'Class 7': 3.00,
        'Class 8': 4.00,
        'Class 9': 3.00,
        'Class 10': 3.00,
        'Class 11': 4.00,
        'Class 12': 4.00,
        'Class 13': 3.00,
        'Class 14': 2.00,
        'Class 15': 3.00,
        'Class 16': 3.00
    }
    insert(data)