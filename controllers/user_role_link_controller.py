from flask import Flask, jsonify, make_response, request

from model.associations import user_role_link
from model.base import db
from model.user_role_link import UserRoleLink as UserProfile

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../SQLite_DB.sqlite'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Redwo0d$@127.0.0.1:3306/webadvisor_reboot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

def create_tables():
    with app.app_context():
        db.create_all()

# --- CRUD Operations ---

# Read all user profiles (GET)
@app.route('/userprofile', methods=['GET'])
def get_profiles():
    profiles = UserProfile.query.all()
    return make_response(jsonify([user_role_link.json() for profile in profiles]), 200)

# Read a single profile by user ID (GET)
@app.route('/userprofile/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    profile = UserProfile.query.get_or_404(user_id)
    return make_response(jsonify({'profile': user_role_link.json()}), 200)

# Update a profile by user ID (PUT/PATCH)
@app.route('/userprofile/<int:user_id>', methods=['PUT'])
def update_userprofile(user_id):
    userprofile = UserProfile.query.get_or_404(user_id)
    data = request.get_json()

    userprofile.user_id = data.get('user_id', userprofile.user_id)
    userprofile.role_id = data.get('role_id', userprofile.role_id)
    # This might have issues later...
    db.session.commit()
    return make_response(jsonify({'message': 'user profile updated', 'userprofile': userprofile.json()}), 200)

# Delete a user profile by ID (DELETE)
@app.route('/userprofile/<int:user_id>', methods=['DELETE'])
def delete_userprofile(user_id):
    userprofile = UserProfile.query.get_or_404(user_id)
    db.session.delete(userprofile)
    db.session.commit()
    return make_response(jsonify({'message': 'user profile deleted'}), 200)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)