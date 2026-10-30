# `UIHoverEvent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIEvent`
- 9 instance variables, 2 properties, 39 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _touchesByContextId;
@"NSMapTable" _deliveryTableByTouch;
@"NSMutableSet" _touchesWithOutstandingUpdates;
B _pointerLocked;
d _maximumPositionZ;
d _hoverAzimuthAngle;
d _hoverAltitudeAngle;
d _positionZ;
d _hoverRollAngle;
```

## Properties

```
@property (TB,R,N) hasOutstandingUpdates;
@property (TB,N,G_isPointerLocked,S_setPointerLocked:,V_pointerLocked) _pointerLocked;
```

## Instance methods

```
-[UIHoverEvent _allWindows];
-[UIHoverEvent _cleanupAfterDispatch];
-[UIHoverEvent _setHIDEvent:];
-[UIHoverEvent _removeGestureRecognizersSendingCancelledEvent:];
-[UIHoverEvent _removeGestureRecognizer:fromComponents:];
-[UIHoverEvent _gestureRecognizersForWindow:];
-[UIHoverEvent subtype];
-[UIHoverEvent removeTouch:fromGestureRecognizer:];
-[UIHoverEvent removeHoverTouchForContextId:pathIndex:];
-[UIHoverEvent _setNeedsUpdateForWindow:forcingHitTest:];
-[UIHoverEvent _cancelAllGestureRecognizersAndRemoveAllHoverTouches];
-[UIHoverEvent setNeedsUpdateForWindow:];
-[UIHoverEvent _completelyRemoveHoverTouchesForWindow:contextIdNumber:withCancellation:];
-[UIHoverEvent _sendEventToGestureRecognizer:];
-[UIHoverEvent _removeAllHoverTouchesForContextId:];
-[UIHoverEvent _windowDidBecomeHidden:];
-[UIHoverEvent _addHasOutstandingUpdateTouch:];
-[UIHoverEvent _deliveryTableByTouchCreateIfNeeded:];
-[UIHoverEvent dealloc];
-[UIHoverEvent touchesForGestureRecognizer:];
-[UIHoverEvent _cancelAllGestureRecognizers];
-[UIHoverEvent _didSendEvent];
-[UIHoverEvent setNeedsHitTestResetForWindow:];
-[UIHoverEvent _inputPrecision];
-[UIHoverEvent hoverTouchForContextId:pathIndex:];
-[UIHoverEvent _isPointerLocked];
-[UIHoverEvent touchesForWindow:];
-[UIHoverEvent _init];
-[UIHoverEvent _windowDidDetachContext:];
-[UIHoverEvent type];
-[UIHoverEvent setHoverTouch:forContextId:pathIndex:];
-[UIHoverEvent touchesForView:];
-[UIHoverEvent _componentsForGestureRecognizer:];
-[UIHoverEvent hasOutstandingUpdates];
-[UIHoverEvent _pointerStateDidChange:];
-[UIHoverEvent _setPointerLocked:];
-[UIHoverEvent _touchesByContextId:createIfNeeded:];
-[UIHoverEvent _gestureRecognizerNoLongerNeedsSendEvent:];
-[UIHoverEvent allTouches];
```
