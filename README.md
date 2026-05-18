# 🌐 EduCRM - Full‑Stack Educational Platform  
### Курсовая работа (RTU MIREA) • Full‑Stack Architecture • Django + JS

<div align="center>
<img src="https://readme-typing-svg.herokuapp.com?color=00FF4C&size=22&center=true&vCenter=true&width=650&lines=Full‑Stack+разработчик+%7C+UI%2FUX‑ориентированный+инженер;Создатель+студенческой+экосистемы;Чистая+архитектура+%7C+TypeScript+%7C+Node.js;Проектирование+долговечных+цифровых+платформ;РТУ+МИРЭА+%E2%80%94+Инженерия+будущего" />
</div>
---

## Описание проекта

**EduCRM** - модульная образовательная CRM‑система, разработанная в рамках курсовой работы.  
Проект объединяет:

- файловый менеджер  
- систему задач  
- панель студента  
- авторизацию через JWT  
- ролевую модель (студент / админ)  
- адаптивный UI  
- API‑слой `/api/educrm/`  

Фронтенд - чистый JS + Tailwind.  
Бэкенд - Django с кастомной JWT‑аутентификацией.

---

## ⚙️ Стек технологий

### Backend
- Django 5  
- Django ORM  
- Custom JWT Authentication (`accounts/jwt_auth.py`)  
- REST API (без DRF)  
- SQLite / PostgreSQL  

### Frontend
- TailwindCSS  
- Lucide Icons  
- Vanilla JS  
- Адаптивный UI  

### Инфраструктура
- Модульная структура приложений  
- Разделение HTML / API маршрутов  
- Чистая архитектура views / api_views  

---

## 🧩 Основные модули

### 📁 Файловый менеджер

Функционал:
- загрузка файлов  
- создание папок  
- перемещение файлов  
- удаление  
- фильтры (тип, категория)  
- поиск  
- breadcrumb‑навигация  
- drag‑and‑drop загрузка  
- статистика  

API:
GET    /api/educrm/files/
GET    /api/educrm/folders/
POST   /api/educrm/folders/create/
POST   /api/educrm/files/upload/
POST   /api/educrm/files/move/
DELETE /api/educrm/files/delete/<id>/


---

### ✔️ Система задач

Функционал:
- список задач  
- статусы  
- фильтры  
- панель студента  

---

### 🔐 Авторизация (JWT)

Особенности:
- кастомная реализация JWT  
- хранение токена в `localStorage`  
- защита API через `Authorization: Bearer <token>`  

---

### 👤 Роли

- **Студент** - доступ к задачам, файлам, профилю  
- **Админ** - расширенное меню, управление пользователями  

Меню рендерится динамически:
```js
renderSidebarMenu(isAdmin)
```

---

## 🏗 Архитектура проекта
```bash
educrm/
 ├── educrm_app/
 │    ├── templates/educrm/*.html
 │    ├── views.py (HTML)
 │    ├── api_urls.py (API)
 │    ├── views_files.py (API логика)
 │    ├── models.py
 │    └── static/js/*.js
 │
 ├── accounts/
 │    ├── jwt_auth.py (кастомный JWT)
 │    ├── views.py (login/register)
 │    └── urls.py
 │
 ├── crm/
 │    ├── views.py
 │    └── urls.py
 │
 └── educrm/urls.py (главный роутер)
```

---

## 🔌 API‑слой
Пример ответа /api/educrm/files/:
```bash
[
  {
    "id": 1,
    "name": "report.pdf",
    "type": "document",
    "size": "1.2 MB",
    "category": "Assignments",
    "uploaded_by": "student@example.com",
    "uploaded_at": "2026-05-18",
    "folder": null
  }
]
```

---

## 🎨 UI / UX особенности
- единый стиль модалок
- плавные анимации
- адаптивная сетка
- тёмный/светлый режим
- техно‑эстетика интерфейса

---

## 🚀 Запуск проекта
### 1. Установка зависимостей
```bash
pip install -r requirements.txt
```
### 2. Миграции
```bash
python manage.py migrate
```
### 3. Запуск сервера
```bash
python manage.py runserver
```

---

## 📌 Планы по развитию
- drag‑and‑drop перемещение файлов между папками
- предпросмотр изображений
- редактор документов
- интеграция WebSockets
- уведомления

---

## 💻 Автор
glebvisage5 - full‑stack разработчик, RTU MIREA
Проект создан в рамках курсовой работы 2026 года.
