# """"
# riddles = {
#     "riddle1": {"question": "What has keys but can’t open locks?", "answer": "piano"},
#     "riddle2": {"question": "I speak without a mouth and hear without ears. What am I?", "answer": "echo"},
#     "riddle3": {"question": "What has to be broken before you can use it?", "answer": "egg"},
#     "riddle4": {"question": "The more of this there is, the less you see. What is it?", "answer": "darkness"},
#     "riddle5": {"question": "What has one eye but can’t see?", "answer": "needle"}
# }
# """

riddles = {
    "riddle1": {
        "question": "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
        "answer": "echo",
        "clue": "It’s a repeating sound."
    },
    "riddle2": {
        "question": "The more of this there is, the less you see. What is it?",
        "answer": "darkness",
        "clue": "It often comes at night."
    },
    "riddle3": {
        "question": "What has keys but can’t open locks?",
        "answer": "piano",
        "clue": "It’s a musical instrument."
    },
    "riddle4": {
        "question": "What comes once in a minute, twice in a moment, but never in a thousand years?",
        "answer": "the letter m",
        "clue": "It’s a letter in the alphabet."
    },
    "riddle5": {
        "question": "I’m light as a feather, yet the strongest person can’t hold me for five minutes. What am I?",
        "answer": "breath",
        "clue": "You need me to stay alive."
    }
}

more_riddles = {
    "riddle6": {
        "question": "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?",
        "answer": "map",
        "clue": "I help you find your way."
    },
    "riddle7": {
        "question": "What is always in front of you but can’t be seen?",
        "answer": "future",
        "clue": "It’s what’s yet to come."
    },
    "riddle8": {
        "question": "What has to be broken before you can use it?",
        "answer": "egg",
        "clue": "You might have this for breakfast."
    },
    "riddle9": {
        "question": "What has one eye but can’t see?",
        "answer": "needle",
        "clue": "It’s used for sewing."
    },
    "riddle10": {
        "question": "The more you take, the more you leave behind. What am I?",
        "answer": "footsteps",
        "clue": "You make these when you walk."
    }
}

# """
# for key, value in riddles.items():
#     print(f"Riddle: {value['question']}")
#     user_input = input("Your answer: ").strip().lower()
#     if user_input == value['answer']:
#         print("Correct!")
#     else:
#         print(f"Wrong! Here’s a clue: {value['clue']}")
#         user_input = input("Try again: ").strip().lower()
#         if user_input == value['answer']:
#             print("Correct!")
#         else:
#             print(f"Still incorrect. The answer was: {value['answer']}")
#     print()
# """
