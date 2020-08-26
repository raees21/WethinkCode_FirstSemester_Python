

def create_outline():
    """
    TODO: implement your code here
    """

    print("Course Topics:")

    topics={"Introduction to Python", 
            "Tools of the Trade", 
            "How to make decisions", 
            "How to repeat code", 
            "How to structure data", 
            "Functions", 
            "Modules"}
    topics = sorted(topics)
    for x in topics:
        print("*", x)

    print("Problems:")

    problems=["Problem 1",
              "Problem 2",
              "Problem 3"]


    my_map = {}
    for key in topics:
        my_map[key] = problems
        print("*", key, ": "+ ", ".join(my_map[key]))

    print("Student Progress: ")

    students = ("Jim", "Bob", "James")

    status = ["STARTED", "GRADED", "COMPLETED"]

    for n in range(0, len(students)):
        print(str(n+1) + "." + " " + students[n], "-", topics[n], "-",problems[n], "[" + status[n] + "]")

    pass

if __name__ == "__main__":
    create_outline()
