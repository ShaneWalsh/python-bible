
email = input("email please:")

ind = email.find("@")
emailName = email[:ind]
emailDomain = email[ind+1:]

print("Name: {}".format(emailName))
print("Domain: {}".format(emailDomain))

word = "antidisestablishmentarianism"
answer = word[word.find('est'):word.find('est')+len("establishment")]
print(answer)
