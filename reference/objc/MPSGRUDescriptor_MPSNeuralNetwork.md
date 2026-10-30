# `MPSGRUDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSRNNDescriptor`
- 9 instance variables, 9 properties, 21 instance methods, 1 class methods

## Instance variables

```
B _flipOutputGates;
f _gatePnormValue;
@"<MPSCNNConvolutionDataSource>" _inputGateInputWeights;
@"<MPSCNNConvolutionDataSource>" _inputGateRecurrentWeights;
@"<MPSCNNConvolutionDataSource>" _recurrentGateInputWeights;
@"<MPSCNNConvolutionDataSource>" _recurrentGateRecurrentWeights;
@"<MPSCNNConvolutionDataSource>" _outputGateInputWeights;
@"<MPSCNNConvolutionDataSource>" _outputGateInputGateWeights;
@"<MPSCNNConvolutionDataSource>" _outputGateRecurrentWeights;
```

## Properties

```
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_inputGateInputWeights) inputGateInputWeights;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_inputGateRecurrentWeights) inputGateRecurrentWeights;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_recurrentGateInputWeights) recurrentGateInputWeights;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_recurrentGateRecurrentWeights) recurrentGateRecurrentWeights;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_outputGateInputWeights) outputGateInputWeights;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_outputGateRecurrentWeights) outputGateRecurrentWeights;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_outputGateInputGateWeights) outputGateInputGateWeights;
@property (Tf,N,V_gatePnormValue) gatePnormValue;
@property (TB,N,V_flipOutputGates) flipOutputGates;
```

## Class methods

```
+[MPSGRUDescriptor createGRUDescriptorWithInputFeatureChannels:outputFeatureChannels:];
```

## Instance methods

```
-[MPSGRUDescriptor init];
-[MPSGRUDescriptor dealloc];
-[MPSGRUDescriptor setInputGateInputWeights:];
-[MPSGRUDescriptor setInputGateRecurrentWeights:];
-[MPSGRUDescriptor setOutputGateInputWeights:];
-[MPSGRUDescriptor setOutputGateRecurrentWeights:];
-[MPSGRUDescriptor flipOutputGates];
-[MPSGRUDescriptor gatePnormValue];
-[MPSGRUDescriptor initWithInputFeatureChannels:outputFeatureChannels:];
-[MPSGRUDescriptor inputGateInputWeights];
-[MPSGRUDescriptor inputGateRecurrentWeights];
-[MPSGRUDescriptor outputGateInputGateWeights];
-[MPSGRUDescriptor outputGateInputWeights];
-[MPSGRUDescriptor outputGateRecurrentWeights];
-[MPSGRUDescriptor recurrentGateInputWeights];
-[MPSGRUDescriptor recurrentGateRecurrentWeights];
-[MPSGRUDescriptor setFlipOutputGates:];
-[MPSGRUDescriptor setGatePnormValue:];
-[MPSGRUDescriptor setOutputGateInputGateWeights:];
-[MPSGRUDescriptor setRecurrentGateInputWeights:];
-[MPSGRUDescriptor setRecurrentGateRecurrentWeights:];
```
