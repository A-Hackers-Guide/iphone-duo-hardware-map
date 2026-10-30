# `MTL4ToolsCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTL4CommandEncoderGGDSPI`
- 2 instance variables, 8 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"<MTL4CommandBuffer>" _commandBuffer;
@"<MTL4CommandAllocator>" _commandAllocator;
```

## Properties

```
@property (T@"NSString",C) label;
@property (T@"<MTL4CommandBuffer>",R,N) commandBuffer;
@property (T@"<MTL4CommandAllocator>",R,N) commandAllocator;
@property (TQ,R) globalTraceObjectID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTL4ToolsCommandEncoder insertDebugSignpost:];
-[MTL4ToolsCommandEncoder pushDebugGroup:];
-[MTL4ToolsCommandEncoder popDebugGroup];
-[MTL4ToolsCommandEncoder label];
-[MTL4ToolsCommandEncoder setLabel:];
-[MTL4ToolsCommandEncoder endEncoding];
-[MTL4ToolsCommandEncoder globalTraceObjectID];
-[MTL4ToolsCommandEncoder dealloc];
-[MTL4ToolsCommandEncoder commandBuffer];
-[MTL4ToolsCommandEncoder updateFence:afterEncoderStages:];
-[MTL4ToolsCommandEncoder barrierAfterEncoderStages:beforeEncoderStages:options:];
-[MTL4ToolsCommandEncoder barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:];
-[MTL4ToolsCommandEncoder barrierAfterQueueStages:beforeStages:options:];
-[MTL4ToolsCommandEncoder barrierAfterQueueStages:beforeStages:visibilityOptions:];
-[MTL4ToolsCommandEncoder barrierAfterStages:beforeQueueStages:options:];
-[MTL4ToolsCommandEncoder barrierAfterStages:beforeQueueStages:visibilityOptions:];
-[MTL4ToolsCommandEncoder commandAllocator];
-[MTL4ToolsCommandEncoder commandBatchIdOffset];
-[MTL4ToolsCommandEncoder commandBatchIdRangeMin:max:];
-[MTL4ToolsCommandEncoder endEncodingAndRetrieveProgramAddressTable];
-[MTL4ToolsCommandEncoder filterCounterRangeWithFirstBatch:lastBatch:filterIndex:];
-[MTL4ToolsCommandEncoder initWithBaseObject:parent:];
-[MTL4ToolsCommandEncoder waitForFence:beforeEncoderStages:];
-[MTL4ToolsCommandEncoder initWithCommandEncoder:commandBuffer:];
```
