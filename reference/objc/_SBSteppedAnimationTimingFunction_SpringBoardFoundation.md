# `_SBSteppedAnimationTimingFunction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"CAMediaTimingFunction" _timingFunction;
{SBNormalizedTransitionInterval="start"d"duration"d} _constrainedRange;
```

## Properties

```
@property (T@"CAMediaTimingFunction",R,N,V_timingFunction) timingFunction;
@property (T{SBNormalizedTransitionInterval=dd},R,N,V_constrainedRange) constrainedRange;
```

## Class methods

```
+[_SBSteppedAnimationTimingFunction timingFunctionWithTimingFunction:constrainedToIntervalBetween:and:];
```

## Instance methods

```
-[_SBSteppedAnimationTimingFunction timingFunction];
-[_SBSteppedAnimationTimingFunction constrainedRange];
-[_SBSteppedAnimationTimingFunction initWithTimingFunction:constrainedToIntervalBetween:and:];
-[_SBSteppedAnimationTimingFunction valueAtPercentage:];
```
