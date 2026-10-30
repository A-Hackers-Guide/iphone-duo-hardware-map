# `MPSConvolutionDataSourceWrapper`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MPSCNNConvolutionDataSource`
- 5 instance variables, 4 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"<MPSCNNConvolutionDataSource>" _dataSource;
@"MPSCNNConvolutionDescriptor" _convolution;
@"NSObject" _batchNorm;
@"MPSNNNeuronDescriptor" _neuron;
{atomic<long>="__a_"{__cxx_atomic_impl<long, std::__cxx_atomic_base_impl<long>>="__a_value"Aq}} _loadCount;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MPSConvolutionDataSourceWrapper wrapperForDataSource:];
```

## Instance methods

```
-[MPSConvolutionDataSourceWrapper initWithDataSource:];
-[MPSConvolutionDataSourceWrapper load];
-[MPSConvolutionDataSourceWrapper descriptor];
-[MPSConvolutionDataSourceWrapper debugDescription];
-[MPSConvolutionDataSourceWrapper initialize];
-[MPSConvolutionDataSourceWrapper label];
-[MPSConvolutionDataSourceWrapper dealloc];
-[MPSConvolutionDataSourceWrapper purge];
-[MPSConvolutionDataSourceWrapper dataType];
-[MPSConvolutionDataSourceWrapper respondsToSelector:];
-[MPSConvolutionDataSourceWrapper copyWithZone:];
-[MPSConvolutionDataSourceWrapper weights];
-[MPSConvolutionDataSourceWrapper biasTerms];
-[MPSConvolutionDataSourceWrapper lookupTableForUInt8Kernel];
-[MPSConvolutionDataSourceWrapper rangesForUInt8Kernel];
-[MPSConvolutionDataSourceWrapper updateWithCommandBuffer:gradientState:sourceState:];
-[MPSConvolutionDataSourceWrapper updateWithGradientState:sourceState:];
-[MPSConvolutionDataSourceWrapper weightsQuantizationType];
-[MPSConvolutionDataSourceWrapper appendBatchNorm:];
-[MPSConvolutionDataSourceWrapper appendNeuron:];
-[MPSConvolutionDataSourceWrapper appendNeuronDescriptor:];
-[MPSConvolutionDataSourceWrapper hasBatchNorm];
-[MPSConvolutionDataSourceWrapper neuronInfo];
```
