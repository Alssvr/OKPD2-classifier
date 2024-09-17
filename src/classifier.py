# src/classifier.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle


class OKPD2Classifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=5000)  # Векторизация текста
        self.model = LogisticRegression()  # Модель для классификации

    def train(self, df: pd.DataFrame):
        """
        Обучение модели на входных данных.

        :param df: DataFrame с очищенными текстами и кодами ОКПД2
        """
        X = self.vectorizer.fit_transform(df['cleaned_name'])
        y = df['ОКПД2']

        # Разделяем данные на тренировочные и тестовые
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Обучение модели
        self.model.fit(X_train, y_train)

        # Оценка модели
        y_pred = self.model.predict(X_test)
        print(classification_report(y_test, y_pred))

    def predict(self, texts: list):
        """
        Предсказание кодов ОКПД2 для новых текстов.

        :param texts: список текстов для классификации
        :return: список предсказанных кодов ОКПД2
        """
        X = self.vectorizer.transform(texts)
        return self.model.predict(X)

    def save_model(self, model_path: str):
        """
        Сохранение обученной модели на диск.

        :param model_path: путь для сохранения модели
        """
        with open(model_path, 'wb') as f:
            pickle.dump((self.vectorizer, self.model), f)

    def load_model(self, model_path: str):
        """
        Загрузка модели с диска.

        :param model_path: путь до файла модели
        """
        with open(model_path, 'rb') as f:
            self.vectorizer, self.model = pickle.load(f)