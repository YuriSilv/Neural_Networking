import linear_algebra

class associativa():
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


class Adaline():
     def __init__(self, n: float, x_atr: list, t_res: list, maxInterator: int):
          self.n = n
          self.w0 = linear_algebra.create_matrix(6, 3, randomize=True)
          self.x_atr = x_atr
          self.t_res = t_res
          self.maxInterator = maxInterator
          linear_algebra.print_matrix(self.w0)


     def fit(self):
          while(self.maxInterator != 0):
               organismo = linear_algebra.matriz_multi(linear_algebra.transposta(self.w0), self.x_atr)
               erro_matriz = linear_algebra.matriz_sum(self.t_res, organismo, isSub=True)
               print(f'Erro e = {linear_algebra.calcular_erro_abs(erro_matriz)}')
               delta_w = linear_algebra.matriz_multi_scalar(linear_algebra.matriz_multi(self.x_atr, linear_algebra.transposta(erro_matriz)), self.n)
               self.w0 = linear_algebra.matriz_sum(self.w0, delta_w)
               self.maxInterator -= 1

               if(linear_algebra.acceptable_matrix(erro_matriz, limit_lower=-0.0001, limit_upper=0.0001)):
                    print(erro_matriz)
                    break     
     
     def predict(self, estimulo: list):
          return linear_algebra.matriz_multi(self.w0, estimulo)