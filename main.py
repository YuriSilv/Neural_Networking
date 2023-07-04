from neural_nets import *
import linear_algebra

if __name__ == "__main__":

     """n = 0.2

     w0 = [[0, 0, 0, 0], 
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]

     estimulo =  [[-1, 1], 
               [-1,-1],
               [1, -1],
               [-1, 1]]


     model = associativa(n, w0, estimulo, 24)

     model.fit()
     print(model.predict(estimulo))"""

     X_atributos = [[1, 1, 0, 0, 1, 1, 0, 0, 0], 
                    [0, 0, 0, 1, 0, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 1, 1, 1, 1, 0 ,1],
                    [1, 1, 1, 0, 0, 0, 0, 1, 0],
                    [1, 0, 1, 0, 1, 1, 1, 0, 0]]

     T_categorias =  [[0, 0, 0, 0, 0, 0, 1, 1, 1],
                      [1, 1, 1, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 1, 1, 0, 0, 0]]
     
     w0 = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
     
     n = 0.01

     model = Adaline_logistica(n, X_atributos, T_categorias, 30000, 6, 3)

     model.fit()
     
     linear_algebra.print_matrix(linear_algebra.transposta(model.organismo))