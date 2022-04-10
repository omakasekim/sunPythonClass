def GNA(SSN):
    if len(SSN)!= 14:
        return "Retry"
    if SSN[6]!='-':
        return "Retry"
    if(int(SSN[0:2]) > 23):
        res = 100-int(SSN[0:2])
        age = 22+res
    else:
        age = 22-int(SSN[0:2])
    if(SSN[7]=='3'):
        gender = 'Male'
    elif(SSN[7] == '4')
        gender = 'Female'
    else:
        gender = 'Unknown'

    sentence = str(age) + ' year old ' + gender
    return sentence

#>>> GNA("000418-4068711")
#>>> 22 year old Female


        
    
