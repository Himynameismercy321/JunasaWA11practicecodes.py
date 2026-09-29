Machine_Learning = [
    ("Supervised", "Decision tree"),
    ("Supervised", "Random Forest"),
    ("Unsupervised", "K-Means"),
    ("Unsupervised", "Gaussian Mixture Model")
]

print("Learning Type:", Machine_Learning[0][0])
for item in Machine_Learning:
    if item[0] == "Supervised":
        print(item[1])
print("Learning type:", Machine_Learning[2][0])
for D in Machine_Learning:
    if D[0] == "Unsupervised":
        print(D[1])