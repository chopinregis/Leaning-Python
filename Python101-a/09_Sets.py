### Concept: Sets
### A set is an unordered collection with no duplicate elements. Sets are useful for membership testing and eliminating duplicate entries.

# Create a set
fruit_set = {"apple", "banana", "cherry"}
print(fruit_set)  # Note that the order might be different when you print a set.


### Exercise 4: Sets
### Create a set called unique_colors from the colors list. Then, try adding a new color "yellow" to unique_colors using the .add() method and print the set.

colors = ["red", "green", "blue"]
print(colors)

unique_colors = {"red", "green", "blue"}    # or set(colors)
unique_colors.add("yellow")                 # or unique_colors.add("yellow") using the .add() method
unique_colors.update(["brown","white", "black"])    # use update() Method to Add Multiple Colors
print(unique_colors)

color_to_add = ["brown", "white2", "black2"]
for color in color_to_add:
	unique_colors.add(color)
print(unique_colors)



"""
Sets in Python offer several methods beyond `.add()` for working with collections of unique elements. Here are some commonly used methods:

**1. `.update(iterable)`:**

- Adds elements from an iterable (like a list, tuple, or another set) to the set. Duplicates are automatically excluded.
- Example:

```python
my_set = {"a", "b", "c"}
my_list = ["d", "a", "e"]
my_set.update(my_list)  # my_set becomes {"a", "b", "c", "d", "e"}
```

**2. `.remove(element)`:**

- Removes a specific element from the set. Raises a `KeyError` if the element is not found.
- Example:

```python
my_set = {"a", "b", "c"}
my_set.remove("b")  # my_set becomes {"a", "c"}
```

**3. `.discard(element)`:**

- Similar to `.remove()`, but it doesn't raise an error if the element is not found.
- Example:

```python
my_set = {"a", "b", "c"}
my_set.discard("d")  # No error, my_set remains {"a", "b", "c"}
```

**4. `.pop()`:**

- Removes and returns an arbitrary element from the set. Since sets are unordered, you can't predict which element will be removed.
- Example:

```python
my_set = {"a", "b", "c"}
removed_element = my_set.pop()  # my_set might become {"a", "b"} or {"a", "c"} (unpredictable)
```

**5. `.clear()`:**

- Removes all elements from the set, making it empty.
- Example:

```python
my_set = {"a", "b", "c"}
my_set.clear()  # my_set becomes set() (empty set)
```

**6. Set Operators:**

- Python supports set operations like union (`|`), intersection (`&`), and difference (`-`) using these operators on sets.
- Example:

```python
set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
union_set = set1 | set2  # union_set becomes {"a", "b", "c", "d"}
intersection_set = set1 & set2  # intersection_set becomes {"b", "c"}
difference_set = set1 - set2  # difference_set becomes {"a"}
```

Remember that these methods modify the original set object. If you need to preserve the original set, consider creating a copy using methods like `.copy()` before applying modifications.
"""