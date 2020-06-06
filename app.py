import platform

def justCheck():
    return platform.version()


if __name__ == "__main__":

    try:
        value = justCheck()
        print(value)
        exit(1)
        
    except Exception as e:
        print("THIS: ", e)
        exit(0)