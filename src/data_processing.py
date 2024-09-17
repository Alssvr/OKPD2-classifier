# src/data_processing.py
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Загрузка необходимых ресурсов NLTK
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Лемматизатор и список стоп-слов
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('russian'))  # Вы можете добавить сюда свои слова


def clean_text(text: str) -> str:
    """
    Функция для очистки текста от лишних символов и приведения его к стандартному виду.
    Убирает спецсимволы, числа и стоп-слова, проводит лемматизацию.

    :param text: исходный текст
    :return: очищенный текст
    """
    # Приведение текста к нижнему регистру
    text = text.lower()

    # Удаление всех символов, кроме букв и пробелов
    text = re.sub(r'[^а-яА-Яa-zA-Z\s]', '', text)

    # Токенизация текста
    words = nltk.word_tokenize(text, language='russian')

    # Удаление стоп-слов и лемматизация
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]

    # Возвращаем очищенный текст
    return ' '.join(words)


def preprocess_dataframe(df):
    """
    Функция для предобработки данных в DataFrame.

    :param df: DataFrame с текстами
    :return: DataFrame с очищенными текстами
    """
    df['cleaned_name'] = df['Наименование'].apply(clean_text)
    return df