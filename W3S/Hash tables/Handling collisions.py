# Define the hash set as a list of lists, each acting as a bucket for hash collisions
my_hash_set = [
    [None],    # Bucket at index 0
    ['Jones'], # Bucket at index 1
    [None],    # Bucket at index 2
    ['Lisa'],  # Bucket at index 3
    [None],    # Bucket at index 4
    ['Bob'],   # Bucket at index 5
    [None],    # Bucket at index 6
    ['Siri'],  # Bucket at index 7
    ['Pete'],  # Bucket at index 8
    [None]     # Bucket at index 9
]

# Define a simple hash function that maps a string value to an index in the hash set
def hash_function(value):
    # Calculate the sum of ASCII values of all characters in the string
    # Then take the modulo of the sum to get an index within the range of the hash set
    return sum(ord(char) for char in value) % 10

# Function to add a value to the hash set
def add(value):
    # Get the index for the value using the hash function
    index = hash_function(value)
    # Get the bucket at the computed index
    bucket = my_hash_set[index]
    # Check if the value is not already in the bucket to avoid duplicates
    if value not in bucket:
        # Add the value to the bucket
        bucket.append(value)

# Function to check if a value exists in the hash set
def contains(value):
    # Get the index for the value using the hash function
    index = hash_function(value)
    # Get the bucket at the computed index
    bucket = my_hash_set[index]
    # Check if the value is in the bucket and return the result
    return value in bucket

# Add a new value "Stuart" to the hash set
add('Stuart')

# Print the hash set after adding "Stuart"
print(my_hash_set)

# Check if the hash set contains "Stuart" and print the result
print('Contains Stuart:', contains('Stuart'))
