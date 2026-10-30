# `_UIPanOrFlickGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPanGestureRecognizer`
- 14 instance variables, 15 properties, 40 instance methods, 0 class methods

## Instance variables

```
Q _touchCount;
B _didLongPress;
B _longPressOnly;
Q _allowedFlickDirections;
d _maximumFlickDuration;
d _minimumFlickDistance;
d _minimumPressDuration;
d _allowableMovement;
d _responsivenessDelay;
d _timestampBeforeGestureBegan;
d _timestampOfLastEvent;
@"UIDelayedAction" _elapsedAction;
@"UIDelayedAction" _responsivenessAction;
{CGPoint="x"d"y"d} _initialCentroidLocation;
```

## Properties

```
@property (Td,N,V_timestampBeforeGestureBegan) timestampBeforeGestureBegan;
@property (Td,N,V_timestampOfLastEvent) timestampOfLastEvent;
@property (T@"UIDelayedAction",&,N,V_elapsedAction) elapsedAction;
@property (T@"UIDelayedAction",&,N,V_responsivenessAction) responsivenessAction;
@property (T{CGPoint=dd},N,V_initialCentroidLocation) initialCentroidLocation;
@property (T@"<_UIPanOrFlickGestureRecognizerDelegate>",R,N) panOrFlickDelegate;
@property (TQ,N,V_allowedFlickDirections) allowedFlickDirections;
@property (Td,N,V_maximumFlickDuration) maximumFlickDuration;
@property (Td,N,V_minimumFlickDistance) minimumFlickDistance;
@property (TQ,R,N) recognizedFlickDirection;
@property (Td,N,V_minimumPressDuration) minimumPressDuration;
@property (Td,N,V_allowableMovement) allowableMovement;
@property (TB,R,N,V_didLongPress) didLongPress;
@property (TB,N,V_longPressOnly) longPressOnly;
@property (Td,N,V_responsivenessDelay) responsivenessDelay;
```

## Instance methods

```
-[_UIPanOrFlickGestureRecognizer startTimer];
-[_UIPanOrFlickGestureRecognizer allowableMovement];
-[_UIPanOrFlickGestureRecognizer setAllowedFlickDirections:];
-[_UIPanOrFlickGestureRecognizer touchesEnded:withEvent:];
-[_UIPanOrFlickGestureRecognizer elapsedAction];
-[_UIPanOrFlickGestureRecognizer setLongPressOnly:];
-[_UIPanOrFlickGestureRecognizer setResponsivenessAction:];
-[_UIPanOrFlickGestureRecognizer minimumFlickDistance];
-[_UIPanOrFlickGestureRecognizer setTimestampBeforeGestureBegan:];
-[_UIPanOrFlickGestureRecognizer maximumFlickDuration];
-[_UIPanOrFlickGestureRecognizer clearTimer];
-[_UIPanOrFlickGestureRecognizer touchesCancelled:withEvent:];
-[_UIPanOrFlickGestureRecognizer enoughTimeElapsed:];
-[_UIPanOrFlickGestureRecognizer setElapsedAction:];
-[_UIPanOrFlickGestureRecognizer setAllowableMovement:];
-[_UIPanOrFlickGestureRecognizer initialCentroidLocation];
-[_UIPanOrFlickGestureRecognizer longPressOnly];
-[_UIPanOrFlickGestureRecognizer dealloc];
-[_UIPanOrFlickGestureRecognizer reset];
-[_UIPanOrFlickGestureRecognizer allowedFlickDirections];
-[_UIPanOrFlickGestureRecognizer panOrFlickDelegate];
-[_UIPanOrFlickGestureRecognizer touchesBegan:withEvent:];
-[_UIPanOrFlickGestureRecognizer touchesMoved:withEvent:];
-[_UIPanOrFlickGestureRecognizer initWithTarget:action:];
-[_UIPanOrFlickGestureRecognizer recognizedFlickDirection];
-[_UIPanOrFlickGestureRecognizer _shouldTryToBeginWithEvent:];
-[_UIPanOrFlickGestureRecognizer didLongPress];
-[_UIPanOrFlickGestureRecognizer timestampOfLastEvent];
-[_UIPanOrFlickGestureRecognizer setMinimumFlickDistance:];
-[_UIPanOrFlickGestureRecognizer setTimestampOfLastEvent:];
-[_UIPanOrFlickGestureRecognizer timestampBeforeGestureBegan];
-[_UIPanOrFlickGestureRecognizer responsivenessAction];
-[_UIPanOrFlickGestureRecognizer minimumPressDuration];
-[_UIPanOrFlickGestureRecognizer setResponsivenessDelay:];
-[_UIPanOrFlickGestureRecognizer setMaximumFlickDuration:];
-[_UIPanOrFlickGestureRecognizer isValidLongPress];
-[_UIPanOrFlickGestureRecognizer responsivenessDelay];
-[_UIPanOrFlickGestureRecognizer setInitialCentroidLocation:];
-[_UIPanOrFlickGestureRecognizer setMinimumPressDuration:];
-[_UIPanOrFlickGestureRecognizer responsivenessTimeElapsed:];
```
