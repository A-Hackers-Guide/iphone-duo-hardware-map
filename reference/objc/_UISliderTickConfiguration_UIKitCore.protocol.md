# `_UISliderTickConfiguration` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `_UISliderTickProvidingConfiguration`
- 0 instance variables, 5 properties, 11 instance methods, 1 class methods

## Properties

```
@property (Tq,R,N) behavior;
@property (T@"NSArray",R,C,N) ticks;
@property (Tq,N) tickStyle;
@property (Td,N) neutralPosition;
@property (Tf,N) snappingDistance;
```

## Class methods

```
+[_UISliderTickConfiguration new];
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
-[_UISliderTickConfiguration initWithNumberOfTicks:behavior:];
-[_UISliderTickConfiguration setSnappingDistance:];
-[_UISliderTickConfiguration initWithTicks:behavior:];
```
