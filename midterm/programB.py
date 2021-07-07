def whoami():
    return "I'm programB!"


print("I am a rude programB.")

if __name__ == "__main__":
    import programA

    a = programA.whoami()
    b = whoami()
    print("a == {}".format(a))
    print("b == {}".format(b))
