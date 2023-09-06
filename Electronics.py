data = "14inch l@ptop,699|16inch l@ptop,999|sm@rtphone,1099|t@blet,499|g@ming pc,1999"
device_list = data.split("|")
formatted_list = []
for device in device_list:
  device_info_list = device.split(",")
  name = device_info_list[0]
  price = int(device_info_list[1])
  new_price = int(price * 1.1)
  formatted_device = f"Device Name: {name}, Device Price: {new_price}$"
  corrected_formatted_device = formatted_device.replace("@", "a")
  formatted_list.append(corrected_formatted_device)
print(formatted_list)

# PL----------------------------------------------------------------------

dane = "14c@lowy l@top,699|16c@lowy l@ptop,999|sm@rtfon,1099|t@blet,499|komputer do gier,1999"
lista_urzadzen = dane.split("|")
sformatowana_lista = []

for urzadzenie in lista_urzadzen:
    informacje_o_urzadzeniu = urzadzenie.split(",")
    nazwa = informacje_o_urzadzeniu[0]
    cena = int(informacje_o_urzadzeniu[1])
    nowa_cena = int(cena * 1.1)
    sformatowane_urzadzenie = f"Nazwa urządzenia: {nazwa}, Cena urządzenia: {nowa_cena} zł"
    poprawione_sformatowane_urzadzenie = sformatowane_urzadzenie.replace("@", "a")
    sformatowana_lista.append(poprawione_sformatowane_urzadzenie)

print(sformatowana_lista)
