# `SBKeyboardDismissalManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFailureNotifyingTapGestureRecognizerDelegate`, `BKSTouchDeliveryObserving`
- 8 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"__UIKeyboardArbiterManager" _keyboardArbiterManager;
@"SBSystemGestureManager" _systemGestureManager;
@"<SBKeyboardFocusControlling>" _keyboardFocusCoordinator;
@"BKSTouchDeliveryObservationService" _touchService;
@"BSCompoundAssertion" _participantsAssertion;
@"UIGestureRecognizer" _dismissGestureRecognizer;
I _trackedTouchIdentifier;
@"BSAbsoluteMachTimer" _touchExpiryTimer;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBKeyboardDismissalManager _reset];
-[SBKeyboardDismissalManager gestureRecognizerTransitionedToFailed:];
-[SBKeyboardDismissalManager gestureRecognizer:shouldReceiveTouch:];
-[SBKeyboardDismissalManager dealloc];
-[SBKeyboardDismissalManager viewForSystemGestureRecognizer:];
-[SBKeyboardDismissalManager gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[SBKeyboardDismissalManager touchUpOccuredForIdentifier:detached:context:pid:];
-[SBKeyboardDismissalManager _didTap:];
-[SBKeyboardDismissalManager _shouldPreventDismissalForTouch:];
-[SBKeyboardDismissalManager initWithTouchDeliveryService:systemGestureManager:keyboardArbiterManager:focusController:];
-[SBKeyboardDismissalManager registerKeyboardDismissalParticipant:];
```
