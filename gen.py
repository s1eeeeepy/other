s = "SomeCamelCasedText"
output = [" " + i if i.isupper() else i for i in s]
print("".join(output)[1:])
