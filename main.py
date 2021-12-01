def camel_case_split(str):

    words = [[str[0]]]

  

    for c in str[1:]:

        if words[-1][-1].islower() and c.isupper():

            words.append(list(c))

        else:

            words[-1].append(c)

    r = [''.join(word) for word in words]
    res = ' '.join(x for x in r)

    return res

str = "geeksForGeeks"

print(camel_case_split(str))
