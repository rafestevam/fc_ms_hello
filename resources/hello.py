'''
Created on 2 de abr de 2020

@author: RAEO
'''
from flask_restful import Resource

class Hello(Resource):
    
    def get(self, name):
        
        return {"message":f"Hello {name}, welcome to our FinCollab-API"}