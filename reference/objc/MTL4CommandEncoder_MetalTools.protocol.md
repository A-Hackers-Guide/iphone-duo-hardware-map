# `MTL4CommandEncoder` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 12 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C) label;
@property (T@"<MTL4CommandBuffer>",R,N) commandBuffer;
```

## Instance methods

```
-[MTL4CommandEncoder insertDebugSignpost:];
-[MTL4CommandEncoder pushDebugGroup:];
-[MTL4CommandEncoder popDebugGroup];
-[MTL4CommandEncoder label];
-[MTL4CommandEncoder setLabel:];
-[MTL4CommandEncoder endEncoding];
-[MTL4CommandEncoder commandBuffer];
-[MTL4CommandEncoder updateFence:afterEncoderStages:];
-[MTL4CommandEncoder barrierAfterEncoderStages:beforeEncoderStages:visibilityOptions:];
-[MTL4CommandEncoder barrierAfterQueueStages:beforeStages:visibilityOptions:];
-[MTL4CommandEncoder barrierAfterStages:beforeQueueStages:visibilityOptions:];
-[MTL4CommandEncoder waitForFence:beforeEncoderStages:];
```
