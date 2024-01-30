#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        # max_value = " "
        # return (max_value.join(key for key, value in a_dictionary.items()
        # if value == max(a_dictionary.values())))
        return max(a_dictionary, key=a_dictionary.get)
    return None


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 16, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
