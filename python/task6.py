"""
The issue was that .remove() was modifying names while iterating through it.
This caused the indexs to shift and for elements to be skipped over
Each of these shifts also runs in o(n) time complexity leading to an overall quadratic time complexity for the function

To fix this, we conditionally append items that match the criteria to a new list and return this list
With a bit of added space complexity, we can iterate through the list in a linear pass while ensuring that we process every element
"""

def remove_short(names, min_len):
    new_names = []
    for n in names:              
        if len(n) < min_len:
            continue
        new_names.append(n)    
    return new_names


if __name__ == "__main__":
    data = ["A", "B", "Cat", "Do"]
    print(remove_short(data, 2))
