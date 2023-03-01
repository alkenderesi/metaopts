import pickle


def save_individual(population, individual_index, file_path, file_extension = '.pickle'):
    """
    Saves the individual at the specified index in the population to a file.

    Args:
        population: `list` of `tf.Variable` - List of population weights.
        individual_index: `int` - Index of the individual in the population.
        file_path: `str` - Path to the file.
        file_extension: `str` - File extension.
    """

    if file_path[-len(file_extension):] != file_extension:
        file_path += file_extension

    individual = [p[individual_index] for p in population]

    with open(file_path, 'wb') as save_file:
        pickle.dump(individual, save_file)


def load_individual(file_path, file_extension = '.pickle'):
    """
    Loads an individual from a file.

    Args:
        file_path: `str` - Path to the file.
        file_extension: `str` - File extension.
    """

    if file_path[-len(file_extension):] != file_extension:
        file_path += file_extension

    with open(file_path, 'rb') as save_file:
        individual = pickle.load(save_file)

    return individual
