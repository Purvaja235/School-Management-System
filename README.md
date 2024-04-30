# School Management System

### Follow the instructions to run this system

## 1. Clone this repo

```
git clone https://github.com/prakashtaz0091/school-management-system
```

## 2. Create virtualenv of your choice for example in linux

```
pip install virtualenv

virtualenv myenv

source myenv/bin/activate

```

## 3. Create virtualenv in windows NOTE: switch to cmd instead of powershell

```
python -m venv env

env\Scripts\activate


```

## 3. Move to project directory

```
cd project
```

## 4. Install required packages and libraries

```
pip install -r requirements.txt
```

## 5. Run database migrations and migrate them

```
python manage.py makemigrations

python manage.py migrate
```

## 5. Start the development server,

### Note : If python doesn't works for you, try python3 or your installed version of python

```
python manage.py runserver
```

## 6. Open link in browser

```
http://localhost:8000
```
