from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
import pandas as pd
import pickle
import joblib



#Load  dataset
df = pd.read_csv("../csv/training_dataset.csv")

#Split your dataset into features (X) and labels (y)
X = df.iloc[:, :16]  # Features
y = df.iloc[:, 16]  # Labels

#Split your data into training and testing sets
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



# Save the trained model as a pickle string.
saved_model = pickle.dumps(clf)

# Save the model to disk
with open('svm_model.pkl', 'wb') as file:
    pickle.dump(clf, file)
    
# Assuming scaler is your fitted StandardScaler
joblib.dump(scaler, 'scaler.pkl')    


