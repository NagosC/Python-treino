texto1 = "arara"
texto2 = "Python"

texto_format1 = texto1.lower().replace(" ","")
texto_format2 = texto2.lower().replace(" ", "")

palindromo1 = texto_format1 == texto1[::-1]
palindromo2 = texto_format2 == texto2[::-1]

print(palindromo1)
print(palindromo2)
