# `_UITouchForceMessage`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 5 properties, 12 instance methods, 2 class methods

## Instance variables

```
B _isReset;
@"_UITouchForceObservationMessageReader" _observeReader;
B _shouldFilterDueToSystemGestures;
d _unclampedTouchForce;
d _maximumPossibleForce;
d _timestamp;
{CGPoint="x"d"y"d} _centroid;
```

## Properties

```
@property (Td,N,V_unclampedTouchForce) unclampedTouchForce;
@property (Td,N,V_maximumPossibleForce) maximumPossibleForce;
@property (Td,N,V_timestamp) timestamp;
@property (T{CGPoint=dd},N,V_centroid) centroid;
@property (TB,N,V_shouldFilterDueToSystemGestures) shouldFilterDueToSystemGestures;
```

## Class methods

```
+[_UITouchForceMessage reset];
+[_UITouchForceMessage observe:];
```

## Instance methods

```
-[_UITouchForceMessage centroid];
-[_UITouchForceMessage setTimestamp:];
-[_UITouchForceMessage timestamp];
-[_UITouchForceMessage ifObservationUnclamped:ifReset:];
-[_UITouchForceMessage shouldFilterDueToSystemGestures];
-[_UITouchForceMessage ifObservation:ifReset:];
-[_UITouchForceMessage maximumPossibleForce];
-[_UITouchForceMessage setCentroid:];
-[_UITouchForceMessage setMaximumPossibleForce:];
-[_UITouchForceMessage setShouldFilterDueToSystemGestures:];
-[_UITouchForceMessage setUnclampedTouchForce:];
-[_UITouchForceMessage unclampedTouchForce];
```
