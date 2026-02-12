# 💰 SmartExpense - AI-Powered Expense Tracker

## 🎯 Overview
Simple yet powerful expense tracking app with AI-powered category prediction. No complex setup, just works!

## ✨ Features

### Core Features
- ✅ **Add Expenses** - Track all your spending
- ✅ **AI Category Prediction** - Automatically categorizes expenses
- ✅ **Visual Analytics** - Beautiful charts
- ✅ **Real-time Stats** - Total spent, expense count, top category
- ✅ **Delete Expenses** - Remove unwanted entries
- ✅ **Date Tracking** - See when you spent

### AI Magic
The app uses keyword-based AI to automatically predict categories:
- "Zomato" → Food
- "Uber" → Transport
- "Amazon" → Shopping
- "Netflix" → Entertainment
- And more!

## 🛠️ Tech Stack

### Backend
- **Flask** - Python web framework
- **JSON** - Simple file-based storage (no database needed!)
- **AI Keywords** - Smart category prediction

### Frontend
- **Pure HTML/CSS/JS** - No React, no npm install!
- **Tailwind CSS** - Beautiful styling (CDN)
- **Chart.js** - Awesome charts (CDN)
- **Axios** - API calls (CDN)

## 🚀 Installation (SUPER EASY!)

### Step 1: Backend Setup

```bash
cd smartexpense-app/backend

# Install dependencies (only 2!)
pip install Flask Flask-CORS

# Run server
python app.py
```

**Success message:**
```
🚀 SmartExpense API Starting...
📍 Server running on http://localhost:5000
💡 Open frontend on http://localhost:3000
```

### Step 2: Frontend Setup

**NO npm install needed!**

Just open the HTML file:

**Option 1: Double-click**
```bash
# Windows/Mac/Linux
Double-click: frontend/index.html
```

**Option 2: Simple HTTP server**
```bash
cd frontend

# Python 3
python -m http.server 3000

# Or just open in browser
```

**Option 3: Live Server (VS Code)**
- Right-click index.html
- Select "Open with Live Server"

## 🎮 How to Use

### 1. Add Your First Expense

1. **Description:** "Lunch at McDonald's"
2. **Amount:** 250
3. **Category:** Leave empty (AI will predict!)
4. **Date:** Today (auto-filled)
5. Click **Add Expense**

**Result:** AI predicts "Food" category! ✨

### 2. Try More Examples

```
Description: "Uber to office"
AI Prediction: Transport 🚗

Description: "Netflix subscription"
AI Prediction: Entertainment 🎬

Description: "Shopping on Amazon"
AI Prediction: Shopping 🛍️

Description: "Electricity bill"
AI Prediction: Bills 💡
```

### 3. View Analytics

- **Total Spent** - See your total expenses
- **Expense Count** - Number of transactions
- **Top Category** - Where you spend most
- **Pie Chart** - Visual breakdown

### 4. Manage Expenses

- **View List** - All expenses with date, category, amount
- **Delete** - Click trash icon to remove

## 📊 AI Category Prediction

### Keywords Detected:

**Food:**
- food, restaurant, cafe, lunch, dinner, breakfast
- pizza, burger, snack, zomato, swiggy

**Transport:**
- uber, ola, taxi, metro, bus, fuel, petrol, auto, rapido

**Shopping:**
- amazon, flipkart, shopping, clothes, shoes, myntra, meesho

**Bills:**
- electricity, water, rent, wifi, internet, mobile, recharge, bill

**Entertainment:**
- movie, netflix, hotstar, prime, game, spotify, youtube

## 🎨 Features Showcase

### Stats Dashboard
- 💰 Total Amount Spent
- 📊 Total Number of Expenses
- 🏆 Top Spending Category

### Visual Charts
- 🥧 Doughnut Chart
- 📈 Category-wise breakdown
- 🎨 Colorful visualization

### Smart Form
- 🤖 AI auto-prediction
- 📅 Date picker
- 🔽 Manual category override
- ✅ Form validation

## 🐛 Troubleshooting

### Backend Not Running?
```bash
# Check if Flask is installed
pip install Flask Flask-CORS

# Run backend
python app.py

# Should see:
🚀 SmartExpense API Starting...
```

### Frontend Not Loading?
```bash
# Make sure backend is running first!
# Then open: frontend/index.html

# Or use:
cd frontend
python -m http.server 3000
# Open: http://localhost:3000
```

### CORS Error?
```bash
# Make sure Flask-CORS is installed
pip install Flask-CORS

# Restart backend
python app.py
```

### Data Not Saving?
- Check if `expenses.json` file is created in backend folder
- Backend must have write permissions
- Make sure backend is running

## 📂 Project Structure

```
smartexpense-app/
├── backend/
│   ├── app.py              # Flask API
│   ├── requirements.txt    # Dependencies (only 2!)
│   └── expenses.json       # Data storage (auto-created)
│
└── frontend/
    └── index.html          # Complete app in ONE file!
```

## 🎯 Testing Checklist

- ✅ Backend starts successfully
- ✅ Frontend loads without errors
- ✅ Add expense works
- ✅ AI predicts category correctly
- ✅ Stats update in real-time
- ✅ Chart displays correctly
- ✅ Delete expense works
- ✅ Data persists after refresh

## 💡 Pro Tips

1. **No npm install needed** - Everything runs via CDN!
2. **No database setup** - Uses simple JSON file
3. **Portable** - Copy folder anywhere and run
4. **Fast** - Lightweight and quick
5. **Customizable** - Easy to modify

## 🔥 Why This Project?

✅ **Simple Setup** - Just 2 pip installs  
✅ **Works Instantly** - No complex configuration  
✅ **AI Feature** - Shows ML knowledge  
✅ **Full Stack** - Backend + Frontend  
✅ **Professional** - Clean UI, good UX  
✅ **Portfolio Ready** - Impressive demo  

## 📱 Mobile Responsive

- ✅ Works on mobile browsers
- ✅ Responsive design
- ✅ Touch-friendly UI

## 🚀 Future Enhancements

- [ ] Export to CSV/Excel
- [ ] Monthly/Weekly reports
- [ ] Budget limits & alerts
- [ ] Multiple currencies
- [ ] Dark mode
- [ ] User authentication

## 🎓 Portfolio Tips

1. **Live Demo** - Host backend on PythonAnywhere
2. **Screenshots** - Add to README
3. **Video** - Record 2-min walkthrough
4. **Blog** - Write about AI prediction logic
5. **GitHub** - Clean repo with good README

## 👨‍💻 Made By

**Your Name**
- Portfolio: yourportfolio.com
- GitHub: @yourusername
- LinkedIn: /in/yourprofile

---

**Last Updated:** February 2026

**License:** MIT - Use freely for personal/commercial projects

---

Made with ❤️ for Sofccon India Workshop Series
