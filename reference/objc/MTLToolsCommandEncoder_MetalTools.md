# `MTLToolsCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLCommandEncoder`
- 1 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"<MTLToolsRetainingContainer>" _commandBuffer;
```

## Properties

```
@property (T@"<MTLToolsRetainingContainer>",R,N,V_commandBuffer) commandBuffer;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLToolsCommandEncoder insertDebugSignpost:];
-[MTLToolsCommandEncoder pushDebugGroup:];
-[MTLToolsCommandEncoder popDebugGroup];
-[MTLToolsCommandEncoder label];
-[MTLToolsCommandEncoder setLabel:];
-[MTLToolsCommandEncoder endEncoding];
-[MTLToolsCommandEncoder globalTraceObjectID];
-[MTLToolsCommandEncoder commandBuffer];
-[MTLToolsCommandEncoder barrierAfterQueueStages:beforeStages:];
-[MTLToolsCommandEncoder filterCounterRangeWithFirstBatch:lastBatch:filterIndex:];
-[MTLToolsCommandEncoder initWithBaseObject:parent:];
-[MTLToolsCommandEncoder insertSplit];
-[MTLToolsCommandEncoder addRetainedObject:];
-[MTLToolsCommandEncoder initWithBaseObject:parallelRenderCommandEncoder:];
```
