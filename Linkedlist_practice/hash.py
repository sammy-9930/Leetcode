def hash_function(key, size):
    return hash(key) % size

table_size = 10
key = "example_key"
index = hash_function(key, table_size)
print(f"Index for '{key}': {index}")
