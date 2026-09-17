from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.json.compact = False
app.json.sort_keys = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)


class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))

    def __repr__(self):
        return f"{self.name} - {self.description}"


@app.route('/')
def index():
    return "Hello, world!"


@app.route('/drinks', methods=['GET'])
def get_drinks():
    drinks = Drink.query.all()

    return {
        "drinks": [
            {
                "id": drink.id,
                "name": drink.name,
                "description": drink.description
            }
            for drink in drinks
        ]
    }


@app.route('/drinks/<int:id>', methods=['GET'])
def get_drink(id):
    drink = Drink.query.get_or_404(id)

    return {
        "id": drink.id,
        "name": drink.name,
        "description": drink.description
    }


@app.route('/drinks', methods=['POST'])
def add_drink():
    data = request.get_json()

    if isinstance(data, list):
        drinks = []

        for item in data:
            drink = Drink(
                name=item['name'],
                description=item.get('description', '')
            )

            db.session.add(drink)
            drinks.append(drink)

        db.session.commit()

        return {
            "message": "Drinks added successfully",
            "drinks": [
                {
                    "id": drink.id,
                    "name": drink.name,
                    "description": drink.description
                }
                for drink in drinks
            ]
        }, 201

    drink = Drink(
        name=data['name'],
        description=data.get('description', '')
    )

    db.session.add(drink)
    db.session.commit()

    return {
        "id": drink.id,
        "name": drink.name,
        "description": drink.description
    }, 201


@app.route('/drinks/<int:id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get_or_404(id)

    db.session.delete(drink)
    db.session.commit()

    return {
        "message": "Drink deleted successfully"
    }