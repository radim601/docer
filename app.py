from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Конфигурация из переменных окружения
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://user:password@db:5432/mydatabase')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#модель
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Маршрут для добавления пользователя
@app.route('/users', methods=['POST'])
def add_user():
    username = request.json.get('username')
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User already exists'}), 400
    
    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'username': new_user.username}), 201

# Маршрут для получения всех пользователей
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': user.id, 'username': user.username} for user in users]), 200
    
@app.route('/')
def hello():
    return jsonify({'message': 'Hello from Flask!'})
    

if __name__ == '__main__':
    with app.app_context():
        # Создаем таблицы
        db.create_all()
    app.run(host=os.environ.get('HOST'))
