def insert_address(d, val):
    val = val.replace('{', '')
    val = val.replace('}', '')
    val = val.strip()

    address_parts = val.split(',')
    dict_address = {}
    for tmp in address_parts:
        tmp = tmp.split(":")
        dict_address[tmp[0]] = tmp[1]

    d["adresa"] = dict_address


fin = open("persoane.in", 'r')

data = fin.readlines()

lst_pers = []

for entry in data:
    parts = entry.split(",", 2)
    tmp_dict = {}
    for part in parts:  # pt nume, prenume, adresa
        field, value = part.split(":", 1)
        if field != "adresa":
            tmp_dict[field] = value
        else:
            insert_address(tmp_dict, value)

    lst_pers.append(tmp_dict)

print(lst_pers)

dict_orase = {}

for pers in lst_pers:
    dict_orase[pers["adresa"]["oras"]] = dict_orase.get(pers["adresa"]["oras"], []) + [pers["nume"]+' '+pers["prenume"]]

print(dict_orase)
