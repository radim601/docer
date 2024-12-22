from flask import Flask, jsonify
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
    name = db.Column(db.String(50), nullable=False)

    def repr(self):
        return f'<User {self.name}>'

@app.route('/')
def hello():
    return jsonify({'message': 'Hello from Flask!'})

if __name__ == '__main__':
    with app.app_context():
        # Создаем таблицы
        db.create_all()
    app.run(host=os.environ.get('HOST'))
