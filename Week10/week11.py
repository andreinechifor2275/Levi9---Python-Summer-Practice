from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from exercise import Base, User, Role, PaymentMethod, Transaction

app = Flask(__name__)
DATABASE_URL = "postgresql://postgres:admin@localhost/postgres"
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
db = SQLAlchemy(app)

@app.route('/users', methods=['GET'])
def get_users():
    session = SessionLocal()
    users = session.query(User).all()
    data = [{"id": u.id, "name": u.username, "email": u.email} for u in users]
    session.close()
    return jsonify(data)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    session = SessionLocal()
    user = session.query(User).filter(User.id == user_id).first()
    if not user:
        session.close()
        return jsonify({"error": "User not found"}), 404
    data = data = {"id": user.id, "name": user.username, "email": user.email}
    session.close()
    return jsonify(data)

@app.route('/users', methods=['POST'])
def create_user():
    session = SessionLocal()
    data = request.json
    user = User(name=data["name"], email=data["email"])
    session.add(user)
    session.commit()
    session.refresh(user)
    session.close()
    return jsonify({"message": "User created", "id": user.id}), 201

@app.route("/transactions", methods=["GET"])
def get_transactions():
    session = SessionLocal()
    transactions = session.query(Transaction).all()
    result = []
    for t in transactions:
        result.append({
            "id": t.id,
            "amount": t.amount,
            "description": t.description,
            "user_id": t.user_id,
            "payment_method_id": t.payment_method_id
        })
    session.close()
    return jsonify(result)

@app.route("/transactions", methods=["POST"])
def create_transaction():
    data = request.get_json()
    session = SessionLocal()
    new_tx = Transaction(
        amount=data["amount"],
        description=data.get("description"),
        user_id=data["user_id"],
        payment_method_id=data.get("payment_method_id")
    )
    session.add(new_tx)
    session.commit()
    session.refresh(new_tx)
    session.close()
    return jsonify({"id": new_tx.id, "amount": new_tx.amount}), 201

@app.route("/transactions/<int:transaction_id>", methods=["DELETE"])
def delete_transaction(transaction_id):
    session = SessionLocal()
    tx = session.query(Transaction).get(transaction_id)
    if not tx:
        session.close()
        return jsonify({"error": "Transaction not found"}), 404
    session.delete(tx)
    session.commit()
    session.close()
    return jsonify({"message": "Transaction deleted successfully"})

def get_payment_methods():
    session = SessionLocal()
    methods = session.query(PaymentMethod).all()
    session.close()
    return jsonify([{"id": m.id, "name": m.name} for m in methods])

@app.route("/roles", methods=["GET"])
def get_roles():
    session = SessionLocal()
    roles = session.query(Role).all()
    session.close()
    return jsonify([{"id": r.id, "name": r.name} for r in roles])

if __name__ == "__main__":
    app.run(debug=True)