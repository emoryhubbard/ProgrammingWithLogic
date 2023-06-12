def main():
    friend = None
    friends = []
    while friend != "end":
        friend = input("Type the name of a friend: ")
        if friend != "end":
            friends.append(friend)
    print("\nYour friends are: ")
    for friend in friends:
        print(f"{friend}")
if __name__ == "__main__":
    main()