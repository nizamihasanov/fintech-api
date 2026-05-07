from fastapi import FastAPI, HTTPException
from db import init_db, get_conn
from models import *

app = FastAPI()
init_db()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post('/register')
def register(user: UserCreate):
    conn = get_conn()
    c = conn.cursor()
    c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (user.email, user.password))
    user_id = c.lastrowid
    c.execute("INSERT INTO accounts (user_id, balance) VALUES (?, ?)", (user_id, 100))
    conn.commit()
    conn.close()
    return {"message": "User created successfully", "user_id": user_id}

@app.post('/login')
def login(data: UserLogin):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE email=? AND password=?", (data.email, data.password))
    user = c.fetchone()
    conn.close()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful", "user_id": user[0]}

@app.get('/accounts/{account_id}')
def account_details(account_id: int):
    conn = get_conn()
    c = conn.cursor()
    c.execute("SELECT * FROM accounts WHERE id=?", (account_id))
    account = c.fetchone()
    conn.close()
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"user_id": account[1], "balance": account[2]}

@app.post('/transfer')
def transfer(data: Transfer):
    conn = get_conn()
    c = conn.cursor()
    c.execute("UPDATE accounts SET balance = balance - ? WHERE id=?", (data.amount, data.from_account))
    c.execute("UPDATE accounts SET balance = balance + ? WHERE id=?", (data.amount, data.to_account))
    conn.commit()
    conn.close()
    return {"message": "Transfer completed"}