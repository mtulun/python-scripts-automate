def diffrence(param_list_one,param_list_two):
    """
    It returns a list of all elements in param_list_one that aren't in param_list_two
    """
    _param_list_two = set(param_list_two)
    return [item for item in param_list_one if item not in _param_list_two]