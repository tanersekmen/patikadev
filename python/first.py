firstList = [[1, 2], [3, 4], [5, 6, 7]]

def reverseTutorial(input_values):
    output_list = []
    for i in input_values:
        if isinstance(i, list):
            output_list.append(reverseTutorial(i))
        else:
            output_list.append(i)
    output_list.reverse()
    return output_list




if __name__=='__main__':
    print(reverseTutorial(firstList))