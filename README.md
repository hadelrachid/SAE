# SAE - Sistematização da Assistência de Enfermagem

## Descrição
O projeto SAE (Sistematização da Assistência de Enfermagem) precisa ser desenvolvido como uma resposta a um desafio proposto pela 
Secretaria de Saúde da Prefeitura de São José dos Campos, voltado para as unidades de Pronto Atendimento 24 Horas. O sistema 
visa digitalizar o processo de anotações manuais, exigido pelo Conselho Federal de Enfermagem (COFEN), que é atualmente realizado 
em cinco fichas distintas.

O aplicativo precisa ser desenvolvido como um protótipo na linguagem Python, utilizando o framework PyQt6 para a interface gráfica e SQLite 
para o banco de dados. Ele tem que permitir a entrada, visualização, impressão e armazenamento de dados de pacientes de forma digital, facilitando 
o processo de assistência de enfermagem.

## Estrutura do Projeto
Por enquanto, a estrutura do projeto é organizada da seguinte forma:
Classes: 
- SDiagnosisPrescription (Diagnóstico e Prescrição)
- SPatient (Dados do Paciente)
- SPhysicalExamination (Exame Físico)
- Test (Classe para testar as classes)

## Tecnologias Utilizadas
- **Python**: Linguagem principal do desenvolvimento.
- **PyQt6**: Utilizado para a interface gráfica.
- **SQLite**: Banco de dados leve e portável para armazenamento de dados.
