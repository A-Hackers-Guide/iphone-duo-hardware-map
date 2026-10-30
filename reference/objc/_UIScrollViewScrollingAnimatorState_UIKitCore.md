# `_UIScrollViewScrollingAnimatorState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
Q _granularity;
Q _direction;
{CGPoint="x"d"y"d} _offset;
{CGPoint="x"d"y"d} _maximumVelocity;
{CGPoint="x"d"y"d} _force;
```

## Properties

```
@property (T{CGPoint=dd},N,V_offset) offset;
@property (T{CGPoint=dd},N,V_maximumVelocity) maximumVelocity;
@property (T{CGPoint=dd},N,V_force) force;
@property (TQ,N,V_granularity) granularity;
@property (TQ,N,V_direction) direction;
```

## Instance methods

```
-[_UIScrollViewScrollingAnimatorState granularity];
-[_UIScrollViewScrollingAnimatorState setGranularity:];
-[_UIScrollViewScrollingAnimatorState setDirection:];
-[_UIScrollViewScrollingAnimatorState direction];
-[_UIScrollViewScrollingAnimatorState force];
-[_UIScrollViewScrollingAnimatorState setOffset:];
-[_UIScrollViewScrollingAnimatorState setForce:];
-[_UIScrollViewScrollingAnimatorState offset];
-[_UIScrollViewScrollingAnimatorState maximumVelocity];
-[_UIScrollViewScrollingAnimatorState setMaximumVelocity:];
```
