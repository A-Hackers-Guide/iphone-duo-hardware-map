# `_UIContinuousSelectionGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 4 instance variables, 4 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _locationInWindow;
@"NSMutableArray" _windows;
{CGVector="dx"d"dy"d} _allowableMovement;
{CGPoint="x"d"y"d} _originalLocation;
```

## Properties

```
@property (T{CGPoint=dd},N,V_originalLocation) originalLocation;
@property (T@"NSMutableArray",&,N,V_locationInWindow) locationInWindow;
@property (T@"NSMutableArray",&,N,V_windows) windows;
@property (T{CGVector=dd},N,V_allowableMovement) allowableMovement;
```

## Class methods

```
+[_UIContinuousSelectionGestureRecognizer _supportsTouchContinuation];
```

## Instance methods

```
-[_UIContinuousSelectionGestureRecognizer allowableMovement];
-[_UIContinuousSelectionGestureRecognizer setWindows:];
-[_UIContinuousSelectionGestureRecognizer touchesEnded:withEvent:];
-[_UIContinuousSelectionGestureRecognizer _resetGestureRecognizer];
-[_UIContinuousSelectionGestureRecognizer _shouldReceiveTouch:withEvent:];
-[_UIContinuousSelectionGestureRecognizer touchesCancelled:withEvent:];
-[_UIContinuousSelectionGestureRecognizer setAllowableMovement:];
-[_UIContinuousSelectionGestureRecognizer setOriginalLocation:];
-[_UIContinuousSelectionGestureRecognizer setLocationInWindow:];
-[_UIContinuousSelectionGestureRecognizer init];
-[_UIContinuousSelectionGestureRecognizer originalLocation];
-[_UIContinuousSelectionGestureRecognizer touchesBegan:withEvent:];
-[_UIContinuousSelectionGestureRecognizer touchesMoved:withEvent:];
-[_UIContinuousSelectionGestureRecognizer locationInView:];
-[_UIContinuousSelectionGestureRecognizer windows];
-[_UIContinuousSelectionGestureRecognizer _cancelOrFail];
-[_UIContinuousSelectionGestureRecognizer locationInWindow];
```
