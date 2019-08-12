

# Reference Tutorial
* ``` https://github.com/pallets/flask/tree/1.0.2/examples/tutorial ```
*  ```http://flask.pocoo.org/docs/1.0/tutorial/#tutorial```


# Project Details
* Source director under CMPE287. 
    * /SeeCow
* Set up virtual python environment for SeeCow
``` python3 -m venv venv```
```. venv/bin/activate```
```pip install --upgrade pip```
```pip install -U Flask```

```export FLASK_APP=seecow```
```export FLASK_ENV=development```
```flask init-db ```
```flask run```

* Step1 :  ```http://flask.pocoo.org/docs/1.0/tutorial/factory/``` has to work
    * added ```@app.route('/')``` to get to root URL 
        * Local/Single route - for testing purposes
    * Works

* Step 2:  Fix DB issues with SQLite
    * from command line (after setting FLASK_APP, FLASK_ENV)
        * ``` flask init-db ```
    * Bug was in name of .sql file --> should be ```schema.sql```
    * Basic screen is now visible


* Step 3: Blueprints & Views
    * Views are registered into Blueprint
    * Blueprint is registered with app when available from App Factory

* Step 4: User Management
    * ```/register``` checks for existence of user in DB
        * If yes --> redirect to ```/login```
        * If no --> get new user name, save password as hash
    * ```/login``` success
        * ```session['user_id'] = user['id']```
            * ```session``` preserves state across requests
            * ```g``` needs to be updated with  user record using ```session['user_id']```
    * ```login_required```
        * decorator that can be used to intercept (like Aspect Oriented Programming) user calls
        * forces login even if route is hacked
    * Queries with parameters
        * The database library will take care of escaping the values to prevent SQL injection attack.
    
* Step 5: Unit Tests
    * ``` pip install pytest coverage```

## Security safe guards
* Display list only if user is authorized
    * Needs ```{% if current_user.is_authenticated %}```
    * This is set by LoginManager ```from flask_login import LoginManager```
    * Set variable for decorators to work ``` login_manager = LoginManager()```
    * Grab user when loaded ```@login_manager.user_loader```
    * By getting from global ```login_manager(g.user)```

* Ensure that next url is also safe
    * ```is_safe_url(next)```
    * Official Documentation is missing. However from WayBack machine this is the output:
    * Ref: From Wayback machine - snippets
    * http://flask.pocoo.org/snippets/62/


Securely Redirect Back
Posted by Armin Ronacher on 2011-07-28 @ 11:44 and filed in Security

A common pattern with form processing is to automatically redirect back to the user. There are usually two ways this is done: by inspecting a next URL parameter or by looking at the HTTP referrer. Unfortunately you also have to make sure that users are not redirected to malicious attacker's pages and just to the same host. If you are using Flask-WTF there is a nicer way: Redirects with Flask-WTF.

A function that ensures that a redirect target will lead to the same server is here:
````
from urlparse import urlparse, urljoin
from flask import request, url_for

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc
````
A simple way to to use it is by writing a get_redirect_target function that looks at various hints to find the redirect target:

````
def get_redirect_target():
    for target in request.values.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return target
````
Since we don't want to redirect to the same page we have to make sure that the actual back redirect is slightly different (only use the submitted data, not the referrer). Also we can have a fallback there:
````
def redirect_back(endpoint, **values):
    target = request.form['next']
    if not target or not is_safe_url(target):
        target = url_for(endpoint, **values)
    return redirect(target)
````
It will tried to use next and the referrer first and fall back to a given endpoint. You can then use it like this in the views:

````
@app.route('/login', methods=['GET', 'POST'])
def login():
    next = get_redirect_target()
    if request.method == 'POST':
        # login code here
        return redirect_back('index')
    return render_template('index.html', next=next)
````
The or is important so that we have a redirect target if all hints fail (in this case the index page).

In the template you have to make sure to relay the redirect target:

````
<form action="" method=post>
  <dl>
    <dt>Username:
    <dd><input type=text name=username>
    <dt>Password:
    <dd><input type=password name=password>
  </dl>
  <p>
    <input type=submit value=Login>
    <input type=hidden value="{{ next or '' }}" name=next>
</form>
````
The or here is just here to make None become an empty string.

This snippet by Armin Ronacher can be used freely for anything you like. Consider it public domain.

## Login Manager use 
* Ref: https://flask-login.readthedocs.io/en/latest/ 
* User Class
    * https://github.com/shekhargulati/flask-login-example/blob/master/flask-login-example.py
    * 





## Deploy to Production
* Ref: http://flask.pocoo.org/docs/1.0/tutorial/deploy/ 
    * ``` pip install wheel```
    * ``` python setup.py bdist_wheel ```
        * Will generate file in ``` dist/seecow-1.0.0-py3-none-any.whl ``` 
    * Installation
        * Copy to new machine
        * Set up venv
        * ``` pip install seecow-1.0.0-py3-none-any.whl```
        * ``` export FLASK_APP=seecow```
        * ``` flask init-db ```
    * Instance folder is created in a different location
        * ``` venv/var/seecow-instance ``` <-- This is why SECRET is placed in this folder>
    * Configure secret
        * ``` python -c 'import os; print(os.urandom(16))' ```
        * In ``` venv/var/seecow-instance/config.py```
            * ``` SECRET_KEY = b'_5#y2L"F4Q8z\n\xec]/' ```
    * Use Production Server
        * ``` Werkzeug ``` is for development/debug purposes
        * ``` pip install waitress ```
        * ``` waitress-serve --call 'seecow:create_app' ```

## Deploy on AWS Elastic Beanstalk
* Ref: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html 




## Miscellaneous info
* Fix:  ```sqlite3.OperationalError: no such table: post``` in ```blog.py```
    * Ref: https://stackoverflow.com/questions/28126140/python-sqlite3-operationalerror-no-such-table
````
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "PupilPremiumTable.db")
with sqlite3.connect(db_path) as db:
````



