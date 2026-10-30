# `MTL4DebugCommandEncoder`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 2 properties, 17 instance methods, 0 class methods

## Instance variables

```
@ _baseObject;
@"MTLToolsDevice" _device;
@"MTL4DebugCommandBuffer" _commandBuffer;
Q _afterEncoderStageMaskForBarriers;
Q _afterEncoderStageMaskForFences;
Q _beforeEncoderStageMask;
{MTL4DebugCommandEncoderState="canEndEncoding"b1"hasEndEncoding"b1} _encoderState;
```

## Properties

```
@property (TB,N) canEndEncoding;
@property (TB,R,N) hasEndEncoding;
```

## Instance methods

```
-[MTL4DebugCommandEncoder updateFence:afterEncoderStages:];
-[MTL4DebugCommandEncoder barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:];
-[MTL4DebugCommandEncoder barrierAfterQueueStages:beforeStages:visibilityOptions:];
-[MTL4DebugCommandEncoder barrierAfterStages:beforeQueueStages:visibilityOptions:];
-[MTL4DebugCommandEncoder commandBatchIdOffset];
-[MTL4DebugCommandEncoder commandBatchIdRangeMin:max:];
-[MTL4DebugCommandEncoder endEncodingAndRetrieveProgramAddressTable];
-[MTL4DebugCommandEncoder filterCounterRangeWithFirstBatch:lastBatch:filterIndex:];
-[MTL4DebugCommandEncoder waitForFence:beforeEncoderStages:];
-[MTL4DebugCommandEncoder initWithBaseObject:device:commandBuffer:afterEncoderStageMaskForBarriers:afterEncoderStageMaskForFences:beforeEncoderStageMask:];
-[MTL4DebugCommandEncoder canEndEncoding];
-[MTL4DebugCommandEncoder endEncodingPreamble];
-[MTL4DebugCommandEncoder hasEndEncoding];
-[MTL4DebugCommandEncoder initWithBaseObject:device:commandBuffer:encoderStageMask:];
-[MTL4DebugCommandEncoder resetEncoderState];
-[MTL4DebugCommandEncoder setCanEndEncoding:];
-[MTL4DebugCommandEncoder validateFunctionArguments:stage:functionName:argumentTable:boundThreadgroupMemoryArguments:bindings:allowNullBufferBindings:];
```
