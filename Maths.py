import math

def sigmoid(value):
    return 1/(1+(math.e**(-value)))

class node:
    value = 0
    weights = []
    bias = 0
    def compute(self, lastNodes):
        additionOfNodes = 0
        onNode = 0
        for currentNode in lastNodes:
            additionOfNodes += currentNode.value*self.weights[onNode]
            onNode += 1
        return sigmoid(additionOfNodes+self.bias)

class layer:
    nodes = []
    def compute(self, lastLayer):
        for currentNode in self.nodes:
            currentNode.value = currentNode.compute(lastLayer.nodes)

class network:
    layers = []
    def compute(self):
        onLayer = 0
        for currentLayer in self.layers:
            if onLayer != 0:
                currentLayer.compute(self.layers[onLayer-1])
            onLayer += 1

def costOnNode(nodeValue, shouldBe):
    return (nodeValue - shouldBe)**2

def cost(outputNodes, shouldBe):
    totalCost = 0
    onNode = 0
    for currentNode in outputNodes:
        totalCost += costOnNode(currentNode.value, shouldBe[onNode])
        onNode += 1
    return totalCost

def test2():
    myNetwork = network()
    myNetwork.layers = [layer(),layer()]
    myNetwork.layers[0].nodes = [node(),node(),node()]
    myNetwork.layers[0].nodes[0].value = 1
    myNetwork.layers[0].nodes[1].value = 1
    myNetwork.layers[0].nodes[2].value = 0

    myNetwork.layers[1].nodes = [node(),node(),node()]
    myNetwork.layers[1].nodes[0].weights = [1,1,1]
    myNetwork.layers[1].nodes[1].weights = [0,0,1]
    myNetwork.layers[1].nodes[2].weights = [0,0,1]
    myNetwork.layers[1].nodes[1].bias = 100

    myNetwork.compute()

    for i in myNetwork.layers[1].nodes:
        print(str(i.value) + " - " + str(costOnNode(i.value, 1)))
    print()
    print(cost(myNetwork.layers[1].nodes,[1,1,1]))
    
        
def test():
    layer1 = layer()
    layer1.nodes = [node(),node(),node()]
    layer1.nodes[0].value = 1
    layer1.nodes[1].value = 1
    layer1.nodes[2].value = 0

    layer2 = layer()
    layer2.nodes = [node(),node(),node()]
    layer2.nodes[0].weights = [1,1,1]
    layer2.nodes[1].weights = [0,0,1]
    layer2.nodes[2].weights = [0,0,1]

    layer2.nodes[1].bias = 100
    
    layer2.compute(layer1)
    
    for i in layer2.nodes:
        print(i.value)
    
