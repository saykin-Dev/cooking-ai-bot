import os
from dotenv import load_dotenv
import google.generativeai


load_dotenv()
gemapi = os.getenv("GEMINI_API_KEY") # АПИШКА ОТ ДЖЕМКИ
name_model = 'gemini-3.8-flash' # !!! НАЗВАНИЕ МОДЕЛИ ДЖЕМИНИ
google.generativeai.configure(api_key=gemapi)

def test_connection(gemapi, name_model, query):
    print("--- Запуск функции проверки ---")

    if not gemapi:
        return "Ты где-то посеял апи от джемини!"

    try:

        print(f"Использую модель: {name_model}")
        test_model = google.generativeai.GenerativeModel(
            name_model, 
            system_instruction='Ты - помощник для всех.'
        )

        response = test_model.generate_content(query)

        if response.parts:
            print("Текст на месте:")
            print(response.text)
        else:
            print("Текста нет. Maybe проблема в фильтрах безопасности.")
            print(response.prompt_feedback)

    except Exception as e:
        print(f"Ошибка при обращении к джемини: {e}")
        

if __name__ == "__main__":

    if not gemapi:
            print("Ты где-то посеял апи от джемини!")
    user_test_query = input("Проверь коннект своим запросом: ")
    test_connection(gemapi=gemapi, name_model=name_model, query=user_test_query)




