# `MLNeuralNetworkMLComputeLayer`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 18 class methods

## Class methods

```
+[MLNeuralNetworkMLComputeLayer sigmoid];
+[MLNeuralNetworkMLComputeLayer softmax];
+[MLNeuralNetworkMLComputeLayer adamOptimizerWithLearningRate:beta1:beta2:epsilon:timeStep:];
+[MLNeuralNetworkMLComputeLayer batchNormLayerWithFeatureChannels:varianceEpsilon:gamma:beta:mean:variance:];
+[MLNeuralNetworkMLComputeLayer categoricalCrossEntropyLossWithNumberOfClasses:];
+[MLNeuralNetworkMLComputeLayer concatNDLayerWithAxis:];
+[MLNeuralNetworkMLComputeLayer convolutionalLayerWithKernelHeight:kernelWidth:inputChannels:outputChannels:strideInX:strideInY:dilationRateInX:dilationRateInY:nGroups:weight:bias:paddingPolicy:];
+[MLNeuralNetworkMLComputeLayer fullyConnectedLayerWithKernelWidth:kernelHeight:inputChannels:outputChannels:weight:bias:];
+[MLNeuralNetworkMLComputeLayer leakyRelu];
+[MLNeuralNetworkMLComputeLayer matMulLayerWithTransposesX:transposesY:];
+[MLNeuralNetworkMLComputeLayer meanSquaredErrorLoss];
+[MLNeuralNetworkMLComputeLayer poolingLayerWithKernelWidth:kernelHeight:strideInX:strideInY:paddingPolicy:poolingType:];
+[MLNeuralNetworkMLComputeLayer relu];
+[MLNeuralNetworkMLComputeLayer reluNLayerWithAlpha:beta:];
+[MLNeuralNetworkMLComputeLayer reshapeLayerWithChannelFirstOrderingAndTargetShape:];
+[MLNeuralNetworkMLComputeLayer sgdOptimizerWithLearningRate:momentum:];
+[MLNeuralNetworkMLComputeLayer transposeLayerWithAxes:];
+[MLNeuralNetworkMLComputeLayer uniDirectionalLSTMLayerWithInputSize:outputSize:inputWeightsData:recursionWeightsData:hasBias:biasTermsData:sequenceOutput:inputGateActivation:cellGateActivation:hiddenOutputActivation:];
```
