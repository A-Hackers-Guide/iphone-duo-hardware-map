# `UIKeyboardPinchGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 7 instance variables, 3 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _pinchDetected;
d _initialPinchSeparation;
[4d] _pinchSeparationValues;
@"NSMutableSet" _activeTouches;
@"NSMutableDictionary" _initialTouchPoints;
d _beginPinchTimestamp;
@"<UIKeyboardPinchGestureRecognizerDelegate>" _pinchDelegate;
```

## Properties

```
@property (TB,R,N,V_pinchDetected) pinchDetected;
@property (Td,R,N,V_initialPinchSeparation) initialPinchSeparation;
@property (T@"<UIKeyboardPinchGestureRecognizerDelegate>",W,N,V_pinchDelegate) pinchDelegate;
```

## Instance methods

```
-[UIKeyboardPinchGestureRecognizer canPreventGestureRecognizer:];
-[UIKeyboardPinchGestureRecognizer touchesEnded:withEvent:];
-[UIKeyboardPinchGestureRecognizer canBePreventedByGestureRecognizer:];
-[UIKeyboardPinchGestureRecognizer touchesCancelled:withEvent:];
-[UIKeyboardPinchGestureRecognizer reset];
-[UIKeyboardPinchGestureRecognizer touchesBegan:withEvent:];
-[UIKeyboardPinchGestureRecognizer touchesMoved:withEvent:];
-[UIKeyboardPinchGestureRecognizer initWithTarget:action:];
-[UIKeyboardPinchGestureRecognizer finalProgressForInitialProgress:];
-[UIKeyboardPinchGestureRecognizer initialPinchSeparation];
-[UIKeyboardPinchGestureRecognizer interpretTouchesForSplit];
-[UIKeyboardPinchGestureRecognizer pinchDelegate];
-[UIKeyboardPinchGestureRecognizer pinchDetected];
-[UIKeyboardPinchGestureRecognizer resetPinchCalculations];
-[UIKeyboardPinchGestureRecognizer setPinchDelegate:];
```
