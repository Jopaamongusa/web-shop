# web-shop

Проект підтримується та розвивається наступними учасниками команди:
  - https://github.com/111Andre
  -
  -


Проект "Інтернет Магазин" – це повнофункціональний веб-додаток для онлайн продажу товарів. Він включає 
авторизацію для користувачів та адміністраторів, управління товарами (додавання, редагування, видалення), 
відправку повідомлень про замовлення, інтеграцію з Telegram для отримання та редагування інформації про 
користувачів та товари.

## Чому проект корисний
Проект "Інтернет Магазин" корисний як для користувачів, так і для розробників:
- **Користувачі** швидко розбираються з інтерфейсом та функціоналом, отримують зручний інструмент для покупок.
- **Замовники** отримують впевненість в тому, що проект може бути реалізований на високому рівні.
- **Розробники** набувають практичних навичок, покращують алгоритмічне мислення, вчаться працювати в команді та
відповідально ставитися до своїх завдань.

## Для роботи проекту необхідно встановити наступні модулі:
- `aiofiles` 23.2.1 	– 	для роботи з файлами асинхронно.
- `aiogram` 3.8.0 	– 	для роботи з Telegram API.
- `aiohttp` 3.9.5 	– 	асинхронний HTTP-клієнт/сервер.
- `alembic` 1.13.1 	– 	для управління міграціями бази даних.
- `Flask` 3.0.3 	– 	мікрофреймворк для веб-додатків на Python.
- `Flask-Login` 0.6.3 	– 	для управління сесіями користувачів.
- `Flask-Mail` 0.10.0 	– 	для відправки електронних листів.
- `Flask-Migrate` 4.0.7 – 	для роботи з міграціями бази даних.
- `Flask-SQLAlchemy` 3.1.1 – 	ORM для Flask.
- `openpyxl` 3.1.2 	– 	для роботи з Excel файлами.
- `pandas` 2.2.2 	– 	для аналізу даних.
- `SQLAlchemy` 2.0.29 	– 	ORM для Python.

## Інструкція по запуску проекту
#### Локально

1. Клонуйте репозиторій:
git clone https://github.com/your-repository.git


2. Перейдіть до директорії проекту:
 ``` cd your-repository ```  

3. Встановіть необхідні модулі:
<code> pip install -r requirements.txt </code>

4Запустіть додаток:
<code> flask run </code>

#### Віддалено (pythonanywhere)
1.  Зареєструйтеся на pythonanywhere.com.
2.  Створіть новий веб-додаток, вибравши відповідні налаштування для Flask.
3.  Завантажте код вашого проекту на сервер (через Git або вручну).
4.  Встановіть необхідні модулі
    <code> pip install -r requirements.txt </code>
5.  Налаштуйте конфігураційні файли та запустіть веб-додаток.

## Приклад створення головного додатку які ви можете бачити в нащому проекті

### Shop_app
``` python
import flask 

# Blueprint for shop functionality / Блюпринт для функціоналу магазину
shop = flask.Blueprint(
    name = "shop",  # Name of the blueprint / Назва блупринта
    import_name = "app",  # Import name for the blueprint / Ім'я імпорту для блупринта
    template_folder = "shop_page/templates",  # Folder for shop templates / Папка для шаблонів магазину
    static_folder = "static/shop_page",  # Folder for shop static files / Папка для статичних файлів магазину
    static_url_path = "/shop/"  # URL path for shop static files / URL шлях для статичних файлів магазину
)

```
### reg_app / registration_app
``` python
import flask

# Blueprint for registration functionality / Блюпринт для функціоналу реєстрації
reg = flask.Blueprint(
    name = 'registration',  # Name of the blueprint / Назва блупринта
    import_name = "app",  # Import name for the blueprint / Ім'я імпорту для блупринта
    template_folder = "reg_page/templates",  # Folder for registration templates / Папка для шаблонів реєстрації
    static_folder = "static",  # Folder for registration static files / Папка для статичних файлів реєстрації
    static_url_path = "/reg"  # URL path for registration static files / URL шлях для статичних файлів реєстрації
)
```
### log_app
``` python
import flask

# Blueprint for login functionality / Блюпринт для функціоналу входу
log = flask.Blueprint(
    name = "login_page",  # Name of the blueprint / Назва блупринта
    import_name = "app",  # Import name for the blueprint / Ім'я імпорту для блупринта
    template_folder = "log_page/templates",  # Folder for login templates / Папка для шаблонів входу
    static_folder = "static",  # Folder for login static files / Папка для статичних файлів входу
    static_url_path = "/log"  # URL path for login static files / URL шлях для статичних файлів входу
)
```
### home_app
``` python
import flask 

# Blueprint for home functionality / Блюпринт для функціоналу домашньої сторінки
home = flask.Blueprint(
    name = "home",  # Name of the blueprint / Назва блупринта
    import_name = "app",  # Import name for the blueprint / Ім'я імпорту для блупринта
    template_folder = "home_page/templates",  # Folder for home templates / Папка для шаблонів домашньої сторінки
    static_folder = "static/home_page",  # Folder for home static files / Папка для статичних файлів домашньої сторінки
    static_url_path = "/home/"  # URL path for home static files / URL шлях для статичних файлів домашньої сторінки
)
```
### basket_app
``` python
import flask 

# Blueprint for basket functionality / Блюпринт для функціоналу кошика
basket = flask.Blueprint(
    name = "basket",  # Name of the blueprint / Назва блупринта
    import_name = "basket_app",  # Import name for the blueprint / Ім'я імпорту для блупринта
    template_folder = "basket_page/templates",  # Folder for basket templates / Папка для шаблонів кошика
    static_folder = "static/basket_page",  # Folder for basket static files / Папка для статичних файлів кошика
    static_url_path = "/basket/"  # URL path for basket static files / URL шлях для статичних файлів кошика
)
```
### admin_app
``` python
import flask

# Blueprint for admin functionality / Блюпринт для функціоналу адміністратора
admin = flask.Blueprint(
    name = 'admin',  # Name of the blueprint / Назва блупринта
    import_name = 'admin_page',  # Import name for the blueprint / Ім'я імпорту для блупринта
    template_folder = 'templates',  # Folder for admin templates / Папка для шаблонів адміністратора
    static_folder= 'static',  # Folder for admin static files / Папка для статичних файлів адміністратора
    static_url_path= '/admin/'  # URL path for admin static files / URL шлях для статичних файлів адміністратора
)
```
### example/приклад
```python
import flask

example = flask.Bkueprint(
    name = 'name_of_Blueprint',
    import_name - 'name_of_file',
    template_folder = 'path_to_your_templates_folred',
    static_folder = 'path_to_your_templates_folred',
    static_url_path = 'url_path_sabe_with_url_in_url'
)
```

### project ursl
``` python
import home_page  # Import the home_page module / Імпортуємо модуль home_page
from .settings import project  # Import the project object from settings / Імпортуємо об'єкт project з налаштувань
import log_page  # Import the log_page module / Імпортуємо модуль log_page
import reg_page  # Import the reg_page module / Імпортуємо модуль reg_page
import shop_page  # Import the shop_page module / Імпортуємо модуль shop_page
import basket_page  # Import the basket_page module / Імпортуємо модуль basket_page
import admin_page  # Import the admin_page module / Імпортуємо модуль admin_page

# Add a URL rule for the home page / Додаємо правило URL для домашньої сторінки
# Mapping the root URL to the render_home function / Відповідність кореневого URL функції render_home
home_page.home.add_url_rule(rule="/", view_func=home_page.render_home)

# Add a URL rule for the shop page / Додаємо правило URL для сторінки магазину
# Mapping /shop/ to the render_shop function / Відповідність /shop/ функції render_shop
# Allowing both GET and POST methods / Дозволяємо методи GET та POST
shop_page.shop.add_url_rule(rule="/shop/", view_func=shop_page.render_shop, methods=['GET', 'POST'])

# Add a URL rule for the registration page / Додаємо правило URL для сторінки реєстрації
# Mapping /reg/ to the render_reg function / Відповідність /reg/ функції render_reg
# Allowing both GET and POST methods / Дозволяємо методи GET та POST
reg_page.reg.add_url_rule(rule='/reg/', view_func=reg_page.render_reg, methods=['GET', 'POST'])

# Add a URL rule for the login page / Додаємо правило URL для сторінки входу
# Mapping /log/ to the show_authorization function / Відповідність /log/ функції show_authorization
# Allowing both GET and POST methods / Дозволяємо методи GET та POST
log_page.log.add_url_rule(rule='/log/', view_func=log_page.show_authorization, methods=['GET', 'POST'])

# Add a URL rule for the basket page / Додаємо правило URL для сторінки кошика
# Mapping /cart/ to the render_basket function / Відповідність /cart/ функції render_basket
# Allowing both GET and POST methods / Дозволяємо методи GET та POST
basket_page.basket.add_url_rule(rule='/cart/', view_func=basket_page.render_basket, methods=['GET', 'POST'])

# Add a URL rule for the admin page / Додаємо правило URL для сторінки адміністратора
# Mapping /admin/ to the render_admin function / Відповідність /admin/ функції render_admin
# Allowing both GET and POST methods / Дозволяємо методи GET та POST
admin_page.admin.add_url_rule(rule='/admin/', view_func=admin_page.render_admin, methods=["GET", "POST"])

# Register the basket blueprint with the project / Реєструємо блупринт кошика з проектом
project.register_blueprint(blueprint=basket_page.basket)

# Register the home blueprint with the project / Реєструємо блупринт домашньої сторінки з проектом
project.register_blueprint(blueprint=home_page.home)

# Register the shop blueprint with the project / Реєструємо блупринт магазину з проектом
project.register_blueprint(blueprint=shop_page.shop)

# Register the registration blueprint with the project / Реєструємо блупринт реєстрації з проектом
project.register_blueprint(blueprint=reg_page.reg)

# Register the login blueprint with the project / Реєструємо блупринт входу з проектом
project.register_blueprint(blueprint=log_page.log)

# Register the admin blueprint with the project / Реєструємо блупринт адміністратора з проектом
project.register_blueprint(blueprint=admin_page.admin)
```

## Усі файли інші файли які в project

### project settings

``` python
import flask  # Import Flask framework / Імпортуємо Flask фреймворк
import flask_sqlalchemy  # Import SQLAlchemy for database management / Імпортуємо SQLAlchemy для керування базою даних
import flask_migrate  # Import Flask-Migrate for database migrations / Імпортуємо Flask-Migrate для міграцій бази даних
import os  # Import os module for operating system interactions / Імпортуємо модуль os для взаємодії з операційною системою

# Initialize Flask project / Ініціалізуємо Flask проект
project = flask.Flask(
    import_name="settings",  # Import name / Ім'я імпорту
    template_folder="project/templates",  # Folder for templates / Папка для шаблонів
    instance_path=os.path.abspath(__file__ + "/.."),  # Instance path / Шлях до інстансу
)

# Configure the database URI / Налаштовуємо URI бази даних
project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

# Initialize SQLAlchemy with the Flask project / Ініціалізуємо SQLAlchemy з Flask проектом
DATABASE = flask_sqlalchemy.SQLAlchemy(app=project)

# Initialize Flask-Migrate with the Flask project and database / Ініціалізуємо Flask-Migrate з Flask проектом і базою даних
migrate = flask_migrate.Migrate(app=project, db=DATABASE)



```

### project login_manager
``` python
import flask_login  # Import Flask-Login for user session management / Імпортуємо Flask-Login для керування сесіями користувачів

from .settings import project  # Import the Flask project from settings / Імпортуємо Flask проект з налаштувань
from reg_page.models import Users  # Import the Users model from reg_page.models / Імпортуємо модель Users з reg_page.models

# Set secret key for the project / Встановлюємо секретний ключ для проекту
project.secret_key = '200'

# Initialize LoginManager with the Flask project / Ініціалізуємо LoginManager з Flask проектом
login_manager = flask_login.LoginManager(project)

# Define user loader function for LoginManager / Визначаємо функцію завантажувача користувачів для LoginManager
@login_manager.user_loader
def load_user(id):
    return Users.query.get(id)  # Get user by ID / Отримати користувача за ID

```

### project mail_config 
``` python
import flask_mail  # Import Flask-Mail for email support / Імпортуємо Flask-Mail для підтримки електронної пошти
from project.settings import project  # Import the Flask project from settings / Імпортуємо Flask проект з налаштувань

# Define the Gmail address / Визначаємо адресу Gmail
gmail_address = "arzon.art125@gmail.com"

# Configure Flask-Mail settings / Налаштовуємо параметри Flask-Mail
project.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Mail server / Поштовий сервер
project.config['MAIL_PORT'] = 587  # Mail port / Поштовий порт
project.config['MAIL_USE_TLS'] = True  # Use TLS / Використовувати TLS
project.config['MAIL_USE_SSL'] = False  # Use SSL / Використовувати SSL
project.config['MAIL_USERNAME'] = gmail_address  # Mail username / Ім'я користувача пошти
project.config['MAIL_PASSWORD'] = ''  # Mail password / Пароль до пошти

# Initialize Flask-Mail with the Flask project / Ініціалізуємо Flask-Mail з Flask проектом
mail = flask_mail.Mail(project)
```

## html код в нашому проекті / html code in our project

### project base html
``` html 
<html lang="en">
    <head>
        <meta charset="UTF-8"> <!-- Character encoding / Кодування символів -->
        <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Responsive design / Адаптивний дизайн -->
        <title>{% block title %}{% endblock %}</title> <!-- Title block / Блок заголовку -->
        {% block link %} {% endblock %} <!-- Block for additional links / Блок для додаткових посилань -->
    <body>
        {% if not is_authenticated %} <!-- If user is not authenticated / Якщо користувач не авторизований -->
            <a href="/log/">AUTHORIZATION</a> <!-- Link to login / Посилання для авторизації -->
            <a href="/reg/">REGISTRATION</a> <!-- Link to registration / Посилання для реєстрації -->
        {% endif %}
        
        {% if is_admin %} <!-- If user is admin / Якщо користувач адміністратор -->
            <a href="/admin/">ADMIN</a> <!-- Link to admin page / Посилання на адмін-сторінку -->
        {% endif %}

        {% block content %} <!-- Content block / Блок контенту -->
        {% endblock %}
    </body>
</html>
```
### shop html 
``` html 
{% extends "base.html" %} <!-- Extends base template / Розширює базовий шаблон -->

{% block title %} 
    Shop Page
{% endblock %}

{% block link %}
    <link rel="stylesheet" href="{{ url_for('static', filename = 'shop_page/css/style.css') }}"> <!-- Link to CSS / Посилання на CSS -->
{% endblock %}

{% block content %}
    {% for value, tagname in body['content'].items() %} <!-- Loop through content items / Прохід по елементах контенту -->
        {% if tagname["tagname"] == 'a' %}
            <{{ tagname["tagname"] }} href="{{ tagname["href"] }}"> {{ tagname["text"] }} </{{ tagname["tagname"] }}> <!-- Anchor tag / Якірний тег -->
        {% else %}
            <{{ tagname["tagname"] }}> {{ tagname["text"] }} </{{ tagname["tagname"] }}> <!-- Other tags / Інші теги -->
        {% endif %}
    {% endfor %}
    <p>{{ user_name }}</p> <!-- Display user name / Відображення імені користувача -->

    {% if count %}
        <div class="message">
            <h1> {{ count }} </h1> <!-- Display count / Відображення кількості -->
        </div>
    {% endif %}

    {% for product in products %} <!-- Loop through products / Прохід по продуктах -->
        {% set current_product = product %} <!-- Set current product / Встановлення поточного продукту -->
        
        <div class="container">
            <img src="{{ url_for('static', filename = 'shop_page/images/' + product.name + '.png') }}" alt=""> <!-- Product image / Зображення продукту -->
            
            <div class="vertical-line-right"></div> 
            <div class="text">
                {% for value, key in body['cataloge'].items() %} <!-- Loop through catalog items / Прохід по елементах каталогу -->
                    {% if key["tagname"] == 'button' %}
                        <{{ key["tagname"] }} class="{{ key["class"] }}" id="{{ product.id }}"> {{ key["text"] }} </{{ key["tagname"] }}> <!-- Button tag / Тег кнопки -->
                    {% elif key["tagname"] == 'h2' %}
                        <{{ key["tagname"] }}> {{ current_product.name }} </{{ key["tagname"] }}> <!-- Product name / Назва продукту -->
                    {% elif key["tagname"] == 'h3' %}
                        <{{ key["tagname"] }}> {{ key["text"] }} {{ current_product.price }} </{{ key["tagname"] }}> <!-- Product price / Ціна продукту -->
                    {% elif key["tagname"] == 'h4' %}
                        <{{ key["tagname"] }}> {{ key["text"] }} {{ current_product.description }} </{{ key["tagname"] }}> <!-- Product description / Опис продукту -->
                    {% else %}
                        <{{ key["tagname"] }}> {{ key["text"] }} </{{ key["tagname"] }}> <!-- Other tags / Інші теги -->
                    {% endif %}
                {% endfor %}
                <h2>Ємність</h2> <!-- Capacity label / Мітка ємності -->
                <div class="div_memory">
                    <button class="memory">256</button> <!-- Memory button / Кнопка пам'яті -->
                    <button class="memory">512</button> <!-- Memory button / Кнопка пам'яті -->
                    <button class="memory">1028</button> <!-- Memory button / Кнопка пам'яті -->
                </div>
            </div>
            <div class="vertical-line-left"></div> 
        </div>
    {% endfor %}
    <script src="{{ url_for('static', filename='shop_page/js/set_cookies.js') }}" defer></script> <!-- Set cookies script / Скрипт встановлення кукі -->
    <script src="{{ url_for('static', filename = 'js/set_cookie.js') }}"></script> <!-- Set cookie script / Скрипт встановлення кукі -->
{% endblock %}
```
### reg html/ registratin html
``` html
{% extends "base.html" %} <!-- Extends base template / Розширює базовий шаблон -->

{% block title %} 
    Registration Page
{% endblock %}

{% block link %}
    <link rel="stylesheet" href="{{ url_for('static', filename = 'reg_page/css/style.css') }}"> <!-- Link to CSS / Посилання на CSS -->
{% endblock %}

{% block content %}
<form method="post"> <!-- Form with POST method / Форма з методом POST -->
    {% for value, tagname in body['content'].items() %} <!-- Loop through content items / Прохід по елементах контенту -->
        <span>
        {% if tagname["tagname"] == "input" %}
            <{{ tagname["tagname"] }} class="{{ tagname["class"] }}" type="{{ tagname["type"] }}" name="{{ tagname["name"] }}" placeholder="{{ tagname["placeholder"] }}"> <!-- Input tag / Тег вводу -->
        {% elif tagname["tagname"] == "button" %}
            <{{ tagname["tagname"] }} type="{{ tagname["type"] }}"> {{ tagname["text"] }} </{{ tagname['tagname'] }}> <!-- Button tag / Тег кнопки -->
        </span>
        {% else %}
            <{{ tagname["tagname"] }}> {{ tagname["text"] }} </{{ tagname["tagname"] }}> <!-- Other tags / Інші теги -->
        {% endif %}
    {% endfor %}
</form> 
{% endblock %}
```       
### log html
``` html

{% extends "base.html" %} <!-- Extends base template / Розширює базовий шаблон -->

{% block title %} 
    Authorization Page
{% endblock %}

{% block link %}
    <link rel="stylesheet" href="{{ url_for('static', filename = 'log_page/css/style.css') }}"> <!-- Link to CSS / Посилання на CSS -->
{% endblock %}

{% block content %}
<form method="post"> <!-- Form with POST method / Форма з методом POST -->
    {% for value, tagname in body['content'].items() %} <!-- Loop through content items / Прохід по елементах контенту -->
        <span>
        {% if tagname["tagname"] == 'a' %}
            <{{ tagname["tagname"] }} href="{{ tagname["href"] }}"> {{ tagname["text"] }} </{{ tagname["tagname"] }}> <!-- Anchor tag / Якірний тег -->
        {% elif tagname["tagname"] == "input" %}
            <{{ tagname["tagname"] }} class="{{ tagname["class"] }}" type="{{ tagname["type"] }}" name="{{ tagname["name"] }}" placeholder="{{ tagname["placeholder"] }}"> <!-- Input tag / Тег вводу -->
        {% elif tagname["tagname"] == "button" %}
            <{{ tagname["tagname"] }} type="{{ tagname["type"] }}"> {{ tagname["text"] }} </{{ tagname['tagname'] }}> <!-- Button tag / Тег кнопки -->
        </span>
        {% else %}
            <{{ tagname["tagname"] }}> {{ tagname["text"] }} </{{ tagname["tagname"] }}> <!-- Other tags / Інші теги -->
        {% endif %}
    {% endfor %}
</form> 
{% endblock %}
```
### Home html
``` html
{% extends "base.html" %} <!-- Extend base.html for consistent structure -->

{% block title %}
    Home Page <!-- Page title -->
{% endblock %}

{% block link %}
    <link rel="stylesheet" href="{{ url_for('static', filename='home_page/css/style.css') }}"> <!-- Link to CSS file -->
{% endblock %}

{% block content %}
    <div>
        {% for value, tagname in body['content'].items() %}
            {% if tagname["tagname"] == 'a' %}
                <{{ tagname["tagname"] }} href="{{ tagname["href"] }}">{{ tagname["text"] }}</{{ tagname["tagname"] }}>
            {% elif tagname["tagname"] != "a"  %}
                <{{ tagname["tagname"] }}>{{ tagname["text"] }}</{{ tagname["tagname"] }}>
            {% endif %}       
        {% endfor %}
        <p>{{ user_name }}</p> <!-- Display user's name -->
    </div>
{% endblock %}
```
### Basket html 
``` html
{% extends "base.html" %} <!-- Extend base.html for consistent structure -->

{% block title %}
    Basket Page <!-- Page title -->
{% endblock %}

{% block link %}
    <link rel="stylesheet" href="{{ url_for('static', filename='basket_page/css/style.css') }}"> <!-- Link to CSS file -->
{% endblock %}

{% block content %}
    {% for value, tagname in body['content'].items() %}
        {% if tagname["tagname"] == 'a' %}
            <{{ tagname["tagname"] }} href="{{ tagname["href"] }}">{{ tagname["text"] }}</{{ tagname["tagname"] }}>
        {% else %}
            <{{ tagname["tagname"] }}>{{ tagname["text"] }}</{{ tagname["tagname"] }}>
        {% endif %}       
    {% endfor %}
    <p>{{ user_name }}</p> <!-- Display user's name -->

    {% if products %}
        <div class="message">
            <h1>{{ count }}</h1> <!-- Display count of products -->
        </div>

        {% for product in products %}
            <div id="{{ product.id }}" class="container">
                <img src="{{ url_for('static', filename='shop_page/images/' + product.name + '.png') }}" alt="photo"> <!-- Product image -->
                <div class="vertical-line-right"></div>
                <div class="text">
                    <h2>{{ product.name }}</h2> <!-- Product name -->
                    <h3>{{ product.price }}</h3> <!-- Product price -->
                    <h4>{{ product.description }}</h4> <!-- Product description -->
                    <button class="minus" id="{{ product.id }}">-</button> <!-- Button to decrease quantity -->
                    <h5>{{ product.count }}</h5> <!-- Product count -->
                    <button class="add" id="{{ product.id }}">+</button> <!-- Button to increase quantity -->
                </div>
            </div>
        {% endfor %} 

        <div class="price">
            {% for price, value in body['together'].items() %} 
                {% if value["tagname"] == "button" %}
                    <form method="post">
                        <{{ value["tagname"] }} type="submit" name="sent" value="{{ product_id }}" class="{{ value["class"] }}">{{ value["text"] }}</{{ value["tagname"] }}>
                    </form>
                {% else %}
                    <{{ value["tagname"] }}>{{ value["text"] }}</{{ value["tagname"] }}>
                {% endif %}
            {% endfor %}
        </div>         

        <div id="modal1" class="modal-window-div" style="display: none;">
            <form class="modal-window-form" method="post" enctype="multipart/form-data">
                <h6 class="modal-h6">Order Confirmation</h6>
                <!-- Input fields for order details -->
                <input type="text" name="username" placeholder="Enter name" class="input-data-users">
                <input type="text" name="forname" placeholder="Enter surname" class="input-data-users">
                <input type="number" name="phone-number" placeholder="Enter phone number" class="input-data-users">
                <input type="text" name="email" placeholder="Enter email" class="input-data-users">                
                <input type="text" name="city" placeholder="Enter city" class="input-data-users">
                <input type="text" name="post" placeholder="Enter post office" class="input-data-users">
                <input type="text" name="more_info" placeholder="Additional info" class="input-data-users">
                <button type="submit" class="modal-window-button" name="new-product" value="new">Confirm</button>
            </form>
        </div>
    {% else %}
        <h2>Cart is empty</h2>
    {% endif %}
    
    <script src="{{ url_for('static', filename='basket_page/js/modal_window.js') }}"></script>
    <script src="{{ url_for('static', filename='basket_page/js/cookie_minus.js') }}"></script>    
    <script src="{{ url_for('static', filename='basket_page/js/cookie_add.js') }}"></script> 
{% endblock %}

```
### Admin html
``` html
{% extends "base.html" %} <!-- Extend base.html for consistent structure -->

{% block title %}
    Admin Page <!-- Page title -->
{% endblock %}

{% block link %}
    <link rel="stylesheet" href="{{ url_for('static', filename='admin_page/css/style.css') }}"> <!-- Link to CSS file -->
{% endblock %}

{% block content %}
    {% for value, tagname in body['content'].items() %}
        {% if tagname['tagname'] == 'a' %}
            <{{ tagname['tagname'] }} href="{{ tagname['href'] }}">{{ tagname['text'] }}</{{ tagname['tagname'] }}>
        {% else %}
            <{{ tagname['tagname'] }}>{{ tagname['text'] }}</{{ tagname['tagname'] }}>
        {% endif %}
    {% endfor %}

    <p>{{ user_name }}</p> <!-- Display user's name -->

    <br>

    <form method="post">
        <div class="modal-window-add-div">
            <h6>Add New Product</h6>
            <button class="modal-window-add-button">+</button> <!-- Button to add new product -->
        </div>
    </form>

    <div id="modal1" class="modal-window-add" style="display: none;">
        <form class="modal-window-add-form" method="post" enctype="multipart/form-data">
            <h6 class="modal-h6">Add New Product</h6>
            <h6>Product Photo</h6>
            <input type="file" name="image-add" accept="image/*" class="image-add"> <!-- Input field for product image -->
            <input type="text" name="name-add" placeholder="Enter name" class="input-data-add"> <!-- Input field for product name -->
            <input type="number" name="price-add" placeholder="Enter price" class="input-data-add"> <!-- Input field for product price -->
            <input type="number" name="discount-add" placeholder="Enter discount" class="input-data-add"> <!-- Input field for product discount -->
            <input type="number" name="count-add" placeholder="Enter quantity" class="input-data-add"> <!-- Input field for product quantity -->
            <textarea name="description-add" placeholder="Enter description" class="input-label"></textarea> <!-- Textarea for product description -->
            <button type="submit" name="new-product" value="new">Confirm</button> <!-- Button to confirm adding new product -->
        </form>
    </div>

    <br>

    {% for product in products %}
        <form method="post">
            <div class="container">
                <img src="{{ url_for('static', filename='shop_page/images/' + product.name + '.png') }}" alt=""> <!-- Product image -->
                <div class="edit">
                    <button class="edit-img" id="{{ product.id }}">/</button> <!-- Button to edit product image -->
                </div>                
                <div class="vertical-line-right"></div>
                <div class="text">
                    {% for value, key in body['cataloge'].items() %}
                        {% if key["tagname"] == 'button' %}
                            <{{ key["tagname"] }} class="{{ key["class"] }}" id="{{ product.id }}">{{ key["text"] }}</{{ key["tagname"] }}>
                        {% elif key["tagname"] == 'h2' %}
                            <{{ key["tagname"] }}>{{ product.name }}</{{ key["tagname"] }}>
                            <div class="edit">
                                <button class="edit-text" name="name" id="{{ product.id }}">/</button> <!-- Button to edit product name -->
                            </div>
                        {% elif key["tagname"] == 'h3' and key['text'] == 'Price' %}
                            <{{ key["tagname"] }}>{{ key["text"] }} {{ product.price }}</{{ key["tagname"] }}> <!-- Display product price -->
                            <div class="edit">
                                <button class="edit-text" name="price" class="price" id="{{ product.id }}">/</button> <!-- Button to edit product price -->
                            </div>
                        {% elif key["tagname"] == 'h3' and key["text"] == 'Discount' %}
                            <{{ key["tagname"] }}>{{ key["text"] }} {{ product.discount }}</{{ key["tagname"] }}> <!-- Display product discount -->
                            <div class="edit">
                                <button class="edit-text" name="discount" id="{{ product.id }}">/</button> <!-- Button to edit product discount -->
                            </div>
                        {% elif key["tagname"] == 'h4' %}
                            <{{ key["tagname"] }}>{{ key["text"] }} {{ product.description }}</{{ key["tagname"] }}> <!-- Display product description -->
                            <div class="edit">
                                <button class="edit-text" name="description" id="{{ product.id }}">/</button> <!-- Button to edit product description -->
                            </div>
                        {% else %}
                            <{{ key["tagname"] }}>{{ key["text"] }}</{{ key["tagname"] }}> <!-- Display other information -->
                            <div class="edit">
                                <button class="edit-text" name="count" id="{{ product.id }}">/</button> <!-- Button to edit product quantity -->
                            </div>
                        {% endif %}
                    {% endfor %}
                    <h2>Capacity</h2>
                    <div class="div_memory">
                        <button class="memory">256</button>
                        <div class="edit">
                            <button class="edit-memory-1">/</button>
                        </div>
                        <button class="memory">512</button>
                        <div class="edit">
                            <button class="edit-memory-2">/</button>
                        </div>
                        <button class="memory">1028</button>
                        <div class="edit">
                            <button class="edit-memory-3">/</button>
                        </div>
                    </div>
                    <button name="del" id="{{ product.id }}" value="{{ product.id }}">Delete Product</button> <!-- Button to delete product -->
                </div>
                <div class="vertical-line-left"></div>
            </div>
        </form>
    {% endfor %}

    <div class="modal-window" style="display: none;">
        <form class="modal-form" method="post" enctype="multipart/form-data">
            <label for="" class="modal-label"></label>
            <input type="" accept="" name="" placeholder="" class="input-data">
            <button class="change-submit" type="submit" value="" name="set-changes">Save Changes</button> <!-- Button to save changes -->
        </form>
    </div>
    <script src="{{ url_for('static', filename='admin_page/js/editCookie.js') }}"></script> <!-- Script for editing cookies -->
{% endblock %}

```
## views в нашому проекті  
### shop views 
```python
import flask, os, json, pandas  # Importing necessary modules: Flask, os, json, pandas / Імпортуємо необхідні модулі: Flask, os, json, pandas
from project.settings import DATABASE  # Importing DATABASE constant from project.settings / Імпортуємо константу DATABASE з project.settings
from .models import Product  # Importing Product model from current package's models module / Імпортуємо модель Product з модуля models поточного пакету
from flask_login import current_user  # Importing current_user object from Flask-Login / Імпортуємо об'єкт current_user з Flask-Login

def render_shop():
    if len(Product.query.all()) == 0:  # Checking if there are no products in the database / Перевірка, чи в базі даних немає продуктів
        path = os.path.abspath(__file__+'/../Product.xlsx')  # Setting absolute path to Product.xlsx file / Встановлення абсолютного шляху до файлу Product.xlsx

    path_json = os.path.abspath(__file__ + "/../../static/shop_page/json/data.json")  # Setting absolute path to data.json file / Встановлення абсолютного шляху до файлу data.json
    with open(path_json, "r", encoding="utf-8") as file:  # Opening and reading data.json file / Відкриття та зчитування файлу data.json
        data_dict = json.load(file)  # Loading JSON data into data_dict variable / Завантаження даних JSON у змінну data_dict

    path_xlsx = os.path.abspath(__file__+"/../Product.xlsx")  # Setting absolute path to Product.xlsx file / Встановлення абсолютного шляху до файлу Product.xlsx

    read_xl = pandas.read_excel(io= path_xlsx,header=None, names=["name", "description", "price"])  # Reading Excel file into pandas DataFrame / Читання файлу Excel у DataFrame pandas

    list_products = []  # Initializing an empty list for products / Ініціалізація пустого списку для продуктів

    repeate_id = []  # Initializing an empty list for repeated IDs / Ініціалізація пустого списку для повторюваних ID

    for row in read_xl.iterrows():  # Iterating through rows of the DataFrame / Ітерація по рядках DataFrame
        row_data = row[1]  # Extracting row data / Витяг рядкових даних
        product = Product(  # Creating a Product object / Створення об'єкта Product
            name = row_data["name"],  # Assigning name attribute / Присвоєння атрибута name
            description = row_data["description"],  # Assigning description attribute / Присвоєння атрибута description
            price = row_data["price"],  # Assigning price attribute / Присвоєння атрибута price
            count = 1  # Assigning count attribute / Присвоєння атрибута count
        )

        DATABASE.session.add(product)  # Adding product to database session / Додавання продукту до сесії бази даних
        DATABASE.session.commit()  # Committing changes to the database / Застосування змін до бази даних

    if current_user.is_authenticated:  # Checking if user is authenticated / Перевірка, чи користувач аутентифікований
        is_authenticated = current_user.is_authenticated,  # Setting is_authenticated to True / Встановлення is_authenticated на True
        user_name = current_user.name,  # Setting user_name to current user's name / Встановлення user_name на ім'я поточного користувача
    else:
        is_authenticated = None  # Setting is_authenticated to None if user is not authenticated / Встановлення is_authenticated на None, якщо користувач не аутентифікований
        user_name = None  # Setting user_name to None / Встановлення user_name на None

    cookie = flask.request.cookies.get("products")  # Getting the "products" cookie from the request / Отримання куки "products" з запиту
    if cookie != None and cookie != 0:  # Checking if cookie exists and is not zero / Перевірка, чи існує куки і воно не є нулем
        for id in cookie:  # Iterating through IDs in cookie / Ітерація по ID у куці
            count = cookie.count(id)  # Counting occurrences of each ID / Підрахунок кількості входжень кожного ID
        try:
            return flask.render_template(template_name_or_list= "shop.html", body = data_dict,products = Product.query.all(), count = count, is_authenticated= is_authenticated, user_name= user_name, is_admin = current_user.is_admin)
        except UnboundLocalError:  # Handling UnboundLocalError exception / Обробка винятку UnboundLocalError
            count = 0  # Setting count to 0 / Встановлення count на 0
            return flask.render_template(template_name_or_list= "shop.html", body = data_dict,products = Product.query.all(), count = count, is_authenticated= is_authenticated, user_name= user_name, is_admin = current_user.is_admin)
    else:
        return flask.render_template(template_name_or_list= "shop.html", body = data_dict,products = Product.query.all(), is_authenticated= is_authenticated, user_name= user_name, is_admin = current_user.is_admin)

```
### reg/registration views 
```python
import flask  # Importing Flask module / Імпортуємо модуль Flask
from .models import Users  # Importing Users model from current package's models module / Імпортуємо модель Users з модуля models поточного пакету
from project.settings import DATABASE  # Importing DATABASE constant from project.settings / Імпортуємо константу DATABASE з project.settings
import os  # Importing os module / Імпортуємо модуль os
import json  # Importing json module / Імпортуємо модуль json
from sqlalchemy import create_engine  # Importing create_engine function from sqlalchemy / Імпортуємо функцію create_engine з sqlalchemy
# from flask_login import current_user

def render_reg():
    path_json = os.path.abspath(__file__ + "/../../static/reg_page/json/data.json")  # Setting absolute path to data.json file / Встановлення абсолютного шляху до файлу data.json
    with open(path_json, "r", encoding="utf-8") as file:  # Opening and reading data.json file / Відкриття та зчитування файлу data.json
        data_dict = json.load(file)  # Loading JSON data into data_dict variable / Завантаження даних JSON у змінну data_dict

    if flask.request.method == 'POST':  # Checking if request method is POST / Перевірка, чи метод запиту є POST
        if flask.request.form['name'] == 'Artem':  # Checking if name in form is 'Artem' / Перевірка, чи ім'я в формі є 'Artem'
            is_admin = True  # Setting is_admin to True if name is 'Artem' / Встановлення is_admin на True, якщо ім'я є 'Artem'
        else:
            is_admin = False  # Setting is_admin to False if name is not 'Artem' / Встановлення is_admin на False, якщо ім'я не є 'Artem'

        print(flask.request.form)  # Printing the form data / Виведення даних форми

        users = Users(  # Creating a Users object / Створення об'єкта Users
            name = flask.request.form['name'],  # Assigning name attribute / Присвоєння атрибута name
            email = flask.request.form['email'],  # Assigning email attribute / Присвоєння атрибута email
            password = flask.request.form['password'],  # Assigning password attribute / Присвоєння атрибута password
            is_admin = is_admin  # Assigning is_admin attribute / Присвоєння атрибута is_admin
        )
        
        DATABASE.session.add(users)  # Adding users to database session / Додавання користувачів до сесії бази даних
        DATABASE.session.commit()  # Committing changes to the database / Застосування змін до бази даних
        return flask.redirect('/')  # Redirecting to home page / Перенаправлення на домашню сторінку
        
    return  flask.render_template(template_name_or_list= "reg.html", body = data_dict)#, is_auth= current_user.is_authenticated
```
### log views
``` python
from flask import request, redirect, render_template  # Importing necessary modules: request, redirect, render_template / Імпортуємо необхідні модулі: request, redirect, render_template
from reg_page.models import Users  # Importing Users model from reg_page's models module / Імпортуємо модель Users з модуля models reg_page
import flask_login  # Importing flask_login module / Імпортуємо модуль flask_login
import os, flask, json  # Importing os, flask, json modules / Імпортуємо модулі os, flask, json
# from project.settings import login_manager
from flask_login import login_user, current_user  # Importing login_user and current_user from Flask-Login / Імпортуємо login_user і current_user з Flask-Login
from project.login_manager import login_manager  # Importing login_manager from project.login_manager / Імпортуємо login_manager з project.login_manager
import json  # Importing json module again / Імпортуємо модуль json знову

def show_authorization():
    print(0)  # Printing 0 (for debugging purposes?) / Виведення 0 (для налагодження?)
    path_json = os.path.abspath(__file__ + "/../../static/log_page/json/data.json")  # Setting absolute path to data.json file / Встановлення абсолютного шляху до файлу data.json
    with open(path_json, "r", encoding="utf-8") as file:  # Opening and reading data.json file / Відкриття та зчитування файлу data.json
        data_dict = json.load(file)  # Loading JSON data into data_dict variable / Завантаження даних JSON у змінну data_dict
        
    if request.method == 'POST':  # Checking if request method is POST / Перевірка, чи метод запиту є POST
        for user in Users.query.filter_by(name = flask.request.form["name"]):  # Iterating through Users with matching name / Ітерація по користувачах з відповідним ім'ям
            if user.password == flask.request.form["password"]:  # Checking if password matches / Перевірка, чи співпадає пароль
                login_user(user)  # Logging in the user / Авторизація користувача
                return flask.redirect("/")  # Redirecting to home page / Перенаправлення на домашню сторінку
            return "Невірний пароль"  # Returning message for incorrect password / Повернення повідомлення про невірний пароль

    return render_template(template_name_or_list='log.html', body=data_dict, is_auth = current_user.is_authenticated, login_meneger = login_manager)
    # Returning rendered template log.html with data_dict and authentication status / Повернення відображеного шаблону log.html з data_dict і статусом аутентифікації

```
### home views
``` python
import flask  # Importing Flask module / Імпортуємо модуль Flask
import os  # Importing os module / Імпортуємо модуль os
import json  # Importing json module / Імпортуємо модуль json
from flask_login import current_user  # Importing current_user from Flask-Login / Імпортуємо current_user з Flask-Login

def render_home():
    path_json = os.path.abspath(__file__ + "/../../static/home_page/json/data.json")  # Setting absolute path to data.json file / Встановлення абсолютного шляху до файлу data.json
    with open(path_json, "r", encoding="utf-8") as file:  # Opening and reading data.json file / Відкриття та зчитування файлу data.json
        data_dict = json.load(file)  # Loading JSON data into data_dict variable / Завантаження даних JSON у змінну data_dict
    
    print(current_user.is_authenticated)  # Printing current authentication status of user / Виведення поточного статусу аутентифікації користувача
    if current_user.is_authenticated:  # Checking if user is authenticated / Перевірка, чи користувач аутентифікований
        print(current_user.is_authenticated)  # Printing current authentication status again / Виведення поточного статусу аутентифікації ще раз
        return flask.render_template(
            template_name_or_list="home.html",  # Rendering home.html template / Відображення шаблону home.html
            body=data_dict,  # Passing data_dict as body / Передача data_dict як body
            is_authenticated=current_user.is_authenticated,  # Passing authentication status / Передача статусу аутентифікації
            user_name=current_user.name,  # Passing user's name / Передача імені користувача
            is_admin=current_user.is_admin  # Passing admin status / Передача статусу адміністратора
        )

    return flask.render_template(template_name_or_list="home.html", body=data_dict)
    # Rendering home.html template with data_dict if user is not authenticated / Відображення шаблону home.html з data_dict, якщо користувач не аутентифікований

```
### basket views
```python
import flask  # Importing Flask module / Імпортуємо модуль Flask
import os  # Importing os module / Імпортуємо модуль os
import json  # Importing json module / Імпортуємо модуль json
from shop_page import Product  # Importing Product model from shop_page / Імпортуємо модель Product з shop_page
from flask_login import current_user  # Importing current_user from Flask-Login / Імпортуємо current_user з Flask-Login
from project.main_config import mail  # Importing mail object from project.main_config / Імпортуємо об'єкт mail з project.main_config
from flask_mail import Message  # Importing Message class from flask_mail / Імпортуємо клас Message з flask_mail
# from reg_page.models import Users
from basket_page.models import Delivery  # Importing Delivery model from basket_page / Імпортуємо модель Delivery з basket_page

def render_basket():
    global id_products  # Declaring id_products as a global variable / Оголошення id_products як глобальної змінної
    path_json = os.path.abspath(__file__ + "/../../static/basket_page/json/data.json")  # Setting absolute path to data.json file / Встановлення абсолютного шляху до файлу data.json
    with open(path_json, "r", encoding="utf-8") as file:  # Opening and reading data.json file / Відкриття та зчитування файлу data.json
        data_dict = json.load(file)  # Loading JSON data into data_dict variable / Завантаження даних JSON у змінну data_dict

    if current_user.is_authenticated:  # Checking if user is authenticated / Перевірка, чи користувач аутентифікований
        is_authenticated = current_user.is_authenticated,  # Setting is_authenticated to True / Встановлення is_authenticated на True
        user_name = current_user.name,  # Setting user_name to current user's name / Встановлення user_name на ім'я поточного користувача
    else:
        is_authenticated = None  # Setting is_authenticated to None if user is not authenticated / Встановлення is_authenticated на None, якщо користувач не аутентифікований
        user_name = None  # Setting user_name to None / Встановлення user_name на None

    if flask.request.cookies.get('products'):  # Checking if 'products' cookie exists in the request / Перевірка, чи існує куки 'products' у запиті
        products = flask.request.cookies.get('products')  # Getting 'products' cookie data / Отримання даних куки 'products'
        count = len(products)  # Calculating number of products / Обчислення кількості продуктів
        count = count // 2 + 1  # Adjusting count (not sure about the logic here) / Виправлення count (не впевнений у логіці тут)
        list_products = []  # Initializing an empty list for products / Ініціалізація пустого списку для продуктів
        repeate_id = []  # Initializing an empty list for repeated IDs / Ініціалізація пустого списку для повторюваних ID

        for id_products in products:  # Iterating through product IDs in cookies / Ітерація по ID продуктів у куці
            count_products = products.count(id_products)  # Counting occurrences of each product ID / Підрахунок кількості входжень кожного ID продукту
            if id_products not in repeate_id:  # Checking if ID is not repeated / Перевірка, чи ID не є повторним
                list_products.append(Product.query.get(id_products))  # Adding product to list_products / Додавання продукту до list_products
                print(list_products)  # Printing list_products (for debugging?) / Виведення list_products (для налагодження?)
                repeate_id.append(id_products)  # Adding ID to repeate_id list / Додавання ID до списку repeate_id

        if flask.request.method == 'POST':  # Checking if request method is POST / Перевірка, чи метод запиту є POST
            print(flask.request.form['email'])  # Printing email from form data / Виведення електронної пошти з даних форми
            delivery = Delivery(  # Creating Delivery object / Створення об'єкта Delivery
                name=flask.request.form['username'],  # Assigning name attribute / Присвоєння атрибута name
                forname=flask.request.form['forname'],  # Assigning forname attribute / Присвоєння атрибута forname
                email=flask.request.form['email'],  # Assigning email attribute / Присвоєння атрибута email
                phone_number=flask.request.form['phone-number'],  # Assigning phone_number attribute / Присвоєння атрибута phone_number
                city=flask.request.form['city'],  # Assigning city attribute / Присвоєння атрибута city
                post=flask.request.form['post'],  # Assigning post attribute / Присвоєння атрибута post
                more_info=flask.request.form['more_info'],  # Assigning more_info attribute / Присвоєння атрибута more_info
            )

            message_text = f'Order № {Delivery.product}: \n\n' + f"Ваше замовлення {Delivery.product} було надіслано в місто {delivery.city} та в віділ {delivery.post} "  # Setting up message text / Встановлення тексту повідомлення
            for product in list_products:  # Iterating through products in list_products / Ітерація по продуктах у list_products
                message_text += f'{product.name}\n'  # Adding product name to message text / Додавання назви продукту до тексту повідомлення
    
            message = Message(  # Creating Message object / Створення об'єкта Message
                subject=f'Order № {list_products}',  # Setting subject of message / Встановлення теми повідомлення
                sender='arzon.art125@gmail.com',  # Setting sender email / Встановлення електронної адреси відправника
                recipients=[delivery.email],  # Setting recipients of message / Встановлення отримувачів повідомлення
                body=message_text  # Setting body of message / Встановлення тіла повідомлення
            )    
            mail.send(message)  # Sending email / Відправлення електронної пошти

        try:
            return flask.render_template(template_name_or_list='basket.html', body=data_dict, products=list_products, count=count, is_authenticated=is_authenticated, user_name=user_name, is_admin=current_user.is_admin)
        except UnboundLocalError:  # Handling UnboundLocalError exception / Обробка винятку UnboundLocalError
            count_products = 0  # Setting count_products to 0 / Встановлення count_products на 0
            return flask.render_template(template_name_or_list='basket.html', body=data_dict, products=list_products, count=count, is_authenticated=is_authenticated, user_name=user_name, is_admin=current_user.is_admin)
    
    else:
        print(data_dict)  # Printing data_dict (for debugging?) / Виведення data_dict (для налагодження?)
        return flask.render_template(template_name_or_list="basket.html", body=data_dict, is_authenticated=is_authenticated, user_name=user_name, is_admin=current_user.is_admin)

```
### admin views
``` python
def render_admin():
    path_json = os.path.abspath(__file__ + "/../../static/admin_page/json/data.json")  # Setting absolute path to data.json file / Встановлення абсолютного шляху до файлу data.json
    print(path_json)  # Printing path_json (for debugging?) / Виведення path_json (для налагодження?)
    with open(path_json, "r", encoding='utf-8') as file:  # Opening and reading data.json file / Відкриття та зчитування файлу data.json
        data_dict = json.load(file)  # Loading JSON data into data_dict variable / Завантаження даних JSON у змінну data_dict

    if flask.request.method == 'POST':  # Checking if request method is POST / Перевірка, чи метод запиту є POST
        try:
            if flask.request.form.get('new-product'):  # Checking if 'new-product' form field exists / Перевірка, чи існує поле форми 'new-product'
                product = Product(  # Creating new Product object / Створення нового об'єкта Product
                    name=flask.request.form['name-add'],  # Assigning name attribute / Присвоєння атрибута name
                    description=flask.request.form['description-add'],  # Assigning description attribute / Присвоєння атрибута description
                    price=flask.request.form['price-add'],  # Assigning price attribute / Присвоєння атрибута price
                    count=flask.request.form['count-add'],  # Assigning count attribute / Присвоєння атрибута count
                    discount=flask.request.form['discount-add']  # Assigning discount attribute / Присвоєння атрибута discount
                )
                DATABASE.session.add(product)  # Adding product to database session / Додавання продукту до сеансу бази даних
                DATABASE.session.commit()  # Committing changes to database / Збереження змін у базі даних
                image_file = flask.request.files['image-add']  # Getting image file from form data / Отримання зображення з даних форми
                image_file.save(os.path.abspath(__file__ + f'/../../../reg_projec/static/shop_page/images/{product.name}.png'))  # Saving image file to specified path / Збереження зображення за вказаним шляхом
            
            elif flask.request.form.get('del'):  # Checking if 'del' form field exists / Перевірка, чи існує поле форми 'del'
                product_id = int(flask.request.form['del'])  # Getting product ID from form data and converting to integer / Отримання ID продукту з даних форми і перетворення у ціле число
                print(product_id)  # Printing product_id (for debugging?) / Виведення product_id (для налагодження?)
                product_del = Product.query.get(product_id)  # Retrieving product to delete by ID / Отримання продукту для видалення за ID
                print(product_del)  # Printing product_del (for debugging?) / Виведення product_del (для налагодження?)
                if Product.query.get(product_id):  # Checking if product exists / Перевірка, чи існує продукт
                    DATABASE.session.delete(product_del)  # Deleting product from database session / Видалення продукту з сеансу бази даних
                    DATABASE.session.commit()  # Committing changes to database / Збереження змін у базі даних
                    os.remove(os.path.abspath(__file__ + f"/../../../reg_projec/static/shop_page/images/{product_del.name}.png"))  # Removing associated image file / Видалення пов'язаного файлу зображення

            elif flask.request.form.get('set-changes'):  # Checking if 'set-changes' form field exists / Перевірка, чи існує поле форми 'set-changes'
                product_data = flask.request.form.get("set-changes").split('-')  # Splitting form data to get product details / Розбивка даних форми для отримання деталей продукту
                print(product_data)  # Printing product_data (for debugging?) / Виведення product_data (для налагодження?)
                product_id = int(product_data[-1])  # Getting product ID from product_data and converting to integer / Отримання ID продукту з product_data і перетворення у ціле число
                get_product = Product.query.get(product_id)  # Retrieving product to modify by ID / Отримання продукту для зміни за ID
                abspath = os.path.abspath(__file__ + "/../../../reg_projec/static/shop_page/images")  # Setting absolute path to images directory / Встановлення абсолютного шляху до каталогу зображень

                if "0" == product_data[0]:  # Checking if action is for image change / Перевірка, чи дія стосується зміни зображення
                    os.remove(abspath + f'/{get_product.name}.png')  # Removing old image file / Видалення старого файлу зображення
                    new_image = flask.request.files['image']  # Getting new image file from form data / Отримання нового файлу зображення з даних форми
                    new_image.save(abspath + f'/{get_product.name}.png')  # Saving new image file / Збереження нового файлу зображення

                elif '1' == product_data[0]:  # Checking if action is for name change / Перевірка, чи дія стосується зміни назви
                    if product_data[1] == '1':  # Checking specific action for name change / Перевірка конкретної дії для зміни назви
                        print(100)  # Printing 100 (for debugging?) / Виведення 100 (для налагодження?)
                        new_product_name = flask.request.form['name']  # Getting new product name from form data / Отримання нової назви продукту з даних форми
                        os.rename(src=abspath + f'\{get_product.name}.png', dst=abspath + f'\{new_product_name}.png')  # Renaming image file / Перейменування файлу зображення
                        get_product.name = new_product_name  # Updating product name / Оновлення назви продукту
                        DATABASE.session.commit()  # Committing changes to database / Збереження змін у базі даних

                    elif '2' == product_data[1]:  # Checking specific action for price change / Перевірка конкретної дії для зміни ціни
                        print(200)  # Printing 200 (for debugging?) / Виведення 200 (для налагодження?)
                        new_product_name = flask.request.form["price"]  # Getting new product price from form data / Отримання нової ціни продукту з даних форми
                        get_product.price = new_product_name  # Updating product price / Оновлення ціни продукту
                        DATABASE.session.commit()  # Committing changes to database / Збереження змін у базі даних

                    elif '3' == product_data[1]:  # Checking specific action for description change / Перевірка конкретної дії для зміни опису
                        new_product_name = flask.request.form["description"]  # Getting new product description from form data / Отримання нового опису продукту з даних форми
                        get_product.description = new_product_name  # Updating product description / Оновлення опису продукту
                        DATABASE.session.commit()  # Committing changes to database / Збереження змін у базі даних
                    elif '4' == product_data[1]:  # Checking specific action for count change / Перевірка конкретної дії для зміни кількості
                        new_product_name = flask.request.form["count"]  # Getting new product count from form data / Отримання нової кількості продукту з даних форми
                        get_product.count = new_product_name  # Updating product count / Оновлення кількості продукту
                        DATABASE.session.commit()  # Committing changes to database / Збереження змін у базі даних
                
        except Exception as e:
            print(e)  # Printing exception (for debugging?) / Виведення винятку (для налагодження?)

    if current_user.is_authenticated and current_user.is_admin:
        return flask.render_template(  # Rendering admin.html template with data / Відображення шаблону admin.html з даними
            body=data_dict,
            template_name_or_list='admin.html',
            products=Product.query.all(),  # Querying all products from database / Отримання всіх продуктів з бази даних
            is_authenticated=current_user.is_authenticated,
            user_name=current_user.name,
            is_admin=current_user.is_admin
        )

    return flask.redirect('/')  # Redirecting to home page if user is not authenticated or not an admin / Перенаправлення на домашню сторінку, якщо користувач не аутентифікований або не адміністратор

```
## Всі бази даних які ми зробили та використвовуємо

### Prduct database
``` python
from project.settings import DATABASE  # Importing DATABASE from project settings / Імпорт DATABASE з налаштувань проекту

class Product(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)  # Creating id column as primary key / Створення стовпця id як первинного ключа
    name = DATABASE.Column(DATABASE.String(100), nullable=True)  # Creating name column as String with max length 100, nullable / Створення стовпця name як рядок з максимальною довжиною 100 символів, можливість є
    description = DATABASE.Column(DATABASE.Text, nullable=True)  # Creating description column as Text, nullable / Створення стовпця description як текст, можливість є
    price = DATABASE.Column(DATABASE.Integer, nullable=True)  # Creating price column as Integer, nullable / Створення стовпця price як ціле число, можливість є
    count = DATABASE.Column(DATABASE.Integer, nullable=True)  # Creating count column as Integer, nullable / Створення стовпця count як ціле число, можливість є
    discount = DATABASE.Column(DATABASE.Integer, nullable=True)  # Creating discount column as Integer, nullable / Створення стовпця discount як ціле число, можливість є

    def __repr__(self):
        return f"{self.name} Номер в базі - {self.id}"  # Returning representation of Product instance / Повернення представлення екземпляра продукту

```

### Users database
``` python
from project.settings import DATABASE  # Importing DATABASE from project settings / Імпорт DATABASE з налаштувань проекту

class Users(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)  # Creating id column as primary key / Створення стовпця id як первинного ключа
    name = DATABASE.Column(DATABASE.String(50))  # Creating name column as String with max length 50 / Створення стовпця name як рядок з максимальною довжиною 50 символів
    email = DATABASE.Column(DATABASE.String(50))  # Creating email column as String with max length 50 / Створення стовпця email як рядок з максимальною довжиною 50 символів
    password = DATABASE.Column(DATABASE.String(50))  # Creating password column as String with max length 50 / Створення стовпця password як рядок з максимальною довжиною 50 символів
    is_admin = DATABASE.Column(DATABASE.Boolean)  # Creating is_admin column as Boolean / Створення стовпця is_admin як логічний тип (Boolean)
    
    def __repr__(self):
        return f'Користувач {self.name}'  # Returning representation of Users instance / Повернення представлення екземпляра користувача
    
    def is_active(self):
        return True  # Method to indicate that user is active / Метод, що підтверджує активність користувача
    
    def get_id(self):
        return str(self.id)  # Method to return string representation of user id / Метод для повернення рядкового представлення ідентифікатора користувача
    
    def is_authenticated(self):
        return True  # Method to indicate that user is authenticated / Метод, що підтверджує аутентифікацію користувача
    
    def is_anonymous(self):
        return False  # Method to indicate that user is not anonymous / Метод, що підтверджує, що користувач не анонімний

```

### Delivery/Order database
``` python
from project.settings import DATABASE  # Importing DATABASE from project settings / Імпорт DATABASE з налаштувань проекту

class Delivery(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)  # Creating id column as primary key / Створення стовпця id як первинного ключа
    name = DATABASE.Column(DATABASE.String(50))  # Creating name column as String with max length 50 / Створення стовпця name як рядок з максимальною довжиною 50 символів
    forname = DATABASE.Column(DATABASE.String(100))  # Creating forname column as String with max length 100 / Створення стовпця forname як рядок з максимальною довжиною 100 символів
    email = DATABASE.Column(DATABASE.String(50))  # Creating email column as String with max length 50 / Створення стовпця email як рядок з максимальною довжиною 50 символів
    phone_number = DATABASE.Column(DATABASE.String(50))  # Creating phone_number column as String with max length 50 / Створення стовпця phone_number як рядок з максимальною довжиною 50 символів
    city = DATABASE.Column(DATABASE.Text())  # Creating city column as Text / Створення стовпця city як текст
    post = DATABASE.Column(DATABASE.Text())  # Creating post column as Text / Створення стовпця post як текст
    more_info = DATABASE.Column(DATABASE.Text())  # Creating more_info column as Text / Створення стовпця more_info як текст
    product = DATABASE.Column(DATABASE.String(50))  # Creating product column as String with max length 50 / Створення стовпця product як рядок з максимальною довжиною 50 символів

    def __reor__(self):  # Typo correction: should be __repr__ instead of __reor__ / Виправлення орфографічної помилки: повинно бути __repr__ замість __reor__
        return f'Користувач {self.email}'  # Returning representation of Delivery instance / Повернення представлення екземпляра доставки

```
## як провести міграція та ініціалізувати бд/базу даних 
### 1. ініціалізація
``` dash
flasl --app settings db ini
```
### 2. міграція
```dash
flask --app settings db migrate
```
### 3. завершення проведень міграцій
```dash
flask --app settings db upgrade
```
## Що таке бази даних 
###
База даних зберігає всю інформацію про користувачів, товари та замовлення. Ми використовуємо SQLite3 для
простоти налаштування та використання у невеликих проектах. id у таблицях бази даних використовується для 
унікальної ідентифікації записів.

## усі файли js які ми використовували та створили 
### shop set_cookies
``` javascript
const listButtons = document.querySelectorAll('.buy');  // Selecting all elements with class 'buy' and storing them in listButtons / Вибір всіх елементів з класом 'buy' і збереження їх в listButtons
for (let count = 0; count < listButtons.length; count++) {  // Looping through each button in listButtons / Цикл по кожній кнопці в listButtons
    let button = listButtons[count];  // Assigning current button to variable button / Присвоєння поточної кнопки змінній button
    button.addEventListener(  // Adding event listener to button / Додавання обробника подій до кнопки
        type = 'click',  // Event type is 'click' / Тип події - 'click'
        listener = function (event) {  // Event listener function declaration / Оголошення функції обробника подій
            if (document.cookie == '') {  // Checking if document.cookie is empty / Перевірка, чи document.cookie порожній
                document.cookie = `products=${button.id}; path=/`;  // Setting cookie with product id / Встановлення cookie з ідентифікатором продукту
            } else {
                product_id = document.cookie.split('=')[1];  // Extracting product_id from document.cookie / Вилучення product_id з document.cookie
                document.cookie = `products=${product_id} ${button.id}; path=/`;  // Appending new product id to existing cookie / Додавання нового ідентифікатора продукту до існуючого cookie
            }
        }
    );
}

```
### basket cookie_add
``` javascript
const buttons = document.querySelectorAll('.add');  // Selecting all elements with class 'add' and storing them in buttons / Вибір всіх елементів з класом 'add' і збереження їх в buttons
for (let i = 0; i < buttons.length; i++) {  // Looping through each button in buttons / Цикл по кожній кнопці в buttons
    let button = buttons[i];  // Assigning current button to variable button / Присвоєння поточної кнопки змінній button
    button.addEventListener(  // Adding event listener to button / Додавання обробника подій до кнопки
        type = 'click',  // Event type is 'click' / Тип події - 'click'
        listener = function(event) {  // Event listener function declaration / Оголошення функції обробника подій
            if (document.cookie == "") {  // Checking if document.cookie is empty / Перевірка, чи document.cookie порожній
                document.cookie = `products=${button.id}; path=/`;  // Setting cookie with product id / Встановлення cookie з ідентифікатором продукту
                button.previousElementSibling.textContent = +button.previousElementSibling.textContent + 1;  // Incrementing previous sibling's text content by 1 / Збільшення текстового вмісту попереднього сусіда на 1
            } else {
                let currentProduct = document.cookie.split('=')[1];  // Extracting current product ids from document.cookie / Вилучення поточних ідентифікаторів продуктів з document.cookie
                document.cookie = `products=${currentProduct} ${button.id}; path=/`;  // Appending new product id to existing cookie / Додавання нового ідентифікатора продукту до існуючого cookie
                button.previousElementSibling.textContent = +button.previousElementSibling.textContent + 1;  // Incrementing previous sibling's text content by 1 / Збільшення текстового вмісту попереднього сусіда на 1
            }
        }
    );
}

```
### basket cookie_minus
``` javascript
let listButtonsMinus = document.querySelectorAll(".minus");  // Selecting all elements with class 'minus' and storing them in listButtonsMinus / Вибір всіх елементів з класом 'minus' і збереження їх в listButtonsMinus
for (let count = 0; count < listButtonsMinus.length; count++ ) {  // Looping through each button in listButtonsMinus / Цикл по кожній кнопці в listButtonsMinus
    let button = listButtonsMinus[count];  // Assigning current button to variable button / Присвоєння поточної кнопки змінній button
    button.addEventListener(  // Adding event listener to button / Додавання обробника подій до кнопки
      type = "click",  // Event type is 'click' / Тип події - 'click'
      listener = (event) => {  // Event listener function declaration / Оголошення функції обробника подій
        let cookiesProducts = document.cookie.split('=')[1];  // Extracting product ids from document.cookie / Вилучення ідентифікаторів продуктів з document.cookie
        
        let listIdProducts = cookiesProducts.split(" ");  // Splitting extracted product ids into array listIdProducts / Розбивка вилучених ідентифікаторів продуктів на масив listIdProducts
        
        for (let index = 0; index < listIdProducts.length; index++) {  // Looping through each id in listIdProducts / Цикл по кожному ідентифікатору в listIdProducts
          if (button.id == listIdProducts[index]) {  // Checking if button id matches current id in listIdProducts / Перевірка, чи ідентифікатор кнопки відповідає поточному ідентифікатору в listIdProducts
            listIdProducts.splice(index, 1);  // Removing current id from listIdProducts / Видалення поточного ідентифікатора з listIdProducts
            button.nextElementSibling.textContent = Number(button.nextElementSibling.textContent) - 1;  // Decreasing text content of next sibling by 1 / Зменшення текстового вмісту наступного сусіда на 1
            break;  // Exiting loop / Вихід з циклу
          }
        }
        
        if (button.nextElementSibling.textContent == 0) {  // Checking if next sibling's text content is 0 / Перевірка, чи текстовий вміст наступного сусіда дорівнює 0
            document.querySelector(`#product-${button.id}`).remove();  // Removing element with id 'product-{button.id}' from the document / Видалення елемента з ідентифікатором 'product-{button.id}' з документу
        }
        
        document.cookie = `products=${listIdProducts.join(" ")}; path=/`;  // Setting updated list of product ids as cookie / Встановлення оновленого списку ідентифікаторів продуктів як cookie
        
        if (document.cookie.split('=')[1] == '') {  // Checking if document.cookie is empty / Перевірка, чи document.cookie порожній
            let h2 = document.createElement('h2');  // Creating new h2 element / Створення нового елемента h2
            h2.textContent = 'Корзина порожня';  // Setting text content of h2 element / Встановлення текстового вмісту для елемента h2
            document.body.append(h2);  // Appending h2 element to document body / Додавання елемента h2 до тіла документа
        }
      }
    );
}

```
### basket modal_window
``` javascript
let modal_window = document.querySelectorAll(".confirm");  // Selecting all elements with class 'confirm' and storing them in modal_window / Вибір всіх елементів з класом 'confirm' і збереження їх в modal_window
for (let count = 0; count < modal_window.length; count++) {  // Looping through each element in modal_window / Цикл по кожному елементу в modal_window
    let window = modal_window[count];  // Assigning current element to variable window / Присвоєння поточного елемента змінній window
    window.addEventListener(  // Adding event listener to element / Додавання обробника подій до елементу
        type = 'click',  // Event type is 'click' / Тип події - 'click'
        listener = (event) => {  // Event listener function declaration / Оголошення функції обробника подій
            event.preventDefault();  // Preventing default behavior of the event / Попередження типової поведінки події
            document.querySelector(".modal-window-div").style.display = "flex";  // Displaying the modal window by setting its display style to 'flex' / Відображення модального вікна шляхом встановлення його стилю відображення на 'flex'
        }
    );
}

```
### admin editCookie
``` javascript
let listButtonImage = document.querySelectorAll(".edit-img");

console.log(listButtonImage);
for (let count = 0; count < listButtonImage.length; count++) {
    let button = listButtonImage[count];
    button.addEventListener(
        'click',  // Event type is 'click' / Тип події - 'click'
        (event) => {
            console.log('img');
            event.preventDefault();
            document.querySelector(".modal-window").style.display = "flex";
            let inputData = document.querySelector(".input-data");
            inputData.type = "file";
            inputData.accept = "image/*";
            inputData.name = "image";
            document.querySelector(".modal-label").textContent = "Оберіть нове зображення:";
            document.querySelector('.change-submit').value = `0-${button.id}`;
        }
    );
}

let listButtonName = document.querySelectorAll(".edit-text");
console.log(listButtonName);
for (let count = 0; count < listButtonName.length; count++) {
    let button = listButtonName[count];
    button.addEventListener(
        'click',  // Event type is 'click' / Тип події - 'click'
        (event) => {
            console.log('text');
            event.preventDefault();
            document.querySelector(".modal-window").style.display = "flex";
            let inputData = document.querySelector(".input-data");
            inputData.type = "text";
            inputData.placeholder = "Введіть нову назву продукту";
            if (button.name === "name") {
                document.querySelector(".modal-label").textContent = "Задайте нову назву продукту:";
                document.querySelector('.change-submit').value = `1-1-${button.id}`;
                inputData.name = "name";
            }
            if (button.name === "price") {
                document.querySelector(".modal-label").textContent = "Задайте нову ціну продукту:";
                document.querySelector('.change-submit').value = `1-2-${button.id}`;
                inputData.name = "price";
            }
            if (button.name === "description") {
                document.querySelector(".modal-label").textContent = "Задайте новий опис продукту:";
                document.querySelector('.change-submit').value = `1-3-${button.id}`;
                inputData.name = "description";
            }
            if (button.name === "count") {
                document.querySelector(".modal-label").textContent = "Задайте нову кількість товару:";
                document.querySelector('.change-submit').value = `1-4-${button.id}`;
                inputData.name = "count";
            }
        }
    );
}

let listButton = document.querySelectorAll('.modal-window-add-button');
console.log(listButton);
console.log(200);
for (let count = 0; count < listButton.length; count++) {
    let button = listButton[count];
    console.log(200);
    button.addEventListener(
        'click',  // Event type is 'click' / Тип події - 'click'
        (event) => {
            event.preventDefault();
            document.querySelector(".modal-window-add").style.display = "flex";
            console.log(200);
        }
    );
}

```
## Висновок
Робота над проектом "Інтернет Магазин" була дуже корисною. Ми покращили свої навички програмування, вивчили 
нові бібліотеки та інструменти, а також отримали цінний досвід командної роботи. Цей проект став важливим 
кроком у нашій кар'єрі розробників.
