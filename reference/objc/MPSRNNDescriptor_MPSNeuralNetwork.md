# `MPSRNNDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _useLayerInputUnitTransformMode;
B _useFloat32Weights;
Q _inputFeatureChannels;
Q _outputFeatureChannels;
@"<MPSCNNConvolutionDataSource>" _inputTransform;
@"<MPSCNNConvolutionDataSource>" _outputTransform;
@"<MPSCNNConvolutionDataSource>" _recurrentOutputTransform;
Q _layerSequenceDirection;
Q _internalKernelSelector;
```

## Properties

```
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_inputTransform) inputTransform;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_outputTransform) outputTransform;
@property (T@"<MPSCNNConvolutionDataSource>",&,N,V_recurrentOutputTransform) recurrentOutputTransform;
@property (TQ,N,V_internalKernelSelector) internalKernelSelector;
@property (TQ,N,V_inputFeatureChannels) inputFeatureChannels;
@property (TQ,N,V_outputFeatureChannels) outputFeatureChannels;
@property (TB,N,V_useLayerInputUnitTransformMode) useLayerInputUnitTransformMode;
@property (TB,N,V_useFloat32Weights) useFloat32Weights;
@property (TQ,N,V_layerSequenceDirection) layerSequenceDirection;
```

## Instance methods

```
-[MPSRNNDescriptor init];
-[MPSRNNDescriptor dealloc];
-[MPSRNNDescriptor outputTransform];
-[MPSRNNDescriptor inputTransform];
-[MPSRNNDescriptor setInputTransform:];
-[MPSRNNDescriptor inputFeatureChannels];
-[MPSRNNDescriptor outputFeatureChannels];
-[MPSRNNDescriptor setUseFloat32Weights:];
-[MPSRNNDescriptor setInputFeatureChannels:];
-[MPSRNNDescriptor setOutputFeatureChannels:];
-[MPSRNNDescriptor internalKernelSelector];
-[MPSRNNDescriptor layerSequenceDirection];
-[MPSRNNDescriptor recurrentOutputTransform];
-[MPSRNNDescriptor setInternalKernelSelector:];
-[MPSRNNDescriptor setLayerSequenceDirection:];
-[MPSRNNDescriptor setOutputTransform:];
-[MPSRNNDescriptor setRecurrentOutputTransform:];
-[MPSRNNDescriptor setUseLayerInputUnitTransformMode:];
-[MPSRNNDescriptor useFloat32Weights];
-[MPSRNNDescriptor useLayerInputUnitTransformMode];
```
