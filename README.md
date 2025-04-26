# Django Menu App

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue) ![Flask](https://img.shields.io/badge/Flask-2.3.3-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

Django-приложение реализует древовидное меню.



## Описание проекта

Это Django-приложение реализует древовидное меню с поддержкой следующих функций:

1. Меню хранится в базе данных.
2. Редактирование меню осуществляется через стандартную админку Django.
3. Активный пункт меню определяется исходя из текущего URL.
4. На одной странице может быть несколько меню, которые различаются по имени.
5. При клике на пункт меню происходит переход по заданному URL (явный или named URL).
6. Для отрисовки каждого меню требуется ровно один запрос к базе данных.
7. Все пункты над активным и первый уровень под ним развернуты.

---

## Установка

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/your-repo/tfidf-app.git
cd tfidf-app
```

### 2. Установите зависимости
```poetry install```

### 3. Настройка базы данных
```commandline
python manage.py makemigrations
python manage.py migrate
```

### 4. Создание суперпользователя
```commandline
python manage.py createsuperuser
```

### 5. Запустите приложение
```python manage.py runserver```

## Использование
```commandline
1. Откройте браузер и перейдите по адресу http://127.0.0.1:8000/ .
2. Перейдите в админку Django: http://127.0.0.1:8000/admin/ .
3. Войдите с учетными данными суперпользователя.
4. Добавьте новые пункты меню через раздел Menu items :
    • Name : Название пункта меню.
    • URL : Явный URL или named URL.
    • Parent : Родительский пункт (если есть).
    • Menu name : Имя меню (например, main_menu).
Пример структуры:
    • Home → URL: /
    • About → URL: /about/
    • Services → URL: /services/
    • Web Development → URL: /services/web-dev/, Parent: Services
    • Frontend → URL: /services/web-dev/frontend/, Parent: Web Development
    • Backend → URL: /services/web-dev/backend/, Parent: Web Development
    • SEO → URL: /services/seo/, Parent: Services
```

## Особенности реализации
```commandline
 • Один запрос к БД : Для отрисовки каждого меню используется только один запрос к базе данных благодаря select_related('parent').
 • Активный пункт : Активный пункт определяется исходя из текущего URL (request.path).
 • Развертывание меню : Все пункты над активным и первый уровень под ним автоматически разворачиваются.
 • HTML/CSS — для создания интерфейса.
 • Гибкость : Поддерживается несколько меню на одной странице, которые различаются по имени.
```