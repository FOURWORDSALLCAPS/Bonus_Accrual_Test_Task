# Bonus_Accrual_Test_Task

## Как запустить

Скачайте код:
```sh
git clone https://github.com/FOURWORDSALLCAPS/Bonus_Accrual_Test_Task.git
```

Перейдите в каталог проекта:
```sh
cd Bonus_Accrual_Test_Task
```

**Важно!** Версия Python должна быть не ниже 3.13.

В каталоге проекта создайте виртуальное окружение:
```sh
python -m venv venv
```

Установите poetry и зависимости в виртуальное окружение:
```sh
pip install poetry
poetry install
```

Создать файл `.env` по аналогии с example.env:

Запустите проект:

```sh
docker compose up --build
```

## Как настроить

Правила находятся в файле `rules.json`

### Структура файла rules.json

Файл rules.json должен содержать массив объектов, каждый из которых представляет собой правило начисления бонусов. Каждый объект правила должен иметь следующие поля:

- type (строка): Название типа правила. Это имя метода в классе BonusAccrualService, который будет применяться для расчета бонусов.

- order (целое число): Порядок применения правила. Правила будут применяться в порядке возрастания этого значения. Если порядок не указан, по умолчанию будет использовано значение 0.

- Дополнительные параметры, специфичные для каждого правила, например:

- multiplier (число): Множитель для выходных и праздничных дней.

- percentage (число): Процент для VIP-клиентов.

### Как добавить новое правило

Добавьте новый объект правила: 

```json
{
    "type": "holiday_bonus",
    "multiplier": 2,
    "order": 3
}
```

Реализуйте логику правила в коде: 

Откройте файл, содержащий класс BonusAccrualService, и добавьте метод, который будет обрабатывать новое правило.

```python
async def holiday_bonus(self, current_bonus, rule, timestamp, customer_status):
    if self.__is_holiday(timestamp):
        return current_bonus * rule['multiplier']
    return current_bonus
```

Добавьте метод проверки праздников: 

```python
def __is_holiday(self, timestamp):
    # Логика для определения, является ли день праздничным
    # Например, можно использовать список фиксированных дат или библиотеку для работы с праздниками
    return True
```

Сохраните изменения и перезапустите приложение

## Как использовать

Свагер доступен по адресу:
`http://127.0.0.1/docs`

Откройте ручку `calculate_bonus` и укажите обязательные параметры:

transaction_amount (сумма покупки)
timestamp (дата покупки)
customer_status (обычный или VIP)

```json
{
"transaction_amount": 150,
"timestamp": "2025-03-08T14:30:00Z",
"customer_status": "vip"
}
```
