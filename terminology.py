import pandas as pd
import os

class ProcessMemoqTerminology:
    def __init__(self, file_paths):
        self.file_paths = file_paths
        self.terminology_merged = None
        self.check_file()

    def check_file(self):
        for path in self.file_paths:
             name, ext = os.path.splitext(path)

             if ext.lower() not in [".csv", ".xlsx"]:
                raise ValueError(f"Ungültige Datei: {path}. Nur CSV oder XLSX erlaubt.")


    def import_xlsx(self, file_path):
        df = pd.read_excel(file_path)
        return df

    def import_csv(self, file_path):
        df = pd.read_csv(file_path)
        return df

    def merge_terminology(self):
        dataframes = []

        for path in self.file_paths:
            name, ext = os.path.splitext(path)

            if ext.lower() == ".xlsx":
                df = self.import_xlsx(path)
            elif ext.lower() == ".csv":
                df = self.import_csv(path)
            else:
                continue

            dataframes.append(df)

        self.terminology_merged = pd.concat(dataframes, ignore_index=True)

    def export_merged_terminology_as_xlsx(self):
        if not self.terminology_merged:
            self.merge_terminology()

        self.terminology_merged.to_excel("tb_merged.xlsx", index=False)

#new
    def list_languages(self):
        columns = self.terminology_merged.columns
        languages = []

        for column in columns:
            language = column.split(".")[0]
            if language not in languages:
                languages.append(language)
        return languages