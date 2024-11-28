class SimpleHashSet:
    def __init__(self, size=100):
        # Initialize the hash set with a specified number of buckets (default: 100)
        self.size = size
        # Create a list of buckets, where each bucket is an empty list (used for separate chaining)
        self.buckets = [[] for _ in range(size)]

    def hash_function(self, value):
        # Compute the hash code for the given value
        # The hash function sums up the ASCII values of the characters in the string
        # and takes modulo with the size of the hash set to ensure the index is within bounds
        return sum(ord(char) for char in value) % self.size

    def add(self, value):
        # Add a value to the hash set
        index = self.hash_function(value)  # Get the index for the value using the hash function
        bucket = self.buckets[index]      # Find the corresponding bucket
        if value not in bucket:           # Check if the value is already in the bucket to avoid duplicates
            bucket.append(value)          # Add the value to the bucket if not present

    def contains(self, value):
        # Check if a value exists in the hash set
        index = self.hash_function(value) # Get the index for the value using the hash function
        bucket = self.buckets[index]      # Find the corresponding bucket
        return value in bucket            # Check if the value exists in the bucket

    def remove(self, value):
        # Remove a value from the hash set
        index = self.hash_function(value) # Get the index for the value using the hash function
        bucket = self.buckets[index]      # Find the corresponding bucket
        if value in bucket:               # If the value exists in the bucket
            bucket.remove(value)          # Remove the value

    def print_set(self):
        # Print all elements in the hash set
        print("Hash Set Contents:")
        for index, bucket in enumerate(self.buckets):  # Iterate through all buckets
            print(f"Bucket {index}: {bucket}")         # Print the contents of each bucket


# Create a hash set with 10 buckets
hash_set = SimpleHashSet(size=10)

# Add values to the hash set
hash_set.add("Charlotte")
hash_set.add("Thomas")
hash_set.add("Jens")
hash_set.add("Peter")
hash_set.add("Lisa")
hash_set.add("Adele")
hash_set.add("Michaela")
hash_set.add("Bob")

# Print the contents of the hash set
hash_set.print_set()

# Check if 'Peter' is in the set
print("\n'Peter' is in the set:", hash_set.contains('Peter'))

# Remove 'Peter' from the hash set
print("Removing 'Peter'")
hash_set.remove('Peter')

# Check again if 'Peter' is in the set
print("'Peter' is in the set:", hash_set.contains('Peter'))

# Get the hash code for 'Adele'
print("'Adele' has hash code:", hash_set.hash_function('Adele'))
