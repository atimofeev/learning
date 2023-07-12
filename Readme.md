# Python Data Types

## Numeric Types

- `int`: This is the integer type. These are whole numbers, both positive and negative. For example, `5`, `0`, `-10`.

- `float`: This is the floating point type. These are real numbers, with decimal points. For example, `5.0`, `1.25`, `-0.75`.

- `complex`: This is the complex number type. These numbers have a real and imaginary part. For example, `3+5j`.

## Sequence Types

- `str`: This is the string type. Strings are sequences of Unicode characters. For example, `'hello'`, `"world"`.

- `list`: This is the list type. Lists are ordered sequences of values. The values can be of any type. For example, `[1, 2, 3]`, `['a', 'b', 'c']`.

- `tuple`: This is the tuple type. Tuples are like lists, but they are immutable. This means you cannot change their values once they are created. For example, `(1, 2, 3)`, `('a', 'b', 'c')`.

## Mapping Type

- `dict`: This is the dictionary type. Dictionaries are unordered collections of key-value pairs. For example, `{'name': 'John', 'age': 30}`.

## Set Types

- `set`: This is the set type. Sets are unordered collections of unique elements. For example, `{1, 2, 3}`.

- `frozenset`: This is the frozenset type. Frozensets are like sets, but they are immutable. 

## Boolean Type

- `bool`: This is the boolean type. The two boolean values are `True` and `False`.

## Special Types

- `None`: This is the `None` type. There is exactly one `None` value.

## Binary Types

- `bytes`: This is the bytes type. These are sequences of bytes.

- `bytearray`: This is the bytearray type. Bytearrays are like bytes, but they are mutable.

- `memoryview`: This is the memoryview type. These are sequences of memory.

# Python Data Types Examples

```python
# integer
my_int = 10
print(f"Value: {my_int}, type: {type(my_int)}")

# float
my_float = 10.5
print(f"Value: {my_float}, type: {type(my_float)}")

# complex
my_complex = 3 + 4j
print(f"Value: {my_complex}, type: {type(my_complex)}")

# string
my_str = 'Hello, Python!'
print(f"Value: {my_str}, type: {type(my_str)}")

# list
my_list = [1, 2, 3, 'Python', my_int, my_float]
print(f"Value: {my_list}, type: {type(my_list)}")

# tuple
my_tuple = (1, 2, 3, 'Python', my_int, my_float)
print(f"Value: {my_tuple}, type: {type(my_tuple)}")

# set
my_set = {1, 2, 2, 3, 4, 4}
print(f"Value: {my_set}, type: {type(my_set)}")  # duplicates removed

# frozenset
my_frozenset = frozenset([1, 2, 2, 3, 4, 4])
print(f"Value: {my_frozenset}, type: {type(my_frozenset)}")  # duplicates removed

# dictionary
my_dict = {'name': 'Python', 'year': 1991}
print(f"Value: {my_dict}, type: {type(my_dict)}")

# boolean
my_bool = True
print(f"Value: {my_bool}, type: {type(my_bool)}")

# bytes
my_bytes = b'This is a bytes example.'
print(f"Value: {my_bytes}, type: {type(my_bytes)}")

# bytearray
my_bytearray = bytearray(b'Hello Python')
my_bytearray[0] = 74  # change the first character
print(f"Value: {my_bytearray}, type: {type(my_bytearray)}")

# memoryview
my_memoryview = memoryview(bytes(5))
print(f"Value: {my_memoryview}, type: {type(my_memoryview)}")
