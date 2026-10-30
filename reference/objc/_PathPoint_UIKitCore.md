# `_PathPoint`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _sentinelPoint;
d _force;
d _relativeTime;
d _absoluteTime;
d _decay;
d _length;
{CGPoint="x"d"y"d} _point;
```

## Properties

```
@property (TB,N,GisSentinelPoint,V_sentinelPoint) sentinelPoint;
@property (T{CGPoint=dd},N,V_point) point;
@property (Td,N,V_force) force;
@property (Td,N,V_relativeTime) relativeTime;
@property (Td,N,V_absoluteTime) absoluteTime;
@property (Td,N,V_decay) decay;
@property (Td,N,V_length) length;
```

## Instance methods

```
-[_PathPoint absoluteTime];
-[_PathPoint length];
-[_PathPoint decay];
-[_PathPoint setRelativeTime:];
-[_PathPoint relativeTime];
-[_PathPoint point];
-[_PathPoint description];
-[_PathPoint force];
-[_PathPoint setForce:];
-[_PathPoint setPoint:];
-[_PathPoint setLength:];
-[_PathPoint isSentinelPoint];
-[_PathPoint setAbsoluteTime:];
-[_PathPoint setDecay:];
-[_PathPoint setSentinelPoint:];
```
