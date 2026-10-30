# `_MTL4MachineLearningCommandEncoder`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTL4CommandEncoder`
- Protocols: `MTL4MachineLearningCommandEncoderGGDSPI`
- 6 instance variables, 9 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<MTL4MachineLearningPipelineState>" _currentPipelineState;
@"<MTL4ArgumentTable>" _currentArgumentTable;
^v _dispatchList;
@"<MTLSharedEvent>" _event;
@"<MTLSharedEvent>" _anePrePowerUpEvent;
Q _agentMask;
```

## Properties

```
@property (TQ,R,V_agentMask) agentMask;
@property (T@"NSString",C) label;
@property (T@"<MTL4CommandBuffer>",R,N) commandBuffer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) globalTraceObjectID;
@property (T@"<MTL4CommandAllocator>",R,N) commandAllocator;
```

## Instance methods

```
-[_MTL4MachineLearningCommandEncoder initWithDevice:];
-[_MTL4MachineLearningCommandEncoder endEncoding];
-[_MTL4MachineLearningCommandEncoder dealloc];
-[_MTL4MachineLearningCommandEncoder event];
-[_MTL4MachineLearningCommandEncoder setPipelineState:];
-[_MTL4MachineLearningCommandEncoder agentMask];
-[_MTL4MachineLearningCommandEncoder setArgumentTable:];
-[_MTL4MachineLearningCommandEncoder startEventValue];
-[_MTL4MachineLearningCommandEncoder dispatchNetworkWithIntermediatesHeap:];
-[_MTL4MachineLearningCommandEncoder encodeToCommandQueue:];
-[_MTL4MachineLearningCommandEncoder endEncodingWithSignalEvent:waitEvent:signalValue:waitValue:];
-[_MTL4MachineLearningCommandEncoder endEventValue];
-[_MTL4MachineLearningCommandEncoder initWithCommandBuffer:allocator:];
```
