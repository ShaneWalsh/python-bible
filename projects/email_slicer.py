
email = input("email please:")

ind = email.find("@")
if ind > -1:
    emailName = email[:ind]
    emailDomain = email[ind+1:]

    print("Name: {}".format(emailName))
    print("Domain: {}".format(emailDomain))

    word = "antidisestablishmentarianism"
    answer = word[word.find('est'):word.find('est')+len("establishment")]
    print(answer)
else:
    print('Invalid email, muppet.')

number = int(input("give me a number to compare with 100 please"))

if number < 100 :
    print("{} is less than 100".format(number))
elif number > 100:
    print("{} is grater than 100".format(number))
else :
    print("{} is equal to 100".format(number))
