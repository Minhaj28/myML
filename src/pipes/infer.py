from visualizer import plot_predictions
import numpy as np
import utils

def evaluate(model, X_train, y_train, X_test, y_test):
    y_preds = model.predict(X_test)
    plot_predictions(train_data=X_train, train_labels=y_train,  test_data=X_test, test_labels=y_test,  predictions=y_preds)


    # Calculate model_1 metrics
    mae_1 = np.round(float(utils.mae(y_test, y_preds.squeeze()).numpy()), 2)
    mse_1 = np.round(float(utils.mse(y_test, y_preds.squeeze()).numpy()), 2)
    
    return mae_1, mse_1