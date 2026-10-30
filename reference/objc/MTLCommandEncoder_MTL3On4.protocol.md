# `MTLCommandEncoder` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MTL3On4.framework/MTL3On4`](../userland/System__Library__PrivateFrameworks__MTL3On4.framework__MTL3On4.md) (iOS 27.2 dyld shared cache) **[DSC]**
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
