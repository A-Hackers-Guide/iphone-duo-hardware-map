# `MPSRNNSingleGateDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSRNNDescriptor`
- 2 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"<MPSCNNConvolutionDataSource>" _inputWeights;
@"<MPSCNNConvolutionDataSource>" _recurrentWeights;
```

## Properties

```
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_inputWeights) inputWeights;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_recurrentWeights) recurrentWeights;
```

## Class methods

```
+[MPSRNNSingleGateDescriptor createRNNSingleGateDescriptorWithInputFeatureChannels:outputFeatureChannels:];
```

## Instance methods

```
-[MPSRNNSingleGateDescriptor init];
-[MPSRNNSingleGateDescriptor dealloc];
-[MPSRNNSingleGateDescriptor inputWeights];
-[MPSRNNSingleGateDescriptor setInputWeights:];
-[MPSRNNSingleGateDescriptor initWithInputFeatureChannels:outputFeatureChannels:];
-[MPSRNNSingleGateDescriptor recurrentWeights];
-[MPSRNNSingleGateDescriptor setRecurrentWeights:];
```
