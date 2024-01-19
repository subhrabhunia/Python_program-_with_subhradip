from itertools import chain, combinations

def get_all_subsets(lst):
    return list(chain.from_iterable(combinations(lst, r) for r in range(len(lst)+1)))
    #example 
my_list = [1,2,3,4,5,6,7,8,9]
all_subsets = get_all_subsets(my_list)

for subset in all_subsets:
    print(list(subset))
