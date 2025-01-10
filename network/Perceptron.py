import random

class Perceptron:
    def __init__(self, size):
        self.weights = []
        self.learning_rate = 0.1

        for i in range(size):
            self.weights.append(random.uniform(-1.0, 1.0))

    def forward(self, inputs):
        return sum([i * w for i, w in zip(inputs, self.weights)])
    
    def activate(self, x):
        return 1 if x >= 0 else -1

    def guess(self, inputs):
        return self.activate(self.forward(inputs))
    
    def train(self, inputs, target):
        guess = self.guess(inputs)
        error = target - guess
        for i in range(len(self.weights)):
            self.weights[i] += error * inputs[i] * self.learning_rate
        return error