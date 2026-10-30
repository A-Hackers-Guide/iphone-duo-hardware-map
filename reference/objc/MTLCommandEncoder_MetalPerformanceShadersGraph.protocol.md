# `MTLCommandEncoder` (protocol)

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 8 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",C) label;
```

## Instance methods

```
-[MTLCommandEncoder insertDebugSignpost:];
-[MTLCommandEncoder pushDebugGroup:];
-[MTLCommandEncoder popDebugGroup];
-[MTLCommandEncoder device];
-[MTLCommandEncoder label];
-[MTLCommandEncoder setLabel:];
-[MTLCommandEncoder endEncoding];
-[MTLCommandEncoder barrierAfterQueueStages:beforeStages:];
```
