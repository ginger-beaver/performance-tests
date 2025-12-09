# Python Performance Tests

Реализация нагрузочных тестов
для [Performance Testing Stand](https://github.com/Nikita-Filonov/performance-qa-engineer-course).
Стенд имитирует архитектуру банковских микросервисов (Kafka, Redis, PostgreSQL, MinIO, Grafana,
Prometheus) и предоставляет API через протоколы HTTP и gRPC. Нагрузочные тесты написаны на Python с использованием
Locust.

## Описание проекта

Фреймворк предназначен для оценки производительности банковского стенда, выявления узких мест и демонстрации лучших
практик нагрузочного тестирования:

- **Locust сценарии**: моделируют реалистичное поведение пользователей.
- **API-клиенты**: переиспользуемые HTTP и gRPC клиенты, полностью независимые от внутренней реализации Locust.
- **Seeding**: автоматическая генерация тестовых данных с помощью гибкого seeding builder, который запускается через
  хуки событий Locust.
- **Отчеты**: встроенные HTML-отчеты для запусков Locust; метрики Prometheus и Grafana доступны через учебный стенд.
- **GitLab CI**: ручной запуск пайплайна с выбором тестового сценария. Отчет публикуется
  на [GitLab Pages](https://ginger-beaver.gitlab.io/performance-tests/). Проект синхронизирован с GitHub через mirror -
  все изменения дублируются.

## Установка

### Клонируйте репозиторий

```bash
git clone https://github.com/ginger-beaver/performance-tests.git
cd performance-tests
```

### Создайте виртуальное окружение

#### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Установите зависимости

```bash
pip install -r requirements.txt
```

## Запуск нагрузочных тестов

Каждый сценарий может быть запущен через собственный конфигурационный файл. Отчёт будет автоматически сохранён в той же
директории.

Пример:

```bash
locust --config=./scenarios/http/gateway/existing_user_get_documents/v1.0.conf
```

После выполнения теста откройте сгенерированный HTML-отчёт:
`./scenarios/http/gateway/existing_user_get_documents/report.html`

