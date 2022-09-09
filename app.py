from flask import Flask
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)

SENSOR = {
    'sensor1': {'val': '10', 'tipo': 'temperatura'},
    'sensor2': {'val': '60', 'tipo': 'humedad'},
    'sensor3': {'val': '40', 'tipo': 'temperatura'},
    'sensor4': {'val': '80', 'tipo': 'humedad'}}


def abort_if_sensor_doesnt_exist(sensor_id):
    if sensor_id not in SENSOR:
        abort(404, message=f"No existe {sensor_id}")

parser = reqparse.RequestParser()
parser.add_argument('valor')
parser.add_argument('tipo')


# Todo
# shows a single todo item and lets you delete a todo item
class Sensor(Resource):
    def get(self, sensor_id):
        abort_if_sensor_doesnt_exist(sensor_id)
        return SENSOR[sensor_id]

    def delete(self, sensor_id):
        abort_if_sensor_doesnt_exist(sensor_id)
        del SENSOR[sensor_id]
        return '', 204

    def put(self, sensor_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        SENSOR[sensor_id] = task
        return task, 201


# ListaSensores
# shows a list of all SENSOR, and lets you POST to add new tasks
class ListaSensores(Resource):
    def get(self):
        return SENSOR

    def post(self):
        args = parser.parse_args()
        sensor_id = int(max(SENSOR.keys()).lstrip('todo')) + 1
        sensor_id = 'todo%i' % sensor_id
        SENSOR[sensor_id] = {'task': args['task']}
        return SENSOR[sensor_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(ListaSensores, '/sensores')
api.add_resource(Sensor, '/sensores/<sensor_id>')


if __name__ == '__main__':
    app.run(debug=True)
