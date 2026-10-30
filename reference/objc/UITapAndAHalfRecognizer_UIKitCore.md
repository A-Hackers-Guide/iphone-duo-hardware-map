# `UITapAndAHalfRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 8 instance variables, 5 properties, 23 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _startPoint;
d _allowableMovement;
i _numberOfFullTaps;
d _minimumFinalPressDuration;
@"NSMutableSet" _activeTouches;
i _currentNumberOfTaps;
@"UITouch" _touch;
@"UIDelayedAction" _tapTimer;
```

## Properties

```
@property (T@"UITouch",&,N,V_touch) touch;
@property (Ti,N,V_numberOfFullTaps) numberOfFullTaps;
@property (Td,N,V_allowableMovement) allowableMovement;
@property (Td,N,V_minimumFinalPressDuration) minimumFinalPressDuration;
@property (T{CGPoint=dd},R,N) locationOfFirstTap;
```

## Instance methods

```
-[UITapAndAHalfRecognizer allowableMovement];
-[UITapAndAHalfRecognizer tooSlow:];
-[UITapAndAHalfRecognizer touchesEnded:withEvent:];
-[UITapAndAHalfRecognizer touch];
-[UITapAndAHalfRecognizer _resetGestureRecognizer];
-[UITapAndAHalfRecognizer touchesCancelled:withEvent:];
-[UITapAndAHalfRecognizer setAllowableMovement:];
-[UITapAndAHalfRecognizer locationOfFirstTap];
-[UITapAndAHalfRecognizer startTapTimer:];
-[UITapAndAHalfRecognizer clearTapTimer];
-[UITapAndAHalfRecognizer dealloc];
-[UITapAndAHalfRecognizer setTouch:];
-[UITapAndAHalfRecognizer recognized:];
-[UITapAndAHalfRecognizer touchesBegan:withEvent:];
-[UITapAndAHalfRecognizer touchesMoved:withEvent:];
-[UITapAndAHalfRecognizer initWithTarget:action:];
-[UITapAndAHalfRecognizer _verifyMovementInAllowableRange];
-[UITapAndAHalfRecognizer numberOfFullTaps];
-[UITapAndAHalfRecognizer minimumFinalPressDuration];
-[UITapAndAHalfRecognizer translationInWindowCoordinates];
-[UITapAndAHalfRecognizer startRecognitionTimer:];
-[UITapAndAHalfRecognizer setMinimumFinalPressDuration:];
-[UITapAndAHalfRecognizer setNumberOfFullTaps:];
```
