class Calculator:
    """A simple calculator class to perform basic arithmetic operations."""
    
    @staticmethod
    def add(a, b):
        """Function to add two numbers"""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Function to subtract two numbers"""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Function to multiply two numbers"""
        return a * b

    @staticmethod
    def divide(a, b):
        """Function to divide two numbers"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
