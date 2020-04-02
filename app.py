'''
Created on 2 de abr de 2020

@author: RAEO
'''
from flask.app import Flask
from flask_restful import Api

from configs import config
from resources.hello import Hello

app = Flask(__name__)
app.config.from_object(config)
api= Api(app)

api.add_resource(Hello, '/api/hello/<string:name>', endpoint='hello')

if __name__ == '__main__':
    app.run(debug=True)
