<img align="right" width="120" alt="rmotr.com" src="https://user-images.githubusercontent.com/7065401/45454218-80bee800-b6b9-11e8-97bb-bb5e7675f440.png">

# Coinmarketcap clone

Today, we want to build a copy of [https://coinmarketcap.com/](https://coinmarketcap.com/) 💪

We will set everything up from scratch, including Python requirements, Django project, database schema, etc. If you are not familiar with Django, we always recommend to take a look at the [official documentation](https://docs.djangoproject.com/en/2.0/), and always refer to it when you have doubts.

This project is part of RMOTR's [Web Development Career](https://rmotr.com/web-development-django-python-course).

If we do it right, the final result should look something like this:
![image](https://user-images.githubusercontent.com/1155573/38173232-207f77b0-3591-11e8-9e95-cd14da306186.png)

So, let's get started! 🎉

## 1) Setting up the environment

Before we get started with Django, we need to make sure our local Python environment is properly set up. For that, we will use `virtualenv` and the awesome `virtualenvwrapper` tool.

*note: this app has been developed using Python 3.5*

```bash
$ mkvirtualenv -p $(which python3.5)
$ pip install -r requirements/base.txt
```

_Note: If you're using RMOTR Notebooks, you don't need to create a virtualenv_

## 2) Creating the Django project

Now that we have the environment ready, we can create our Django project and app.

```bash
$ django-admin startproject coinmarketcap

$ cd coinmarketcap/
$ django-admin startapp cryptocoins
```

## 3) Run the app for the first time

If we did everything right, we should be able to run our Django app now. It will be a completely empty app, but at least we should see a welcome page, confirming that our initial set up is working fine.

```bash
$ make runserver
```

Once the Django server is running, visit [http://localhost:8080/](http://localhost:8080/) in your browser. If you see the following page, that means your Django project is fully up and running. 💪 🎉 🙌

![image](https://user-images.githubusercontent.com/1155573/38176781-7765511e-35cb-11e8-9950-81b87a641111.png)


## 4) The data model

First we need to add `cryptocoins` to our `settings.INSTALLED_APPS`. Apps are a way that Django has to modularize projects.

Second, we'll copy the data model from Coinmarketcap. This is an example of the information we will store in our `Cryptocurrency` model.

```bash
{
  id: "bitcoin",
  name: "Bitcoin",
  symbol: "BTC",
  rank: "1",
  price_usd: "6974.84",
  price_btc: "1.0",
  24h_volume_usd: "4666070000.0",
  market_cap_usd: "118238359535",
  available_supply: "16952125.0",
  total_supply: "16952125.0",
  max_supply: "21000000.0",
  percent_change_1h: "2.26",
  percent_change_24h: "-1.19",
  percent_change_7d: "-18.72",
  last_updated: "1522611567"
}
```

All we need to do is create a new model in the `cryptocoins/models.py` module, and match all the information as different fields of the model.

Once the model class is created, we will now build our database schema using the magnificent Django ORM.

```bash
$ django-admin makemigrations
$ django-admin migrate
```

For the purpose of this project, it will be very handy to import some testing data. Coinmarketcap has a cool and open API we can use to load data into our app. Just make a request to [https://api.coinmarketcap.com/v1/ticker/](https://api.coinmarketcap.com/v1/ticker/), loop through all results in the JSON response, and for each of them create an instance of our new `Cryptocurrency` model.

## 5) Accessing the Django Admin interface

The Django Admin is one of the most famous features of this framework. It will allow us to access, add, edit and delete (CRUD) all our models out of the box.
To be able to access it, we will first need to create an admin user. To do so, execute the following command.

```bash
$ django-admin createsuperuser
```

Make sure to register the app models in the `cryptocoins/admin.py` module. If you are done, just visit [http://localhost:8000/admin/](http://localhost:8000/admin/) and login using your admin user. You should see a page similar to this one.

![image](https://user-images.githubusercontent.com/1155573/38176867-231a00b2-35cd-11e8-83cb-472b57e1c56b.png)

## 6) Display data in an actual template

It's great to have the Django Admin, but most of the times you will need to write your own templates. To prevent you from wasting time writing HTML and CSS code, we already provide you with a static version of the app template, named `static-index.html`. Just make a copy of it, and modify it properly using the Django Template Engine to make it show all the cryptocurrencies dynamically.

Of course, you will also need to define a custom view (provable a TemplateView is a good choice for this use case), and link it with the correct URL rule.

## Final notes

That's all! 🎉 We have a fully functional Django App just by completing these few steps.  Of course, this is probably using just a 10% of all Django features. But, don't worry. We will have plenty of time to cover the rest in our [Web Development with Django](https://rmotr.com/web-development-django-python-course) career 😁.
