import numpy as np
#testing dat(X,Y)
x = np.array([[1,-1],[-1,1],[-1,2],[2,-1],[3,1]])
y = np.array([1,1,1,-1,-1])
#print(zip(x,y))
x1 = np.concatenate([x, np.ones((x.shape[0],1))], axis=1)
w = np.random.random(x.shape[1]+1)
#print(w)
xt = x1.transpose()
#print(xt)
#shuffling i,j parallel values
# for i,j in zip(x,y):
#     np.random.shuffle(x)
#     np.random.shuffle(y)
def shuffle(x,y):
    z = np.array(list(zip(x,y)))
    #print(z)
    np.random.shuffle(z)
    #unzipping values
    x , y = np.array(list(zip(*z)))
    return (x,y)

y1=(w.dot(xt))

mul_ = np.multiply(y1, y)
#print(mul_)

#w_update = []
for i in range(len(y1)):
    if (mul_[i] < 0):
        # print(w_update)
        # print("---pre-----")
        # print(np.dot(y.reshape(1,len(y)) ,(x1)))
        # print("---dot-----")
        #w_update = w + np.dot(y.reshape(1,len(y)) ,(x1))
        w_update = w+y[i] * x1[i]
        #print(w_update)
        # print("--------")
        x1 , y = shuffle(x1,y)

print(w_update)