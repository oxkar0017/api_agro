from flask import Flask, request
from flask_restful import abort, Api, Resource


app = Flask(__name__)
api = Api(app)

REGISTROS = {
    '1': {'valor': '10', 'tipo': 'temperatura'},
    '2': {'valor': '60', 'tipo': 'humedad'},
    '3': {'valor': '40', 'tipo': 'temperatura'},
    '4': {'valor': '80', 'tipo': 'humedad'}}


def abortar_si_no_existe_registro(id_registro):
    if id_registro not in REGISTROS:
        abort(404, message=f"No existe registro con id {id_registro}")


# Registro
# Muestra, borra o crea un registro en REGISTROS
class Registro(Resource):
    def get(self, id_registro):
        abortar_si_no_existe_registro(id_registro)
        return REGISTROS[id_registro]

    def delete(self, id_registro):
        abortar_si_no_existe_registro(id_registro)
        del REGISTROS[id_registro]
        return '', 204

    def put(self, id_registro):
        REGISTROS[id_registro] = {
            'valor': request.args.get('valor'),
            'tipo': request.args.get('tipo')}
        return REGISTROS[id_registro], 201


# ListaRegistros
# Muestra todos los registros y hace un POST de un nuevo registro
class ListaRegistros(Resource):
    def get(self):
        return REGISTROS

    def post(self):
        id_registro = int(max(REGISTROS.keys())) + 1
        id_registro = f'{id_registro}'
        REGISTROS[id_registro] = {
            'valor': request.args.get('valor'),
            'tipo': request.args.get('tipo')}
        return REGISTROS[id_registro], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(ListaRegistros, '/registros')
api.add_resource(Registro, '/registros/<string:id_registro>')


if __name__ == '__main__':
    app.run(debug=True)
