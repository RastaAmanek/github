
import numpy as np

first_vector = np.array([1, 4, 0, 10, 13, 9, 10])
second_vector = np.array([8, 4, 9, -1, 1, 19, 99])
print()

# suma
sum_of_vectors = first_vector + second_vector
print("suma:", sum_of_vectors)

# roznica
diff_of_vectors = first_vector - second_vector
print("roznica: ", diff_of_vectors)

# iloraz
divi_of_vectors = first_vector / second_vector
print("iloraz: ", divi_of_vectors)

# trzyktotnosci kwadratu pierwszego wektora
three_square = (first_vector**2)*3
print("kwadrat: ", three_square)
