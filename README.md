# test-oauth

Django OAuth 2 Test

```
$ pipenv --python 3.8
```
## Provider

test_provider directory.

```
$ pipenv install django-oauth-toolkit django-cors-headers
```

```
$ pipenv shell
$ manage.py migrate
$ manage.py createsuperuser
$ manage.py runserver 8000
```

open http://127.0.0.1:8000/admin/

When logged in, open http://127.0.0.1:8000/o/applications/

and add applications

```
Name: test-consumer (any)
Client type: Confidential
Authorization grant type: Authorization code
Redirect urls:
http://localhost:8001/accounts/testprovider/login/callback/
http://127.0.0.1:8001/accounts/testprovider/login/callback/
```

## Consumer

test_consumer directory.

```
$ pipenv install django-allauth
```

```
$ manage.py migrate
$ manage.py createsuperuser
$ manage.py runserver 8001
```

open http://127.0.0.1:8001/admin/ and add "Social applications".

open http://127.0.0.1:8001/ and click "Test Provider でログイン" (Login with test provider)
