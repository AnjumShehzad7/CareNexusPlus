from flask import Blueprint, request, jsonify
from models.appointment import Appointment
from app import db

appointment_bp = Blueprint('appointments', __name__)

@appointment_bp.route('/', methods=['POST'])
def create_appointment():
    data = request.json
    new_appointment = Appointment(
        user_id=data['user_id'],
        doctor_name=data['doctor_name'],
        date=data['date']
    )
    db.session.add(new_appointment)
    db.session.commit()
    return jsonify({'message': 'Appointment created successfully'}), 201
