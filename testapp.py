def greet(name):
  """Greets the given name."""
  return f"Hello, {name}!"

if __name__ == "__main__":
  user_name = "World"
  greeting_message = greet(user_name)
  print(greeting_message)
