# `MPSCNNKernel`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSKernel`
- 23 instance variables, 16 properties, 83 instance methods, 0 class methods

## Instance variables

```
{?="x"q"y"q"z"q} _offset;
{?="origin"{?="x"Q"y"Q"z"Q}"size"{?="width"Q"height"Q"depth"Q}} _clipRect;
Q _destinationFeatureChannelOffset;
Q _sourceFeatureChannelOffset;
Q _sourceFeatureChannelMaxCount;
@"MPSExternalCNNUnary" _plugin;
B _pluginSupportsBatchEncode;
Q _kernelWidth;
Q _kernelHeight;
Q _strideInPixelsX;
Q _strideInPixelsY;
Q _dilationRateX;
Q _dilationRateY;
@"<MPSNNPadding>" _padding;
Q _maxBatchSize;
B _isBackwards;
Q _edgeMode;
i _checkFlags;
^? _encode;
^? _batchEncode;
^v _encodeData;
Q _pluginOptions;
@"<MPSImageAllocator>" _destinationImageAllocator;
```

## Properties

```
@property (T{?=qqq},N,V_offset) offset;
@property (T{?={?=QQQ}{?=QQQ}},N,V_clipRect) clipRect;
@property (TQ,N,V_destinationFeatureChannelOffset) destinationFeatureChannelOffset;
@property (TQ,N,V_sourceFeatureChannelOffset) sourceFeatureChannelOffset;
@property (TQ,N,V_sourceFeatureChannelMaxCount) sourceFeatureChannelMaxCount;
@property (TQ,N,V_edgeMode) edgeMode;
@property (TQ,R,N,V_kernelWidth) kernelWidth;
@property (TQ,R,N,V_kernelHeight) kernelHeight;
@property (TQ,R,N,V_strideInPixelsX) strideInPixelsX;
@property (TQ,R,N,V_strideInPixelsY) strideInPixelsY;
@property (TQ,R,N,V_dilationRateX) dilationRateX;
@property (TQ,R,N,V_dilationRateY) dilationRateY;
@property (TB,R,N,V_isBackwards) isBackwards;
@property (TB,R,N) isStateModified;
@property (T@"<MPSNNPadding>",&,N,V_padding) padding;
@property (T@"<MPSImageAllocator>",&,N,V_destinationImageAllocator) destinationImageAllocator;
```

## Instance methods

```
-[MPSCNNKernel padding];
-[MPSCNNKernel initWithDevice:];
-[MPSCNNKernel debugDescription];
-[MPSCNNKernel maxBatchSize];
-[MPSCNNKernel init];
-[MPSCNNKernel dealloc];
-[MPSCNNKernel setPadding:];
-[MPSCNNKernel resultStateForSourceImage:sourceStates:destinationImage:];
-[MPSCNNKernel plugin];
-[MPSCNNKernel copyWithZone:device:];
-[MPSCNNKernel initWithCoder:device:];
-[MPSCNNKernel temporaryResultStateForCommandBuffer:sourceImage:sourceStates:destinationImage:];
-[MPSCNNKernel encodeWithCoder:];
-[MPSCNNKernel setOffset:];
-[MPSCNNKernel isResultStateReusedAcrossBatch];
-[MPSCNNKernel offset];
-[MPSCNNKernel setPlugin:];
-[MPSCNNKernel clipRect];
-[MPSCNNKernel setClipRect:];
-[MPSCNNKernel encodeBatchToCommandBuffer:sourceImages:destinationImages:];
-[MPSCNNKernel encodeBatchToCommandBuffer:sourceImages:destinationStates:destinationImages:];
-[MPSCNNKernel encodeToCommandBuffer:sourceImage:destinationImage:];
-[MPSCNNKernel encodeToCommandBuffer:sourceImage:destinationState:destinationImage:];
-[MPSCNNKernel kernelHeight];
-[MPSCNNKernel kernelWidth];
-[MPSCNNKernel resultStateBatchForSourceImage:sourceStates:destinationImage:];
-[MPSCNNKernel setDestinationFeatureChannelOffset:];
-[MPSCNNKernel setEdgeMode:];
-[MPSCNNKernel encodeBatchToCommandBuffer:sourceImages:];
-[MPSCNNKernel encodeBatchToCommandBuffer:sourceImages:destinationStates:destinationStateIsTemporary:];
-[MPSCNNKernel strideInPixelsX];
-[MPSCNNKernel strideInPixelsY];
-[MPSCNNKernel edgeMode];
-[MPSCNNKernel destinationImageAllocator];
-[MPSCNNKernel dilationRateX];
-[MPSCNNKernel dilationRateY];
-[MPSCNNKernel setDestinationImageAllocator:];
-[MPSCNNKernel sourceRegionForDestinationSize:];
-[MPSCNNKernel encodeToCommandEncoder:commandBuffer:sourceImage:destinationImage:];
-[MPSCNNKernel destinationFeatureChannelOffset];
-[MPSCNNKernel isStateModified];
-[MPSCNNKernel appendBatchBarrier];
-[MPSCNNKernel batchEncodingStorageSizeForSourceImage:sourceStates:destinationImage:];
-[MPSCNNKernel copyToGradientState:sourceImage:sourceStates:destinationImage:];
-[MPSCNNKernel destinationImageDescriptorForSourceImages:sourceStates:];
-[MPSCNNKernel destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:sourceOffset:];
-[MPSCNNKernel destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:sourceOffset:kernelOffset:];
-[MPSCNNKernel destinationImageWithCommandBuffer:sourceImage:inState:];
-[MPSCNNKernel encodeBatchToCommandBuffer:sourceImages:inStates:];
-[MPSCNNKernel encodeBatchToCommandBuffer:sourceImages:inStates:destinationImages:];
-[MPSCNNKernel encodeBatchToCommandBuffer:sourceImages:sourceStates:destinationStates:destinationStateIsTemporary:];
-[MPSCNNKernel encodeBatchToCommandEncoder:commandBuffer:sourceImages:];
-[MPSCNNKernel encodeBatchToCommandEncoder:commandBuffer:sourceImages:destinationImages:];
-[MPSCNNKernel encodeBatchToCommandEncoder:commandBuffer:sourceImages:destinationStates:destinationImages:];
-[MPSCNNKernel encodeBatchToCommandEncoder:commandBuffer:sourceImages:destinationStates:destinationStateIsTemporary:];
-[MPSCNNKernel encodeBatchToCommandEncoder:commandBuffer:sourceImages:inStates:];
-[MPSCNNKernel encodeBatchToCommandEncoder:commandBuffer:sourceImages:inStates:destinationImages:];
-[MPSCNNKernel encodeBatchToCommandEncoder:commandBuffer:sourceImages:sourceStates:destinationStates:destinationStateIsTemporary:];
-[MPSCNNKernel encodeInternalBatchToCommandEncoder:commandBuffer:sourceImages:inStates:destinationImages:clipRect:];
-[MPSCNNKernel encodeInternalToCommputeEncoder:commandBuffer:sourceImage:inState:destinationImage:subBatchIndex:batchSize:clipRect:shouldHandleCompoundImageNatively:];
-[MPSCNNKernel encodeToCommandBuffer:sourceImage:];
-[MPSCNNKernel encodeToCommandBuffer:sourceImage:destinationState:destinationStateIsTemporary:];
-[MPSCNNKernel encodeToCommandBuffer:sourceImage:inState:];
-[MPSCNNKernel encodeToCommandBuffer:sourceImage:inState:destinationImage:];
-[MPSCNNKernel encodeToCommandBuffer:sourceImage:inState:destinationImage:subBatchIndex:batchSize:];
-[MPSCNNKernel encodeToCommandBuffer:sourceImage:sourceState:destinationState:destinationStateIsTemporary:];
-[MPSCNNKernel encodeToCommandEncoder:commandBuffer:sourceImage:];
-[MPSCNNKernel encodeToCommandEncoder:commandBuffer:sourceImage:destinationState:destinationImage:];
-[MPSCNNKernel encodeToCommandEncoder:commandBuffer:sourceImage:destinationState:destinationStateIsTemporary:];
-[MPSCNNKernel encodeToCommandEncoder:commandBuffer:sourceImage:inState:];
-[MPSCNNKernel encodeToCommandEncoder:commandBuffer:sourceImage:inState:destinationImage:];
-[MPSCNNKernel encodeToCommandEncoder:commandBuffer:sourceImage:inState:destinationImage:subBatchIndex:batchSize:];
-[MPSCNNKernel encodeToCommandEncoder:commandBuffer:sourceImage:sourceState:destinationState:destinationStateIsTemporary:];
-[MPSCNNKernel encodingStorageSizeForSourceImage:sourceStates:destinationImage:];
-[MPSCNNKernel filterHandlesPlugin];
-[MPSCNNKernel isBackwards];
-[MPSCNNKernel pluginSupportsBatchEncode];
-[MPSCNNKernel setSourceFeatureChannelMaxCount:];
-[MPSCNNKernel setSourceFeatureChannelOffset:];
-[MPSCNNKernel sourceFeatureChannelMaxCount];
-[MPSCNNKernel sourceFeatureChannelOffset];
-[MPSCNNKernel sourcePositionOfTopLeftCornerOfFilterWindow];
-[MPSCNNKernel temporaryResultStateBatchForCommandBuffer:sourceImage:sourceStates:destinationImage:];
```
