import tensorflow as tf

def get_model():
    return tf.keras.Sequential([
        tf.keras.layers.Input(shape=(1,)),
        tf.keras.layers.Dense(1),
        tf.keras.layers.Dense(1)
    ])