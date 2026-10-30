# `MTLDepthStencilDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 0 instance variables, 7 properties, 1 instance methods, 2 class methods

## Properties

```
@property (Tr^{MTLDepthStencilDescriptorPrivate=@@QB@Q},R,D) depthStencilPrivate;
@property (TQ,D,N) resourceIndex;
@property (TQ,D,N) depthCompareFunction;
@property (TB,D,N,GisDepthWriteEnabled) depthWriteEnabled;
@property (T@"MTLStencilDescriptor",C,D,N) frontFaceStencil;
@property (T@"MTLStencilDescriptor",C,D,N) backFaceStencil;
@property (T@"NSString",C,D,N) label;
```

## Class methods

```
+[MTLDepthStencilDescriptor allocWithZone:];
+[MTLDepthStencilDescriptor alloc];
```

## Instance methods

```
-[MTLDepthStencilDescriptor copyWithZone:];
```
