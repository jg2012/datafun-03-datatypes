# import from local util_datafun_logger.py
from util_datafun_logger import setup_logger

# Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)

def tupules(): 
    # Create some tuples
    tupleA = (1, 2, 3, 4, 5)
    tupleB = (4, 5, 6, 7, 8)

    logger.info(f"tupleA = {tupleA}")
    logger.info(f"tupleB = {tupleB}")

def sets_example():
    setA = {1, 2, 3, 4, 5}
    setB = {4, 5, 6, 7, 8}

    logger.info(f"setA = {setA}")
    logger.info(f"setB = {setB}")

    # set union
    setC = setA | setB
    logger.info(f"Union: {setC}")

    # set intersection
    setD = setA & setB
    logger.info(f"Intersection: {setD}")

def dictionaries_example(): 
    recordA_dict = {"name": "The Good Life", "Artist": "The Good Life"}
    recordB_dict = {"name": "YHLQMDLG", "Artist": "Bad Bunny"}

    logger.info(f"recrodA_dict = {recordA_dict}")
    logger.info(f"recrodB_dict = {recordB_dict}")
    
   
    with open("text_simple.txt") as file_object:
        word_list = file_object.read().split()
        
        word_counts_dict2 = {word: word_list.count(word) for word in word_list}
        logger.info("Given text_simple.txt and comprehensions,")
        logger.info(f"the the word_counts_dict2 = {word_counts_dict2}")


if __name__ == "__main__":
    logger.info("Calling functions from main block")
    tupules()
    sets_example()
    dictionaries_example()