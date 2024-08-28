#-------------------------------------------------------------------------------
# Name:        PhysicalExamination.py
# Purpose:     As informações dos campos da classe PhysicalExamination devem 
#              preencher a ficha Exame Físico
# Author:      RACHID DAHER JR
#
# Created:     19/08/2024
# Copyright:   (c) Rachid-PC 2024
#-------------------------------------------------------------------------------


# Definição da classe Exame Físico (PhysicalExamination)
class SPhysicalExamination:
    def __init__(self):
        # Cada campo agora é uma lista, onde cada item pode ser um dicionário detalhado
        self.__neurological_assessment = []     # Avaliação Neurológica
        self.__respiratory_assessment = []      # Avaliação do Aparelho Respiratório
        self.__cardiological_assessment = []    # Avaliação Cardiológica
        self.__gastrointestinal_assessment = [] # Avaliação do Aparelho Gastrointestinal
        self.__urinary_assessment = []          # Avaliação do Aparelho Urinário
        self.__skin_assessment = []             # Avaliação da Pele
        self.__catheters = []                   # Cateteres

    # ##################################################################### 

    # Métodos Setters - Adiciona itens às listas
    def add_neurological_assessment(self, assessment_item):
        self.__neurological_assessment.append(assessment_item)

    def add_respiratory_assessment(self, assessment_item):
        self.__respiratory_assessment.append(assessment_item)

    def add_cardiological_assessment(self, assessment_item):
        self.__cardiological_assessment.append(assessment_item)

    def add_gastrointestinal_assessment(self, assessment_item):
        self.__gastrointestinal_assessment.append(assessment_item)

    def add_urinary_assessment(self, assessment_item):
        self.__urinary_assessment.append(assessment_item)

    def add_skin_assessment(self, assessment_item):
        self.__skin_assessment.append(assessment_item)

    def add_catheters(self, catheter_item):
        self.__catheters.append(catheter_item)

    # ##################################################################### 

    # Métodos Getters - Retorna as listas completas
    def get_neurological_assessment(self):
        return self.__neurological_assessment

    def get_respiratory_assessment(self):
        return self.__respiratory_assessment

    def get_cardiological_assessment(self):
        return self.__cardiological_assessment

    def get_gastrointestinal_assessment(self):
        return self.__gastrointestinal_assessment

    def get_urinary_assessment(self):
        return self.__urinary_assessment

    def get_skin_assessment(self):
        return self.__skin_assessment

    def get_catheters(self):
        return self.__catheters
