import datetime


fitness_cache = []

def log_fitness_value(fitness_value, log_file_name='fitness_log', max_cache_size=100, force_file_write=False):
    """
    Log the fitness value to a csv file.

    Args:
        fitness_value: `float` - Fitness value to log.
        log_file_name: `str` - Name of the log file.
        max_cache_size: `int` - Maximum number of lines to cache before writing to the file.
        force_file_write: `bool` - If `True`, the cache will be written to the file regardless of its size.
    """

    # Current date and time
    now = datetime.datetime.now()
    date = now.strftime('%Y,%m,%d')
    time = now.strftime('%H,%M,%S,%f')

    # Append time and fitness value to the cache
    fitness_cache.append('{0},{1},{2}'.format(date, time, fitness_value))

    # If the cache is full or we are forcing a file write, write the cache to the log file
    if len(fitness_cache) >= max_cache_size or force_file_write:

        # Open file for appending or create it if it doesn't exist
        with open('{0}.csv'.format(log_file_name), 'a') as log_file:

            # Write the cache to the file
            for fitness in fitness_cache:
                log_file.write('{0}\n'.format(fitness))

        # Clear the cache
        fitness_cache.clear()
