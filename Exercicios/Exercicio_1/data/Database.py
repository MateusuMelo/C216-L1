import pandas as pd

class SimpleDB:
    def __init__(self, data_path=None):
        if data_path is None:
            self.data = pd.DataFrame()
        else:
            self.data = pd.read_csv(data_path)

    def insert_one(self, data: pd.Series):
        try:
            self.data = pd.concat([self.data, data.to_frame().T], ignore_index=True)
        except Exception as e:
            raise e

    def read_all(self):
        return self.data

    def read_by_mat(self, mat):
        try:
            data_filter = self.data[self.data['matricula'] == mat]
            return data_filter
        except Exception as e:
            raise e

    def update(self, mat, new_values: dict):
        try:
            indices = self.data[self.data['matricula'] == mat].index
            for key, value in new_values.items():
                self.data.loc[indices, key] = value
        except Exception as e:
            raise e

    def delete(self, condition):
        try:
            self.data = self.data.drop(self.data.query(condition).index).reset_index(drop=True)
        except Exception as e:
            raise e

    def save_to_csv(self, file_path):
        try:
            self.data.to_csv(file_path, index=False)
        except Exception as e:
            raise e
