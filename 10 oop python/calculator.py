class calculator:
  def __init__(self):
    self.result = 0
  def add(self, value1,value2):
    self.result += value1 + value2
    return self.result
  def subtract(self, value1,value2):
    self.result -= value1 - value2
    return self.result
  def multiply(self, value1,value2):
    self.result *= value1 * value2
    return self.result
  def divide(self, value1,value2):
    if value2 != 0:
      self.result /= value2
      return self.result
    else:
      return "Error: Division by zero is not allowed."
  def clear(self):
    self.result = 0
    return self.result

calc = calculator()
# menerima input dari pengguna
while True:
  print("\nCalculator Menu:")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Clear")
  print("6. Exit")
  
  choice = input("Choose an operation (1-6): ")
  
  if choice == '6':
    print("Exiting the calculator.")
    break
  
  if choice == '5':
    calc.clear()
    print("Calculator cleared.")
    continue
  
  value = float(input("Enter a number: "))
  
  if choice == '1':
    print(f"Result: {calc.add(value)}")
  elif choice == '2':
    print(f"Result: {calc.subtract(value)}")
  elif choice == '3':
    print(f"Result: {calc.multiply(value)}")
  elif choice == '4':
    result = calc.divide(value)
    print(f"Result: {result}")
  else:
    print("Invalid choice, please try again.")