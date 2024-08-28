
#-------------------------------------------------------------------------------
# Name:        Patient.py
# Purpose:     As informações dos campos da classe Patient devem preencher a ficha
#              HISTÓRICO DE ENFERMAGEM
# Author:      RACHID DAHER JR
#
# Created:     19/08/2024
# Copyright:   (c) Rachid-PC 2024
#-------------------------------------------------------------------------------

# Definição da classe Paciente (Patient)

class SPatient:
    def __init__(self):
        # Campos da ficha HISTÓRICO DE ENFERMAGEM
        self.__name = None                  # Nome
        self.__birth_date = None            # Data de Nascimento
        self.__age = None                   # Idade
        self.__nationality = None           # Nacionalidade
        self.__attendance_number = None     # Número da Ficha de Atendimento
        self.__department = None            # Setor ou Departamento
        self.__bed_number = None            # Número do leito ou cama
        self.__diagnosis_hypothesis = None  # Hipótese diagnóstica
        self.__main_complaints = None       # Queixas principais
        self.__arrival_history = None       # Histórico de chegada
        self.__previous_clinical_info = []  # Informações clínicas prévias
        self.__personal_history = []        # Antecedentes pessoais        
        self.__medications_in_use = []      # Medicações em uso
        self.__cervical_protection = []     # Proteção da Coluna Cervical
        self.__information_provider = []    # Responsável pelas informações
        self.__additional_info = None       # Outras informações
        
    # ##################################################################### 
        
    # Métodos Setters
    # Configura Nome
    def set_name(self, name):
        self.__name = name

    # Configura Data de nascimento
    def set_birth_date(self, birth_date):
        self.__birth_date = birth_date

    # Configura a Idade baseada na data de nascimento e ano corrente
    def set_age(self, age):
        self.__age = age

    # Configura a Nacionalidade
    def set_nationality(self, nationality):
        self.__nationality = nationality

    # Configura o número da Ficha de Atendimnento (FAA)
    def set_attendance_number(self, attendance_number):
        self.__attendance_number = attendance_number

    # Configura a área do Setor ou Departamento: Emergência, Medicação, etc...
    def set_department(self, department):
        self.__department = department

    # Configura o número do leito
    def set_bed_number(self, bed_number):
        self.__bed_number = bed_number

    # Configura a hipótese diagnóstica
    def set_diagnosis_hypothesis(self, diagnosis_hypothesis):
        self.__diagnosis_hypothesis = diagnosis_hypothesis

    # Configura sobre queixas principais
    def set_main_complaints(self, main_complaints):
        self.__main_complaints = main_complaints

    # Configura o Histórico de chegada
    def set_arrival_history(self, arrival_history):
        self.__arrival_history = arrival_history

    # Informações Clínicas Prévias
    def set_previous_clinical_info(self, previous_clinical_info):
        
        '''
        Espera um dicionário com a seguinte estrutura (copie e cole esse modelo):
        ---------------------------------------------------------------------------------
        {
            "procedencia": 1,  # 1 - Residência, 2 - Samu, 3 - ESF, 4 - UBS, 5 - Outros
            "tabagismo": {
                "status": "Yes",
                "duration": "10 years"  # Optional if status is "Yes"
            },
            "drogas_ilicitas": {
                "status": "No",
                "duration": None  # Optional if status is "No"
            },
            "etilismo": {
                "status": "Yes",
                "duration": "5 years"
            },
            "alergia": {
                "status": "Yes",
                "description": "Pollen"
            }
        }
        --------------------------------------------------------------------------------------------------------
        1. Estrutura do Dicionário:
        - "procedencia": Um valor inteiro que representa a origem.
        - "tabagismo", "drogas_ilicitas", "etilismo" e "alergia": Cada um é um dicionário com um 
          "status" (Yes/No) e, opcionalmente, uma "duration" ou "description".
        
        2. Validação Básica:
        - O método set_previous_clinical_info verifica se todas as chaves esperadas estão presentes no 
          dicionário antes de armazená-lo. Se alguma chave estiver faltando, ele lança um erro (ValueError).
        
        3. Acesso aos Dados:
        - O método get_previous_clinical_info retorna o dicionário completo, permitindo que você acesse cada 
          item conforme necessário.
        ----------------------------------------------------------------------------------------------------------
        '''
        # Validação básica (opcional)
        expected_keys = ["procedencia", "tabagismo", "drogas_ilicitas", "etilismo", "alergia"]
        if not all(key in previous_clinical_info for key in expected_keys):
            raise ValueError(f"Missing keys in previous_clinical_info. Expected keys are: {expected_keys}")
        
        
        self.__previous_clinical_info = previous_clinical_info

    # Configura Antecedentes Pessoais
    def set_personal_history(self, personal_history):
        
        '''
        Espera um dicionário com a seguinte estrutura (copie e cole esse modelo):
        --------------------------------------------------------------------------------------------------------
         {
            "antecedentes": 1,  # 1 - DM, 2 - HAS, 3 - Cadiopatia, 4 - Respiratoria, 5 - Neurologica
            "cirurgia": {
                "status": "Yes",
                "description": "cardiology"  # Optional if status is "Yes"
            }     
        }
        --------------------------------------------------------------------------------------------------------
        1. Estrutura do Dicionário:
        - "antecedentes": Um valor inteiro que representa a doença.
        - "cirurgia", possui "status" (Yes/No) e, opcionalmente, uma "description".
        
        2. Validação Básica:
        - O método set_personal_history verifica se todas as chaves esperadas estão presentes no 
          dicionário antes de armazená-lo. Se alguma chave estiver faltando, ele lança um erro (ValueError).
        
        3. Acesso aos Dados:
        - O método set_personal_history retorna o dicionário completo, permitindo que você acesse cada 
          item conforme necessário.
        ----------------------------------------------------------------------------------------------------------       
        '''
        # Validação básica (opcional)
        expected_keys = ["antecedentes", "cirurgia"]
        if not all(key in personal_history for key in expected_keys):
            raise ValueError(f"Missing keys in previous_clinical_info. Expected keys are: {expected_keys}")
            
        self.__personal_history = personal_history

    # Configura Medicações em Uso
    def set_medications_in_use(self, medications_in_use):
        self.__medications_in_use = medications_in_use

    # Configura Proteção da Coluna Cervical
    def set_cervical_protection(self, cervical_protection):
        self.__cervical_protection = cervical_protection

    # Configura Responsável pelas informações
    def set_information_provider(self, information_provider):
        self.__information_provider = information_provider

    # Configura Outras informações
    def set_additional_info(self, additional_info):
        self.__additional_info = additional_info
        
    # ##################################################################### 

    # Métodos Getters
    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date

    def get_age(self):
        return self.__age

    def get_nationality(self):
        return self.__nationality

    def get_attendance_number(self):
        return self.__attendance_number

    def get_department(self):
        return self.__department

    def get_bed_number(self):
        return self.__bed_number

    def get_diagnosis_hypothesis(self):
        return self.__diagnosis_hypothesis

    def get_main_complaints(self):
        return self.__main_complaints

    def get_arrival_history(self):
        return self.__arrival_history

    def get_previous_clinical_info(self):
        return self.__previous_clinical_info

    def get_personal_history(self):
        return self.__personal_history

    def get_medications_in_use(self):
        return self.__medications_in_use

    def get_cervical_protection(self):
        return self.__cervical_protection

    def get_information_provider(self):
        return self.__information_provider

    def get_additional_info(self):
        return self.__additional_info
