linguagens = ["Cobol", "java", "python", "csharp"]
linguagens.sort()
print(linguagens)


linguagens = ["HTML", "CSS", "java", "python", "csharp"]
linguagens.sort(reverse=True)
print(linguagens)


linguagens = ["HTML", "CSS", "java", "python", "csharp"]
linguagens.sort(key=lambda x:len(x))
print(linguagens)

linguagens = ["HTML", "CSS", "java", "python", "csharp"]
linguagens.sort(key=lambda x:len(x), reverse=True)

print(linguagens)


