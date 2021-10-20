



import re

scrable = ["AA", "AB", "AD", "AE", "AG", "AH", "AI", "AL", "AM", "AN", "AR", "AS", "AT", "AW", "AX", "AY" "BA", "BE", "BI", "BO", "BY", "DA", "DE", "DO", "ED", "EF", "EH", "EL", "EM", "EN", "ER", "ES", "ET", "EW", "EX" "FA", "FE", "GI", "GO", "HA", "HE", "HI", "HM", "HO", "ID", "IF", "IN", "IS", "IT", "JO", "KA", "KI" "LA", "LI", "LO", "MA", "ME", "MI", "MM", "MO", "MU", "MY", "NA", "NE", "NO", "NU" ,"OD", "OE", "OF", "OH", "OI", "OK", "OM", "ON", "OP", "OR", "OS", "OW", "OX", "OY", "PA", "PE", "PI", "PO" ,"QI" ,"RE", "SH", "SI", "SO", "TA", "TE", "TI", "TO" ,"UH", "UM", "UN", "UP", "US", "UT", "WE", "WO", "XI", "XU", "YA", "YE", "YO", "ZA", "CH", "DI", "EA", "EE", "FY", "GU" ,"IO", "JA", "KO", "KY", "NY", "OB", "OO", "OU", "ST", "UG", "UR", "YU" ,"ZE", "ZO"]
scrable_str = "AA, AB, AD, AE, AG, AH, AI, AL, AM, AN, AR, AS, AT, AW, AX, AY BA, BE, BI, BO, BY DA, DE, DO ED, EF, EH, EL, EM, EN, ER, ES, ET, EW, EX FA, FE GI, GO HA, HE, HI, HM, HO ID, IF, IN, IS, IT JO KA, KI LA, LI, LO MA, ME, MI, MM, MO, MU, MY NA, NE, NO, NU OD, OE, OF, OH, OI, OK, OM, ON, OP, OR, OS, OW, OX, OY PA, PE, PI, PO QI RE SH, SI, SO TA, TE, TI, TO UH, UM, UN, UP, US, UT WE, WO XI, XU YA, YE, YO ZA CH DI EA, EE FY GU IO JA KO, KY NY OB, OO, OU ST UG, UR YU ZE, ZO"

buffer = []
with open('/Users/steniof/Downloads/scrable.csv','r') as l:
	for m in l:
		k=m.split(",")
		buffer.append(k[0])
	buffer = [x.replace("\r\n","") for x in buffer]
	buffer = ' '.join(buffer)

for word in scrable: #AB
	temp_scrable = scrable.copy()
	temp_scrable.remove(word)
	for word2 in temp_scrable: #CD
		B = word[1]
		C = word2[0]
		if "{0}{1}".format(B,C) in scrable_str:
			temp_scrable2 = temp_scrable.copy()
			temp_scrable2.remove(word2)
			for word3 in temp_scrable2:# DE
				D = word2[1]
				reg = r"{0}[a-zA-Z]".format(D)
				match = re.findall(reg, ' '.join(temp_scrable2))
				temp_scrable3 = temp_scrable2.copy()
				temp_scrable3.remove(word3)
				for word4 in match: # EF
					E = word4[1]
					reg2 = r"{0}[a-zA-Z]".format(E)
					match2 = re.findall(reg2, ' '.join(temp_scrable3))
					for word5 in match2:
						F = word5[1]
						DC = word2 [::-1] #reverses
						reg3 = r"{0}{1}{2}[a-zA-Z]{3}".format(word, F, E,  DC)
						result = re.findall(reg3, buffer)
						if result != []:
							print(result)
# Output will require manual validation for FG