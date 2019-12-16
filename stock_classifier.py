import tensorflow as tf
import numpy as np

STOCK_TRAINING = "2.csv"

STOCK_TEST = "8.csv"

def main():
    training_set=tf.contrib.learn.datasets.base.load_csv_without_header(
        filename=STOCK_TRAINING,
        target_dtype=np.float32,
        features_dtype=np.float32)
    test_set=tf.contrib.learn.datasets.base.load_csv_without_header(
        filename=STOCK_TEST,
        target_dtype=np.float32,
        features_dtype=np.float32)
    
    feature_columns = [tf.feature_column.numeric_column("x",shape=[50])]
    
    classifier = tf.estimator.DNNClassifier(feature_columns=feature_columns,
                                            hidden_units=[1],
                                            n_classes=2,
                                            model_dir="model")
    
    train_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x":np.array(training_set.data)},
        y=np.array(training_set.target),
        num_epochs=None,
        shuffle=True)
    
    classifier.train(input_fn=train_input_fn, steps=2000)
    
    test_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": np.array(test_set.data)},
        y=np.array(test_set.target),
        num_epochs=1,
        shuffle=False)
    
    accuracy_score = classifier.evaluate(input_fn=test_input_fn)["accuracy"]
    
    print("\nTest Accuracy: {0:f}\n".format(accuracy_score))

    
if __name__ == "__main__":
    main()