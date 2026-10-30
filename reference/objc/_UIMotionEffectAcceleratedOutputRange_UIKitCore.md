# `_UIMotionEffectAcceleratedOutputRange`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCoding`, `NSCopying`
- 3 instance variables, 1 properties, 11 instance methods, 0 class methods

## Instance variables

```
{UIOffset="horizontal"d"vertical"d} _referenceOffset;
{CGPoint="x"d"y"d} _referenceAcceleration;
{CGPoint="x"d"y"d} _acceleration;
```

## Properties

```
@property (T{CGPoint=dd},R,N,V_acceleration) acceleration;
```

## Instance methods

```
-[_UIMotionEffectAcceleratedOutputRange init];
-[_UIMotionEffectAcceleratedOutputRange acceleration];
-[_UIMotionEffectAcceleratedOutputRange reset];
-[_UIMotionEffectAcceleratedOutputRange encodeWithCoder:];
-[_UIMotionEffectAcceleratedOutputRange hash];
-[_UIMotionEffectAcceleratedOutputRange description];
-[_UIMotionEffectAcceleratedOutputRange initWithCoder:];
-[_UIMotionEffectAcceleratedOutputRange copyWithZone:];
-[_UIMotionEffectAcceleratedOutputRange isEqual:];
-[_UIMotionEffectAcceleratedOutputRange acceleratedOutputForViewerOffset:accelerationBoostFactor:];
-[_UIMotionEffectAcceleratedOutputRange setAcceleration:fixingOutputForViewerOffset:];
```
