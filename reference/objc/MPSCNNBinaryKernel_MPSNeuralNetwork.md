# `MPSCNNBinaryKernel`

- Image: [`/System/Library/Frameworks/MetalPerformanceShaders.framework/Frameworks/MPSNeuralNetwork.framework/MPSNeuralNetwork`](../userland/System__Library__Frameworks__MetalPerformanceShaders.framework__Frameworks__MPSNeuralNetwork.framework__MPSNeuralNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSKernel`
- 33 instance variables, 26 properties, 88 instance methods, 0 class methods

## Instance variables

```
{?="x"q"y"q"z"q} _primaryOffset;
{?="x"q"y"q"z"q} _secondaryOffset;
{?="origin"{?="x"Q"y"Q"z"Q}"size"{?="width"Q"height"Q"depth"Q}} _clipRect;
Q _destinationFeatureChannelOffset;
Q _primarySourceFeatureChannelOffset;
Q _secondarySourceFeatureChannelOffset;
Q _primarySourceFeatureChannelMaxCount;
Q _secondarySourceFeatureChannelMaxCount;
@"MPSExternalCNNBinary" _plugin;
B _pluginSupportsBatchEncode;
Q _primaryKernelWidth;
Q _primaryKernelHeight;
Q _secondaryKernelWidth;
Q _secondaryKernelHeight;
Q _primaryStrideInPixelsX;
Q _primaryStrideInPixelsY;
Q _secondaryStrideInPixelsX;
Q _secondaryStrideInPixelsY;
Q _primaryDilationRateX;
Q _primaryDilationRateY;
Q _secondaryDilationRateX;
Q _secondaryDilationRateY;
B _isBackwards;
B _supportsBroadcasting;
@"<MPSNNPadding>" _padding;
Q _primaryEdgeMode;
Q _secondaryEdgeMode;
i _checkFlags;
^? _encode;
^? _batchEncode;
^v _encodeData;
@"<MPSImageAllocator>" _destinationImageAllocator;
Q _pluginOptions;
```

## Properties

```
@property (T{?=qqq},N,V_primaryOffset) primaryOffset;
@property (T{?=qqq},N,V_secondaryOffset) secondaryOffset;
@property (T{?={?=QQQ}{?=QQQ}},N,V_clipRect) clipRect;
@property (TQ,N,V_destinationFeatureChannelOffset) destinationFeatureChannelOffset;
@property (TQ,N,V_primarySourceFeatureChannelOffset) primarySourceFeatureChannelOffset;
@property (TQ,N,V_secondarySourceFeatureChannelOffset) secondarySourceFeatureChannelOffset;
@property (TQ,N,V_primarySourceFeatureChannelMaxCount) primarySourceFeatureChannelMaxCount;
@property (TQ,N,V_secondarySourceFeatureChannelMaxCount) secondarySourceFeatureChannelMaxCount;
@property (TQ,N,V_primaryEdgeMode) primaryEdgeMode;
@property (TQ,N,V_secondaryEdgeMode) secondaryEdgeMode;
@property (TQ,R,N,V_primaryKernelWidth) primaryKernelWidth;
@property (TQ,R,N,V_primaryKernelHeight) primaryKernelHeight;
@property (TQ,R,N,V_secondaryKernelWidth) secondaryKernelWidth;
@property (TQ,R,N,V_secondaryKernelHeight) secondaryKernelHeight;
@property (TQ,N,V_primaryStrideInPixelsX) primaryStrideInPixelsX;
@property (TQ,N,V_primaryStrideInPixelsY) primaryStrideInPixelsY;
@property (TQ,N,V_secondaryStrideInPixelsX) secondaryStrideInPixelsX;
@property (TQ,N,V_secondaryStrideInPixelsY) secondaryStrideInPixelsY;
@property (TQ,R,N,V_primaryDilationRateX) primaryDilationRateX;
@property (TQ,R,N,V_primaryDilationRateY) primaryDilationRateY;
@property (TQ,R,N,V_secondaryDilationRateX) secondaryDilationRateX;
@property (TQ,R,N,V_secondaryDilationRateY) secondaryDilationRateY;
@property (TB,R,N,V_isBackwards) isBackwards;
@property (TB,R,N) isStateModified;
@property (T@"<MPSNNPadding>",&,N,V_padding) padding;
@property (T@"<MPSImageAllocator>",&,N,V_destinationImageAllocator) destinationImageAllocator;
```

## Instance methods

```
-[MPSCNNBinaryKernel padding];
-[MPSCNNBinaryKernel initWithDevice:];
-[MPSCNNBinaryKernel debugDescription];
-[MPSCNNBinaryKernel maxBatchSize];
-[MPSCNNBinaryKernel init];
-[MPSCNNBinaryKernel dealloc];
-[MPSCNNBinaryKernel setPadding:];
-[MPSCNNBinaryKernel plugin];
-[MPSCNNBinaryKernel copyWithZone:device:];
-[MPSCNNBinaryKernel initWithCoder:device:];
-[MPSCNNBinaryKernel encodeWithCoder:];
-[MPSCNNBinaryKernel isResultStateReusedAcrossBatch];
-[MPSCNNBinaryKernel setPlugin:];
-[MPSCNNBinaryKernel clipRect];
-[MPSCNNBinaryKernel setClipRect:];
-[MPSCNNBinaryKernel encodeBatchToCommandBuffer:primaryImages:secondaryImages:destinationImages:];
-[MPSCNNBinaryKernel encodeToCommandBuffer:primaryImage:secondaryImage:destinationImage:];
-[MPSCNNBinaryKernel setDestinationFeatureChannelOffset:];
-[MPSCNNBinaryKernel setPrimaryOffset:];
-[MPSCNNBinaryKernel setSecondaryEdgeMode:];
-[MPSCNNBinaryKernel setSecondaryOffset:];
-[MPSCNNBinaryKernel setSecondaryStrideInPixelsX:];
-[MPSCNNBinaryKernel setSecondaryStrideInPixelsY:];
-[MPSCNNBinaryKernel secondaryOffset];
-[MPSCNNBinaryKernel primaryEdgeMode];
-[MPSCNNBinaryKernel secondaryEdgeMode];
-[MPSCNNBinaryKernel destinationImageAllocator];
-[MPSCNNBinaryKernel setDestinationImageAllocator:];
-[MPSCNNBinaryKernel encodeToCommandEncoder:commandBuffer:primaryImage:secondaryImage:destinationImage:];
-[MPSCNNBinaryKernel primaryOffset];
-[MPSCNNBinaryKernel primarySourceRegionForDestinationSize:];
-[MPSCNNBinaryKernel secondarySourceRegionForDestinationSize:];
-[MPSCNNBinaryKernel setPrimaryEdgeMode:];
-[MPSCNNBinaryKernel destinationFeatureChannelOffset];
-[MPSCNNBinaryKernel isStateModified];
-[MPSCNNBinaryKernel appendBatchBarrier];
-[MPSCNNBinaryKernel batchEncodingStorageSizeForPrimaryImage:secondaryImage:sourceStates:destinationImage:];
-[MPSCNNBinaryKernel copyToBinaryGradientState:primaryImage:secondaryImage:sourceStates:destinationImage:];
-[MPSCNNBinaryKernel destinationImageDescriptorForSourceImages:sourceStates:];
-[MPSCNNBinaryKernel destinationImageDescriptorForSourceImages:sourceStates:paddingMethod:primaryOffset:secondaryOffset:kernelOffset:];
-[MPSCNNBinaryKernel encodeBatchToCommandBuffer:primaryImages:secondaryImages:];
-[MPSCNNBinaryKernel encodeBatchToCommandBuffer:primaryImages:secondaryImages:destinationStates:destinationStateIsTemporary:];
-[MPSCNNBinaryKernel encodeBatchToCommandBuffer:primaryImages:secondaryImages:inStates:];
-[MPSCNNBinaryKernel encodeBatchToCommandBuffer:primaryImages:secondaryImages:inStates:destinationImages:];
-[MPSCNNBinaryKernel encodeBatchToCommandEncoder:commandBuffer:primaryImages:secondaryImages:];
-[MPSCNNBinaryKernel encodeBatchToCommandEncoder:commandBuffer:primaryImages:secondaryImages:destinationImages:];
-[MPSCNNBinaryKernel encodeBatchToCommandEncoder:commandBuffer:primaryImages:secondaryImages:destinationStates:destinationStateIsTemporary:];
-[MPSCNNBinaryKernel encodeBatchToCommandEncoder:commandBuffer:primaryImages:secondaryImages:inStates:];
-[MPSCNNBinaryKernel encodeBatchToCommandEncoder:commandBuffer:primaryImages:secondaryImages:inStates:destinationImages:];
-[MPSCNNBinaryKernel encodeInternalBatchToCommandEncoder:commandBuffer:primaryImages:secondaryImages:inStates:destinationImages:clipRect:];
-[MPSCNNBinaryKernel encodeInternalToCommandEncoder:commandBuffer:primaryImage:secondaryImage:inState:destinationImage:subBatchIndex:batchSize:clipRect:];
-[MPSCNNBinaryKernel encodeToCommandBuffer:primaryImage:secondaryImage:];
-[MPSCNNBinaryKernel encodeToCommandBuffer:primaryImage:secondaryImage:destinationState:destinationStateIsTemporary:];
-[MPSCNNBinaryKernel encodeToCommandBuffer:primaryImage:secondaryImage:inState:destinationImage:];
-[MPSCNNBinaryKernel encodeToCommandEncoder:commandBuffer:primaryImage:secondaryImage:];
-[MPSCNNBinaryKernel encodeToCommandEncoder:commandBuffer:primaryImage:secondaryImage:destinationState:destinationStateIsTemporary:];
-[MPSCNNBinaryKernel encodeToCommandEncoder:commandBuffer:primaryImage:secondaryImage:inState:];
-[MPSCNNBinaryKernel encodeToCommandEncoder:commandBuffer:primaryImage:secondaryImage:inState:destinationImage:];
-[MPSCNNBinaryKernel encodeToCommandEncoder:commandBuffer:primaryImage:secondaryImage:inState:destinationImage:subBatchIndex:batchSize:];
-[MPSCNNBinaryKernel encodingStorageSizeForPrimaryImage:secondaryImage:sourceStates:destinationImage:];
-[MPSCNNBinaryKernel filterHandlesPlugin];
-[MPSCNNBinaryKernel isBackwards];
-[MPSCNNBinaryKernel primaryDilationRateX];
-[MPSCNNBinaryKernel primaryDilationRateY];
-[MPSCNNBinaryKernel primaryKernelHeight];
-[MPSCNNBinaryKernel primaryKernelWidth];
-[MPSCNNBinaryKernel primarySourceFeatureChannelMaxCount];
-[MPSCNNBinaryKernel primarySourceFeatureChannelOffset];
-[MPSCNNBinaryKernel primaryStrideInPixelsX];
-[MPSCNNBinaryKernel primaryStrideInPixelsY];
-[MPSCNNBinaryKernel resultStateBatchForPrimaryImage:secondaryImage:sourceStates:destinationImage:];
-[MPSCNNBinaryKernel resultStateForPrimaryImage:secondaryImage:sourceStates:destinationImage:];
-[MPSCNNBinaryKernel secondaryDilationRateX];
-[MPSCNNBinaryKernel secondaryDilationRateY];
-[MPSCNNBinaryKernel secondaryKernelHeight];
-[MPSCNNBinaryKernel secondaryKernelWidth];
-[MPSCNNBinaryKernel secondarySourceFeatureChannelMaxCount];
-[MPSCNNBinaryKernel secondarySourceFeatureChannelOffset];
-[MPSCNNBinaryKernel secondaryStrideInPixelsX];
-[MPSCNNBinaryKernel secondaryStrideInPixelsY];
-[MPSCNNBinaryKernel setPrimarySourceFeatureChannelMaxCount:];
-[MPSCNNBinaryKernel setPrimarySourceFeatureChannelOffset:];
-[MPSCNNBinaryKernel setPrimaryStrideInPixelsX:];
-[MPSCNNBinaryKernel setPrimaryStrideInPixelsY:];
-[MPSCNNBinaryKernel setSecondarySourceFeatureChannelMaxCount:];
-[MPSCNNBinaryKernel setSecondarySourceFeatureChannelOffset:];
-[MPSCNNBinaryKernel temporaryResultStateBatchForCommandBuffer:primaryImage:secondaryImage:sourceStates:destinationImage:];
-[MPSCNNBinaryKernel temporaryResultStateForCommandBuffer:primaryImage:secondaryImage:sourceStates:destinationImage:];
```
