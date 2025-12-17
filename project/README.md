 # Pizza Kiosk
    #### Video Demo:  https://youtu.be/r6Qc3R1UO-U
    #### Description:
      The concept of my program is online tracking of a pizza order. The program encompasses ordering the pizza from the consumer's perspective, updating the order from the producer's perspective, checking what status it is at from the consumer's perspective, and lastly, picking up the order when the food is ready from the consumer's perspective.

	In the project.py file, the first line is an import statement for CSV since I am storing the information in a CSV file; therefore, I need to import the CSV library to read and write to the file. Then a variable is a code required for the producer to input to verify that it is the producer. Then there is the primary function, which starts by asking the user if they are a customer or a producer.

   If it is a customer, it asks the customer if they want to do a new order or look into a current.

	If it's a new order, it asks what size they want -small, medium, or large-the number of toppings they want, what toppings they want on their pizza. Lastly, it enters into a while loop where it asks the customer for a name for the order. Then the information enters the "new" function. Where it first checks if the name already exists. If so, a print statement prints that "The name already exists.", and returns a string with the input information and a boolean value of "True". This return statement will cause the while loop to repeat. If the name is not already used, the information is written as a dictionary line to the CSV file for easy retrieval. Then the return statement returns a string representing all the inputted values and a boolean value "False."

	 If the user types current to represent a current order, the program asks for the order name and inputs the information into the current function. In the current function, the makeup of the order is printed, and the status is returned. The status is recorded as a number, so every time the status is printed, the status value is first input into the "stat" function, which returns the appropriate string to be printed. For example, when the status value reaches 4, the corresponding string is "Ready for Pickup."

   If the returned value for the current function is 4, the customer is asked if they are ready to pick up their order. Then the name and their answer to that question are inputted into the pickup function. If they type "y" for yes, the program returns "Pick up for the order name" and also removes their order from the CSV file. If they type "n," the program will print and "Okay! Come back when you are Ready!".
	If the user states they are a producer, the program will prompt the user for a code. If they type an incorrect code, it will re-prompt the user until they type the correct code. After typing the valid code, the producer is prompted for the name of the order. It also asks the producer if they wish to update the status to the next stage. The name of the order and the producer's answer to the update question is passed into the produce function. Then the return statement contains the status before and after asking if they want an update.

	Each method first reads all the information in the file and writes it to a dictionary to be manipulated. This was a design choice since putting the information in a dictionary allows us to manage the data efficiently.



