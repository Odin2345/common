from flask import Flask, current_app
from flask_restful import Api

from config import run_config
from rooms_bp.room import rooms_api_bp, GetRooms
from staff_bp.staff import staff_api_bp, GetStaff
from tenants_bp.tenant import tenants_api_bp, GetTenants

app = Flask(__name__)
api = Api(app)

app.config.from_object(run_config())

api.add_resource(GetRooms, '/rooms', '/rooms/<int:room_number>')
api.add_resource(GetStaff, '/staff', '/staff/<staff_id>')
api.add_resource(GetTenants, '/tenants', '/tenants/<tenant_id>')

app.register_blueprint(rooms_api_bp)
app.register_blueprint(staff_api_bp)
app.register_blueprint(tenants_api_bp)

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=current_app.config["DEBUG"])
