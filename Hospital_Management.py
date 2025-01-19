# author: Chetan Parteek Sandhu
# Doctor and DoctorManagement classes
class Doctor:
    def __init__(self, doctor_id=None, name=None, specialization=None,
                 timing=None, qualification=None, room_number=None):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.timing = timing
        self.qualification = qualification
        self.room_number = room_number

    def get_doctor_id(self):
        return self.doctor_id

    def set_doctor_id(self, new_id):
        self.doctor_id = new_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_specialist(self):
        return self.specialization

    def set_specialist(self, new_specialization):
        self.specialization = new_specialization

    def get_timing(self):
        return self.timing

    def set_timing(self, new_timing):
        self.timing = new_timing

    def get_qualification(self):
        return self.qualification

    def set_qualification(self, new_qualification):
        self.qualification = new_qualification

    def get_room_number(self):
        return self.room_number

    def set_room_number(self, new_room_number):
        self.room_number = new_room_number

    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_" \
               f"{self.timing}_{self.qualification}_{self.room_number}"


class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_file()

    @staticmethod
    def format_dr_info(doctor):
        return f"{doctor.doctor_id}_{doctor.name}_{doctor.specialization}_" \
               f"{doctor.timing}_{doctor.qualification}_{doctor.room_number}"

    @staticmethod
    def enter_dr_info():
        doctor_id = input("Enter Doctor's ID: ")
        name = input("Enter Doctor's Name: ")
        specialization = input("Enter Doctor's Specialization: ")
        timing = input("Enter Doctor's Timing (e.g., 7am-10pm): ")
        qualification = input("Enter Doctor's Qualification: ")
        room_number = input("Enter Doctor's Room Number: ")

        doctor = Doctor(doctor_id, name, specialization, timing, qualification, room_number)
        return doctor

    def read_doctors_file(self):
        with open("doctors.txt", "r") as doc_data:

            for data in doc_data:
                doctor_id, name, specialization, timing, qualification, room_number = data.strip().split("_")
                doctor = Doctor(doctor_id, name, specialization, timing, qualification, room_number)
                self.doctors.append(doctor)
            doc_data.close()

    def search_doctor_by_id(self):
        doctor_id = input("Enter Doctor ID: ")
        for doctor in self.doctors:
            if doctor.doctor_id == doctor_id:
                print("{:<5} {:<15} {:<15} "
                      "{:<15} {:<15} {:<15}".format("ID", "Name", "Specialization",
                                                    "Timing", "Qualification", "Room Number"))
                self.display_doctor_info(doctor)
                return
        else:
            print("Can't find the doctor with the same ID on the system")

    def search_doctor_by_name(self):
        name = input("Enter Doctor Name: ")
        for doctor in self.doctors:
            if doctor.name == name:
                print("{:<5} {:<15} {:<15} "
                      "{:<15} {:<15} {:<15}".format("ID", "Name", "Specialization",
                                                    "Timing", "Qualification", "Room Number"))
                self.display_doctor_info(doctor)
                return
        else:
            print("Can't find the doctor with the same name on the system")

    @staticmethod
    def display_doctor_info(doctor):
        print("{:<5} {:<15} {:<15} "
              "{:<15} {:<15} {:<15}".format(doctor.doctor_id, doctor.name, doctor.specialization,
                                            doctor.timing, doctor.qualification, doctor.room_number))

    def edit_doctor_info(self):
        # Asks for a Doctor's ID
        doctor_id = input("Please enter the id of the doctor that you want to edit their information: ")

        # Searches Doctor List
        for doctor in self.doctors:

            # If ID matches, asks for updated values
            if doctor.doctor_id == doctor_id:
                doctor.name = input("Enter Doctor Name: ")
                doctor.specialization = input("Enter Doctor's Specialization: ")
                doctor.timing = input("Enter Doctor's Timing (e.g., 7am-10pm): ")
                doctor.qualification = input("Enter Doctor's Qualification: ")
                doctor.room_number = input("Enter Doctor's Room Number: ")

                # Updates Doctors in original text file
                self.write_list_of_doctors_to_file()

                # Confirms Doctor has been edited
                print(f"Doctor whose ID is {doctor.doctor_id} has been edited.")
                return

        # If Doctor doesn't exist, prints error
        else:
            print("Cannot find the doctor in the data")

    def display_doctors_list(self):
        # Displays Doctor List
        for doctor in self.doctors:
            self.display_doctor_info(doctor)
            print()

    def write_list_of_doctors_to_file(self):
        # Writes new doctor in the list
        with open("doctors.txt", "w") as doc_data:
            for doctor in self.doctors:
                doc_data.write(f"{self.format_dr_info(doctor)}\n")
            doc_data.close()

    def add_dr_to_file(self):
        # User inputs new doctor
        doctor = self.enter_dr_info()

        # Appends new doctor into doctor list
        self.doctors.append(doctor)

        # Appends new doctor into Doctor text file
        with open("doctors.txt", "a") as doc_data:
            doc_data.write(f"\n{self.format_dr_info(doctor)}")
        doc_data.close()
        # Confirms new doctor has been added
        print(f"Doctor whose ID is {doctor.doctor_id} has been added")


class Patient:
    def __init__(self, pid=None, name=None, disease=None, gender=None, age=None):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def get_pid(self):
        return self.pid

    def get_name(self):
        return self.name

    def get_disease(self):
        return self.disease

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

    def set_pid(self, new_id):
        self.pid = new_id

    def set_name(self, new_name):
        self.name = new_name

    def set_disease(self, new_disease):
        self.disease = new_disease

    def set_gender(self, new_gender):
        self.gender = new_gender

    def set_age(self, new_age):
        self.age = new_age

    def __str__(self):
        return f'{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}'


class PatientManger:
    def __init__(self):
        self.patient_list = []
        self.read_patients_file()

    @staticmethod
    def format_patient_info_for_file(patient):
        # ^ Takes an Object and Formats it
        return f'{patient.pid}_{patient.name}_{patient.disease}_{patient.gender}_{patient.age}'

    @staticmethod
    def enter_patient_info():
        # Asks the User to Enter Patient Info
        new_patient = Patient()
        new_patient.set_pid(input("Enter Patient id: "))
        new_patient.set_name(input("Enter Patient name: "))
        new_patient.set_disease(input("Enter Patient disease: "))
        new_patient.set_gender(input("Enter Patient gender: "))
        new_patient.set_age(input("Enter Patient age: "))

        # Creates a Patient Object using entered information
        patient = Patient(new_patient.get_pid(), new_patient.get_name(),
                       new_patient.get_disease(), new_patient.get_gender(), new_patient.get_age())

        # Returns patient object
        return patient

    def read_patients_file(self):
        # Reads Patients' Data
        patients_data = open("patients.txt", "r")

        # Creates an Object for each Patient Record
        for line in patients_data:
            patient_data = line.strip().split("_")
            patient = Patient(patient_data[0], patient_data[1], patient_data[2],
                              patient_data[3], patient_data[4])

            # Appends Patient Objects to Patient List
            self.patient_list.append(patient)
        patients_data.close()

    def search_patient_by_id(self):
        # Accepts Patient ID from User
        search_id = input("Enter the Patient Id: ")

        # Iterates Through List
        for searching_patient in self.patient_list:
            if searching_patient.pid == search_id:
                print(f'{Patient.get_pid(self.patient_list[0]):<5} '
                      f'{Patient.get_name(self.patient_list[0]):<15} '
                      f'{Patient.get_disease(self.patient_list[0]):<15} '
                      f'{Patient.get_gender(self.patient_list[0]):<15} '
                      f'{Patient.get_age(self.patient_list[0])}')
                self.display_patient_info(searching_patient)
                return

        # If Patient doesn't exist, prints error
        else:
            print("Can't find the patient with the same id on the system")

    @staticmethod
    def display_patient_info(patient):
        print("{:<5} {:<15} {:<15}"
              " {:<15} {:<15}".format(patient.pid, patient.name,
                                      patient.disease, patient.gender, patient.age))

    def edit_patient_info_by_id(self):
        # Asks for a Patient's ID
        search_id = input("Please enter the id of the Patient that you want to edit their information: ")

        # Searches Patient List
        for searching_patient in self.patient_list:

            # # If ID matches, asks for updated values
            if searching_patient.pid == search_id:
                searching_patient.name = input("Enter new Name: ")
                searching_patient.disease = input("Enter new disease: ")
                searching_patient.gender = input("Enter new gender: ")
                searching_patient.age = input("Enter new age: ")

                # Updates Patients in original text file
                self.write_list_of_patients_to_file()

                # Confirms Patient has been edited
                print(f'Patient whose ID is {searching_patient.pid} has been edited.')
                return
        else:
            print("Can't find the patient with the same id on the system")

    def display_patients_list(self):
        # Displays Patient List
        for displaying_patient in self.patient_list:
            self.display_patient_info(displaying_patient)
            print()

    def write_list_of_patients_to_file(self):
        patients_data = open("patients.txt", "w")
        # Writes new patient in the list
        for updating in self.patient_list:
            patients_data.write(f"{self.format_patient_info_for_file(updating)}\n")
        patients_data.close()

    def add_patient_to_file(self):
        # User inputs new patient
        new_patient = self.enter_patient_info()

        # Appends new patient into patient list
        self.patient_list.append(new_patient)

        # Appends new patient into Patient text file
        patients_data = open("patients.txt", "a")
        patients_data.write(f"\n{new_patient}")
        patients_data.close()

        # Confirms new patient has been added
        print(f"Patient whose ID is {Patient.get_pid(new_patient)} has been added.")


# This section will be for Management Class
class Management:
    @staticmethod
    def display_menu():
        # Asks the user to select their desired choice
        while True:
            print("Welcome to Alberta Hospital (AH) Management system ")
            print("Select from the following options, or select 3 to stop:")
            print("1 - Doctors")
            print("2 - Patients")
            print("3 - Exit Program ")
            choice = input(">>> ")

            if choice == "1":
                # If user selects 1, it displays the Doctors submenu
                while True:
                    print("Doctors Menu:")
                    print("1 - Display Doctors list")
                    print("2 - Search for doctor by ID")
                    print("3 - Search for doctor by name")
                    print("4 - Add doctor")
                    print("5 - Edit doctor info")
                    print("6 - Back to the Main Menu")
                    doctor_submenu = input(">>> ")
                    if doctor_submenu == "1":
                        DoctorManager().display_doctors_list()
                    elif doctor_submenu == "2":
                        DoctorManager().search_doctor_by_id()
                    elif doctor_submenu == "3":
                        DoctorManager().search_doctor_by_name()
                    elif doctor_submenu == "4":
                        DoctorManager().add_dr_to_file()
                    elif doctor_submenu == "5":
                        DoctorManager().edit_doctor_info()
                    elif doctor_submenu == "6":
                        break
                    else:
                        print("Invalid Input")
                continue

            elif choice == "2":
                # If user selects 2, it displays the Patients submenu
                while True:
                    print("Patients Menu:")
                    print("1 - Display patients list")
                    print("2 - Search for patient by ID")
                    print("3 - Add patient")
                    print("4 - Edit patient info")
                    print("5 - Back to the Main Menu")
                    patient_submenu = input(">>> ")
                    if patient_submenu == "1":
                        PatientManger().display_patients_list()
                    elif patient_submenu == "2":
                        PatientManger().search_patient_by_id()
                    elif patient_submenu == "3":
                        PatientManger().add_patient_to_file()
                    elif patient_submenu == "4":
                        PatientManger().edit_patient_info_by_id()
                    elif patient_submenu == "5":
                        break
                    else:
                        print("Invalid Input")
                continue

            elif choice == "3":
                # If user selects 3, The program Ends.
                print("Thanks for using the program. Bye!")
                break

            else:
                # Error check if user enters any wrong input
                print("Invalid Input")


# Running Code Output.
Management().display_menu()
