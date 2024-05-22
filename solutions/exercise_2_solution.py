
class Clinic:
    def __init__(self, clinic_name, staff):
        self.clinic_name = clinic_name
        self.staff = staff

        self.open = False

    def open_clinic(self):
        self.open = True

    def close_clinic(self):
        self.open = False

    def list_staff(self):
        print (f"Staff at {self.clinic_name} are :")
        for member in self.staff:
            print (member)

class Weight_Loss_Clinic(Clinic):
    def __init__(self, clinic_name, staff, lead_nurse):
        super().__init__(clinic_name, staff)

        self.lead_nurse = lead_nurse

    def check_lead_in_staff(self):
        if self.lead_nurse in self.staff:
            print ("Lead nurse is in staff list")
        else:
            print ("Lead nurse not in staff list")
            self.staff.append(self.lead_nurse)
            print ("Lead nurse added")

class Sexual_Health_Clinic(Clinic):
    def __init__(self, clinic_name, staff):
        super().__init__(clinic_name, staff)

        self.appointment_book = {}

    def book_test(self, patient_name, time):
        self.appointment_book[patient_name] = time

    def print_appointments(self):
        print (self.appointment_book)

wl_corn_staff = ["Dan", "Sammi", "Amy"]
wl_corn_clinic = Weight_Loss_Clinic("Cornwall Weight Loss Clinic",
                                    wl_corn_staff,
                                    "Anna")

wl_dev_staff = ["Mike", "Tom", "Kerry"]
wl_dev_clinic = Weight_Loss_Clinic("Devon Weight Loss Clinic",
                                   wl_dev_staff,
                                   "Kerry")

wl_corn_clinic.check_lead_in_staff()
wl_corn_clinic.list_staff()

wl_dev_clinic.check_lead_in_staff()
wl_dev_clinic.list_staff()

sh_corn_clinic = Sexual_Health_Clinic("Cornwall Sexual Health Clinic",
                                      wl_corn_staff)
sh_corn_clinic.book_test("Jessica Fletcher", "1100")
sh_corn_clinic.print_appointments()

