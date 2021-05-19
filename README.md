# insurance_estimator_app

In this app, we will examine how factors such as age, sex, BMI, number of children, and smoking status contribute to medical insurance costs.

we will use some gudelines from diffrent resources like WHO (World Health Organization) that gives people advice on how to lower their medical insurance costs.
### our model function
we are using the following function to calculate the insurance cost:
insurance_cost=250∗age−128∗sex+370∗bmi+425∗num_of_children+24000∗smoker−12500

where:
age: age of the individual in years
sex: 0 for female, 1 if male
bmi: individual’s body mass index
num_of_children: number of children the individual has
smoker: 0 for a non-smoker, 1 for a smoker

