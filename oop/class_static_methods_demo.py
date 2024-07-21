# File: class_static_methods_demo.py

# Calculator Class
class Calculator:
    calculation_type = "Arithmetic Operations"

    # Static Method - add
    @staticmethod
    def add(a, b):
        return a + b

    # Class Method - multiply
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
