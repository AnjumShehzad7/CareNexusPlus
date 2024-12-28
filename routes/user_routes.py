from flask import Blueprint, request, jsonify
from models.user import User
from app import db

user_bp = Blueprint('users', __name__)

@user_bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    new_user = User(
        name=data['name'],
        email=data['email'],
        password=data['password']  # In production, hash this!
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201
