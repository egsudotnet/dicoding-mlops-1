def preprocessing_fn(inputs):
    # Preprocessing untuk Transform
    return inputs

def run_fn(fn_args):
    import tensorflow as tf
    from tensorflow.keras import layers

    # Model sederhana untuk latihan
    model = tf.keras.Sequential([
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    model.fit(fn_args.transformed_examples, epochs=5)
    model.save(fn_args.serving_model_dir, save_format='tf')
