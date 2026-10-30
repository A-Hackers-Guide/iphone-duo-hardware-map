# `SBLongPressGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBClickGestureRecognizer`
- 4 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _firstEventAfterClicksWasReceived;
B _hardwareLongPressActive;
B _beginsOnHardwareLongPress;
d _minimumPressDuration;
```

## Properties

```
@property (TQ,D,N) numberOfClicksRequired;
@property (Td,N,V_minimumPressDuration) minimumPressDuration;
@property (TB,N,V_beginsOnHardwareLongPress) beginsOnHardwareLongPress;
```

## Instance methods

```
-[SBLongPressGestureRecognizer beginsOnHardwareLongPress];
-[SBLongPressGestureRecognizer setState:];
-[SBLongPressGestureRecognizer dealloc];
-[SBLongPressGestureRecognizer reset];
-[SBLongPressGestureRecognizer initWithTarget:action:];
-[SBLongPressGestureRecognizer gestureStateInfoForUnbalancedPressBeganCount:previousCount:];
-[SBLongPressGestureRecognizer minimumPressDuration];
-[SBLongPressGestureRecognizer setMinimumPressDuration:];
-[SBLongPressGestureRecognizer setBeginsOnHardwareLongPress:];
-[SBLongPressGestureRecognizer _updateHardwareLongPressRegistration];
```
