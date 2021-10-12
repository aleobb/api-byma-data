def convertDataMin (msg):
    dataMin = [msg[0]]
    for i in range(len(msg)):
        timeValidateMin=(msg[i]['datetime'].split(" ")[1].split(":")[1])
        timeValidateMinAux=(dataMin[len(dataMin)-1]['datetime'].split(" ")[1].split(":")[1])
        timeValidateHour=(msg[i]['datetime'].split(" ")[1].split(":")[0])
        timeValidateHourAux=(dataMin[len(dataMin)-1]['datetime'].split(" ")[1].split(":")[0])
        if(timeValidateMin>timeValidateMinAux or timeValidateHour != timeValidateHourAux ):
            dataMin.append(msg[i])

    return (dataMin)