'''
Ex 7:
Implement a search to find the index of a target value in a sorted list.
Return -1 if not found.
Example: input search_list=[1, 3, 5, 7, 9, 11], value=7 should return 3
'''

def find_index(l:list, target:int) -> int:
    return [int(e) for e in l.replace(" ", "")].index(int(target))

print(find_index(input("search_list: "), input("value: ")))