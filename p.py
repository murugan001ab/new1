import subprocess
# Get the Python code as input from the user
user_input = input("Enter your Python code:\n")

# Specify the file name where you want to save the input
file_name = "user_input.py"

# Write the input to a Python file

with open(file_name, "w") as file:
	while True:
    		file.write(user_input)

# Inform the user that the file has been created
print(f"Python code has been saved to {file_name}")

# Now, you can execute the Python file if needed
# You can use subprocess or other methods to run the file, for example:
# import subprocess
# subprocess.run(["python", file_name])

# Replace 'script_to_run.py' with the name of your Python script
user_input = 'user_input.py'

# Run the script
try:
	subprocess.run(['python', user_input])
except Exception as e:
	print(e)
