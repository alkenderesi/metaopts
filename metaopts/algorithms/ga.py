import tensorflow as tf


def ga(model_weights, model_fitness, population_size):
    """
    Implemetation of a simple Genetic Algorithm.
    """

    @tf.function
    def update_fitness():
        print('Tracing update_fitness...')
        for i in range(population_size):
            for mw, p in zip(model_weights, population):
                mw.assign(p[i])
            fitness_values[i].assign(model_fitness())

    def selection():
        pass

    def crossover():
        pass

    def mutation():
        pass


    population = [tf.Variable(tf.repeat(tf.expand_dims(weights, axis=0), population_size, axis=0)) for weights in model_weights]
    fitness_values = tf.Variable(tf.zeros(population_size, dtype=tf.float32))
