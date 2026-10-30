# `UIScrollEvent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIEvent`
- 15 instance variables, 9 properties, 36 instance methods, 0 class methods

## Instance variables

```
@"NSMapTable" _gestureRecognizersByWindow;
{CGPoint="x"d"y"d} _sceneReferenceLocation;
Q _lastDeliveredPhase;
Q _lastReceivedPhase;
@"BKSHIDEventPointerAttributes" _pointerAttributes;
@"<_UIScrollEventAsyncDeliveryTarget>" _asyncDeliveryTarget;
@"UIGestureRecognizer" _asyncDeliveryGesture;
B _isDoingAsyncDelivery;
B _isCloneForAsyncDelivery;
@"NSMutableSet" _outstandingSnapshotEventsForAsyncDelivery;
B _isStiflingDeltas;
B _hasSimulatedMomentumDelta;
{CGVector="dx"d"dy"d} _simulatedMomentumDelta;
Q _phase;
{CGVector="dx"d"dy"d} _stifledDelta;
```

## Properties

```
@property (T{CGVector=dd},R) acceleratedDelta;
@property (T{CGVector=dd},R) nonAcceleratedDelta;
@property (TB,R) directionInvertedFromDevice;
@property (TQ,R,N,G_scrollType) scrollType;
@property (TB,R,N,G_isHighResolution) highResolution;
@property (TQ,R,N,G_scrollDeviceCategory) scrollDeviceCategory;
@property (Td,R,N,G_beganScrollTimestamp) beganScrollTimestamp;
@property (T{CGVector=dd},R,N,G_stifledDelta,V_stifledDelta) stifledDelta;
@property (TQ,R,V_phase) phase;
```

## Instance methods

```
-[UIScrollEvent _allWindows];
-[UIScrollEvent _cleanupAfterDispatch];
-[UIScrollEvent _setHIDEvent:];
-[UIScrollEvent _removeGestureRecognizersSendingCancelledEvent:];
-[UIScrollEvent _removeGestureRecognizer:fromComponents:];
-[UIScrollEvent _gestureRecognizersForWindow:];
-[UIScrollEvent subtype];
-[UIScrollEvent _cloneEvent];
-[UIScrollEvent _beginStiflingDeltas];
-[UIScrollEvent _simulateMomentumWithDelta:inView:];
-[UIScrollEvent _convertDeltaFromHIDDeviceSpaceToSceneReferenceSpaceIfNeeded:];
-[UIScrollEvent _sendEventToGestureRecognizer:];
-[UIScrollEvent phase];
-[UIScrollEvent _convertPointFromSceneReferenceSpace:toView:];
-[UIScrollEvent directionInvertedFromDevice];
-[UIScrollEvent nonAcceleratedDelta];
-[UIScrollEvent _hasDeliveredTerminalPhase];
-[UIScrollEvent _adjustedDeltaForPanWithAcceleration:honoringScrollDirectionPreference:];
-[UIScrollEvent _wasDeliveredToGestureRecognizers];
-[UIScrollEvent locationInView:];
-[UIScrollEvent _init];
-[UIScrollEvent _isHighResolution];
-[UIScrollEvent _convertPointToSceneReferenceSpace:fromView:];
-[UIScrollEvent type];
-[UIScrollEvent _removeGestureRecognizersFromWindows];
-[UIScrollEvent _scrollType];
-[UIScrollEvent _windowServerHitTestWindow];
-[UIScrollEvent _initWithEvent:touches:];
-[UIScrollEvent _endStiflingDeltas];
-[UIScrollEvent _beganScrollTimestamp];
-[UIScrollEvent _stifledDelta];
-[UIScrollEvent _scrollDeviceCategory];
-[UIScrollEvent _adjustedAcceleratedDeltaInView:];
-[UIScrollEvent _shouldSendEvent];
-[UIScrollEvent _consumeBeforeDeliveryToGestureRecognizers:inWindow:];
-[UIScrollEvent acceleratedDelta];
```
