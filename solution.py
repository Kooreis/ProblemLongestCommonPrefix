Here is a Python console application that computes the longest common prefix among a list of strings:

```python
def longest_common_prefix(strs):
    if not strs:
        return ""
    shortest_str = min(strs, key=len)
    for i, char in enumerate(shortest_str):
        for other in strs:
            if other[i] != char:
                return shortest_str[:i]
    return shortest_str

def main():
    strs = input("Enter strings separated by space: ").split()
    print("Longest common prefix: ", longest_common_prefix(strs))

if __name__ == "__main__":
    main()
```

You can run this application in the console. It will ask you to enter strings separated by space. After you enter the strings and press enter, it will print the longest common prefix among the entered strings.