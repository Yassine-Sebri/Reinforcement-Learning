# the point of this code is to demonstrate how epsilon greedy works

import numpy as np
import matplotlib.pyplot as plt


class Bandit:
    def __init__(self, m):
        self.m = m
        self.mean = 0
        self.N = 0

    def pull(self):
        return np.random.rand() + self.m

    def update(self, x):
        self.N += 1
        self.mean = (1 - 1 / self.N) * self.mean + (1 / self.N) * x


def run_experiment(m1, m2, m3, eps, N):
    bandits = [Bandit(m1), Bandit(m2), Bandit(m3)]

    data = np.empty(N)

    for i in range(N):
        p = np.random.rand()
        if p < eps:
            j = np.random.choice(3)
        else:
            j = np.argmax([b.mean for b in bandits])
        x = bandits[j].pull()
        bandits[j].update(x)

        data[i] = x

    cumulative_average = np.cumsum(data) / (np.arange(N) + 1)

    plt.plot(cumulative_average)
    plt.plot(np.ones(N) * m1)
    plt.plot(np.ones(N) * m2)
    plt.plot(np.ones(N) * m3)
    plt.xscale('log')
    plt.show()

    for b in bandits:
        print(b.mean)

    return cumulative_average


if __name__ == '__main__':
    c_1 = run_experiment(1.0, 2.0, 3.0, 0.1, 10000)
    c_05 = run_experiment(1.0, 2.0, 3.0, 0.05, 10000)
    c_01 = run_experiment(1.0, 2.0, 3.0, 0.01, 10000)

    plt.plot(c_1)
    plt.plot(c_05)
    plt.plot(c_01)
    plt.legend(('eps = 0.1', 'eps = 0.05', 'eps = 0.01'))
    plt.show()