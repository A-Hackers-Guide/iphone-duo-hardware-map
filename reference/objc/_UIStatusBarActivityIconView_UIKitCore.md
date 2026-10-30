# `_UIStatusBarActivityIconView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarImageView`
- Protocols: `_UIStatusBarPersistentAnimation`
- 4 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _ringing;
d _ringingIconScale;
@"CAShapeLayer" _innerRingShapeLayer;
@"CAShapeLayer" _outerRingShapeLayer;
```

## Properties

```
@property (T@"CAShapeLayer",&,N,V_innerRingShapeLayer) innerRingShapeLayer;
@property (T@"CAShapeLayer",&,N,V_outerRingShapeLayer) outerRingShapeLayer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIStatusBarActivityIconView actionForLayer:forKey:];
-[_UIStatusBarActivityIconView resumePersistentAnimation];
-[_UIStatusBarActivityIconView applyStyleAttributes:];
-[_UIStatusBarActivityIconView outerRingShapeLayer];
-[_UIStatusBarActivityIconView alignmentRectInsets];
-[_UIStatusBarActivityIconView layoutSubviews];
-[_UIStatusBarActivityIconView _teardownRingingLayers];
-[_UIStatusBarActivityIconView setInnerRingShapeLayer:];
-[_UIStatusBarActivityIconView innerRingShapeLayer];
-[_UIStatusBarActivityIconView setRinging:forUpdate:];
-[_UIStatusBarActivityIconView setOuterRingShapeLayer:];
-[_UIStatusBarActivityIconView _setupRingingLayersForStyleAttributes:];
```
