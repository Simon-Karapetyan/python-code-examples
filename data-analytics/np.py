import numpy as np

# # One dimensional array
# first_list = [1, 2, 3, 4]
# one_dim_array = np.array(first_list)
# print(type(one_dim_array))


# # Two dimensional array
# second_list = [5, 6, 7, 8]
# two_dim_array = np.array([first_list, second_list])
# print(two_dim_array)


# # Shape of the array
# print(two_dim_array.shape)


# # Size of the array
# print(two_dim_array.size)


# # Type of the array
# print(two_dim_array.dtype)


# my_data = np.random.uniform(-1, 1, 25)
# for index, number in enumerate(my_data):
#     if number < 0:
#         my_data[index] = 0
# print(my_data)


# my_data = np.random.uniform(-1, 1, 25)
# my_data = np.where(my_data < 0, 0, my_data)
# print(my_data)


# def func(*arg, **kwargs):
#     print(arg)
#     print(kwargs)
# func(10, 20, a=1, b=2)


