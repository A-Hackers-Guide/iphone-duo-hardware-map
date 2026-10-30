# `_UITouchForceObservationMessageReader`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UITouchForceObservationMessageReading`
- 4 instance variables, 8 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _shouldFilterDueToSystemGestures;
d _touchForce;
d _timestamp;
{CGPoint="x"d"y"d} _centroid;
```

## Properties

```
@property (Td,N,V_touchForce) touchForce;
@property (Td,N,V_timestamp) timestamp;
@property (T{CGPoint=dd},N,V_centroid) centroid;
@property (TB,N,V_shouldFilterDueToSystemGestures) shouldFilterDueToSystemGestures;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITouchForceObservationMessageReader centroid];
-[_UITouchForceObservationMessageReader setTimestamp:];
-[_UITouchForceObservationMessageReader timestamp];
-[_UITouchForceObservationMessageReader touchForce];
-[_UITouchForceObservationMessageReader shouldFilterDueToSystemGestures];
-[_UITouchForceObservationMessageReader setCentroid:];
-[_UITouchForceObservationMessageReader setShouldFilterDueToSystemGestures:];
-[_UITouchForceObservationMessageReader setTouchForce:];
```
