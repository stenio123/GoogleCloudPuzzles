# Word:
# Cypher: AB BC CD DE EF FG are two letter Scrabble words
# Secret: AB FE G DC
# Rule 1: Two last letters of secret (DC) is the reverse of a Scrabble word (CD)
# Rule 2: Last letter (C) must be the second letter of a Scrabble word (BC)
# Rule 3: The first letter of the Scrabble word from Rule 2 must be second letter of another Scrabble word
# Rule 4: Scrabble word from Rule 2 must be second letter of secret 
 
# import re
# import csv
# # Scrabble 2 letter words
# # https://en.wikibooks.org/wiki/Scrabble/Two_Letter_Words
# scrable = ["AA", "AB", "AD", "AE", "AG", "AH", "AI", "AL", "AM", "AN", "AR", "AS", "AT", "AW", "AX", "AY" "BA", "BE", "BI", "BO", "BY", "DA", "DE", "DO", "ED", "EF", "EH", "EL", "EM", "EN", "ER", "ES", "ET", "EW", "EX" "FA", "FE", "GI", "GO", "HA", "HE", "HI", "HM", "HO", "ID", "IF", "IN", "IS", "IT", "JO", "KA", "KI" "LA", "LI", "LO", "MA", "ME", "MI", "MM", "MO", "MU", "MY", "NA", "NE", "NO", "NU" ,"OD", "OE", "OF", "OH", "OI", "OK", "OM", "ON", "OP", "OR", "OS", "OW", "OX", "OY", "PA", "PE", "PI", "PO" ,"QI" ,"RE", "SH", "SI", "SO", "TA", "TE", "TI", "TO" ,"UH", "UM", "UN", "UP", "US", "UT", "WE", "WO", "XI", "XU", "YA", "YE", "YO", "ZA", "CH", "DI", "EA", "EE", "FY", "GU" ,"IO", "JA", "KO", "KY", "NY", "OB", "OO", "OU", "ST", "UG", "UR", "YU" ,"ZE", "ZO"]
# scrable_str = "AA, AB, AD, AE, AG, AH, AI, AL, AM, AN, AR, AS, AT, AW, AX, AY BA, BE, BI, BO, BY DA, DE, DO ED, EF, EH, EL, EM, EN, ER, ES, ET, EW, EX FA, FE GI, GO HA, HE, HI, HM, HO ID, IF, IN, IS, IT JO KA, KI LA, LI, LO MA, ME, MI, MM, MO, MU, MY NA, NE, NO, NU OD, OE, OF, OH, OI, OK, OM, ON, OP, OR, OS, OW, OX, OY PA, PE, PI, PO QI RE SH, SI, SO TA, TE, TI, TO UH, UM, UN, UP, US, UT WE, WO XI, XU YA, YE, YO ZA CH DI EA, EE FY GU IO JA KO, KY NY OB, OO, OU ST UG, UR YU ZE, ZO"

# def rule1(str):
#     # Reverses string
#     return str [::-1]

# def rule2(str, words):
#     last_char = str[-1]
#     reg = r"[a-zA-Z]{0}".format(last_char)
#     match = re.findall(reg, words)
#     return match
#     #print match

# def rule3(matches, words, reverse):
#     # find AB
#     for word in matches:
#         first_char = word[0]
#         reg = r"[a-zA-Z]{0}".format(first_char)
#         match = re.findall(reg, words)
#         # find CD  
#         #second_char = word[1] # this is C from BC
#         #reg2 = r"{0}[a-zA-Z]".format(second_char) # CD
#         #for word2 in match:
#         #    words2 = words.replace(word2, '')
#         #    match2 = re.findall(reg2, words2)
#             # find DE
#         #    second_char3 = word[1] # this is D from CD
#         #    reg3 = r"{0}[a-zA-Z]".format(second_char3) # DE
#         #    for word3 in match2:
#         #        words3 = words.replace(word3, '')
#         #        match3 = re.findall(reg3, words3)
#                 # find EF
#         #        second_char4 = word[1] # this is E from DE
#         #        reg4 = r"{0}[a-zA-Z]".format(second_char4) # EF
#         #        for word4 in match3:
#         #            words4 = words.replace(word4, '')
#         #            match4 = re.findall(reg4, words4)
#        # print 'found: AB'
#         #print match
#         #return match
#         #match = AB

#         #reverse = DC
#                    # print "{0}_ _ _ {1}".format(match, reverse)
#         #rule4(word, match)

# def rule4(match1, matches):
#     filepath = "/Users/steniof/Downloads/scrable.csv"
#     # In original secret, word is 'AB' and match1 is 'DC' (obtained in Rule2)
#     for word in matches:
#         #reg = r"{0}[a-zA-Z][a-zA-Z][a-zA-Z]{1}".format(word, match1)
#         #print 'word, match1'
#         #print word
#         #print match1
#         reg = r"{0}[a-zA-Z][a-zA-Z][a-zA-Z]{1}".format('MI', 'OW')
#         #with open(filepath, 'r') as f:
#         #    data = f.read().strip()
#         #    print(re.findall(reg,data))
#         with open(filepath, 'r') as bigCSV:
#            # for line in re.findall(reg, bigCSV):
#             #    print(line)
#             data=bigCSV.read()
#             search=re.findall(reg,data)
#             if search != []:
#                 print search
#             #contents = csv.reader(bigCSV, delimiter=',')
#             #for row in contents:
#              #   print row
#                     #cell = re.findall(reg,cell)
                   
#             #for i in contents:
#             #    print(re.findall(reg, contents))

# # FG
# def rule5(word, words):
#     #for word in matches:
#     second_char = word[1] #EF
#     reg = r"{0}[a-zA-Z]".format(second_char) # want to find FG
#     match = re.findall(reg, words)
#     return match

# for word in scrable:
#     reverse = rule1(word)
#     match = rule2(reverse, scrable_str)
#     #print 'Found: DC'
#     #print reverse
#     temp_scrable = scrable_str.replace(word, '')
#     ab = rule3(match, temp_scrable, reverse)
#     dc = reverse
#     for word2 in scrable:
#         if word2 != word:
#             reverse2 = rule1(word2) #fe
#             if match != []:
#                 temp_scrable2 = temp_scrable.replace(word2, '')
                
#                 match2 = rule5(word2, temp_scrable2)
#                 for fg in match2:
#                     g = word[1]
#                     #print "{0}{1}{2}{3}".format(match, reverse2, g, reverse)
#                     for ab in match:
#                         a="{0}{1}{2}{3}".format(ab, reverse2, g, reverse)     #String that you want to search
#                         print 'looking for'
#                         print a
#                         with open("/Users/steniof/Downloads/scrable.csv") as f_obj:
#                             reader = csv.reader(f_obj, delimiter=',')
#                             for line in reader:      #Iterates through the rows of your csv
#                                 #print(line)          #line here refers to a row in the csv
#                                 if a in line:      #If the string you want to search is in the row
#                                     print("String found in first row of csv")
#                                 break
#     #print reverse
        
        

