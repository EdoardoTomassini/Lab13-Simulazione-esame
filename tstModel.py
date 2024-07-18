from model.model import Model

mymodel = Model()
mymodel.buildGraph('circle', 2010)
print(mymodel.getGraphDetails())