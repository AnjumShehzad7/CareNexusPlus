from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models.appointment import Appointment

appointment_bp = Blueprint('appointments', __name__)

# Create a new appointment
@appointment_bp.route('/', methods=['POST'])
@jwt_required()
def create_appointment():
    data = request.get_json()
    if not data or not data.get('doctor_name') or not data.get('date'):
        return jsonify({"message": "Missing required fields"}), 400

    user_id = get_jwt_identity()
    new_appointment = Appointment(
        user_id=user_id,
        doctor_name=data['doctor_name'],
        date=data['date']
    )
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({"message": "Appointment created successfully"}), 201

# Get all appointments for the current user
@appointment_bp.route('/', methods=['GET'])
@jwt_required()
def get_appointments():
    user_id = get_jwt_identity()
    appointments = Appointment.query.filter_by(user_id=user_id).all()
    result = [
        {
            "id": a.id,
            "doctor_name": a.doctor_name,
            "date": a.date,
            "status": a.status
        } for a in appointments
    ]
    return jsonify(result), 200

# Get a specific appointment by ID
@appointment_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_appointment(id):
    user_id = get_jwt_identity()
    appointment = Appointment.query.filter_by(id=id, user_id=user_id).first()
    if not appointment:
        return jsonify({"message": "Appointment not found"}), 404

    return jsonify({
        "id": appointment.id,
        "doctor_name": appointment.doctor_name,
        "date": appointment.date,
        "status": appointment.status
    }), 200

# Update an appointment
@appointment_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_appointment(id):
    data = request.get_json()
    user_id = get_jwt_identity()
    appointment = Appointment.query.filter_by(id=id, user_id=user_id).first()

    if not appointment:
        return jsonify({"message": "Appointment not found"}), 404

    if data.get('doctor_name'):
        appointment.doctor_name = data['doctor_name']
    if data.get('date'):
        appointment.date = data['date']
    if data.get('status'):
        appointment.status = data['status']

    db.session.commit()
    return jsonify({"message": "Appointment updated successfully"}), 200

# Delete an appointment
@appointment_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_appointment(id):
    user_id = get_jwt_identity()
    appointment = Appointment.query.filter_by(id=id, user_id=user_id).first()

    if not appointment:
        return jsonify({"message": "Appointment not found"}), 404

    db.session.delete(appointment)
    db.session.commit()
    return jsonify({"message": "Appointment deleted successfully"}), 200
