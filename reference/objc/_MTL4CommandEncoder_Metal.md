# `_MTL4CommandEncoder`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTL4CommandEncoderGGDSPI`
- 5 instance variables, 10 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"<MTLDevice>" _device;
@"<MTL4CommandAllocator>" _commandAllocator;
Q _globalTraceObjectID;
Q _labelTraceID;
@"<MTL4CommandBuffer>" _commandBuffer;
```

## Properties

```
@property (T@"<MTL4CommandBuffer>",&,N,V_commandBuffer) commandBuffer;
@property (T@"<MTL4CommandAllocator>",R,N,V_commandAllocator) commandAllocator;
@property (T@"<MTLDevice>",R,V_device) device;
@property (TQ,R,V_globalTraceObjectID) globalTraceObjectID;
@property (Tq,R,N,GgetType) type;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_MTL4CommandEncoder insertDebugSignpost:];
-[_MTL4CommandEncoder pushDebugGroup:];
-[_MTL4CommandEncoder popDebugGroup];
-[_MTL4CommandEncoder device];
-[_MTL4CommandEncoder endEncoding];
-[_MTL4CommandEncoder globalTraceObjectID];
-[_MTL4CommandEncoder dealloc];
-[_MTL4CommandEncoder getType];
-[_MTL4CommandEncoder setCommandBuffer:];
-[_MTL4CommandEncoder commandBuffer];
-[_MTL4CommandEncoder updateFence:afterEncoderStages:];
-[_MTL4CommandEncoder barrierAfterEncoderStages:beforeEncoderStages:options:];
-[_MTL4CommandEncoder barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:];
-[_MTL4CommandEncoder barrierAfterQueueStages:beforeStages:options:];
-[_MTL4CommandEncoder barrierAfterQueueStages:beforeStages:visibilityOptions:];
-[_MTL4CommandEncoder barrierAfterStages:beforeQueueStages:options:];
-[_MTL4CommandEncoder barrierAfterStages:beforeQueueStages:visibilityOptions:];
-[_MTL4CommandEncoder commandAllocator];
-[_MTL4CommandEncoder commandBatchIdOffset];
-[_MTL4CommandEncoder commandBatchIdRangeMin:max:];
-[_MTL4CommandEncoder endEncodingAndRetrieveProgramAddressTable];
-[_MTL4CommandEncoder filterCounterRangeWithFirstBatch:lastBatch:filterIndex:];
-[_MTL4CommandEncoder initWithCommandAllocator:];
-[_MTL4CommandEncoder waitForFence:beforeEncoderStages:];
```
