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

    @tf.function
    def roulette_wheel_selection():
        print('Tracing roulette_wheel_selection...')
        normalized = tf.reduce_sum(fitness_values) / fitness_values
        extended = tf.repeat(tf.expand_dims(normalized, axis=0), population_size, axis=0)
        selected = tf.random.categorical(tf.math.log(extended), 2, dtype=tf.int32)
        selected_individuals.assign(selected)

    def crossover():
        pass

    def mutation():
        pass


    population = [tf.Variable(tf.repeat(tf.expand_dims(weights, axis=0), population_size, axis=0)) for weights in model_weights]
    fitness_values = tf.Variable(tf.zeros(population_size, dtype=tf.float32))
    selected_individuals = tf.Variable(tf.zeros((population_size, 2), dtype=tf.int32))
