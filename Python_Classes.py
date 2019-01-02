import random

class Patient:
    instances = 0

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        Patient.instances += 1

    def getPatientInfo(self):
        print("Patient name is {}".format(self.name))
        print("Patient gender is {}".format(self.gender))

p1 = Patient("William", "male")
p2 = Patient("Test", "Female")

p1.getPatientInfo()
print(Patient.instances)