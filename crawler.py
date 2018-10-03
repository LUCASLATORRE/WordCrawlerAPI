from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
import requests
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config = {'CACHE_TYPE':'simple'}) # configurao cache 
cache.init_app(app)
api = Api(app)

# adiciona os argumentos
parser = reqparse.RequestParser()
parser.add_argument('url', action='append') 
parser.add_argument('word')
parser.add_argument('ignorecase')

# Função que faz um GET para a URL e retorna quantas vezes a palavra especificada aparece no conteudo
def countWord(url, word, ignore_case):
    try:
        r = requests.get(url)
        data = str(r.text)
        if (str(ignore_case).lower() == 'true'):
            return data.lower().count(word.lower())
        else:   
            return data.count(word)
    except Exception as e:
        raise e

# Função que inclui 'http://' na url e retorna a URL válida
def validate_url(url):
    if not(url.startswith('http')):
        url = 'http://' + url
    return url


# Função que retorna o json com as URLs válidas e a palavra word
class CrawlerAPI(Resource):
    @cache.memoize(300)  # cache de 5 minutos
    def get(self):
        try:
            args = parser.parse_args()
            valid_urls = [validate_url(url) for url in args['url']]
            lista = []
            for valid_url in valid_urls:
                lista.append({valid_url: {args['word']: countWord(valid_url, args['word'], args['ignorecase'])}})
            return lista
        except AttributeError:
            return {'message': 'Please provide URL and WORD arguments'}
        except Exception as e:
            return {'message': 'Unhandled Exception: ' + str(e)}


api.add_resource(CrawlerAPI, "/")

if __name__ == '__main__':
    app.run(debug=True)