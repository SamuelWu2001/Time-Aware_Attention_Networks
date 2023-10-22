# Introduction

In Taiwan, over 12% of the population suffers from chronic kidney disease, with as many as 94,000 individuals requiring regular dialysis. Moreover, the number of dialysis patients increases annually at a staggering rate of 8,000 to 9,000 people, making Taiwan's prevalence of dialysis the highest in the world.

Hypotension during dialysis is one of the most common complications for dialysis patients. It not only affects the patients' quality of life but also increases the risk of arrhythmias, chronic or acute cardiovascular, and cerebrovascular ischemia. The occurrence of hypotension often leads to interruptions in the dialysis process, resulting in inadequate clearance of toxins and insufficient fluid removal, which can exacerbate the symptoms of uremia and heart failure over the long term. Previous literature has indicated that hypotension during dialysis is associated with increased mortality among dialysis patients.

However, hypotension during dialysis is preventable through various measures such as saline infusion, lowering the dialysate temperature, and increasing dialysate calcium levels. Therefore, our primary objective is to utilize a machine learning model to predict the occurrence of hypotension during dialysis in real-time and take appropriate actions to prevent it, thereby reducing the risk for patients during the dialysis procedure.

From past statistical data, we have observed a significant interaction between environmental temperature and patients' blood pressure. Therefore, we aim to incorporate temperature information using a time-series model to enhance the predictive outcomes of the model.

![image](https://github.com/SamuelWu2001/Time-Aware_Attention_Networks/assets/71746159/1c458ac3-b9c5-4d12-b1e5-dcbfd7375df9)
![image](https://github.com/SamuelWu2001/Time-Aware_Attention_Networks/assets/71746159/716e2a91-2ad1-4aa6-b0e5-4d1734a2abd8)

# Dataset & Data Preprocess
- Data Source
  - Cheng Kung University Hospital, Department of Nephrology (De-identified) (IRB: A-ER-110-327)
- Sample Size
  - Total of 522,845 records
  - IDH Incidence Rate: Approximately 10%
- Data Collection Period
  - 2016 to 2021
- Vital Sign
  - Systolic Blood Pressure, Diastolic Blood Pressure, Heart Rate, Respiratory Rate
- Patient Physiological Information
  - Systolic Blood Pressure, Diastolic Blood Pressure, Heart Rate, Respiratory Rate, Dialysis Blood Temperature, Blood Flow Rate, Anticipated Dialysate Volume, Weight, Gender, Age, Diabetes, Hypertension, Cardiovascular Disease
- Dataset Splitting
  - There are a total of 194 individuals, divided into: 120 for the training set, 40 for the validation set, and 34 for the test set.
  - Each patient can contribute up to 10 data entries (an equal number of positive and negative samples).
- Environmental Data Acquisition
  - Retrieve temperature and humidity data for the patient from the nearest monitoring station for the past 24 hours.
  ![image](https://github.com/SamuelWu2001/Time-Aware_Attention_Networks/assets/71746159/4afbe91c-dd7f-4ea0-929d-89e3beebd933)
- Definition of Hypotension Events
  - When the systolic blood pressure at the next time point is less than 90, it is considered hypotension.
  - If the systolic blood pressure at the current time point is greater than 160 and the systolic blood pressure at the next time point is less than 100, it is also classified as hypotension.

# Model & Training
We utilize a Transformer Encoder to extract temporal features from the patient's previous dialysis session. This includes four key parameters: systolic blood pressure, diastolic blood pressure, heart rate, and respiratory rate. The aim is to leverage information from the previous dialysis session to assist in predicting the outcome of the current one.

We employ a Time-Aware Transformer to capture the temporal features of temperature and humidity over the patient's preceding 24 hours. The original input is first subjected to embedding, and then the corresponding temporal values are incorporated before feeding it into the Transformer.

![image](https://github.com/SamuelWu2001/Time-Aware_Attention_Networks/assets/71746159/6b97b070-5725-4df7-bfa2-e3a8d461c85a)

- Hyperparameter & Optimizer
  - Learning Rate : 0.001
  - Epoch : 50
  - Batch Size : 8
  - Optimizer : Stochastic Gradient Decent (momentum : 0.9)
  - Loss Function : Binary Cross-Entorpy With Logits

 # Result
 ![image](https://github.com/SamuelWu2001/Time-Aware_Attention_Networks/assets/71746159/ea34456d-87cd-4aba-94a8-2867c91a2d03)
 ![image](https://github.com/SamuelWu2001/Time-Aware_Attention_Networks/assets/71746159/69ca2e4c-5162-42ba-9d04-596d7d8d2549)

   






