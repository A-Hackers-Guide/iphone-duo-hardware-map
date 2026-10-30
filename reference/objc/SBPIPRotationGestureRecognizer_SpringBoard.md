# `SBPIPRotationGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIRotationGestureRecognizer`
- 6 instance variables, 3 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _touches;
{CGPoint="x"d"y"d} _accumulatedMovement;
{CGPoint="x"d"y"d} _maximumAbsoluteAccumulatedMovement;
B _achievedMaximumAbsoluteAccumulatedMovement;
B _failsPastHysteresis;
Q _maximumNumberOfTouches;
```

## Properties

```
@property (TQ,N,V_maximumNumberOfTouches) maximumNumberOfTouches;
@property (TB,N,V_failsPastHysteresis) failsPastHysteresis;
@property (T@"<SBPIPSystemGestureRecognizerDelegate>",N) delegate;
```

## Instance methods

```
-[SBPIPRotationGestureRecognizer touchesEnded:withEvent:];
-[SBPIPRotationGestureRecognizer touchesCancelled:withEvent:];
-[SBPIPRotationGestureRecognizer reset];
-[SBPIPRotationGestureRecognizer touchesBegan:withEvent:];
-[SBPIPRotationGestureRecognizer touchesMoved:withEvent:];
-[SBPIPRotationGestureRecognizer initWithTarget:action:];
-[SBPIPRotationGestureRecognizer setDelegate:];
-[SBPIPRotationGestureRecognizer setMaximumNumberOfTouches:];
-[SBPIPRotationGestureRecognizer delegate];
-[SBPIPRotationGestureRecognizer failsPastHysteresis];
-[SBPIPRotationGestureRecognizer maximumNumberOfTouches];
-[SBPIPRotationGestureRecognizer setFailsPastHysteresis:];
```
