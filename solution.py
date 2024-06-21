def main():
    strs = input("Enter strings separated by space: ").split()
    print("Longest common prefix: ", longest_common_prefix(strs))