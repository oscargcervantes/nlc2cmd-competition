from nlc2cmd import predict_nl2bash


def predict(invocations, result_cnt=5):
    """ 
    Function called by the evaluation script to interface the participants model
    `predict` function accepts the natural language invocations as input, and returns
    the predicted commands along with confidences as output. For each invocation, 
    `result_cnt` number of predicted commands are expected to be returned.

    Args:
        1. invocations : `list (str)` : list of `n_batch` (default 16) natural language invocations
        2. result_cnt : `int` : number of predicted commands to return for each invocation

    Returns:
        1. commands : `list [ list (str) ]` : a list of list of strings of shape (n_batch, result_cnt)
        2. confidences: `list[ list (float) ]` : confidences corresponding to the predicted commands
                                                 confidence values should be between 0.0 and 1.0. 
                                                 Shape: (n_batch, result_cnt)
    """

    n_batch = len(invocations)

    # `commands` and `confidences` have shape (n_batch, result_cnt)
    commands = [
        [''] * result_cnt
        for _ in range(n_batch)
    ]
    confidences = [
        [1.0] * (result_cnt - 1) + [0.0]
        for _ in range(n_batch)
    ]

    ################################################################################################
    #     Participants should add their codes to fill predict `commands` and `confidences` here    #
    ################################################################################################

    commands = predict_nl2bash(invocations, result_cnt)

    ################################################################################################
    #                               Participant code block ends                                    #
    ################################################################################################

    return commands, confidences
