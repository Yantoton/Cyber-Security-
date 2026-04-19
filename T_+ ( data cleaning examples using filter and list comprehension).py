data = [0,7,False,"hello",True,"","Darkness"]
clear_data = list(filter(lambda item: item !=False, data))
print(clear_data)

data_lst_comp = [item for item in data if item != False]
print(data_lst_comp)

clean_data = list(filter(None, data))
print(clean_data)
