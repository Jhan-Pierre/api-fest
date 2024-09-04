from flask import Blueprint, jsonify, request

festividades = [
    {"fecha": "2024-10-07", "nombre": "Día no laborable para el sector público"},
    {"fecha": "2024-10-08", "nombre": "Combate de Angamos"},
    {"fecha": "2024-11-01", "nombre": "Día de Todos los Santos"},
    {"fecha": "2024-12-06", "nombre": "Día no laborable para el sector público"},
    {"fecha": "2024-12-08", "nombre": "Inmaculada Concepción"},
    {"fecha": "2024-12-09", "nombre": "Batalla de Ayacucho"},
    {"fecha": "2024-12-23", "nombre": "Día no laborable para el sector público"},
    {"fecha": "2024-12-24", "nombre": "Día no laborable para el sector público"},
    {"fecha": "2024-12-25", "nombre": "Navidad"},
    {"fecha": "2024-12-30", "nombre": "Día no laborable para el sector público"},
    {"fecha": "2024-12-31", "nombre": "Día no laborable para el sector público"}
]

bp = Blueprint('festividades', __name__)

@bp.route('/festividades', methods=['GET'])
def obtener_festividades():
    return jsonify(festividades)

@bp.route('/festividad', methods=['GET'])
def obtener_festividad_por_fecha():
    fecha = request.args.get('fecha')
    if not fecha:
        return jsonify({"error": "Parámetro de fecha es requerido"}), 400

    festividad = next((f for f in festividades if f['fecha'] == fecha), None)
    if festividad:
        return jsonify(festividad)
    else:
        return jsonify({}), 404
