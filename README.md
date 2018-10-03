# WordCrawlerAPI

This API will take a url(s), a word, and will count the number of matches (case-sensitive). 

### How it works

This web crawler is responsible for crawling the URL(s) reported and returning a response containing a json with the number of occurrences of the reported word, per site.

Example:

http://127.0.0.1:5000/?url=www.pyhon.org&url=flask.pocoo.org&url=www.djangoproject.com&word=docs&ignorecase=true

```?url=python.org```, ```&url=flask.pocoo.org``` and ```&url=www.djangoproject.com```  are the url's to be requested

```&word=docs``` is the word to be searched and counted

```&ignorecase=true``` pass this argument to match ignoring case

Return JSON:

```[
    {
        "http://www.pyhon.org": {
            "docs": 13
        }
    },
    {
        "http://flask.pocoo.org": {
            "docs": 10
        }
    },
    {
        "http://www.djangoproject.com": {
            "docs": 16
        }
    }
]
```

## Setup

To run this script, you'll need [Python 3.x](https://www.python.org/downloads/) installed and [pip](https://pip.pypa.io/en/stable/installing/) to get the packages.

Then you must get the extensions [Flask-restful](http://flask-restful-cn.readthedocs.io/en/0.3.5/installation.html), [requests](http://docs.python-requests.org/en/master/user/install/) and [Flask-Caching](https://pythonhosted.org/Flask-Caching/).



To get then you can simply open a terminal and type:
`pip install flask-restful` then `pip install requests` and finnaly `pip install Flask-Caching`.

## Running

To run the program, `clone` the repository or download `crawler.py`

Open a terminal and go to the folder that contains `crawler.py` 

Type `python crawler.py` and it will run the service under http://127.0.0.1:5000/

Then all you need to do is request the service passing the arguments:

- via Browser : you can do it on your browser, just type this in the address box = `http://127.0.0.1:5000/?url=globo.com&url=terra.com.br&word=google`

- via Postman : [See the documentation](https://learning.getpostman.com/docs/postman/launching_postman/installation_and_updates/)

## Testing

The file `crawler_test.py` is a *test suit* that was created to be used with the library [pytest](https://docs.pytest.org/en/latest/getting-started.html) 

Install [pytest](https://docs.pytest.org/en/latest/getting-started.html) by running in your terminal `pip install pytest`

Then, on the root folder of this project, run the terminal command `pytest`. It will automatically look for and run tests files (that follow a naming convention)
