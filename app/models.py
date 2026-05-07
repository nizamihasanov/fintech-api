from pydantic import BaseModel

# User

class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class User(BaseModel):
    id: int
    email: str

# Account

class Account(BaseModel):
    id: int
    user_id: int
    balance: int

# Transaction

class Transfer(BaseModel):
    from_account: int
    to_account: int
    amount: int

class Transaction(BaseModel):
    id: int
    from_account: int
    to_account: int
    amount: int