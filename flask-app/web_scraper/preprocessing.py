import os

import numpy as np
import pandas as pd


class Preprocessing:
    def preprocess(self, filenames: list) -> dict:
        yearly_dict = {}
        for name in filenames:
            print(f"Preprocessing {name}")
            day_average_list = []
            df = pd.read_csv(name)
            for ind, row in df.iterrows():
                day_average_list.append(row["PM2.5"])
            yearly_dict[name] = day_average_list
        return yearly_dict

    def clean_combined_data(self, combined_data: pd.DataFrame) -> pd.DataFrame:
        combined_data = combined_data.replace('', np.nan)
        combined_data.dropna(how='any', inplace=True)
        return combined_data

    def save_combined_data(self, combined_data: pd.DataFrame, folder_name: str, file_name: str) -> None:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        combined_data.to_csv(f'{folder_name}/{file_name}', index=None)
