# `SBPIPPinchGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPinchGestureRecognizer`
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
-[SBPIPPinchGestureRecognizer touchesEnded:withEvent:];
-[SBPIPPinchGestureRecognizer touchesCancelled:withEvent:];
-[SBPIPPinchGestureRecognizer reset];
-[SBPIPPinchGestureRecognizer touchesBegan:withEvent:];
-[SBPIPPinchGestureRecognizer touchesMoved:withEvent:];
-[SBPIPPinchGestureRecognizer initWithTarget:action:];
-[SBPIPPinchGestureRecognizer setDelegate:];
-[SBPIPPinchGestureRecognizer setMaximumNumberOfTouches:];
-[SBPIPPinchGestureRecognizer delegate];
-[SBPIPPinchGestureRecognizer failsPastHysteresis];
-[SBPIPPinchGestureRecognizer maximumNumberOfTouches];
-[SBPIPPinchGestureRecognizer setFailsPastHysteresis:];
```
