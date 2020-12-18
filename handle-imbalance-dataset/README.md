# handle-imbalance-dataset
how to handle imbalance dataset
# Under Sampling :
Randomly eleminates Majority class instances/records until it balance with the Minority class Disadvantage: As it eleminates randomly there is a possibility of elemination of USEFUL DATA thus making the algorithm predicts inaccurately

NearMiss is an under-sampling technique. It aims to balance class distribution by randomly eliminating majority class examples. When instances of two different classes are very close to each other, we remove the instances of the majority class to increase the spaces between the two classes. This helps in the classification process.

# OverSampling :
Randomly replicates the Minority Class to increase its frequency (in numbers to match Majority class) in this technique there is 'no loss of information' but possibility of 'overfitting' the model since it is replicating the data

Using SMOTETomek
SMOTETomek is a hybrid method which uses an under sampling method (Tomek) in with an over sampling method (SMOTE).
it is combination of undersampling and oversampling.
