# `MTLRenderPassAttachmentDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 0 instance variables, 11 properties, 1 instance methods, 0 class methods

## Properties

```
@property (T@"<MTLTexture>",&,D,N) texture;
@property (TQ,D,N) level;
@property (TQ,D,N) slice;
@property (TQ,D,N) depthPlane;
@property (T@"<MTLTexture>",&,D,N) resolveTexture;
@property (TQ,D,N) resolveLevel;
@property (TQ,D,N) resolveSlice;
@property (TQ,D,N) resolveDepthPlane;
@property (TQ,D,N) loadAction;
@property (TQ,D,N) storeAction;
@property (TQ,D,N) storeActionOptions;
```

## Instance methods

```
-[MTLRenderPassAttachmentDescriptor copyWithZone:];
```
