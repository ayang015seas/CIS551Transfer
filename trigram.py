import sys

cipher = """HIZALRGTIGPNUJPRHAEDHYASGEERELSGEKRTRRJLXHTRTPNKDDCPJTZQASZXTZFLPOCDVFZRCBITUPEZXTPDXIFXCRKLWPTCFPPEGTCFQOVOIEGRHIFXTJWCERTDVITGWIAEGTXGUIJFLPRTFZFTXOGERWYMUWTDDCIDGOGRCXWDNJQZAWCTYHOEMHOWWSITGEVPLVYTTNKPRCJRTRFRHGYNDDEHDPZQOYGIRZDWTCLEIWSIFTWRVLGQDUEWLFWAIKBESHWEJWZGYWOCGPVHWETDCRSVIVVELSBECOZRGIHVPPRHWAKEFMZITYLDKFTAKLYHIHTILLPSBPZUPQOSEJXCICUIKEPGOJSVLEAOHTYHTVADNVBLXGIABHESRPYDDYEUTMVQELOHNFVEEYTIEWSIQDMGDYCOALKRRIHWEIWSIGTMVQDMHIIEJFTVTRVSZMBIIEJESHTLUDCQOCAXHXIBIONQWIGHTYDYTSGCVQESTIHVFZQDPNPDYHKWEIHOSSHMIFCSALECOAYHWIJPTPZXOEGZPZPRJDWEFNNFWTRHTLUDCWHDCBKPSKCSCHDWHWAESPVQTNKBZYCLNKKPGCBPRQJXVPTJUTKVIYFXELSHTFFVLCADVULRRNOLDCIOALSHTRUGOPDWPMHCIHHIRDVVUMCHWEJHELSHESXCIOJCIDEWKXTYWSIWGSKHLOZJNTKPWHWEZUSYBIIEJLRRUIJKTRUIRZSDXVTIIFZVDDRRWPNSISRQOKCADVQAEFPCYXEIGIHZVTWOCOLWCEUTYFXCICJTFIWMBTGVNVSHTLUDCTOEEIPCGFDMNHWPHTLUDCTOEEIKLWRXFWHCIBIVZFPTFTSZGPRHHERFSIOGNZQRSJTRKKZYGPNUGZPZPRJDJIOGNFZTLOKEJSPRHIHVOLWHIWFPZRHWSRQLPMOIEJHLOIACOELSHEXXJWRDAEGTWHXLCFLRHUIXXCIWIOLWZRSIHZQRMRDKERHMGIHRWZYFEAGHCGCBPRQJPCHTDLWPWDNURWPOGSCDDXMTAIDYHWALSHEXVPTYDWJCUTYDEAOHSGHYXWCACOELSEAGHCACGKXRTRUQATNLRRUOIWSFSIWVHYEZATYHDIJXCVSCIGXDVQEWUTKBRELSCENOLACUEMRWYHXOELYGCGPFULXSPMVUTGOHEVPDXCQEJXCZWKACRQXVTUEITXHTSKZPPZXNDBMSCZYFXPMHWEIGZMHGIXKESFNOLJPXSAIDLYEHTDZQ"""

trigramDict = {}
offSetDict = {}
offSetMap = {}


for i in range(0, len(cipher) - 2):
	curr = cipher[i:i+2]
	if (curr in trigramDict.keys()):
		trigramDict[curr].append(i)
	else:
		trigramDict[curr] = []
		trigramDict[curr].append(i)

# for key in trigramDict.keys():
# 	print(key)
# 	print(trigramDict[key])

for key in trigramDict.keys():
	arr = trigramDict[key]
	offset = []
	if (len(arr) > 1):
		for i in range (0, (len(arr) - 1)):
			offset.append(arr[i + 1] - arr[i])
		offSetDict[key] = offset

# for key in offSetDict.keys():
#  	print(key)
#  	print(offSetDict[key])

for key in offSetDict.keys():
	arr = offSetDict[key]
	for element in arr:	
		if element in offSetMap.keys():
			offSetMap[element] += 1
		else:
			offSetMap[element] = 1

sort_orders = sorted(offSetMap.items(), key=lambda x: x[1], reverse=True)

# print(sort_orders)

# print(len(cipher))
en_freq = {
0: 0.08167,
1: 0.01492,
2: 0.02782,
3: 0.04253,
4: 0.12702,
5: 0.02228,
6: 0.02015,
7: 0.06094,
8: 0.06996,
9: 0.00153,
10: 0.00772,
11: 0.04025,
12: 0.02406,
13: 0.06749,
14: 0.07507,
15: 0.01929,
16: 0.00095,
17: 0.05987,
18: 0.06327,
19: 0.09056,
20: 0.02758,
21: 0.00978,
22: 0.02360,
23: 0.00150,
24: 0.01974,
25: 0.00074
 }

# print "Number of arguments:", len(sys.argv), "arguments."
# print ("Argument List:", str(sys.argv))

if (len(sys.argv) is not 2):
	print("NEED 1 ARGUMENTS (FILENAME)")
	exit()

args = str(sys.argv)
filename = sys.argv[1]

file = open(filename)
all_of_it = file.read()


# print(all_of_it)


def shift(symbol, offset):
	return (symbol + offset) % 26

def unshift(symbol, offset):
	return (symbol + 26 - (offset % 26)) % 26;

def cipherToArr(cipher):
	cipherArr = []
	for i in range(0, len(cipher)):
		# print(cipher[i])
		cipherArr.append(ord(cipher[i]) - 65)
	return cipherArr

def arrToCipher(arr):
	s = ""
	for i in range(0, len(arr)):
		s += chr(arr[i] + 65)
	return s
	

def compareFrequencies(frequencies):
	total = 0
	for key in frequencies.keys():
		# print(en_freq[key])
		# print(frequencies[key])
		total = total + abs(frequencies[key] - en_freq[key])
	return total

def getVariance(frequencies):
	total = 0
	for key in frequencies.keys():
		# print(en_freq[key])
		# print(frequencies[key])
		total = total + (abs(frequencies[key] - en_freq[key]) * abs(frequencies[key] - en_freq[key]))
	return total

def getFrequencies(cipher):
	cipherRes = {}
	length = len(cipher)
	for i in range(0, length):
		if cipher[i] in cipherRes.keys():
			cipherRes[cipher[i]] += 1
		else:
			cipherRes[cipher[i]] = 1
	for key in cipherRes.keys():
		cipherRes[key] = cipherRes[key] / length
	return cipherRes

def analyzeFreq(cipher):
	minimum = sys.float_info.max
	cArr = cipherToArr(cipher)
	offset = -1
	for i in range(0, 26):
		tempArr = [-1] * len(cArr)
		for j in range(0, len(cArr)):
			tempArr[j] = unshift(cArr[j], i)
		freqDict = getFrequencies(tempArr)
		# print(freqDict)
		currFreq = compareFrequencies(freqDict)
		if (currFreq < minimum):
			# print(currFreq)
			minimum = currFreq
			offset = i
	return minimum, offset

def analyzeString(cipher, keylength):
	# append everything to lists
	cipherGroups = []
	totalScore = 0.0
	keylist = []
	key = ""

	for i in range(0, keylength):
		cipherGroups.append("")

	for i in range(0, len(cipher)):
		cipherGroups[i % keylength] += cipher[i]

	# print(cipherGroups)

	for i in range(0, len(cipherGroups)):
		# print(cipherGroups[i])
		minimum, key = analyzeFreq(cipherGroups[i])
		totalScore += minimum
		keylist.append(key)
	totalScore = totalScore / keylength
	key = arrToCipher(keylist)
	# print(key)
	# print(totalScore)
	return totalScore, key

def decrypt(cipher, key):
	cipherarr = cipherToArr(cipher)
	keyarr = cipherToArr(key)
	newarr = []
	for i in range(0, len(cipherarr)):
		newarr.append(unshift(cipherarr[i], keyarr[i % len(keyarr)]))
	return arrToCipher(newarr)

def analyzeAllKeys(cipher):
	minimum = sys.float_info.max
	key = ""
	print("PARSING...")
	for i in range(1, int(len(cipher) / 2)):
		infostring = "Currently Parsing " + str(i)
		# print(infostring)
		score, newkey = analyzeString(cipher, i)
		# print(score)
		if (score < minimum):
			key = newkey
			# print(key)
			# print(decrypt(cipher, key))
			minimum = score
	# print(cipher)
	print("KEY " + key)
	print(decrypt(cipher, key))



cipher2 = """ZNKEKRRUCLUMZNGZXAHYOZYHGIQAVUTZNKCOTJUCVGTKYZNKEKRRUCYSUQKZNGZXAHYOZYSAFFRKUTZNKCOTJUCVGTKYROIQKJOZYZUTMAKOTZUZNKIUXTKXYULZNKKBKTOTMROTMKXKJAVUTZNKVUURYZNGZYZGTJOTJXGOTYRKZLGRRAVUTOZYHGIQZNKYUUZZNGZLGRRYLXUSINOSTKEYYROVVKJHEZNKZKXXGIKSGJKGYAJJKTRKGVGTJYKKOTMZNGZOZCGYGYULZUIZUHKXTOMNZIAXRKJUTIKGHUAZZNKNUAYKGTJLKRRGYRKKV"""

# minimum, offset = analyzeFreq(cipher2)
# print(minimum)
# print(offset)
# print(decrypt(cipher2, "G"))
# print(analyzeAllKeys(cipher2))
analyzeAllKeys(cipher)
# assume that the answer is 21 in terms of length 


# freqDict = getFrequencies(tempArr)
# print(freqDict)
# currFreq = getVariance(freqDict)
