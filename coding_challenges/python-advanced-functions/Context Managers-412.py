## 2. Using Context Managers ##

with open('my_file.txt') as my_file:
    text = my_file.read()
    
print(text)

## 3. Using Context Managers Continued ##

with open('alice.txt') as file:
    text = file.read()

n = 0
for word in text.split():
    if word.lower() in ['cat', 'cats']:
        n += 1


print('Lewis Caroll uses the word "cat" {} times'.format(n))

## 4. Writing Context Managers ##

import contextlib
import time

@contextlib.contextmanager
def timer():
    """Time the execution of a context block.

    Yields:
      None
    """
    start = time.time()
    # Send control back to the context block
    yield

    end = time.time()
    print('Elapsed: {:.2f}s'.format(end - start))

with timer():
    print('This should take approximately 0.25 seconds')
    time.sleep(0.25)

## 5. Writing Context Managers Continued ##

@contextlib.contextmanager
def open_read_only(filename):
    """Opens a file in read only mode and cleans up.
    
    Yields:
      read_only_file
    """
    
    read_only_file = open(filename, 'r')
    
    yield read_only_file
    
    read_only_file.close()
    
with open_read_only('my_file.txt') as my_file:
    print(my_file.read())
    
    