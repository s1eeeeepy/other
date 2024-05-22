raw_text = """"""

formatted_text = [value for value in raw_text.split()]
values = [int(value) for value in formatted_text if value.isdigit()]
print(values)

dates = [text[1:] for text in formatted_text if "[" in text]
for i in range(len(values)):
    print(f"{values[i]} on {dates[i]}")

print("Total records", len(values))
print("Total value =", sum(values))
