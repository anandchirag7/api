from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class multiply_var(BaseModel):
    a: int
    b: int

class calculator_var(BaseModel):
    a: float
    b: float
    operation: str

@app.post("/multiply")
def multiply(var: multiply_var):
    try:
        print("Multiplying:", var.a, "and", var.b)
        result = var.a * var.b
        print("Multiplication result is:", result)
    except Exception as e:
        print("Error occurred:", e)
        # result = {"error": str(e)}
    else:
        return result
    
@app.post("/calculator")
def calculator(var: calculator_var):
    if var.operation == "add":
        result = var.a + var.b
    elif var.operation == "subtract":
        result = var.a - var.b
    elif var.operation == "multiply":
        result = var.a * var.b
    elif var.operation == "divide":
        if var.b == 0:
            raise HTTPException(
        status_code=4020,
        detail={"location": "ValueError", "msg": "Cannot divide by 0","type": "ValueError"}
    )
        result = var.a / var.b
    else:
        raise HTTPException(
        status_code=4020,
        detail={"location": "ValueError", "msg": "Cannot divide by 0","type": "ValueError"}
    )

