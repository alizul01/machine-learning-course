sum = 0
angka = [0.5, 1, 0.271, 0.324]
normalizer = 4.25
angka_baru = []

# for i in angka:
#     angka_baru.append(i / normalizer)
#
# print(f"Angka Baru {angka_baru}")

for i in angka:
    sum += (i / normalizer)

print(f"Sum ==> {sum}, Mean = {sum / 4}")