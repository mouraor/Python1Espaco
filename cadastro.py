
import pandas as pd
import email_service

arq = pd.ExcelFile(r"C:/Temp/Python/UmEspaco/Controle.xlsx")
#sheet start Start from 0
Sheet_cadastro = arq.parse(1)

#varre cada linha da coluna selecioanda e retorna o valor sem header e sem indice
var = 0

for linha in Sheet_cadastro:
   print(linha)

   Responsavel = Sheet_cadastro.loc[[var], ['Responsável']]
   nome = Responsavel.to_string(header=None, index=False)
   
   # Contato = Sheet_cadastro.loc[[var], ['Contato']]
   # destino = Contato.to_string(header=None, index=False)
   
   print(nome)
   # print(destino)
   var = var + 1

#Call the sendEmail service
#If the name is not fill the attachment is not sent
#email_service.SendEmail('prof.erikaathie.umespaco@gmail.com', 'Rodrigo Mourao Lino Silva')

