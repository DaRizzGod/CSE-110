print("Please enter the following information: \n")
#Variables
first_name = input("First name: ")
last_name = input("Last name: ")
email = input("Email address: ")
phone = input("Phone number: ")
job_title = input("Job title: ")
id_num = input("ID Number: ")
dob = input("Date of birth:")
#ID card printout
print("\nThe ID Card is:\n"
      "--------------------\n"
      f"{last_name.upper()}, {first_name.capitalize()} \n"
      f"{job_title.title()} \n"
      "\n"
      f"Email Address: {email.lower()} \n"
      f"Phone Number: {phone} \n"
      "\n"
      f"ID: {id_num}		DOB: {dob} \n"
      "--------------------"
    )


