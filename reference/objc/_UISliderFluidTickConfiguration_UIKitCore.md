# `_UISliderFluidTickConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISliderFluidConfiguration`
- Protocols: `_UISliderTickConfiguration`, `_UISliderTickProvidingConfiguration`
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
-[_UISliderFluidTickConfiguration tickStyle];
-[_UISliderFluidTickConfiguration setTickStyle:];
-[_UISliderFluidTickConfiguration init];
-[_UISliderFluidTickConfiguration ticks];
-[_UISliderFluidTickConfiguration behavior];
-[_UISliderFluidTickConfiguration snappingDistance];
-[_UISliderFluidTickConfiguration neutralPosition];
-[_UISliderFluidTickConfiguration setNeutralPosition:];
-[_UISliderFluidTickConfiguration copyWithZone:];
-[_UISliderFluidTickConfiguration isEqual:];
-[_UISliderFluidTickConfiguration initWithNumberOfTicks:behavior:];
-[_UISliderFluidTickConfiguration setSnappingDistance:];
-[_UISliderFluidTickConfiguration ticksAreEvenlySpaced];
-[_UISliderFluidTickConfiguration initWithTicks:behavior:];
-[_UISliderFluidTickConfiguration adjustPositionForTargetPosition:adjustedPosition:startPosition:endPosition:];
```
