import linear_algebra

class neural_net():
     def __init__(self, n: float, w0: list, estimulo: list, maxInterator: int):
          self.n = n
          self.w0 = w0
          self.estimulo = estimulo
          self.maxInterator = maxInterator

     def fit(self):
          while(self.maxInterator != 0):
               similarity = linear_algebra.matriz_multi(self.w0, self.estimulo)
               erro = linear_algebra.matriz_sum(self.estimulo, similarity, isSub=True) 
               w1 = linear_algebra.matriz_multi(linear_algebra.matriz_multi_scalar(erro, self.n), linear_algebra.transposta(self.estimulo))
               self.w0 = linear_algebra.matriz_sum(self.w0, w1)
               self.maxInterator -= 1

               if(linear_algebra.acceptable_matrix(erro, limit_lower=-0.0001, limit_upper=0.0001)):
                    print(erro)
                    break     
     
     def predict(self, estimulo: list):
          return linear_algebra.matriz_multi(self.w0, estimulo)
