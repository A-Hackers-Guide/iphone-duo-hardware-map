# `UIEvent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 13 properties, 58 instance methods, 1 class methods

## Instance variables

```
^{__GSEvent=} _gsEvent;
^{__IOHIDEvent=} _hidEvent;
B _hasValidModifiers;
q _mzModifierFlags;
Q _mzClickCount;
q _buttonMask;
@"UIScreen" _cachedScreen;
@"NSMutableSet" _eventObservers;
@"NSMutableOrderedSet" _hitTestObservers;
B _isInteractionBehaviorInactive;
Q _lastPointerSenderID;
d _timestamp;
@"UIEventEnvironment" _eventEnvironment;
q _trackpadFingerDownCount;
d __initialTouchTimestamp;
```

## Properties

```
@property (Td,N,S_setTimestamp:,V_timestamp) timestamp;
@property (T@"NSSet",R,N) _allWindows;
@property (T@"NSSet",R,N) _dispatchWindows;
@property (TQ,R,N) _currentPointerEventSource;
@property (TQ,R,N) _inputPrecision;
@property (Tq,R,N,G_trackpadFingerDownCount,V_trackpadFingerDownCount) trackpadFingerDownCount;
@property (Td,R,N,V__initialTouchTimestamp) _initialTouchTimestamp;
@property (T@"BKSHIDEventAuthenticationMessage",R,N) _authenticationMessage;
@property (Tq,R,N) type;
@property (Tq,R,N) subtype;
@property (Tq,R,N) modifierFlags;
@property (Tq,R,N) buttonMask;
@property (T@"NSSet",R,N) allTouches;
```

## Class methods

```
+[UIEvent _inputPrecisionForTouches:];
```

## Instance methods

```
-[UIEvent _allWindows];
-[UIEvent _cleanupAfterDispatch];
-[UIEvent _setHIDEvent:];
-[UIEvent _removeGestureRecognizersSendingCancelledEvent:];
-[UIEvent _removeGestureRecognizer:fromComponents:];
-[UIEvent _gestureRecognizersForWindow:];
-[UIEvent subtype];
-[UIEvent _cloneEvent];
-[UIEvent _screen];
-[UIEvent _sendEventToGestureRecognizer:];
-[UIEvent _currentPointerEventSource];
-[UIEvent _sendEventToResponder:];
-[UIEvent dealloc];
-[UIEvent timestamp];
-[UIEvent touchesForGestureRecognizer:];
-[UIEvent modifierFlags];
-[UIEvent _didSendEvent];
-[UIEvent _inputPrecision];
-[UIEvent _modifierFlags];
-[UIEvent _touchesForGestureRecognizer:];
-[UIEvent _shakeState];
-[UIEvent touchesForWindow:];
-[UIEvent _wasDeliveredToGestureRecognizers];
-[UIEvent _init];
-[UIEvent _digitizerLocation];
-[UIEvent _initialTouchTimestamp];
-[UIEvent type];
-[UIEvent _trackpadFingerDownCount];
-[UIEvent touchesForView:];
-[UIEvent _componentsForGestureRecognizer:];
-[UIEvent _unmodifiedInput];
-[UIEvent predictedTouchesForTouch:];
-[UIEvent _isPhysicalKeyEvent];
-[UIEvent _initWithEvent:touches:];
-[UIEvent _isKeyDown];
-[UIEvent _dispatchWindows];
-[UIEvent _gestureRecognizerNoLongerNeedsSendEvent:];
-[UIEvent _shouldSkipEventDeliveryWithIgnoreInteractionEvents:];
-[UIEvent coalescedTouchesForTouch:];
-[UIEvent _consumeBeforeDeliveryToGestureRecognizers:inWindow:];
-[UIEvent allTouches];
-[UIEvent _modifiedInput];
-[UIEvent _authenticationMessage];
-[UIEvent _buttonMask];
-[UIEvent _clickCount];
-[UIEvent _focusHeading];
-[UIEvent _gsEvent];
-[UIEvent _hidEvent];
-[UIEvent _initWithEnvironment:];
-[UIEvent _isInteractionBehaviorInactive];
-[UIEvent _isTouchRoutingPolicyBased];
-[UIEvent _keyModifierFlags];
-[UIEvent _moveDirection];
-[UIEvent _setGSEvent:];
-[UIEvent _setTimestamp:];
-[UIEvent _triggeringPhysicalButton];
-[UIEvent _wheelVelocity];
-[UIEvent buttonMask];
```
