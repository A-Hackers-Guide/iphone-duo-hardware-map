# `UIInputSwitcherGestureState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _didMoveBeyondThreshold;
B _hideSwitcher;
d _touchDown;
d _lastSeenKeyboardTouchDown;
{CGPoint="x"d"y"d} _firstReferencePoint;
```

## Properties

```
@property (TB,N,V_didMoveBeyondThreshold) didMoveBeyondThreshold;
@property (TB,N,V_hideSwitcher) hideSwitcher;
@property (T{CGPoint=dd},N,V_firstReferencePoint) firstReferencePoint;
@property (Td,N,V_touchDown) touchDown;
@property (Td,N,V_lastSeenKeyboardTouchDown) lastSeenKeyboardTouchDown;
```

## Instance methods

```
-[UIInputSwitcherGestureState didMoveBeyondThreshold];
-[UIInputSwitcherGestureState firstReferencePoint];
-[UIInputSwitcherGestureState gestureConflictsWithTypingWindow];
-[UIInputSwitcherGestureState hideSwitcher];
-[UIInputSwitcherGestureState lastSeenKeyboardTouchDown];
-[UIInputSwitcherGestureState setDidMoveBeyondThreshold:];
-[UIInputSwitcherGestureState setFirstReferencePoint:];
-[UIInputSwitcherGestureState setHideSwitcher:];
-[UIInputSwitcherGestureState setLastSeenKeyboardTouchDown:];
-[UIInputSwitcherGestureState setTouchDown:];
-[UIInputSwitcherGestureState touchDown];
```
