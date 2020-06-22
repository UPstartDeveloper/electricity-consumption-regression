import time

def time_training(fitter):
    """Print the time taken for a machine learning algorithm to train.

       Parameters:
       fitter(function): function used to train the model

       Returns: None

    """
    start = time.time()
    fitter()
    end = time.time()
    diff = end - start
    print(f'Training time: {diff} miliseconds.')
    return None