"""Push Front
This algorithm might be familiar. Write a function that takes in a list and a value, and adds the value to the front of that list, outputting the changed list. This should be done in place> This means you should not create a new list, but change the existing one. Try using your newly discovered Python swap! Here's what your function should look like:

  def push_front(arr, val):
    ...
    return arr"""

def push_front(arr, val):
    
    
    new_list = []
    new_list.append(val)
    for i in arr:
        new_list.append(i)
    
    print new_list       


push_front([1,2,3,4], 0)




