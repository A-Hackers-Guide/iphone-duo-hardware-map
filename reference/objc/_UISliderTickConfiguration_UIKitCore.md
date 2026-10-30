# `_UISliderTickConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UISliderTickConfiguration`, `_UISliderTickProvidingConfiguration`, `_UISliderConfiguration`, `NSCopying`
- 6 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
_behavior;
_ticks;
_ticksAreEvenlySpaced;
q tickStyle;
d neutralPosition;
f snappingDistance;
```

## Properties

```
@property (Tq,N,R) behavior;
@property (T@"NSArray",N,R) ticks;
@property (Tq,N,VtickStyle) tickStyle;
@property (Td,N,VneutralPosition) neutralPosition;
@property (Tf,N,VsnappingDistance) snappingDistance;
@property (TB,N,R) ticksAreEvenlySpaced;
```

## Instance methods

```
-[_UISliderTickConfiguration tickStyle];
-[_UISliderTickConfiguration setTickStyle:];
-[_UISliderTickConfiguration init];
-[_UISliderTickConfiguration ticks];
-[_UISliderTickConfiguration behavior];
-[_UISliderTickConfiguration snappingDistance];
-[_UISliderTickConfiguration neutralPosition];
-[_UISliderTickConfiguration setNeutralPosition:];
-[_UISliderTickConfiguration copyWithZone:];
-[_UISliderTickConfiguration isEqual:];
-[_UISliderTickConfiguration initWithNumberOfTicks:behavior:];
-[_UISliderTickConfiguration setSnappingDistance:];
-[_UISliderTickConfiguration ticksAreEvenlySpaced];
-[_UISliderTickConfiguration initWithTicks:behavior:];
-[_UISliderTickConfiguration adjustPositionForTargetPosition:adjustedPosition:startPosition:endPosition:];
```
