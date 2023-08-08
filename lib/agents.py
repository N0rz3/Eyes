def user_agent():
    with open("useragents.txt", "r") as user_file:
        agent = user_file.read().split('\n')
        return agent