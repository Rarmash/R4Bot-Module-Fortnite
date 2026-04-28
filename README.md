# R4Bot-Module-Fortnite

Внешний Fortnite-модуль для [R4Bot](https://github.com/Rarmash/R4Bot).

## Что делает
- добавляет `/fortnite stats`
- добавляет `/fortnite connect`
- добавляет `/fortnite map`
- привязывает Fortnite-профиль к Discord-учётной записи
- показывает статистику и карту Fortnite
- если установлен модуль `profile`, добавляет в него поле Fortnite-профиля
- использует runtime services из `bot.r4_services`

## Интеграции
- модуль может зарегистрировать profile-provider для `/profile`
- если `profile` не установлен, это не считается ошибкой и Fortnite-модуль продолжает работать сам по себе

## Секреты
API-ключ Fortnite хранится в:

```json
{
  "api_key": "YOUR_FORTNITE_API_KEY"
}
```

Файл должен лежать в:

```txt
config/secrets/fortnite.json
```

## Требования
- R4Bot `>= 2.0`
- runtime context с `bot.r4_services`
- сервисы `config`, `firebase`, `secrets`
- установленный пакет `requests`

## Структура
- `module.json` — метаданные модуля
- `cog.py` — команды Fortnite и основное поведение модуля
- `service.py` — регистрация Fortnite-поля для модуля профиля
- `fortnite.secrets.example.json` — пример файла секретов
- `requirements.txt` — зависимости для IDE и локальной проверки

## Установка в R4Bot
```powershell
python manage_modules.py install github:Rarmash/R4Bot-Module-Fortnite@master --enable
```

## Разработка
Для нормальной подсветки импортов в IDE и локальной проверки модуля рекомендуется установить зависимости:

```powershell
python -m pip install -r requirements.txt
```
