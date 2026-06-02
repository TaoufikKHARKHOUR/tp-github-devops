def saluer(nom):
    return f"Bonjour, {nom} !"

def additionner(a, b):
    return a + b

def diviser(a, b):
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b

import datetime

def log(message):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {message}")

if __name__ == "__main__":
    print(saluer("DevOps"))
