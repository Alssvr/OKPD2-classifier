# main.py
from src.scraper import scrape_zakupki

if __name__ == "__main__":
    # Пример запроса для парсинга данных по наименованию товара или услуги
    query = "IP камера"  # Ваш поисковый запрос
    num_pages = 3  # Количество страниц, которые необходимо спарсить

    # Вызов парсера и сохранение результатов в Excel файл
    data = scrape_zakupki(query=query, num_pages=num_pages, save_to_file=True, output_filename="zakupki_data.xlsx")
    print(data.head())  # Показать первые несколько строк данных для проверки