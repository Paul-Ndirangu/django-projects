# Django Rest Framework

## Simple Django REST API for Food Items

This is a simple REST API built with Django REST Framework that allows you to manage food items. You can:

* **GET** existing food items.
* **POST** new food items.

### Features

* Clean and concise code implementation.
* Model-based API for food items.
* Standard GET and POST requests supported.
* Uses serializers for data validation and transformation.

### Getting Started

1. Clone the repository:

```bash
git clone https://github.com/Paul-Ndirangu/django-projects.git
```

```bash
cd REST-API-With-Django-REST-Framework
```


2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Run the development server:

```bash
python manage.py runserver
```

6. Access the API at http://127.0.0.1:8000/

### API Endpoints

#### GET /api/v1/foods/

Retrieves a list of all food items.

#### POST /api/v1/foods/

Creates a new food item.

**Request Body:**

```json
{
  "name": "string",
  "description": "string"
}
```

**Response:**

```json
{
  "id": integer,
  "name": "string",
  "description": "string"
}
```

### Customization

* You can modify the `models.py` file to add additional fields to the food item model.
* You can customize the serializers in `serializers.py` to define validation rules and data manipulation.
* You can change the API authentication and permissions settings in `settings.py`.

**NOTE**:**Remember to create superuser**


### Contribution

Feel free to contribute to this project by creating pull requests with improvements or new features.

### License

This project is licensed under the MIT License. See the LICENSE file for details.

