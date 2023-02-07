import tensorflow as tf


def create_fitness(model, loss, x, y, batch_size):
    """
    Creates a fitness function which evaluates the model's fitness with a random batch.

    Args:
        model: `tf.keras.Model` - Neural network model.
        loss: `tf.keras.losses.Loss` - Loss function.
        x: `tf.Tensor` - Input data.
        y: `tf.Tensor` - Target data.
        batch_size: `int` - Number of samples per fitness calculation.

    Notes:

    * The created fitness function has no input parameters because it is linked to the model.
    * You must change the model weights first and then call the fitness function for evaluation.
    * Converting the training data to `tf.Tensor` allows graph execution.
    """

    # Shape of network output
    output_shape = (batch_size,) + model.output_shape[1:]

    # Batch randomization index limit
    random_limit = x.shape[0] - batch_size + 1

    # Variables for the fitness function
    batch_start = tf.Variable(0, dtype=tf.int32)
    batch_end = tf.Variable(0, dtype=tf.int32)
    predictions = tf.Variable(tf.zeros(output_shape), dtype=tf.float32)

    @tf.function
    def fitness():

        # Print debug information
        print('Tracing fitness...')

        # Randomize batch
        batch_start.assign(tf.random.uniform(shape=(), minval=0, maxval=random_limit, dtype=tf.int32))
        batch_end.assign(batch_start + batch_size)

        # Make batch prediction
        predictions.assign(model(x[batch_start:batch_end]))

        # Return loss value
        return loss(y[batch_start:batch_end], predictions)

    return fitness
