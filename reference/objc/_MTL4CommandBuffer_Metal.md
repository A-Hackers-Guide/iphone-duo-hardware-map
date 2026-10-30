# `_MTL4CommandBuffer`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTL4CommandBufferGGDSPI`
- 10 instance variables, 12 properties, 43 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
Q _globalTraceObjectID;
Q _labelTraceID;
@"<MTL4CommandAllocator>" _commandAllocator;
@"NSMutableArray" _mlCommandEncoders;
@"<MTLLogState>" _logState;
@"NSMutableArray" _feedbackHandlers;
@"<MTLBuffer>" _privateData;
Q _privateDataOffset;
Q _currentGeneration;
```

## Properties

```
@property (TQ,R,V_globalTraceObjectID) globalTraceObjectID;
@property (T@"<MTLLogState>",&,N,V_logState) logState;
@property (TQ,R,N,V_currentGeneration) currentGeneration;
@property (T@"<MTLBuffer>",&,N,V_privateData) privateData;
@property (TQ,N,V_privateDataOffset) privateDataOffset;
@property (T@"<MTL4CommandAllocator>",R,N,V_commandAllocator) commandAllocator;
@property (T@"<MTLDevice>",R,V_device) device;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTL4CommandBuffer setPrivateDataOffset:];
-[_MTL4CommandBuffer useInternalResidencySet:];
-[_MTL4CommandBuffer pushDebugGroup:];
-[_MTL4CommandBuffer initWithDevice:];
-[_MTL4CommandBuffer sampledRenderCommandEncoderWithDescriptor:programInfoBuffer:capacity:];
-[_MTL4CommandBuffer setPrivateData:];
-[_MTL4CommandBuffer useResidencySet:];
-[_MTL4CommandBuffer privateData];
-[_MTL4CommandBuffer privateDataOffset];
-[_MTL4CommandBuffer useResidencySets:count:];
-[_MTL4CommandBuffer popDebugGroup];
-[_MTL4CommandBuffer encodeSignalEvent:value:];
-[_MTL4CommandBuffer useInternalResidencySets:count:];
-[_MTL4CommandBuffer device];
-[_MTL4CommandBuffer computeCommandEncoder];
-[_MTL4CommandBuffer globalTraceObjectID];
-[_MTL4CommandBuffer dealloc];
-[_MTL4CommandBuffer encodeWaitForEvent:value:];
-[_MTL4CommandBuffer encodeWaitForEvent:value:timeout:];
-[_MTL4CommandBuffer setLogState:];
-[_MTL4CommandBuffer currentGeneration];
-[_MTL4CommandBuffer logState];
-[_MTL4CommandBuffer renderCommandEncoderWithDescriptor:];
-[_MTL4CommandBuffer writeTimestampIntoHeap:atIndex:];
-[_MTL4CommandBuffer beginCommandBufferWithAllocator:];
-[_MTL4CommandBuffer beginCommandBufferWithAllocator:options:];
-[_MTL4CommandBuffer endCommandBuffer];
-[_MTL4CommandBuffer machineLearningCommandEncoder];
-[_MTL4CommandBuffer renderCommandEncoderWithDescriptor:options:];
-[_MTL4CommandBuffer resolveCounterHeap:withRange:intoBuffer:waitFence:updateFence:];
-[_MTL4CommandBuffer addFeedbackHandler:];
-[_MTL4CommandBuffer clearFeedbackHandlers];
-[_MTL4CommandBuffer clearMLCommandEncoderList];
-[_MTL4CommandBuffer commandAllocator];
-[_MTL4CommandBuffer computeCommandEncoderWithSubstreamCount:];
-[_MTL4CommandBuffer feedbackHandlers];
-[_MTL4CommandBuffer mlCommandEncoders];
-[_MTL4CommandBuffer registerMLEncoder:];
-[_MTL4CommandBuffer resetCommandBuffer];
-[_MTL4CommandBuffer resolveCounterHeap:withRange:intoBuffer:atOffset:waitFence:updateFence:];
-[_MTL4CommandBuffer sampledComputeCommandEncoder:capacity:];
-[_MTL4CommandBuffer setUpPrivateData:];
-[_MTL4CommandBuffer setupShaderLoggingWithLogState:allocator:];
```
