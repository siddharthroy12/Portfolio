# My Portfolio Website built using Django

> Visit the live website at https://siddharthroy.pythonanywhere.com/


# Environment Variable setup

```
SECRET_KEY= Your Secret Key
EMAIL_HOST_USER= Your Bot email
EMAIL_HOST_PASSWORD= Your Bot email password
EMAIL_AUTHOR= Your email to send messages
DEBUG=True # Set it to false for production
```


## To run the website

- `git clone https://github.com/siddharthroy12/Portfolio`
- `pipenv install`
- `pipenv shell`
- `touch .env # Fill it with the Evironment Variables`
- `python3 manage.py createsuperuser`
- `python3 manage.py migrate`
- `python3 manage.py runserver`