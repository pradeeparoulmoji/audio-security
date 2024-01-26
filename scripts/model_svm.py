from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import joblib


class Mod:
    #Load  dataset
    df = pd.read_csv("../csv/training_dataset.csv")

    #Split dataset into features (X) and labels (y)
    X = df.iloc[:, :16]  # Features
    y = df.iloc[:, 16]  # Labels

    #Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    #Standardize the features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    #Create a Support Vector Machine (SVM) model
    clf = svm.SVC()

    #Train the model using the training data
    clf.fit(X_train, y_train)

    #Evaluate the model using the testing data
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))

    #Evaluate the model using the new data data

    dz = pd.read_csv("../csv/test2.csv")

    #Split dataset into features (X) and labels (y)
    Xq = dz.iloc[:, :16]  # Features
    yq = dz.iloc[:, 16]  # Labels

    Xq = scaler.transform(Xq)


    #Evaluate the model using the new testing data
    y_predq = clf.predict(Xq)

    print(y_predq)
    
    # Generate confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(cm)

    # Compute ROC curve and ROC area for each class
    fpr, tpr, _ = roc_curve(y_test, y_pred)
    roc_auc = auc(fpr, tpr)

    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='darkorange', lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver Operating Characteristic')
    plt.legend(loc="lower right")
    plt.show()



    # Save the trained model as a pickle string.
    saved_model = pickle.dumps(clf)

    # Save the model to disk
    with open('svm_model.pkl', 'wb') as file:
        pickle.dump(clf, file)
        
    # Assuming scaler is the fitted StandardScaler
    joblib.dump(scaler, 'scaler.pkl')    

m = Mod()
