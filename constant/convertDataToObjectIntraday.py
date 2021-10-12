from datetime import datetime

def convertDataToObjectIntraday(data,symbol):
    


    res=list(dict.values(data))
    response = []
    for i in range(len(res)):
        if isinstance(res[i], list):
            response.append(res[i])
            
    data=[]
    count=0
    while(count<len(response[0])):
        item={}
        for i in range(len(response)):
            item["symbol"]=symbol
            if i == 0:
                item['servertime']=(response[i][count])
                dt_object = datetime.strftime(datetime.fromtimestamp(response[i][count]), '%Y-%m-%d %H:%M:%S')
                item['datetime']=dt_object
            if i == 1:
                item['price']=(response[i][count])
            '''if i == 2:
                item['open']=(response[i][count])
            if i == 3:
                item['high']=(response[i][count])
            if i == 4:
                item['low']=(response[i][count])'''
            if i == 5:
                item['vol']=(response[i][count])
        data.append(item)
        count=count+1
    return(data)
        
