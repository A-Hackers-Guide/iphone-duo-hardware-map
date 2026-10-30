# `UIKeyboardSyntheticTouch`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 19 instance methods, 1 class methods

## Instance variables

```
d timestamp;
q phase;
Q tapCount;
@"UIWindow" window;
{CGPoint="x"d"y"d} locationInWindow;
C _pathIndex;
C _pathIdentity;
f _pathMajorRadius;
```

## Properties

```
@property (Td,N,Vtimestamp) timestamp;
@property (Tq,N,Vphase) phase;
@property (TQ,N,VtapCount) tapCount;
@property (T@"UIWindow",&,N,Vwindow) window;
@property (T{CGPoint=dd},N,VlocationInWindow) locationInWindow;
@property (TC,R,N,V_pathIndex) _pathIndex;
@property (TC,R,N,V_pathIdentity) _pathIdentity;
@property (Tf,N,V_pathMajorRadius) _pathMajorRadius;
```

## Class methods

```
+[UIKeyboardSyntheticTouch syntheticTouchWithPoint:timestamp:window:];
```

## Instance methods

```
-[UIKeyboardSyntheticTouch setTimestamp:];
-[UIKeyboardSyntheticTouch phase];
-[UIKeyboardSyntheticTouch setLocationInWindow:];
-[UIKeyboardSyntheticTouch timestamp];
-[UIKeyboardSyntheticTouch window];
-[UIKeyboardSyntheticTouch locationInView:];
-[UIKeyboardSyntheticTouch setPhase:];
-[UIKeyboardSyntheticTouch setWindow:];
-[UIKeyboardSyntheticTouch locationInWindow];
-[UIKeyboardSyntheticTouch tapCount];
-[UIKeyboardSyntheticTouch initWithPoint:timestamp:window:];
-[UIKeyboardSyntheticTouch _pathIdentity];
-[UIKeyboardSyntheticTouch _pathIndex];
-[UIKeyboardSyntheticTouch _pathMajorRadius];
-[UIKeyboardSyntheticTouch _setLocationInWindow:resetPrevious:];
-[UIKeyboardSyntheticTouch getLocationInWindow];
-[UIKeyboardSyntheticTouch previousLocationInView:];
-[UIKeyboardSyntheticTouch setTapCount:];
-[UIKeyboardSyntheticTouch set_pathMajorRadius:];
```
