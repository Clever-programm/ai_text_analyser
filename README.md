# FastAPI-микросервис: "AI текстовый анализатор"

Цель: закрепить FastAPI, логирование, Docker, базовую структуру проекта.

Описание:

    Пользователь загружает .txt файл (через Post-запрос).

    Сервер обрабатывает его: считает количество слов, определяет язык, делает сводку (можно через OpenAI API или локальный HuggingFace).

    Отдаёт результат в формате JSON.

Плюсы:

    Простая бизнес-логика.

    Практика FastAPI (эндпоинты, схемы, middleware, обработка ошибок).

    Можно контейнеризировать.

    В дальнейшем расширить до Langchain/векторной базы.
