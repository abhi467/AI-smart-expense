from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import json
import os

app = Flask(__name__)
CORS(app)

# Simple JSON file database
DATA_FILE = 'expenses.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {'expenses': [], 'categories': ['Food', 'Transport', 'Shopping', 'Bills', 'Entertainment', 'Other']}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

# AI Prediction function
def predict_category(description):
    """Simple AI to predict category based on keywords"""
    description_lower = description.lower()
    
    keywords = {
        'Food': ['food', 'restaurant', 'cafe', 'lunch', 'dinner', 'breakfast', 'pizza', 'burger', 'snack', 'zomato', 'swiggy'],
        'Transport': ['uber', 'ola', 'taxi', 'metro', 'bus', 'fuel', 'petrol', 'auto', 'rapido'],
        'Shopping': ['amazon', 'flipkart', 'shopping', 'clothes', 'shoes', 'myntra', 'meesho'],
        'Bills': ['electricity', 'water', 'rent', 'wifi', 'internet', 'mobile', 'recharge', 'bill'],
        'Entertainment': ['movie', 'netflix', 'hotstar', 'prime', 'game', 'spotify', 'youtube'],
    }
    
    for category, words in keywords.items():
        if any(word in description_lower for word in words):
            return category
    
    return 'Other'

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'message': 'SmartExpense API is running!'}), 200

@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    data = load_data()
    return jsonify(data['expenses']), 200

@app.route('/api/expenses', methods=['POST'])
def add_expense():
    expense_data = request.get_json()
    data = load_data()
    
    # Auto-predict category if not provided
    if not expense_data.get('category'):
        expense_data['category'] = predict_category(expense_data['description'])
    
    expense = {
        'id': len(data['expenses']) + 1,
        'description': expense_data['description'],
        'amount': float(expense_data['amount']),
        'category': expense_data['category'],
        'date': expense_data.get('date', datetime.now().strftime('%Y-%m-%d')),
        'created_at': datetime.now().isoformat()
    }
    
    data['expenses'].append(expense)
    save_data(data)
    
    return jsonify({
        'message': 'Expense added successfully!',
        'expense': expense,
        'predicted_category': expense_data.get('category') == predict_category(expense_data['description'])
    }), 201

@app.route('/api/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    data = load_data()
    data['expenses'] = [e for e in data['expenses'] if e['id'] != expense_id]
    save_data(data)
    return jsonify({'message': 'Expense deleted successfully!'}), 200

@app.route('/api/stats', methods=['GET'])
def get_stats():
    data = load_data()
    expenses = data['expenses']
    
    if not expenses:
        return jsonify({
            'total': 0,
            'count': 0,
            'by_category': {},
            'recent': []
        }), 200
    
    total = sum(e['amount'] for e in expenses)
    by_category = {}
    
    for expense in expenses:
        cat = expense['category']
        if cat not in by_category:
            by_category[cat] = 0
        by_category[cat] += expense['amount']
    
    recent = sorted(expenses, key=lambda x: x['created_at'], reverse=True)[:5]
    
    return jsonify({
        'total': total,
        'count': len(expenses),
        'by_category': by_category,
        'recent': recent
    }), 200

@app.route('/api/predict-category', methods=['POST'])
def predict():
    data = request.get_json()
    description = data.get('description', '')
    predicted = predict_category(description)
    
    return jsonify({
        'description': description,
        'predicted_category': predicted,
        'confidence': 85.5  # Mock confidence
    }), 200

if __name__ == '__main__':
    print("🚀 SmartExpense API Starting...")
    print("📍 Server running on http://localhost:5000")
    print("💡 Open frontend on http://localhost:3000")
    app.run(debug=True, port=5000)
