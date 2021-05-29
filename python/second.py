data = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flat_list = []

def flatten_list(data):
    for element in data:
        if type(element) == list:
            flatten_list(element)
        else:
            flat_list.append(element)

flatten_list(data)
print(flat_list)