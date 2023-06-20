from Widrow_Hoff_networking import neural_net

n = 0.2

w0 = [[0, 0, 0, 0], 
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

estimulo =  [[-1, 1], 
            [-1,-1],
            [1, -1],
            [-1, 1]]


model = neural_net(n, w0, estimulo, 24)

model.fit()
print(model.predict(estimulo))