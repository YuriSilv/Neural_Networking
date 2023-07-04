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


class Adaline_logistica():
     def __init__(self, n: float, x_atr: list, t_res: list, maxInterator: int, rows: int, cols: int):
          self.n = n
          self.w0 = linear_algebra.create_matrix(rows, cols, randomize=True)
          self.x_atr = x_atr
          self.t_res = t_res  
          self.maxInterator = maxInterator
          linear_algebra.print_matrix(self.w0)


     def fit(self):
          while(self.maxInterator != 0):
               self.organismo = linear_algebra.matriz_multi(linear_algebra.transposta(self.w0), self.x_atr)
               
               for i in range(len(self.organismo)):
                    for j in range(len(self.organismo[0])):
                         self.organismo[i][j] = round(linear_algebra.func_logistica(self.organismo[i][j]), 4)

               erro_matriz = linear_algebra.matriz_sum(self.t_res, self.organismo, isSub=True)
               print(f'Erro e = {linear_algebra.calcular_erro_abs(erro_matriz)} - Interação {self.maxInterator}')

               delta_w = linear_algebra.matriz_multi((linear_algebra.matriz_multi_scalar(self.x_atr, self.n)), 
                                                     (linear_algebra.transposta(
                                                       linear_algebra.hadamard_multi(
                                                       linear_algebra.hadamard_multi(erro_matriz, self.organismo), 
                                                       (linear_algebra.escalar_subtr(1, self.organismo))))))
               
               self.w0 = linear_algebra.matriz_sum(self.w0, delta_w)
               self.maxInterator -= 1

               if(linear_algebra.acceptable_matrix(erro_matriz, limit_lower=-0.0001, limit_upper=0.0001)):
                    print(erro_matriz)
                    break     
     
     def predict(self, estimulo: list):
          return linear_algebra.matriz_multi(self.w0, estimulo)