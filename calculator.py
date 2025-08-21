import math

class Calculator:
    """Advanced Calculator with OOP design and comprehensive functionality."""
    
    def __init__(self):
        """Initialize calculator with memory and history."""
        self.memory = 0  # Memory storage
        self.history = []  # Last 10 calculations
        print("🧮 Advanced Calculator Initialized!")
        print("=" * 50)
    
    def add_to_history(self, operation, result):
        """Add calculation to history (keep last 10)."""
        entry = f"{operation} = {result}"
        self.history.append(entry)
        if len(self.history) > 10:
            self.history.pop(0)  # Remove oldest entry
    
    def format_result(self, result):
        """Pretty print results."""
        if isinstance(result, float) and result.is_integer():
            return f"Result: {int(result)}"
        else:
            return f"Result: {result:.6g}"  # Clean decimal formatting
    
    # Basic Operations
    def add(self, a, b):
        """Addition: a + b"""
        result = a + b
        self.add_to_history(f"{a} + {b}", result)
        return result
    
    def subtract(self, a, b):
        """Subtraction: a - b"""
        result = a - b
        self.add_to_history(f"{a} - {b}", result)
        return result
    
    def multiply(self, a, b):
        """Multiplication: a × b"""
        result = a * b
        self.add_to_history(f"{a} × {b}", result)
        return result
    
    def divide(self, a, b):
        """Division: a ÷ b (with zero check)"""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        self.add_to_history(f"{a} ÷ {b}", result)
        return result
    
    # Advanced Operations
    def power(self, base, exponent):
        """Power: base^exponent"""
        result = base ** exponent
        self.add_to_history(f"{base}^{exponent}", result)
        return result
    
    def square_root(self, number):
        """Square root of number"""
        if number < 0:
            raise ValueError("Cannot calculate square root of negative number!")
        result = math.sqrt(number)
        self.add_to_history(f"√{number}", result)
        return result
    
    def percentage(self, number, percent):
        """Calculate percentage: number × (percent/100)"""
        result = number * (percent / 100)
        self.add_to_history(f"{percent}% of {number}", result)
        return result
    
    def factorial(self, n):
        """Factorial of n (n must be non-negative integer)"""
        if n < 0 or not isinstance(n, int):
            raise ValueError("Factorial requires non-negative integer!")
        result = math.factorial(n)
        self.add_to_history(f"{n}!", result)
        return result
    
    def logarithm(self, number, base=10):
        """Logarithm with custom base (default base 10)"""
        if number <= 0:
            raise ValueError("Logarithm requires positive number!")
        if base <= 0 or base == 1:
            raise ValueError("Base must be positive and not equal to 1!")
        
        result = math.log(number, base)
        base_str = "e" if base == math.e else str(base)
        self.add_to_history(f"log_{base_str}({number})", result)
        return result
    
    # Trigonometric Functions (in degrees)
    def sin(self, degrees):
        """Sine of angle in degrees"""
        radians = math.radians(degrees)
        result = math.sin(radians)
        self.add_to_history(f"sin({degrees}°)", result)
        return result
    
    def cos(self, degrees):
        """Cosine of angle in degrees"""
        radians = math.radians(degrees)
        result = math.cos(radians)
        self.add_to_history(f"cos({degrees}°)", result)
        return result
    
    def tan(self, degrees):
        """Tangent of angle in degrees"""
        radians = math.radians(degrees)
        result = math.tan(radians)
        self.add_to_history(f"tan({degrees}°)", result)
        return result
    
    # Memory Functions
    def memory_add(self, value):
        """Add value to memory (M+)"""
        self.memory += value
        print(f"Added {value} to memory. Memory = {self.memory}")
    
    def memory_subtract(self, value):
        """Subtract value from memory (M-)"""
        self.memory -= value
        print(f"Subtracted {value} from memory. Memory = {self.memory}")
    
    def memory_recall(self):
        """Recall memory value (MR)"""
        print(f"Memory Recall: {self.memory}")
        return self.memory
    
    def memory_clear(self):
        """Clear memory (MC)"""
        self.memory = 0
        print("Memory cleared!")
    
    # Utility Functions
    def show_history(self):
        """Display calculation history"""
        if not self.history:
            print("No calculations in history.")
            return
        
        print("\n📊 Last 10 Calculations:")
        print("-" * 30)
        for i, entry in enumerate(self.history[-10:], 1):
            print(f"{i:2d}. {entry}")
        print("-" * 30)
    
    def reset(self):
        """Reset calculator (clear history and memory)"""
        self.memory = 0
        self.history = []
        print("Calculator reset! Memory and history cleared.")
    
    def get_number_input(self, prompt):
        """Get validated number input from user"""
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("❌ Invalid input! Please enter a number.")
    
    def get_integer_input(self, prompt):
        """Get validated integer input from user"""
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("❌ Invalid input! Please enter an integer.")
    
    def display_menu(self):
        """Display calculator menu"""
        menu = """
🧮 ADVANCED CALCULATOR MENU
═══════════════════════════════════
📐 BASIC OPERATIONS
1.  Addition (+)          2.  Subtraction (-)
3.  Multiplication (×)    4.  Division (÷)

🔢 ADVANCED OPERATIONS  
5.  Power (x^y)          6.  Square Root (√)
7.  Percentage (%)       8.  Factorial (!)
9.  Logarithm (log)

📊 TRIGONOMETRY (Degrees)
10. Sine (sin)           11. Cosine (cos)
12. Tangent (tan)

💾 MEMORY FUNCTIONS
13. Memory Add (M+)      14. Memory Subtract (M-)
15. Memory Recall (MR)   16. Memory Clear (MC)

🛠️  UTILITIES
17. Show History         18. Reset Calculator
19. Exit

═══════════════════════════════════"""
        print(menu)
    
    def run(self):
        """Main calculator loop"""
        while True:
            self.display_menu()
            
            try:
                choice = input("\nEnter your choice (1-19): ").strip()
                
                if choice == '1':  # Addition
                    a = self.get_number_input("Enter first number: ")
                    b = self.get_number_input("Enter second number: ")
                    result = self.add(a, b)
                    print(f"✅ {self.format_result(result)}")
                
                elif choice == '2':  # Subtraction
                    a = self.get_number_input("Enter first number: ")
                    b = self.get_number_input("Enter second number: ")
                    result = self.subtract(a, b)
                    print(f"✅ {self.format_result(result)}")
                
                elif choice == '3':  # Multiplication
                    a = self.get_number_input("Enter first number: ")
                    b = self.get_number_input("Enter second number: ")
                    result = self.multiply(a, b)
                    print(f"✅ {self.format_result(result)}")
                
                elif choice == '4':  # Division
                    a = self.get_number_input("Enter dividend: ")
                    b = self.get_number_input("Enter divisor: ")
                    result = self.divide(a, b)
                    print(f"✅ {self.format_result(result)}")
                
                elif choice == '5':  # Power
                    base = self.get_number_input("Enter base: ")
                    exp = self.get_number_input("Enter exponent: ")
                    result = self.power(base, exp)
                    print(f"✅ {self.format_result(result)}")
                
                elif choice == '6':  # Square Root
                    num = self.get_number_input("Enter number: ")
                    result = self.square_root(num)
                    print(f"✅ {self.format_result(result)}")
                
                elif choice == '7':  # Percentage
                    num = self.get_number_input("Enter number: ")
                    percent = self.get_number_input("Enter percentage: ")
                    result = self.percentage(num, percent)
                    print(f"✅ {self.format_result(result)}")
                
                elif choice == '8':  # Factorial
                    n = self.get_integer_input("Enter integer: ")
                    result = self.factorial(n)
                    print(f"✅ {self.format_result(result)}")
                
                elif choice == '9':  # Logarithm
                    num = self.get_number_input("Enter number: ")
                    base_choice = input("Enter base (or press Enter for base 10): ").strip()
                    base = 10 if base_choice == '' else float(base_choice)
                    result = self.logarithm(num, base)
                    print(f"✅ {self.format_result(result)}")
                
                elif choice == '10':  # Sine
                    degrees = self.get_number_input("Enter angle in degrees: ")
                    result = self.sin(degrees)
                    print(f"✅ {self.format_result(result)}")
                
                elif choice == '11':  # Cosine
                    degrees = self.get_number_input("Enter angle in degrees: ")
                    result = self.cos(degrees)
                    print(f"✅ {self.format_result(result)}")
                
                elif choice == '12':  # Tangent
                    degrees = self.get_number_input("Enter angle in degrees: ")
                    result = self.tan(degrees)
                    print(f"✅ {self.format_result(result)}")
                
                elif choice == '13':  # Memory Add
                    value = self.get_number_input("Enter value to add to memory: ")
                    self.memory_add(value)
                
                elif choice == '14':  # Memory Subtract
                    value = self.get_number_input("Enter value to subtract from memory: ")
                    self.memory_subtract(value)
                
                elif choice == '15':  # Memory Recall
                    self.memory_recall()
                
                elif choice == '16':  # Memory Clear
                    self.memory_clear()
                
                elif choice == '17':  # Show History
                    self.show_history()
                
                elif choice == '18':  # Reset
                    self.reset()
                
                elif choice == '19':  # Exit
                    print("👋 Thank you for using Advanced Calculator!")
                    break
                
                else:
                    print("❌ Invalid choice! Please select 1-19.")
            
            except ValueError as e:
                print(f"❌ Error: {e}")
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
            
            input("\nPress Enter to continue...")

# Example usage and how to run the program
if __name__ == "__main__":
    print("🚀 Starting Advanced Calculator...")
    print("=" * 50)
    
    # Create calculator instance
    calc = Calculator()
    
    # Run the calculator
    calc.run()


