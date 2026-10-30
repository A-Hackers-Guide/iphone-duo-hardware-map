# `PKStrokeRenderMask`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 2 properties, 5 instance methods, 0 class methods

## Instance variables

```
{vector<std::vector<ClipperLib::IntPoint>, std::allocator<std::vector<ClipperLib::IntPoint>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} _maskPaths;
@"PKStroke" _stroke;
@"<PKStrokeRenderCache>" _renderCache;
```

## Properties

```
@property (T@"PKStroke",R,N,V_stroke) stroke;
@property (T@"<PKStrokeRenderCache>",R,N,V_renderCache) renderCache;
```

## Instance methods

```
-[PKStrokeRenderMask copyWithZone:];
-[PKStrokeRenderMask stroke];
-[PKStrokeRenderMask initWithStroke:renderCache:maskPaths:];
-[PKStrokeRenderMask maskPaths];
-[PKStrokeRenderMask renderCache];
```
