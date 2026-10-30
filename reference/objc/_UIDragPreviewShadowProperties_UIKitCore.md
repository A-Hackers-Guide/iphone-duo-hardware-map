# `_UIDragPreviewShadowProperties`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 4 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
q _shadowType;
d _liftedAlpha;
d _radiosityBlurRadius;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _liftedTransform;
```

## Properties

```
@property (Tq,N,V_shadowType) shadowType;
@property (T{CGAffineTransform=dddddd},N,V_liftedTransform) liftedTransform;
@property (Td,N,V_liftedAlpha) liftedAlpha;
@property (Td,N,V_radiosityBlurRadius) radiosityBlurRadius;
```

## Class methods

```
+[_UIDragPreviewShadowProperties supportsSecureCoding];
```

## Instance methods

```
-[_UIDragPreviewShadowProperties init];
-[_UIDragPreviewShadowProperties encodeWithCoder:];
-[_UIDragPreviewShadowProperties initWithCoder:];
-[_UIDragPreviewShadowProperties copyWithZone:];
-[_UIDragPreviewShadowProperties liftedTransform];
-[_UIDragPreviewShadowProperties setLiftedAlpha:];
-[_UIDragPreviewShadowProperties liftedAlpha];
-[_UIDragPreviewShadowProperties radiosityBlurRadius];
-[_UIDragPreviewShadowProperties setLiftedTransform:];
-[_UIDragPreviewShadowProperties setRadiosityBlurRadius:];
-[_UIDragPreviewShadowProperties setShadowType:];
-[_UIDragPreviewShadowProperties shadowType];
```
