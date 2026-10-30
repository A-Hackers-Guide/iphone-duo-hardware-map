# `MTLStencilDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 0 instance variables, 7 properties, 1 instance methods, 2 class methods

## Properties

```
@property (Tr^{MTLStencilDescriptorPrivate=QQQQII},R,D) stencilPrivate;
@property (TQ,D,N) stencilCompareFunction;
@property (TQ,D,N) stencilFailureOperation;
@property (TQ,D,N) depthFailureOperation;
@property (TQ,D,N) depthStencilPassOperation;
@property (TI,D,N) readMask;
@property (TI,D,N) writeMask;
```

## Class methods

```
+[MTLStencilDescriptor allocWithZone:];
+[MTLStencilDescriptor alloc];
```

## Instance methods

```
-[MTLStencilDescriptor copyWithZone:];
```
