# `UITouchesEvent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIEvent`
- Protocols: `_UIEventComponentContaining`
- 13 instance variables, 7 properties, 67 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _allTouchesMutable;
@"NSSet" _allTouchesImmutableCached;
^{__CFDictionary=} _keyedTouches;
^{__CFDictionary=} _keyedTouchesByWindow;
^{__CFDictionary=} _gestureRecognizersByWindow;
@"NSMapTable" _latentSystemGestureWindows;
^{__CFDictionary=} _coalescedTouches;
^{__CFDictionary=} _finalTouches;
B _isCallingEventObservers;
@"NSMutableSet" _exclusiveTouchWindows;
B _containsHIDPointerEvent;
Q _currentPointerEventSource;
q _singleAllowableExternalTouchPathIndex;
```

## Properties

```
@property (Td,R,N) _initialTouchTimestamp;
@property (Tq,N,V_singleAllowableExternalTouchPathIndex) singleAllowableExternalTouchPathIndex;
@property (TB,R,N,G_containsHIDPointerEvent) containsHIDPointerEvent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITouchesEvent _allWindows];
-[UITouchesEvent _setHIDEvent:];
-[UITouchesEvent _removeComponents:];
-[UITouchesEvent _removeGestureRecognizer:fromComponents:];
-[UITouchesEvent _gestureRecognizersForWindow:];
-[UITouchesEvent _cloneEvent];
-[UITouchesEvent _moveTouchesFromView:toView:];
-[UITouchesEvent _touchesForView:withPhase:];
-[UITouchesEvent _sendEventToGestureRecognizer:];
-[UITouchesEvent _currentPointerEventSource];
-[UITouchesEvent _firstTouchForView:];
-[UITouchesEvent _touchesForKey:];
-[UITouchesEvent _windowNoLongerAwaitingSystemGestureNotification:];
-[UITouchesEvent _touchesForGesture:withPhase:];
-[UITouchesEvent _collectGestureRecognizersFromContainer:withBlock:];
-[UITouchesEvent _respondersForWindow:];
-[UITouchesEvent _touchesForGesture:withPhase:intoSet:];
-[UITouchesEvent _rawCoalescedTouchesForTouch:];
-[UITouchesEvent dealloc];
-[UITouchesEvent touchesForGestureRecognizer:];
-[UITouchesEvent _addGestureRecognizersFromContainer:toTouch:forContinuation:];
-[UITouchesEvent _removeTouch:];
-[UITouchesEvent _inputPrecision];
-[UITouchesEvent touchesForResponder:];
-[UITouchesEvent _cancelComponents:];
-[UITouchesEvent singleAllowableExternalTouchPathIndex];
-[UITouchesEvent _invalidateGestureRecognizerForWindowCache];
-[UITouchesEvent _clearViewForTouch:];
-[UITouchesEvent _touchesForGestureRecognizer:];
-[UITouchesEvent touchesForWindow:];
-[UITouchesEvent _sendSynthesizedBeganForTransitioningGESTouchesToGestureIfNeeded:withDispatchedTouchesIntoSet:];
-[UITouchesEvent _lastPendingCoalescedTouchForIndex:hidEvent:];
-[UITouchesEvent _init];
-[UITouchesEvent _allTouches];
-[UITouchesEvent _digitizerLocation];
-[UITouchesEvent setSingleAllowableExternalTouchPathIndex:];
-[UITouchesEvent _removeTouchesForWindow:];
-[UITouchesEvent _initialTouchTimestamp];
-[UITouchesEvent _addWindowAwaitingLatentSystemGestureNotification:deliveredToEventWindow:];
-[UITouchesEvent _removeTouch:fromGestureRecognizer:];
-[UITouchesEvent type];
-[UITouchesEvent touchesForView:];
-[UITouchesEvent _anyInterestedGestureRecognizersForTouchInView:];
-[UITouchesEvent _componentsForGestureRecognizer:];
-[UITouchesEvent _addTouch:forDelayedDelivery:];
-[UITouchesEvent _clearTouches];
-[UITouchesEvent _exclusiveTouchWindows];
-[UITouchesEvent predictedTouchesForTouch:];
-[UITouchesEvent _initWithEvent:touches:];
-[UITouchesEvent _addCoalescedTouch:forIndex:hidEvent:];
-[UITouchesEvent _addGestureRecognizersFromContainer:toTouch:];
-[UITouchesEvent description];
-[UITouchesEvent _touchesForWindow:];
-[UITouchesEvent _moveCoalescedTouchesFromHidEvent:toHidEvent:];
-[UITouchesEvent _windowsAwaitingLatentSystemGestureNotificationDeliveredToEventWindow:];
-[UITouchesEvent _viewsForWindow:];
-[UITouchesEvent _containsHIDPointerEvent];
-[UITouchesEvent _initialTouchTimestampForWindow:];
-[UITouchesEvent _coalescedTouchesForHidEvent:];
-[UITouchesEvent _gestureRecognizerNoLongerNeedsSendEvent:];
-[UITouchesEvent _touchesForResponder:withPhase:];
-[UITouchesEvent _addGestureRecognizersForTouchContinuationFromContainer:toTouch:];
-[UITouchesEvent _shouldSkipEventDeliveryWithIgnoreInteractionEvents:];
-[UITouchesEvent _componentsForWindow:];
-[UITouchesEvent coalescedTouchesForTouch:];
-[UITouchesEvent allTouches];
-[UITouchesEvent _removeTouchesForKey:];
```
