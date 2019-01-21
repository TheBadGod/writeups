import math

#0000000000003196
def addPrimePadding(string, stringLen, outputSize):
    ptr = [0]*stringLen
    calculatePrimes(stringLen, ptr)
    primeLen = 0
    while(primeLen < stringLen and ptr[primeLen] != 0):
        primeLen += 1
    wantedAddition = outputSize - len(string)
    primeIndex = 0
    for j in range(stringLen, wantedAddition+stringLen):
        primeValue = ptr[primeIndex%primeLen]
        primeIndex += 1
        assert outputSize > primeValue
        string += string[primeValue]
    return string
    
#000000000000309D
def calculatePrimes(len, ptr):
    amount = 0
    for i in range(2,len+1):
        v7 = 1
        for j in range(2,int(math.floor(math.sqrt(i)))+1):
            if i%j == 0:
                v7 = 0
                break
        if v7 == 1 and len > i and amount < len:
            ptr[amount] = i # DWORD
            amount += 1
         
#000000000000303E         
def calculateUnionHash(str1, str2):
    value = 0
    for i in range(0x40):
        value += ((ord(str1[i])+ord(str2[i])) ^ 0x3627)
    return value
    

mapping = [0x75, 0x0CE, 0x148, 0x163, 0x19F, 0x1A3, 0x41A, 0x4B2, 0x4F6, 0x512, 0x554, 0x5CA, 0x605, 0x61D, 0x6E1, 0x86A, 0x8ED, 0x996, 0x0A67, 0x0A84, 0x0AFD, 0x0CD2, 0x0E24, 0x0F36, 0x111C, 0x11DF, 0x123F, 0x1254, 0x126F, 0x1281, 0x1299, 0x1363, 0x143E, 0x153A, 0x159A, 0x15A5, 0x1616, 0x16AB, 0x16EA, 0x17B0, 0x17CE, 0x1843, 0x1911, 0x1964, 0x19A7, 0x1A43, 0x1A48, 0x1A89, 0x1B0B, 0x1B72, 0x1BD2, 0x1C5F, 0x1CC4, 0x1DE0, 0x1FF0, 0x204D, 0x2090, 0x20AC, 0x21D6, 0x222D, 0x22AB, 0x23E6, 0x2415, 0x24EB, 0x24EF, 0x252B, 0x2777, 0x27E0, 0x2833, 0x28CD, 0x2980, 0x2A4F, 0x2A88, 0x2A8C, 0x2AB0, 0x2ACB, 0x2ADE, 0x2B24, 0x2B41, 0x2B76, 0x2B85, 0x2C0F, 0x2C29, 0x2CE0, 0x2D0F, 0x2D9F, 0x2DBD, 0x2E21, 0x750, 0x2FB1, 0x3068, 0x3238, 0x3303, 0x3307, 0x332C, 0x334D, 0x336A, 0x33AA, 0x33DC, 0x3407, 0x34B7, 0x351A, 0x3556, 0x3577, 0x3627, 0x363B, 0x3696, 0x36EF, 0x383F, 0x387D, 0x38E1, 0x3958, 0x3981, 0x3ABE, 0x3ACB, 0x3B44, 0x3BC5, 0x3CAC, 0x3D32, 0x3E36, 0x3EE7, 0x3EF8, 0x3FEF, 0x4003, 0x404B, 0x406B, 0x4128, 0x41B5, 0x4217, 0x42BB, 0x4304, 0x4335, 0x43E9, 0x4544, 0x45CB, 0x46A7, 0x46FE, 0x4705, 0x4718, 0x4765, 0x479B, 0x4831, 0x48B7, 0x48E8, 0x49EB, 0x4A4A, 0x4A55, 0x4B0C, 0x4B13, 0x4BA2, 0x4EAD, 0x5052, 0x5065, 0x527D, 0x52AE, 0x53C8, 0x5632, 0x5645, 0x56A1, 0x577D, 0x5821, 0x5896, 0x59A8, 0x5A8A, 0x5A94, 0x5AD9, 0x5B11, 0x5B2E, 0x5C2D, 0x5DF7, 0x5E38, 0x5E3A, 0x5E48, 0x5E5A, 0x5FC3, 0x5FE1, 0x61DA, 0x61FB, 0x630C, 0x6312, 0x63EF, 0x6477, 0x6528, 0x6583, 0x65A3, 0x65D3, 0x6689, 0x668F, 0x66B0, 0x671B, 0x679C, 0x6987, 0x69F1, 0x6A32, 0x6A86, 0x6AEC, 0x6AFE, 0x6B4D, 0x6B86, 0x6BA1, 0x6C44, 0x6CC2, 0x6CCF, 0x6CE9, 0x6D9E, 0x6E0F, 0x6EA5, 0x6FC1, 0x71AE, 0x7220, 0x726B, 0x72AE, 0x7357, 0x737B, 0x73EA, 0x7405, 0x7428, 0x7442, 0x74FC, 0x751A, 0x756A, 0x7597, 0x7684, 0x774F, 0x7789, 0x77D2, 0x7820, 0x7827, 0x7849, 0x786D, 0x78D2, 0x7961, 0x79A4, 0x79FB, 0x7A4E, 0x7AD6, 0x7BE8, 0x7C25, 0x7C9E, 0x7CA1, 0x7D5C, 0x7D6A, 0x7D89, 0x7D9D, 0x7E64, 0x7EC9, 0x7EFC, 0x7EFF, 0x7F58, 0x7FF1, 0x803E, 0x8048, 0x8125, 0x8189, 0x8282, 0x82E8, 0x8358, 0x8535, 0x85CB, 0x867A, 0x8682, 0x87B7, 0x8845, 0x8899, 0x88BB, 0x89E6, 0x8AB1, 0x8AD8, 0x8C93, 0x8CFA, 0x8D0D, 0x8D1D, 0x8D26, 0x8D52, 0x8D6E, 0x8E3C, 0x8E3F, 0x8E83, 0x8F07, 0x8F39, 0x8FB3, 0x8FCF, 0x91A3, 0x91D7, 0x9473, 0x94FB, 0x958D, 0x95D4, 0x9664, 0x974C, 0x98A3, 0x990B, 0x991C, 0x9964, 0x996A, 0x9B0B, 0x9CA2, 0x9CD1, 0x9DF7, 0x9E13, 0x9E47, 0x9E55, 0x9E56, 0x9F2B, 0x9F33, 0x9F46, 0x0A044, 0x0A103, 0x0A153, 0x0A180, 0x0A1A3, 0x0A1CB, 0x0A217, 0x0A223, 0x0A257, 0x0A283, 0x0A28E, 0x0A342, 0x0A36B, 0x0A457, 0x0A4F3, 0x0A50F, 0x0A5EA, 0x0A71E, 0x0A887, 0x0A98B, 0x0AAA3, 0x0AB25, 0x0AB92, 0x0AD45, 0x0AD54, 0x0ADD3, 0x0ADF1, 0x0AE08, 0x0AE40, 0x0AEC8, 0x0AEF4, 0x0AF27, 0x0AF9A, 0x0AFC6, 0x0AFDA, 0x0B026, 0x0B02B, 0x0B02D, 0x0B126, 0x0B169, 0x0B1F2, 0x0B21F, 0x0B238, 0x0B333, 0x0B38D, 0x0B3B2, 0x0B44D, 0x0B451, 0x0B457, 0x0B46F, 0x0B52B, 0x0B557, 0x0B575, 0x0B5BB, 0x0B5DE, 0x0B65B, 0x0B665, 0x0B680, 0x0B794, 0x0B7A3, 0x0B7BE, 0x0B7CA, 0x0B800, 0x0B813, 0x0B87B, 0x0B896, 0x0B8DC, 0x0BA53, 0x0BAA9, 0x0BB17, 0x0BBBD, 0x0BC14, 0x0BC87, 0x0BDA3, 0x0BE2E, 0x0BE48, 0x0BEF8, 0x0BEFB, 0x0BF23, 0x0BF4B, 0x0BFAC, 0x0BFDA, 0x0BFE4, 0x0C00C, 0x0C024, 0x0C290, 0x0C3A3, 0x0C456, 0x0C571, 0x0C59E, 0x0C684, 0x0C713, 0x0C844, 0x0C899, 0x0C8A6, 0x0C8A9, 0x0C8D8, 0x0C928, 0x0CA6F, 0x0CB6A, 0x0CC6A, 0x0CC91, 0x0CDFC, 0x0CE2D, 0x0CE82, 0x0CE91, 0x0CF50, 0x0D123, 0x0D134, 0x0D198, 0x0D1BC, 0x0D21C, 0x0D243, 0x0D33C, 0x0D3F5, 0x0D466, 0x0D47F, 0x0D4BA, 0x0D55F, 0x0D58D, 0x0D59B, 0x0D59D, 0x0D5E1, 0x0D669, 0x0D77C, 0x0D7DF, 0x0D7E4, 0x0D7F8, 0x0D837, 0x0D882, 0x0D8A0, 0x0D8FB, 0x0D91F, 0x0DB4B, 0x0DBB8, 0x0DC55, 0x0DC70, 0x0DCD7, 0x0DCEA, 0x0DD16, 0x0DD1B, 0x0DD86, 0x0DE86, 0x0DFAC, 0x0DFF4, 0x0E087, 0x0E1BC, 0x0E1CB, 0x0E1CF, 0x0E1EB, 0x0E28D, 0x0E2E8, 0x0E3AF, 0x0E3E3, 0x0E3F2, 0x0E440, 0x0E491, 0x0E4C1, 0x0E53A, 0x0E5D2, 0x0E636, 0x0E655, 0x0E665, 0x0E81C, 0x0E870, 0x0E878, 0x0E88B, 0x0E94C, 0x0EA5C, 0x0EAE1, 0x0EE53, 0x0EF68, 0x0EFE5, 0x0F022, 0x0F068, 0x0F0FC, 0x0F117, 0x0F226, 0x0F2A9, 0x0F2EF, 0x0F332, 0x0F3C5, 0x0F3DE, 0x0F3E0, 0x0F3EA, 0x0F439, 0x0F44B, 0x0F4A4, 0x0F53E, 0x0F5C9, 0x0F641, 0x0F667, 0x0F73E, 0x0F799, 0x0F804, 0x0FA80, 0x0FA8D, 0x0FA9D, 0x0FAB6, 0x0FAD1, 0x0FB1F, 0x0FB28, 0x0FB3C, 0x0FC34, 0x0FCF3, 0x0FDD4, 0x0FEF4, 0x0FF36, 0x0FFB6, 0x0FFE4, 0x10108, 0x101A6, 0x101CF, 0x1032B, 0x1037B, 0x10420, 0x104DF, 0x1060A, 0x1065D, 0x10701, 0x10765, 0x10870, 0x10900, 0x1090D, 0x1092D, 0x109C8, 0x10A6B, 0x10AA8, 0x10CD3, 0x10E1C, 0x10E1F, 0x10E65, 0x10F08, 0x10FB3, 0x10FEF, 0x11003, 0x11005, 0x1104D, 0x11116, 0x1113F, 0x11195, 0x11241, 0x113E7, 0x1154A, 0x11580, 0x1160A, 0x1168A, 0x117B7, 0x117F6, 0x11891, 0x1198A, 0x1198E, 0x119AC, 0x119FA, 0x11C87, 0x11CB0, 0x11CB2, 0x11CE5, 0x11EEB, 0x12043, 0x120EE, 0x12185, 0x12281, 0x12328, 0x1232E, 0x123FA, 0x12428, 0x124C9, 0x124E6, 0x12518, 0x1267E, 0x1268A, 0x1268E, 0x12728, 0x127CD, 0x127F6, 0x12819, 0x128AE, 0x128F9, 0x12913, 0x12920, 0x12939, 0x12942, 0x129F3, 0x12A24, 0x12A61, 0x12A97, 0x12ABF, 0x12ACC, 0x12AD3, 0x12D02, 0x12D4E, 0x12DF4, 0x12E8C, 0x12F5F, 0x12FAC, 0x13003, 0x13068, 0x13094, 0x1319E, 0x131DB, 0x13224, 0x132ED, 0x132EE, 0x132FF, 0x13312, 0x13338, 0x133F1, 0x1347A, 0x13488, 0x1354E, 0x135C1, 0x13639, 0x136BA, 0x13815, 0x138C0, 0x13922, 0x139DB, 0x13A8A, 0x13AD6, 0x13B0E, 0x13B27, 0x13B6A, 0x13C82, 0x13DA2, 0x13DA8, 0x13DB1, 0x13DF7, 0x13DFA, 0x13EE3, 0x13F00, 0x13F1C, 0x13F7C, 0x14042, 0x14098, 0x142D3, 0x142F7, 0x14422, 0x14435, 0x1446A, 0x14496, 0x145C2, 0x1464E, 0x147FD, 0x14819, 0x148C2, 0x148DC, 0x1497A, 0x14C27, 0x0]
            
           
#0000000000003857
def calculate(givenName, givenPassword):
    processedName = addPrimePadding(givenName, len(givenName), 0x40)
    
    assert processedName == "73FF9B24EF8DE48C346D93FADCEE01151B0A1644BC81FFB4D44DA156C1FFB4D4" # from debugging binary

    processedPassword = addPrimePadding(givenPassword, len(givenPassword), 0x40)

    if testAssertions:
        processedPassword = processedName

    preValue = ord(processedPassword[0]) - 0x30
    mapValue = preValue + mapping[ord(processedPassword[0x2A])] + 0x27A

    if testAssertions:
        assert mapValue == 0x2311 # from debugging binary for pw == name
        
        
    assert 892360 == calculateUnionHash(processedName, processedName) # as name is constant this should be constant as well

    unionHash = mapValue + 892360 #calculateUnionHash(processedName, processedName)
    

    if testAssertions:
        assert unionHash == 0xdc0d9 # from debugging binary pw == name
        
    loopVar1 = mapping[0x9B - ord(processedPassword[0])] + unionHash

    if testAssertions:
        assert loopVar1 == 0xdf590 # from debugging binary pw == name

    key = [ord(c) for c in ("%lu" % loopVar1)[0:0x13]]
    key += ([0] * (0x10-len(key)))

    AtoSArray = range(0x41,0x54)

    currentLength = 0
    firstMapping = loopVar1

    # calculate how many characters the %lu already takes
    while loopVar1 != 0 and currentLength <= 15:
        loopVar1 = loopVar1 // 10
        currentLength += 1
        
    loopVar2 = firstMapping
    while loopVar2 != 0 and currentLength <= 15:
        index = loopVar2%10
        loopVar2 = loopVar2//10
        key[currentLength] = AtoSArray[index]
        currentLength += 1

    while currentLength <= 15:
        key[currentLength] = 0x61
        currentLength += 1

    keyHexString = ''.join(["%02x" % i for i in key])


    if testAssertions:
        assert keyHexString == "39313438333243444945424a61616161" # from debugging binary pw == name
     
     
    return keyHexString[5:9] == "7303"

    # md5(keyHexString[5:9]) == md5("7303")
    # if matches try to  EVP_AES_128_CBC Decrypt fixed data @ 00000000000033F2 with the "key" as key and fixed IV

    # IV = "1234123412341234"
    # size = 0x40

    # "b0234db3e7823748303290fb70cd9eb220574e1e031f9741c332af2147396bc59e6a48b8dbce4606362102c977a185a69ebdf5f2bc967552f09f1ba49bb15753"
    # encrypted data = [0xb0, 0x23, 0x4d, 0xb3, 0xe7, 0x82, 0x37, 0x48, 0x30, 0x32, 0x90, 0xfb, 0x70, 0xcd, 0x9e, 0xb2, 0x20, 0x57, 0x4e, 0x1e, 0x03, 0x1f, 0x97, 0x41, 0xc3, 0x32, 0xaf, 0x21, 0x47, 0x39, 0x6b, 0xc5, 0x9e, 0x6a, 0x48, 0xb8, 0xdb, 0xce, 0x46, 0x06]

    # b    *(0x0000000000035C4)
    # jump *(0x0000000000033F2)
    

# turn this on to verify that the implementation works as intended
testAssertions = False
givenName             = "73FF9B24EF8DE48C346D93FADCEE01151B0A1644BC81"
possiblePassword = list("00000000000000000000000000000000000000000000")

import string

# bruteforce all possible combinations and print out the ones with matching key part
for a in string.printable:
    for b in string.printable:
        possiblePassword[0] = a
        possiblePassword[0x2A] = b
        givenPassword = ''.join(possiblePassword)
        if(calculate(givenName, givenPassword)):
            print(givenPassword)
            break
print "Done"