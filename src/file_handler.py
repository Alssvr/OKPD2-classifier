# src/file_handler.py
import pandas as pd


def read_excel(file_path: str) -> pd.DataFrame:
    """
    Чтение данных из файла .xlsx.

    :param file_path: путь до файла .xlsx
    :return: DataFrame с данными
    """
    try:
        df = pd.read_excel(file_path, engine='openpyxl')
        return df
    except FileNotFoundError:
        print(f"Файл по пути {file_path} не найден.")
        return pd.DataFrame()


def save_to_excel(df: pd.DataFrame, file_path: str):
    """
    Сохранение данных в файл .xlsx.

    :param df: DataFrame с данными
    :param file_path: путь до файла .xlsx
    """
    df.to_excel(file_path, index=False, engine='openpyxl')
    print(f"Данные успешно сохранены в {file_path}")