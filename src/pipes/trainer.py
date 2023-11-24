import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os

import models
import infer

if __name__ == "__main__":
    # Check Tensorflow version
    print(tf.__version__)


    # Create features
    X = np.arange(-100, 100, 4)

    # Create labels
    y = np.arange(-90, 110, 4)


    # Split data into train and test sets
    X_train = X[:40] # first 40 examples (80% of data)
    y_train = y[:40]

    print(X.shape, y.shape)

    X_test = X[40:] # last 10 examples (20% of data)
    y_test = y[40:]


    # Take a single example of X
    input_shape = X[0].shape 

    # Take a single example of y
    output_shape = y[0].shape


    # Set random seed
    tf.random.set_seed(42)

    # Create a model using the Sequential API
    model = models.get_model()

    # Compile the model
    model.compile(
        loss = tf.keras.losses.mae,
        optimizer = tf.keras.optimizers.SGD(),
        metrics = ['mae']
    )

    # Fit the model
    model.fit(X_train, y_train, epochs=100)


    mae_1, mse_1 = infer.evaluate(model, X_train, y_train, X_test, y_test)
    print(f'\nMean Absolute Error = {mae_1}, Mean Squared Error = {mse_1}.')

    # Write metrics to file
    with open(os.path.abspath('reports/results/metrics.txt'), 'w') as outfile:
        outfile.write(f'\nMean Absolute Error = {mae_1}, Mean Squared Error = {mse_1}.')

    # Save models for prediction
    model.save("models/my_model")