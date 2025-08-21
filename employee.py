#Rachel Hopping
#Create class Employee with name, ID number, department, and job title
#Include initializer method, accessor and mutator methods for each data attribute

class Employee:
    
    def __init__(self, name, id_num, dept, job_title):
        self.__name = name
        self.__id_num = id_num
        self.__dept = dept
        self.__job_title = job_title

    def set_name(self, name):
        self.__name = name

    def set_id_num(self, id_num):
        self.__id_num = id_num

    def set_dept(self, dept):
        self.__dept = dept

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_name(self):
        return self.__name

    def get_id_num(self):
        return self.__id_num

    def get_dept(self):
        return self.__dept

    def get_job_title(self):
        return self.__job_title
