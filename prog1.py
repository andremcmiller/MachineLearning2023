import math
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

func = lambda x: x ** 4 + np.exp(-x)
func_der = lambda x: 4 * x ** 3 - np.exp(-x)

class tangents():
    def __init__(self, a, b, x1 = None, x2 = None, y1 = None, y2 = None, func = None, func_der = None, k = 0):
        self.a = a
        self.b = b
        self.func = func
        self.func_der = func_der
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.k = k
        
    def search(self):
        a1 = self.a
        b1 = self.b

        xx = np.linspace(0, 1, 1000)
        yy = self.func(xx)

        plt.figure(figsize=(10, 10))
        plt.xlim([self.x1,self.x2])
        plt.ylim([self.y1,self.y2])
        plt.plot(xx, yy)

        while abs(b1 - a1) > 0.0001:
            self.k = self.k+1
            print(self.k)
            if self.func_der(a1) >= 0:
                answer = a1
                return answer
                
            elif self.func_der(b1) <= 0:
                answer = b1
                return answer
                
            else:
                yy = self.func(a1) + self.func_der(a1) * (xx - a1)
                yyy = self.func(b1) + self.func_der(b1) * (xx - b1)
                plt.plot(xx, yy, '--', linewidth=1)
                plt.plot(xx, yyy, '--', linewidth=1)

                c1 = (self.func(a1) - self.func(b1) + b1 * self.func_der(b1) - a1 * self.func_der(a1)) / (self.func_der(b1) - self.func_der(a1))
                if self.func_der(c1) == 0:
                    answer = c1
                    return answer

                else:
                    if self.func_der(c1) > 0:
                        b1 = c1
                    if self.func_der(c1) < 0:
                        a1 = c1

        return c1 

result_1 = tangents(a = 0, b = 1, x1 = 0.8, x2 = 1.2, y1 = -0.05, y2 = 0.05, func = func, func_der = func_der)
print('Ответ:', result_1.search())