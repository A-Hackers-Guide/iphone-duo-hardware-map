# `MPSCNNMultiaryKernel`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSKernel`
- 11 instance variables, 7 properties, 88 instance methods, 0 class methods

## Instance variables

```
^{NNKernelSourceParams={?=qqq}QQQQQQQQQ} _srcInfo;
Q _srcCount;
{?="origin"{?="x"Q"y"Q"z"Q}"size"{?="width"Q"height"Q"depth"Q}} _clipRect;
Q _destinationFeatureChannelOffset;
B _isBackwards;
B _supportsBroadcasting;
@"<MPSNNPadding>" _padding;
@"<MPSImageAllocator>" _destinationImageAllocator;
i _checkFlags;
^? _batchEncode;
^v _encodeData;
```

## Properties

```
@property (TQ,R,N,V_srcCount) sourceCount;
@property (T{?={?=QQQ}{?=QQQ}},N,V_clipRect) clipRect;
@property (TQ,N,V_destinationFeatureChannelOffset) destinationFeatureChannelOffset;
@property (TB,R,N,V_isBackwards) isBackwards;
@property (TB,R,N) isStateModified;
@property (T@"<MPSNNPadding>",&,N,V_padding) padding;
@property (T@"<MPSImageAllocator>",&,N,V_destinationImageAllocator) destinationImageAllocator;
```

## Instance methods

```
-[MPSCNNMultiaryKernel padding];
-[MPSCNNMultiaryKernel initWithDevice:];
-[MPSCNNMultiaryKernel maxBatchSize];
-[MPSCNNMultiaryKernel dealloc];
-[MPSCNNMultiaryKernel setPadding:];
-[MPSCNNMultiaryKernel copyWithZone:device:];
-[MPSCNNMultiaryKernel initWithCoder:device:];
-[MPSCNNMultiaryKernel encodeWithCoder:];
-[MPSCNNMultiaryKernel setOffset:];
-[MPSCNNMultiaryKernel isResultStateReusedAcrossBatch];
-[MPSCNNMultiaryKernel offset];
-[MPSCNNMultiaryKernel clipRect];
-[MPSCNNMultiaryKernel setClipRect:];
-[MPSCNNMultiaryKernel encodeBatchToCommandBuffer:sourceImages:destinationImages:];
-[MPSCNNMultiaryKernel initWithDevice:sourceCount:];
-[MPSCNNMultiaryKernel kernelHeight];
-[MPSCNNMultiaryKernel kernelWidth];
-[MPSCNNMultiaryKernel setDestinationFeatureChannelOffset:];
-[MPSCNNMultiaryKernel setDilationRateX:];
-[MPSCNNMultiaryKernel setDilationRateY:];
-[MPSCNNMultiaryKernel setEdgeMode:];
-[MPSCNNMultiaryKernel setStrideInPixelsX:];
-[MPSCNNMultiaryKernel setStrideInPixelsY:];
-[MPSCNNMultiaryKernel setKernelWidth:];
-[MPSCNNMultiaryKernel encodeBatchToCommandBuffer:sourceImages:];
-[MPSCNNMultiaryKernel encodeBatchToCommandBuffer:sourceImages:destinationStates:destinationStateIsTemporary:];
-[MPSCNNMultiaryKernel setKernelHeight:];
-[MPSCNNMultiaryKernel sourceCount];
-[MPSCNNMultiaryKernel offsetAtIndex:];
-[MPSCNNMultiaryKernel strideInPixelsX];
-[MPSCNNMultiaryKernel strideInPixelsY];
-[MPSCNNMultiaryKernel edgeMode];
-[MPSCNNMultiaryKernel destinationImageAllocator];
-[MPSCNNMultiaryKernel dilationRateX];
-[MPSCNNMultiaryKernel dilationRateY];
-[MPSCNNMultiaryKernel setDestinationImageAllocator:];
-[MPSCNNMultiaryKernel copyToGradientState:sourceImages:sourceStates:destinationImage:];
-[MPSCNNMultiaryKernel destinationFeatureChannelOffset];
-[MPSCNNMultiaryKernel isStateModified];
-[MPSCNNMultiaryKernel appendBatchBarrier];
-[MPSCNNMultiaryKernel destinationImageDescriptorForSourceImages:sourceStates:];
-[MPSCNNMultiaryKernel destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:];
-[MPSCNNMultiaryKernel dilationRateXatIndex:];
-[MPSCNNMultiaryKernel dilationRateYatIndex:];
-[MPSCNNMultiaryKernel edgeModeAtIndex:];
-[MPSCNNMultiaryKernel encodeBatchToCommandBuffer:sourceImages:inStates:destinationImages:];
-[MPSCNNMultiaryKernel encodeBatchToCommandBuffer:sourceImages:sourceStates:];
-[MPSCNNMultiaryKernel encodeBatchToCommandEncoder:commandBuffer:sourceImages:];
-[MPSCNNMultiaryKernel encodeBatchToCommandEncoder:commandBuffer:sourceImages:destinationImages:];
-[MPSCNNMultiaryKernel encodeBatchToCommandEncoder:commandBuffer:sourceImages:destinationStates:destinationStateIsTemporary:];
-[MPSCNNMultiaryKernel encodeBatchToCommandEncoder:commandBuffer:sourceImages:inStates:destinationImages:];
-[MPSCNNMultiaryKernel encodeBatchToCommandEncoder:commandBuffer:sourceImages:sourceStates:];
-[MPSCNNMultiaryKernel encodeInternalBatchToCommandEncoder:commandBuffer:sourceImages:inStates:destinationImages:clipRect:];
-[MPSCNNMultiaryKernel encodeToCommandBuffer:sourceImages:];
-[MPSCNNMultiaryKernel encodeToCommandBuffer:sourceImages:destinationImage:];
-[MPSCNNMultiaryKernel encodeToCommandBuffer:sourceImages:destinationState:destinationStateIsTemporary:];
-[MPSCNNMultiaryKernel encodeToCommandBuffer:sourceImages:inState:];
-[MPSCNNMultiaryKernel encodeToCommandBuffer:sourceImages:inState:destinationImage:];
-[MPSCNNMultiaryKernel encodeToCommandEncoder:commandBuffer:sourceImages:];
-[MPSCNNMultiaryKernel encodeToCommandEncoder:commandBuffer:sourceImages:destinationImage:];
-[MPSCNNMultiaryKernel encodeToCommandEncoder:commandBuffer:sourceImages:destinationState:destinationStateIsTemporary:];
-[MPSCNNMultiaryKernel encodeToCommandEncoder:commandBuffer:sourceImages:inState:];
-[MPSCNNMultiaryKernel encodeToCommandEncoder:commandBuffer:sourceImages:inState:destinationImage:];
-[MPSCNNMultiaryKernel isBackwards];
-[MPSCNNMultiaryKernel kernelHeightAtIndex:];
-[MPSCNNMultiaryKernel kernelWidthAtIndex:];
-[MPSCNNMultiaryKernel resultStateBatchForSourceImages:sourceStates:destinationImage:];
-[MPSCNNMultiaryKernel resultStateForSourceImages:sourceStates:destinationImage:];
-[MPSCNNMultiaryKernel setDilationRateX:atIndex:];
-[MPSCNNMultiaryKernel setDilationRateY:atIndex:];
-[MPSCNNMultiaryKernel setEdgeMode:atIndex:];
-[MPSCNNMultiaryKernel setKernelHeight:atIndex:];
-[MPSCNNMultiaryKernel setKernelWidth:atIndex:];
-[MPSCNNMultiaryKernel setOffset:atIndex:];
-[MPSCNNMultiaryKernel setSourceFeatureChannelMaxCount:];
-[MPSCNNMultiaryKernel setSourceFeatureChannelMaxCount:atIndex:];
-[MPSCNNMultiaryKernel setSourceFeatureChannelOffset:];
-[MPSCNNMultiaryKernel setSourceFeatureChannelOffset:atIndex:];
-[MPSCNNMultiaryKernel setStrideInPixelsX:atIndex:];
-[MPSCNNMultiaryKernel setStrideInPixelsY:atIndex:];
-[MPSCNNMultiaryKernel sourceFeatureChannelMaxCount];
-[MPSCNNMultiaryKernel sourceFeatureChannelMaxCountAtIndex:];
-[MPSCNNMultiaryKernel sourceFeatureChannelOffset];
-[MPSCNNMultiaryKernel sourceFeatureChannelOffsetAtIndex:];
-[MPSCNNMultiaryKernel strideInPixelsXatIndex:];
-[MPSCNNMultiaryKernel strideInPixelsYatIndex:];
-[MPSCNNMultiaryKernel temporaryResultStateBatchForCommandBuffer:sourceImages:sourceStates:destinationImage:];
-[MPSCNNMultiaryKernel temporaryResultStateForCommandBuffer:sourceImages:sourceStates:destinationImage:];
```
