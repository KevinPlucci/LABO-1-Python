import re

texto = "QUEVEDO || BZRP Music Sessions #52"
fecha = "2022-07-06 00\\00:00"
print(re.split(r"[\|]{2}|[#]{1}", texto))

print(re.split(r"[\- :]{1}", fecha))
print(re.split(r"\-| |:", fecha))
print(re.split(r"[\\]+", fecha))

print(re.findall(r"[a-zA-Z ]{2,}[|]{2}([a-zA-Z ]{2,}#[0-9]+)", texto))
