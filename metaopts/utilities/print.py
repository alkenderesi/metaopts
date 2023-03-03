def print_function_trace(tf_function_name):
    """
    Print debug information about the tracing process of a `@tf.function`.

    Args:
        tf_function_name: `str` - Name of the `@tf.function` that is being traced.
    """

    print('Tracing {0}...'.format(tf_function_name))


def print_algo_start(algorithm_name):
    """
    Print debug information about the start of an algorithm.

    Args:
        algorithm_name: `str` - Name of the algorithm that is being started.
    """

    print('Starting {0}.'.format(algorithm_name))


def print_algo_end(algorithm_name):
    """
    Print debug information about the end of an algorithm.

    Args:
        algorithm_name: `str` - Name of the algorithm that is being ended.
    """

    print('\n{0} finished.'.format(algorithm_name))


def print_training_status(
        generation,
        generation_limit,
        best_fitness_value
    ):
    """
    Print debug information about the current status of the training process.

    Args:
        generation: `int` - Current generation.
        generation_limit: `int` - Maximum number of generations.
        best_fitness_value: `float` - Best fitness value of the current generation.
    """

    print('Generation: {0}/{1} Best fitness: {2}'.format(generation, generation_limit, best_fitness_value), end='\r')
