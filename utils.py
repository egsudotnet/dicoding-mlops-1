def run_fn(fn_args):
    import tensorflow as tf
    from tensorflow.keras import layers
    from tfx_bsl.public import tfxio

    # Load data dari TFRecord
    def _input_fn(file_pattern, data_accessor, schema, batch_size):
        return data_accessor.tf_dataset_factory(
            file_pattern,
            tfxio.TensorFlowDatasetOptions(batch_size=batch_size),
            schema=schema
        )

    train_dataset = _input_fn(
        fn_args.train_files,
        fn_args.data_accessor,
        fn_args.schema,
        batch_size=32
    )
    eval_dataset = _input_fn(
        fn_args.eval_files,
        fn_args.data_accessor,
        fn_args.schema,
        batch_size=32
    )

    # Model sederhana untuk latihan
    model = tf.keras.Sequential([
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])

    # Training model
    model.fit(train_dataset, validation_data=eval_dataset, epochs=5)

    # Simpan model
    model.save(fn_args.serving_model_dir, save_format='tf')
