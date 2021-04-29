import csv

def write_into_csv(info_list):
     with open('student_info.csv', 'a', newline= '')as csv_projectfile:
          writer = csv.writer(csv_projectfile)

          if csv_projectfile.tell() == 0:
              writer.writerow(["Name", "Age", "ContactNumber", "Email_ID"])

          writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_number = 1

    while(condition):
         student_info = input(" Enter student info. for student #{} in the following form.(Name Age ContactNumber Email_ID): ".format(student_number))

         student_info_list = student_info.split(' ')

         print("\nThe entered information is- \nName: {}\nAge: {}\nContactNumber: {}\nEmail_ID: {}"
               .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

         choice_check = input("Is the entered information correct?(yes/no): ")

         if choice_check == "yes":
             write_into_csv(student_info_list)

             condition_check = input("Enter (yes/no) if you want to add info. for another student: ")
             if condition_check == "yes":
                  condition = True
                  student_number = student_number + 1
             elif condition_check == "no":
                 condition = False
             elif choice_check == "no":
                   print("\nRe-enter the value!")