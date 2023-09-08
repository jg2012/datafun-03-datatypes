"""
Modify this docstring.

"""

# imports first

import random
import math
import statistics

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

# reusable functions next

list_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]

list_colors = ["red", "green", "blue", "yellow", "orange", "purple"]

list_nouns = ["dog", "cat", "mouse", "bird", "fish", "snake"]

list_verbs = ["runs", "jumps", "swims", "flies", "crawls", "studies"]

list_adjectives = ["happy", "sad", "angry", "scared", "confused", "bored"]

# call functions and execute code

def random_choice(): 

    random_selection = (random.choice(list_names))

    logger.info(random_selection)

    sentenece = (f"{random.choice(list_names)} {random.choice(list_nouns)} {random.choice(list_verbs)}")

    logger.info(sentenece)
    logger.info("")

def text_hamlet(): 

    with open("text_hamlet.txt", "r") as fileObject:
        text = fileObject.read()
        list_words = text.split()
        unique_words = set(list_words)

        word_count = len(list_words)
        unique_word_count = len(unique_words)

        logger.info(f"There are {word_count} words in the file.")
        logger.info(f"There are {unique_word_count} unique words in the file.")
        logger.info(f"The set of unique words is: {unique_words}")
        logger.info("")

# use if __name__ == "__main__":
if __name__ == "__main__":

    logger.info("Calling the random functoin")
    logger.info("")
    random_choice()

    logger.info("Calling the text_hamlet function")
    text_hamlet()
    logger.info("")