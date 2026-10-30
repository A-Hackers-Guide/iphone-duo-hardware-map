# `_UIVisualEffectViewCornerMask`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 8 instance variables, 2 properties, 11 instance methods, 6 class methods

## Instance variables

```
@"UIImage" _image;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _imageCenter;
Q _appliedCorners;
{CACornerRadii="minXMaxY"{CGSize="width"d"height"d}"maxXMaxY"{CGSize="width"d"height"d}"maxXMinY"{CGSize="width"d"height"d}"minXMinY"{CGSize="width"d"height"d}} _cornerRadii;
B _continuous;
B _effectsEdges;
B _useCornerRadii;
d _radius;
```

## Properties

```
@property (Td,R,N,V_radius) radius;
@property (TQ,R,N) appliedCorners;
```

## Class methods

```
+[_UIVisualEffectViewCornerMask imageCornerMaskWithImage:radius:];
+[_UIVisualEffectViewCornerMask continuousCornerMaskWithRadius:];
+[_UIVisualEffectViewCornerMask cornerMaskWithRadius:];
+[_UIVisualEffectViewCornerMask cornerMaskWithCornerRadii:continuous:];
+[_UIVisualEffectViewCornerMask _applyZeroMaskToLayer:];
+[_UIVisualEffectViewCornerMask cornerMaskWithRadius:continuous:cornerMask:];
```

## Instance methods

```
-[_UIVisualEffectViewCornerMask init];
-[_UIVisualEffectViewCornerMask _applyToLayer:];
-[_UIVisualEffectViewCornerMask radius];
-[_UIVisualEffectViewCornerMask appliedCorners];
-[_UIVisualEffectViewCornerMask _isCornerWithRadius:continuous:mask:];
-[_UIVisualEffectViewCornerMask cornersAreContinuous];
-[_UIVisualEffectViewCornerMask copyWithZone:];
-[_UIVisualEffectViewCornerMask cornerMaskEffectingEdges:];
-[_UIVisualEffectViewCornerMask isEqual:];
-[_UIVisualEffectViewCornerMask _clone];
-[_UIVisualEffectViewCornerMask cornerMaskAppliedToCorners:];
```
