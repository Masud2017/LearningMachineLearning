#!/usr/bin/python3

def cal_cost(theta,x,y):
    m = len(y)
    predictions = x.dot(theta)
    cost = (1/2*m) *np.sum(np.square(predictions - y))

    return cost

def gradient_descent(x,y,theta,learning_rate=0.01,iterations=100):
    m = len(y)
    cost_history = np.zeros(iterations)
    theta_history = np.zeros(iterations,2)
    for it in range (iterations):
        prediction = np.dot(x,theta)
        theta = theta - (1/m) * learning_rate * (x.T.dot(prediction-y))
        theta_history[it:] = theta.T
        cost_history[it] = cal_cost(theta,x,y)

    return theta,cost_history,theta_history

def main():
    cal_cost()

if __name__ == "__main__":
    main()
