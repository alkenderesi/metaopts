import tensorflow as tf


def create_population(model_weights, population_size, transfer_learning=False, deviation=0.1):
    """
    Creates a population of individuals (candidate solutions).

    Args:
        model_weights: `list` of `tf.Variable` - List of model weights.
        population_size: `int` - Number of individuals in the population.
        transfer_learning: `bool` - Whether to copy current model weights or generate random ones.
        deviation: `float` - Standard deviation of the normal distribution used to generate random weights.
    """

    if (transfer_learning):

        # Return a population of individuals with the same weights as the model
        return [tf.Variable(tf.repeat([weights], population_size, axis=0)) for weights in model_weights]

    # Return a population of individuals with random weights
    return [tf.Variable(tf.repeat([tf.random.normal(weights.shape, 0, deviation)], population_size, axis=0)) for weights in model_weights]


def sort_population(population, fitness_values):
    """
    Sorts the population in ascending order based on fitness values.

    Args:
        population: `list` of `tf.Variable` - List of population weights.
        fitness_values: `tf.Variable` - Fitness values of the population.
    """

    # Print debug information
    print('Tracing sort_population...')

    # Sort fitness values in ascending order
    order = tf.argsort(fitness_values)

    # Assign new order to fitness values and the population
    fitness_values.assign(tf.gather(fitness_values, order, axis=0))
    for p in population:
        p.assign(tf.gather(p, order, axis=0))


sort_population = tf.function(sort_population)
