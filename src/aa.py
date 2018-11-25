import numpy as np

class AA(object):
    def __init__(self, peoples):
        self.peoples = peoples
        self.num_people = len(self.peoples)

    def get_to_pay_matrix(self):
        to_pay_matrix = np.zeros((self.num_people, self.num_people))
        # row: to pay; column: to receive

        for i, people in enumerate(self.peoples):
            others_to_pay = people.paid / self.num_people
            for j in range(i, self.num_people):
                if j != i:
                    to_pay_matrix[j, i] += others_to_pay
                    to_pay_matrix[i, j] += -others_to_pay
        
        return to_pay_matrix
    
    def get_aa_result(self, to_pay_matrix):
        result = ""
        for i in range(self.num_people):
            for j in range(i, self.num_people):
                if to_pay_matrix[i, j] > 0:
                    result += f"{self.peoples[i].name} 向 {self.peoples[j].name} 付款 {to_pay_matrix[i, j]} 元\n"
                elif to_pay_matrix[i, j] < 0:
                    result += f"{self.peoples[j].name} 向 {self.peoples[i].name} 付款 {-to_pay_matrix[i, j]} 元\n"
                else:
                    pass
        
        return result