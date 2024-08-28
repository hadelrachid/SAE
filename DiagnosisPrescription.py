#-------------------------------------------------------------------------------
# Name:        DiagnosisPrescription.py
# Purpose:     As informações dos campos da classe DiagnosisPrescription devem 
#              preencher a ficha Diagnóstico e Prescrição
#              
# Author:      RACHID DAHER JR
#
# Created:     19/08/2024
# Copyright:   (c) Rachid-PC 2024
#-------------------------------------------------------------------------------

# Definição da classe SDiagnosisPrescription
class SDiagnosisPrescription:
    def __init__(self, diagnosis):
        # Atributos privados
        self.__diagnosis = []    # Campo Diagnóstico
        self.__prescription = [] # Campo Prescrição
        self.__time = []         # Campo Horário
        
        # Chama o método __set_diagnosis para validação
        self.__set_diagnosis(diagnosis)
        
    # ##################################################################### 

    # Setters
    # Aqui deve fazer uma validação.
    # Esse método foi deixado como privado 
    def __set_diagnosis(self, diagnosis):
        '''
            Adiciona diagnósticos à lista de diagnósticos:
                
            1 : Risco de aspiração
            2 : Padrão Respiratório Ineficaz
            3 : Risco para troca de Gases Prejudicada
            4 : Ventilação Espontânea Prejudicada"
            5 : Desobstrução ineficaz de vias aéreas
            6 : Mucosa Oral Prejudicada
            7 : Déficit no Auto Cuidado Para Alimentação
            8 : Risco de Motilidade Gastrintestinal Disfuncional
            9 : Risco Para Úlcera de Pressão
            10 : Deglutição Prejudicada
            11 : Integridade da Pele Prejudicada
            12 : Eliminação Urinária Prejudicada
            13 : Dor
            14 : Conforto Prejudicado
            15 : Mobilidade Física Prejudicada
            16 : Déficit no Auto Cuidado: Banho/Higiene
            17 : Perfusão Tissular Cerebral Ineficaz
            18 : Termorregulação Ineficaz
            19 : Perfusão Tissular Cardíaca Ineficaz
            20 : Risco para Queda
            21 : Risco para infecção
            22 : Ansiedade
            23 : Confusão
            24 : Risco para Flebite
            25 : Risco para Perda da Sonda Enteral
        '''
        
        if isinstance(diagnosis, list) and all(isinstance(d, int) and 1 <= d <= 25 for d in diagnosis):
            self.__diagnosis = diagnosis
            self.__set_prescription()  # Atualiza as prescrições com base nos diagnósticos
        else:
            raise ValueError("Diagnóstico inválido. Deve ser uma lista de inteiros entre 1 e 25.")
        
        
    # A prescição vai depender do diagnóstico
    # Esse método foi deixado como privado   
    def __set_prescription(self):
        # Escolhendo os tipos de diagnósticos
        # haverá a opção correspondente para prescrição
        # Por exemplo, se for escolhido apenas a opção 1 : Risco de Aspiração, 
        # as prescrições serão todas as opções que tiverem o número 1.
        # Se o diagnóstico tiver apenas o número 24, terá como opção as prescrições
        # que contém o 24.
        # Se for escolhido mais de diagnósticos, deve-se observar os números correspondentes
        # para escolher as prescrições correspondentes.
        
        '''
        A :  1, 2, 3, 4, 5, 17: Manter decúbito em ___º e região cervical retificada 
        B :  1, 2, 4, 5, 17 : Monitorar e anotar FR (Frequencia Respiratória) antes da alimentação 
        C :  1, 2, 3, 4, 5, 10, 14, 17 : Aspirar VAI e VAS com sonda nº ___ s/h 
        D :  1, 2, 3, 4, 5, 17, 19, 22 : Comunicar e anotar alterações na perfusão periférica, FR e SatO2 <= 94% de 2/2h
        E :  2, 3, 4, 5, 17, 18, 19, 24 : Monitorar e registrar sinais vitais; aplicar o Protocolo MEWS 
        F :  1, 2, 3, 4, 5, 8, 17, 19, 20, 23: Observar e anotar o nível de consciência de ___/___ h 
        G :  1, 2, 3, 4, 5, 8, 17, 19 : Observar, anotar e comunicar palidez cutânea, hipoatividade e/ou vômito 
        H :  6, 7, 8, 9, 10, 11 : Estimular, intalar ou oferecer a dieta prescrita (H)
        I :  24 : Instalar 40 ml de água após administração de medicaão ou dieta por via SNE 
        J :  2, 4, 5, 6, 16, 17 : Estimular ou realizar higiene oral ___/___ 
        K :  8, 12, 13, 14, 15, 17 : Observar e anotar eliminação vesico-intestinal 
        L :  21, 24 : Realizar assepsia ou HUB com álcool a 70% antes e após de desconectar equipos para infosões 
        M :  11, 13, 14, 15, 21 : Realizar curativo oclusivo em ______ com _______; anotar aspecto 
        N :  18, 21, 24 : Observar e anotar aspecto do local do acesso venoso 
        O :  2, 3, 4, 14, 15, 16, 17, 19, 20 : Estimular ou realizar banho de ______ 
        P :  9, 11, 13, 14, 15, 16, 17 : Realizar mudança de decúbito de ___/____ h 
        Q :  8, 9, 11, 13, 14, 17, 19, 22, 23 : Promover conforto e alívio da dor 
        R :  4, 13, 14, 15, 17, 19, 22, 23: Promover apoio emocional e ambiente seguro 
        S :  4, 15, 17, 20, 22, 23 : Manter grade elevadas 
        T :  17, 20, 23 : Manter contenção mecância em _____ 
        U :  17, 20, 23 : Realizar rodízio dos locais de contenção mecância de 2/2h 
        V :  8, 11, 17 : Realizar higiene íntima a cada troca de fralda 
               
        '''
        
        '''
        Atualiza as prescrições com base nos diagnósticos fornecidos.
        
        '''
        mapping_prescription = {
            1: "Manter decúbito em ___º e região cervical retificada",
            2: "Monitorar e anotar FR (Frequencia Respiratória) antes da alimentação",
            3: "Aspirar VAI e VAS com sonda nº ___ s/h",
            4: "Comunicar e anotar alterações na perfusão periférica, FR e SatO2 <= '94%' de 2/2h",
            5: "Monitorar e registrar sinais vitais; aplicar o Protocolo MEWS",
            6: "Observar e anotar o nível de consciência de ___/___ h",
            7: "Observar, anotar e comunicar palidez cutânea, hipoatividade e/ou vômito",
            8: "Estimular, instalar ou oferecer a dieta prescrita",
            9: "Instalar 40 ml de água após administração de medicação ou dieta por via SNE",
            10: "Estimular ou realizar higiene oral ___/___",
            11: "Observar e anotar eliminação vesico-intestinal",
            12: "Realizar assepsia ou HUB com álcool a '70%' antes e após de desconectar equipos para infusões",
            13: "Realizar curativo oclusivo em ______ com _______; anotar aspecto",
            14: "Observar e anotar aspecto do local do acesso venoso",
            15: "Estimular ou realizar banho de ______",
            16: "Realizar mudança de decúbito de ___/____ h",
            17: "Promover conforto e alívio da dor",
            18: "Promover apoio emocional e ambiente seguro",
            19: "Manter grade elevadas",
            20: "Manter contenção mecânica em _____",
            21: "Realizar rodízio dos locais de contenção mecânica de 2/2h",
            22: "Realizar higiene íntima a cada troca de fralda"            
        }
        
        mapping =  {
            1: [1, 2, 3, 4, 5, 17],
            2: [1, 2, 4, 5, 17],
            3: [1, 2, 3, 4, 5, 10, 14, 17],
            4: [1, 2, 3, 4, 5, 17, 19, 22],
            5: [2, 3, 4, 5, 17, 18, 19, 24],
            6: [1, 2, 3, 4, 5, 8, 17, 19, 20, 23],
            7: [1, 2, 3, 4, 5, 8, 17, 19],
            8: [6, 7, 8, 9, 10, 11],
            9: [24],
            10: [2, 4, 5, 6, 16, 17],
            11: [8, 12, 13, 14, 15, 17],
            12: [21, 24],
            13: [11, 13, 14, 15, 21],
            14: [18, 21, 24],
            15: [2, 3, 4, 14, 15, 16, 17, 19, 20],
            16: [9, 11, 13, 14, 15, 16, 17],
            17: [8, 9, 11, 13, 14, 17, 19, 22, 23],
            18: [4, 13, 14, 15, 17, 19, 22, 23],
            19: [4, 15, 17, 20, 22, 23],
            20: [17, 20, 23],
            21: [17, 20, 23],
            22: [8, 11, 17]
        }
        
        self.__prescription.clear()  # Limpa as prescrições anteriores 
        list_key = [] # Tem a função de guardar chaves já adicionads
        
        # Percorre a lista de diagnósticos
        for d in self.__diagnosis:
            # Percorre o dicionário mapping com suas chaves e valores
            for key, values in mapping.items():
                # se o número da lista __diagnosis corresponder 
                # ao valor mapeado de mapping e se for falso que 
                # a chave (key) já foi adicionada a lista de chaves (list_key)
                # adicione mapping_prescription[key]
                if d in values and not(key in list_key):
                    self.__prescription.append(mapping_prescription[key])
                    list_key.append(key) # Adiciona a chave na list_key
        
        
    # Aqui deve fazer uma validação           
    def set_time(self, time):
        '''
        Configura o horário da prescrição.
        '''
        if isinstance(time, list):
            self.__time = time
        else:
            raise ValueError("O tempo deve ser uma lista.")
    
    # #####################################################################    
    # Getters
    def get_diagnosis(self):
        return self.__diagnosis
    
    def get_prescription(self):
        return self.__prescription
    
    def get_time(self):
        return self.__time
    
    # #####################################################################     
    # Aqui sobscreve o método __str__
    def __str__(self):
        string = ""
        for prescription in self.__prescription:
            string += prescription + "\n"
        
        '''
        Retorna uma representação em string da instância de DiagnosisPrescription.
        '''
        return (f"Diagnósticos: {self.__diagnosis}\n"
                f"Prescrições: {string}\n"
                f"Horários: {self.__time}")
