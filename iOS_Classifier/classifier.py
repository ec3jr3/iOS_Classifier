

import turicreate as tc


data =  tc.SFrame('diabetes.csv')

data.column_names()

feature_name = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']

train_data, test_data = data.random_split(0.75)

logistic_model = tc.logistic_classifier.create(train_data, target = 'Outcome',features=feature_name)

model = logistic_model.evaluate(test_data)
print (model["accuracy"])

model.save("Diabetes.model")
model.export_coreml("Diabetes.mlmodel")








