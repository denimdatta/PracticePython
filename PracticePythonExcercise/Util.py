import PracticePythonExcercise

problem_list = {1: "Character Input", 2: "Odd Or Even", 3: "List Less Than Ten",
                4: "Divisors", 5: "List Overlap", 6: "String Lists",
                7: "List Comprehensions", 8: "Rock Paper Scissors", 9: "Guessing Game One",
                10: "List Overlap Comprehensions", 11: "Check Primality Functions",
                12: "List Ends", 13: "Fibonacci", 14: "List Remove Duplicates",
                15: "Reverse Word Order", 16: "Password Generator",
                17: "Decode A Web Page", 18: "Cows And Bulls", 19: "Decode A Web Page Two",
                20: "Element Search", 21: "Write To A File",
                22: "Read From File", 23: "File Overlap", 24: "Draw A Game Board",
                25: "Guessing Game Two", 26: "Check Tic Tac Toe", 27: "Tic Tac Toe Draw",
                28: "Max Of Three", 29: "Tic Tac Toe Game", 30: "Pick Word",
                31: "Guess Letters", 32: "Hangman", 33: "Birthday Dictionaries",
                34: "Birthday Json", 35: "Birthday Months", 36: "Birthday Plots"}


def show_problems():
    var_start = 0
    print(
        "\n------------------------------------------------------------------------------------------Problem "
        "List------------------------------------------------------------------------------------------\n")
    print(
        "--------------------------------------------------------------------Visit http://www.practicepython.org/ "
        "for Problem details--------------------------------------------------------------------\n")

    while var_start < problem_list.__len__():
        problem_line = list(problem_list.keys())[var_start:var_start + 4]
        for _prob in problem_line:
            print("{0}.\t\t{1}".format(str(_prob).rjust(3, " "), str(problem_list.get(_prob)).ljust(32, " ")), " ",
                  end="|\t")
        print("")
        var_start += 4
    print("\n-----------------------------------------------------------------------------------------------"
          "-------------------------------------------------------------------------------------------------\n\n")


def get_integer(display_text="Enter a Number: ", quit_option="__DEFAULT__", help_option="__DEFAULT__"):
    if help_option.upper() != "__DEFAULT__":
        display_text += " or enter [{0}] to See the Problem Details".format(help_option)

    if quit_option.upper() != "__DEFAULT":
        display_text += " or enter [{0}] to exit".format(quit_option)

    display_text += ": "
    while True:
        var_input = input(display_text)

        if quit_option.upper() != "__DEFAULT" and (
                var_input.upper() == quit_option[0].upper() or var_input.upper() == quit_option.upper()):
            return None
        elif help_option.upper() != "__DEFAULT" and (
                var_input.upper() == help_option[0].upper() or var_input.upper() == help_option.upper()):
            show_problems()
            continue
        else:
            try:
                return int(var_input)
            except ValueError:
                print("Invalid input provided. Please check again")
                continue


def call_solution(problem_no):
    solution_dir = {1: PracticePythonExcercise.PracticePythonSolutions.PracticePythonSolution01.solution,
                    2: PracticePythonExcercise.PracticePythonSolutions.PracticePythonSolution02.solution,
                    3: PracticePythonExcercise.PracticePythonSolutions.PracticePythonSolution03.solution,
                    4: PracticePythonExcercise.PracticePythonSolutions.PracticePythonSolution04.solution,
                    5: PracticePythonExcercise.PracticePythonSolutions.PracticePythonSolution05.solution,
                    6: PracticePythonExcercise.PracticePythonSolutions.PracticePythonSolution06.solution,
                    7: PracticePythonExcercise.PracticePythonSolutions.PracticePythonSolution07.solution,
                    8: PracticePythonExcercise.PracticePythonSolutions.PracticePythonSolution08.solution,
                    9: PracticePythonExcercise.PracticePythonSolutions.PracticePythonSolution09.solution,
                    10: PracticePythonExcercise.PracticePythonSolutions.PracticePythonSolution10.solution,
                    11: PracticePythonExcercise.PracticePythonSolutions.PracticePythonSolution11.solution,
                    12: PracticePythonExcercise.PracticePythonSolutions.PracticePythonSolution12.solution
                    # 13: PracticePythonExcercise.PracticePythonSolutions.PracticePythonSolution13.solution,
                    }

    print(
        "\n------------------------------------SOLUTION for {0}------------------------------------\n".format(problem_no))

    if problem_no not in problem_list.keys():
        print("Problem {0} is Not present. Check Problems".format(problem_no))
    elif problem_no not in solution_dir.keys():
        print("Solution for Problem {0} is not yet done".format(problem_no))
    else:
        solution_dir[problem_no]()

    print("\n--------------------------------------------------------------------------------------\n\n")
