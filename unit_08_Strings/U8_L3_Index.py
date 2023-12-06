# Dec 4, 2023
# Author: ogracias


# imports





# functions
def removeLastItemInList(L):
    '''
    Remove last item in list
    (list) --> (list)
    [1, 2] --> [1]
    '''
    del L[-1]
    return L
def removeFirstItemInList(L):
    L.pop(0)
    return L


if __name__ == '__main__':
    print('\n\n********** Add a list **********')
    weekdays = ['Mon', 'Tue', 'Wed', 'Thu']
    print(weekdays)
    big_birds = ['Emu', 'Ostrich', 'Cassowary']
    first_names = ['Sebastian', 'Danielle', 'Anne']
    combined = [weekdays, big_birds, first_names]
    print('Combined:', combined)
    
    print("first element in combined", combined[0])
    print("extract Wed in combined", combined[0][2])
    
    print('\n\n********** offsets **********')
    marxes = ['Groucho', 'Chico', 'Harpo', 'Hunter', 'Marios']
    print(marxes[-1])
    print(marxes[0:4])
    print(marxes[1:4])
    print(marxes[0:5:2])
    print(marxes[::])
    print(marxes[::-1])
    
    print('\n\n********** changes in list **********')
    print(marxes)
    marxes[2] = 'Max'
    print(marxes)
    

    print('\n\n********** append **********')
    marxes.append('Raphael')
    print(marxes)
    extendedValues = ['extended1', 'extended2']
    marxes.extend(extendedValues)
    print(marxes)
    
    
    print('\n\n********** += **********')
    others = ['Gummo', 'Karl']
    marxes += others
    print(marxes)
    
    marxes.insert(0, 'first')
    print(marxes)
    
    marxes.remove('Karl')
    print(marxes)
    
    del marxes[9]
    print(marxes)
    
    marxes.pop() #default = last index
    print(marxes)
    
    marxes.pop(0)
    print(marxes)
    
    
    print('\n\n********** find the index **********')
    print(marxes.index('Raphael'))
    is_Raphael_here = 'Raphael' in marxes
    print(is_Raphael_here)
    
    print('\n\n********** join() **********')
    print(', '.join(marxes))
    
    friends = ['Harry', 'Herminone', 'Ron']
    print(friends)
    separator =  ' & '
    
    join = separator.join(friends)
    print(join)
    
    
    
    print('\n\n********** sort() **********')
    print(marxes)
    sorted_marxes = sorted(marxes)
    print(sorted_marxes)
    
    marxes[0] = 'New'
    print(marxes)
    marxes.sort(reverse=True)
    print(marxes)
    
    
    print('\n\n********** length of list **********')
    myNums = [4, 6, 3, 8, 4.5]
    print(len(myNums))
    
    
    print('\n\n********** use of lists in functions **********')
    print(removeLastItemInList(myNums))
    
    
    #remove first item in number list myNums
    print(removeFirstItemInList(myNums))
    
    print('\n\n********** copying lists **********')
    a = [1, 2, 3]
    print(a)
    
    b = a[:]
    print(b)
    
    #make a change in a
    a[0] = 1000
    print(a)
    print(b)
    
    
    # another note
    c = list()
    c.append(123)
    print(c)
    
    d = list()
    d += [12, 24, 36]
    e = []
    e.extend(d)
    print(d)
    print(e)
    
    print('\n\n********** max and min **********')
    myNums = [4, 8, 1, -3, 2,5, -34]
    print(min(myNums))
    print(max(myNums))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





