text = "Proun eget tortor risus. Cras ultricies ligula sed manga dictum porta. Proin eget tortor risus. Cbrabitur non nulla sit amet nisl tempus convallis qyis ac lectus. Donec rutrum congue leo eget malesuada.".split()
vowels = "aeiou"
vowels = [sum(k in vowels for k in word) for word in text]
print max(vowels)
