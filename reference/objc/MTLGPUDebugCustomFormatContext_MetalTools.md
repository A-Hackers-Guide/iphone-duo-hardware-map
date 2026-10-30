# `MTLGPUDebugCustomFormatContext`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTLCustomFormatContext`
- 2 instance variables, 4 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"MTLGPUDebugDevice" _device;
@"MTLGPUDebugGPULog" _log;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MTLGPUDebugCustomFormatContext handleCustomFormatSpecifier:vaList:vaListCount:vaBytesConsumed:];
-[MTLGPUDebugCustomFormatContext handleTensorFormat:vaListCount:vaBytesConsumed:];
-[MTLGPUDebugCustomFormatContext initWithDevice:log:];
```
