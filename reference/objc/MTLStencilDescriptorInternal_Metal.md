# `MTLStencilDescriptorInternal`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLStencilDescriptor`
- 1 instance variables, 1 properties, 19 instance methods, 0 class methods

## Instance variables

```
{MTLStencilDescriptorPrivate="stencilCompareFunction"Q"stencilFailureOperation"Q"depthFailureOperation"Q"depthStencilPassOperation"Q"readMask"I"writeMask"I} _private;
```

## Properties

```
@property (Tr^{MTLStencilDescriptorPrivate=QQQQII},R) stencilPrivate;
```

## Instance methods

```
-[MTLStencilDescriptorInternal setDepthFailureOperation:];
-[MTLStencilDescriptorInternal stencilFailureOperation];
-[MTLStencilDescriptorInternal formattedDescription:];
-[MTLStencilDescriptorInternal init];
-[MTLStencilDescriptorInternal stencilPrivate];
-[MTLStencilDescriptorInternal readMask];
-[MTLStencilDescriptorInternal setDepthStencilPassOperation:];
-[MTLStencilDescriptorInternal writeMask];
-[MTLStencilDescriptorInternal setWriteMask:];
-[MTLStencilDescriptorInternal hash];
-[MTLStencilDescriptorInternal setReadMask:];
-[MTLStencilDescriptorInternal description];
-[MTLStencilDescriptorInternal setStencilFailureOperation:];
-[MTLStencilDescriptorInternal stencilCompareFunction];
-[MTLStencilDescriptorInternal copyWithZone:];
-[MTLStencilDescriptorInternal isEqual:];
-[MTLStencilDescriptorInternal setStencilCompareFunction:];
-[MTLStencilDescriptorInternal depthFailureOperation];
-[MTLStencilDescriptorInternal depthStencilPassOperation];
```
