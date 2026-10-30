# `MTLCommandQueue` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 11 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
```

## Instance methods

```
-[MTLCommandQueue removeResidencySet:];
-[MTLCommandQueue insertDebugCaptureBoundary];
-[MTLCommandQueue addResidencySets:count:];
-[MTLCommandQueue removeResidencySets:count:];
-[MTLCommandQueue device];
-[MTLCommandQueue label];
-[MTLCommandQueue commandBufferWithDescriptor:];
-[MTLCommandQueue setLabel:];
-[MTLCommandQueue addResidencySet:];
-[MTLCommandQueue commandBuffer];
-[MTLCommandQueue commandBufferWithUnretainedReferences];
```
