# I got this code from ChatGPT just for Demonstrating GitHub Code Scanning, Don't use it in your Production

import sqlite3
import os
import hashlib

# Vulnerability 1: SQL Injection
def get_user_info(user_id):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # Unsafe query vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE id = {user_id};"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result

# Vulnerability 2: Insecure use of eval()
def calculate_expression(expression):
    # Using eval is dangerous and can execute arbitrary code
    result = eval(expression)
    return result

# Vulnerability 3: Hardcoded sensitive data
def get_secret_key():
    # Sensitive data should not be hardcoded in the source code
    secret_key = "super_secret_key_123"
    return secret_key

# Example usage
if __name__ == "__main__":
    user_id = input("Enter the user ID: ")
    user_info = get_user_info(user_id)
    print(f"User Info: {user_info}")

    expression = input("Enter a mathematical expression to calculate: ")
    result = calculate_expression(expression)
    print(f"Result: {result}")

    secret_key = get_secret_key()
    print(f"Secret Key: {secret_key}")
