# `MPSLSTMDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSRNNDescriptor`
- 19 instance variables, 19 properties, 41 instance methods, 1 class methods

## Instance variables

```
B _memoryWeightsAreDiagonal;
B _coupleForgetGateToInputGate;
i _cellToOutputNeuronType;
f _cellToOutputNeuronParamA;
f _cellToOutputNeuronParamB;
f _cellToOutputNeuronParamC;
f _cellClipThreshold;
@"<MPSCNNConvolutionDataSource>" _inputGateInputWeights;
@"<MPSCNNConvolutionDataSource>" _inputGateRecurrentWeights;
@"<MPSCNNConvolutionDataSource>" _inputGateMemoryWeights;
@"<MPSCNNConvolutionDataSource>" _forgetGateInputWeights;
@"<MPSCNNConvolutionDataSource>" _forgetGateRecurrentWeights;
@"<MPSCNNConvolutionDataSource>" _forgetGateMemoryWeights;
@"<MPSCNNConvolutionDataSource>" _outputGateInputWeights;
@"<MPSCNNConvolutionDataSource>" _outputGateRecurrentWeights;
@"<MPSCNNConvolutionDataSource>" _outputGateMemoryWeights;
@"<MPSCNNConvolutionDataSource>" _cellGateInputWeights;
@"<MPSCNNConvolutionDataSource>" _cellGateRecurrentWeights;
@"<MPSCNNConvolutionDataSource>" _cellGateMemoryWeights;
```

## Properties

```
@property (Tf,N,V_cellClipThreshold) cellClipThreshold;
@property (TB,N,V_coupleForgetGateToInputGate) coupleForgetGateToInputGate;
@property (TB,N,V_memoryWeightsAreDiagonal) memoryWeightsAreDiagonal;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_inputGateInputWeights) inputGateInputWeights;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_inputGateRecurrentWeights) inputGateRecurrentWeights;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_inputGateMemoryWeights) inputGateMemoryWeights;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_forgetGateInputWeights) forgetGateInputWeights;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_forgetGateRecurrentWeights) forgetGateRecurrentWeights;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_forgetGateMemoryWeights) forgetGateMemoryWeights;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_outputGateInputWeights) outputGateInputWeights;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_outputGateRecurrentWeights) outputGateRecurrentWeights;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_outputGateMemoryWeights) outputGateMemoryWeights;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_cellGateInputWeights) cellGateInputWeights;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_cellGateRecurrentWeights) cellGateRecurrentWeights;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_cellGateMemoryWeights) cellGateMemoryWeights;
@property (Ti,N,V_cellToOutputNeuronType) cellToOutputNeuronType;
@property (Tf,N,V_cellToOutputNeuronParamA) cellToOutputNeuronParamA;
@property (Tf,N,V_cellToOutputNeuronParamB) cellToOutputNeuronParamB;
@property (Tf,N,V_cellToOutputNeuronParamC) cellToOutputNeuronParamC;
```

## Class methods

```
+[MPSLSTMDescriptor createLSTMDescriptorWithInputFeatureChannels:outputFeatureChannels:];
```

## Instance methods

```
-[MPSLSTMDescriptor init];
-[MPSLSTMDescriptor dealloc];
-[MPSLSTMDescriptor setCellGateInputWeights:];
-[MPSLSTMDescriptor setCellGateRecurrentWeights:];
-[MPSLSTMDescriptor setCellToOutputNeuronType:];
-[MPSLSTMDescriptor setForgetGateInputWeights:];
-[MPSLSTMDescriptor setForgetGateRecurrentWeights:];
-[MPSLSTMDescriptor setInputGateInputWeights:];
-[MPSLSTMDescriptor setInputGateRecurrentWeights:];
-[MPSLSTMDescriptor setOutputGateInputWeights:];
-[MPSLSTMDescriptor setOutputGateRecurrentWeights:];
-[MPSLSTMDescriptor setCellGateMemoryWeights:];
-[MPSLSTMDescriptor setCellToOutputNeuronParamA:];
-[MPSLSTMDescriptor setCellToOutputNeuronParamB:];
-[MPSLSTMDescriptor setCellToOutputNeuronParamC:];
-[MPSLSTMDescriptor setForgetGateMemoryWeights:];
-[MPSLSTMDescriptor setInputGateMemoryWeights:];
-[MPSLSTMDescriptor setOutputGateMemoryWeights:];
-[MPSLSTMDescriptor setCoupleForgetGateToInputGate:];
-[MPSLSTMDescriptor cellClipThreshold];
-[MPSLSTMDescriptor cellGateInputWeights];
-[MPSLSTMDescriptor cellGateMemoryWeights];
-[MPSLSTMDescriptor cellGateRecurrentWeights];
-[MPSLSTMDescriptor cellToOutputNeuronParamA];
-[MPSLSTMDescriptor cellToOutputNeuronParamB];
-[MPSLSTMDescriptor cellToOutputNeuronParamC];
-[MPSLSTMDescriptor cellToOutputNeuronType];
-[MPSLSTMDescriptor coupleForgetGateToInputGate];
-[MPSLSTMDescriptor forgetGateInputWeights];
-[MPSLSTMDescriptor forgetGateMemoryWeights];
-[MPSLSTMDescriptor forgetGateRecurrentWeights];
-[MPSLSTMDescriptor initWithInputFeatureChannels:outputFeatureChannels:];
-[MPSLSTMDescriptor inputGateInputWeights];
-[MPSLSTMDescriptor inputGateMemoryWeights];
-[MPSLSTMDescriptor inputGateRecurrentWeights];
-[MPSLSTMDescriptor memoryWeightsAreDiagonal];
-[MPSLSTMDescriptor outputGateInputWeights];
-[MPSLSTMDescriptor outputGateMemoryWeights];
-[MPSLSTMDescriptor outputGateRecurrentWeights];
-[MPSLSTMDescriptor setCellClipThreshold:];
-[MPSLSTMDescriptor setMemoryWeightsAreDiagonal:];
```
