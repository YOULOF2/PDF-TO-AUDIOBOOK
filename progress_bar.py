from tqdm import tqdm


def progress_bar():
    for i in tqdm(range(4)):
        yield None
