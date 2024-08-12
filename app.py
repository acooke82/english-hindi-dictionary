from flask import Flask, request, jsonify
from flask_cors import CORS
from logging.config import dictConfig

from app.services import Services

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

services = Services()


@app.route('/')
def doc() -> str:
    app.logger.info('doc - Got Request')
    with open("app/doc.html", "r") as f:
        return f.read()


@app.route('/generate_form', methods=['GET'])
def generate_form():
    app.logger.info('generate_form - Grabbed Request')
    with open("web/ui.html", "r") as f:
        return f.read()


@app.route('/generate', methods=['GET'])
def generate():
    input_form = request.args.get('input_form', '')
    data = services.generate_entry(input_form)
    app.logger.info('/generate - Generated entry.')
    return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
