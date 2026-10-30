# `MTLDebugRenderTargetAttachmentInfo`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"<MTLTexture>" _attachmentTexture;
@"<MTLTexture>" _baseResolveTexture;
@"<MTLTexture>" _baseTexture;
Q _renderTargetArrayLength;
Q _baseLevelOffset;
Q _resolveLevelOffset;
{_NSRange="location"Q"length"Q} _baseSliceRangeOffset;
{_NSRange="location"Q"length"Q} _resolveSliceRangeOffset;
```

## Properties

```
@property (T@"<MTLTexture>",R,N,V_attachmentTexture) attachmentTexture;
@property (T@"<MTLTexture>",R,N,V_baseResolveTexture) baseResolveTexture;
@property (T@"<MTLTexture>",R,N,V_baseTexture) baseTexture;
@property (TQ,R,N,V_renderTargetArrayLength) renderTargetArrayLength;
@property (TQ,R,N,V_baseLevelOffset) baseLevelOffset;
@property (TQ,R,N,V_resolveLevelOffset) resolveLevelOffset;
@property (T{_NSRange=QQ},R,N,V_baseSliceRangeOffset) baseSliceRangeOffset;
@property (T{_NSRange=QQ},R,N,V_resolveSliceRangeOffset) resolveSliceRangeOffset;
```

## Instance methods

```
-[MTLDebugRenderTargetAttachmentInfo renderTargetArrayLength];
-[MTLDebugRenderTargetAttachmentInfo hash];
-[MTLDebugRenderTargetAttachmentInfo isEqual:];
-[MTLDebugRenderTargetAttachmentInfo baseLevelOffset];
-[MTLDebugRenderTargetAttachmentInfo attachmentTexture];
-[MTLDebugRenderTargetAttachmentInfo baseResolveTexture];
-[MTLDebugRenderTargetAttachmentInfo baseSliceRangeOffset];
-[MTLDebugRenderTargetAttachmentInfo baseTexture];
-[MTLDebugRenderTargetAttachmentInfo initWithDesc:renderTargetArrayLength:];
-[MTLDebugRenderTargetAttachmentInfo intersectsTexture:];
-[MTLDebugRenderTargetAttachmentInfo resolveLevelOffset];
-[MTLDebugRenderTargetAttachmentInfo resolveSliceRangeOffset];
```
