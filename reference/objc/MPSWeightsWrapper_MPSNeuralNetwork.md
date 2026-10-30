# `MPSWeightsWrapper`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MPSCNNConvolutionDataSource`
- 4 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"<MPSCNNBatchNormalizationDataSource>" _dataSource;
@"<MPSCNNConvolutionDataSource>" _source;
{NeuronInfo="type"i"a"f"b"f"c"f"aData"@"NSData"} _info;
@"MPSCNNConvolutionDescriptor" _descriptor;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MPSWeightsWrapper load];
-[MPSWeightsWrapper descriptor];
-[MPSWeightsWrapper label];
-[MPSWeightsWrapper dealloc];
-[MPSWeightsWrapper purge];
-[MPSWeightsWrapper dataType];
-[MPSWeightsWrapper copyWithZone:];
-[MPSWeightsWrapper weights];
-[MPSWeightsWrapper biasTerms];
-[MPSWeightsWrapper lookupTableForUInt8Kernel];
-[MPSWeightsWrapper rangesForUInt8Kernel];
-[MPSWeightsWrapper initWithSource:neuronInfo:batchNorm:];
```
