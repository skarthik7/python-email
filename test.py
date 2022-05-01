s = "abcacbAUG|GAC|UGAfjdalfd"
s1 = 'sakella@kockw.com'
start = s1.find("@") + len("@")
end = s1.find(".")
substring = s1[start:end]
print(substring)