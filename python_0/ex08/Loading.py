

def generate_bar(indx: int, len: int) -> str:
    return ("["+("█" * int((indx/len*100)))).ljust(101)+"]"


def ft_tqdm(lst: range) -> None:
    """a function that displays a progress bar"""
    length = len(lst)
    for index, elem in enumerate(lst):
        print(f"ETA: {generate_bar(index,length)}{elem}/{lst.stop}", end="\r")
        yield elem
