# #11 Iterate over two lists at the same time using zip().
# def itrate_list():
#     list1=['a', 'b', 'c', 'd', 'e']
#     list2=[1,2,3,4,5,6,7,8,9,]
#     for list1, list2 in zip(list1, list2):
#         print(f"{list2}:{list1}")
# itrate_list()


# # 12 Use enumerate() to print index + value of a list.
# def eum_lsit():
#     list=[1,2,3,4,5,6,7,8,9,]
#     for index, value in enumerate(list):
#         print(f"{index}, {value}")
# eum_lsit()


# 13 Flatten a nested list using a nested loop.
def flat_list():
    nested_list= [[1, 2], [3, 4, 5], [6]]
    flat_list = []
    for sublist in nested_list:
        for item in sublist:
            flat_list.append(item)
    print(flat_list)
    return flat_list
flat_list()