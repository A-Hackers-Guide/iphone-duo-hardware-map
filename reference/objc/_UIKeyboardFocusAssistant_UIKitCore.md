# `_UIKeyboardFocusAssistant`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSHIDEventDeliveryPolicyObserving`
- 12 instance variables, 16 properties, 43 instance methods, 0 class methods

## Instance variables

```
@"BSAbsoluteMachTimer" _enqueuedSelectionRequestTimer;
@"<BKSHIDEventProvenance>" _provenanceForEnqueuedSelectionRequest;
@"<BKSHIDEventProvenance>" _provenanceForActiveInputModality;
B _isFinalSceneInDeferringTargetChain;
B _isAncestorOfDeferringTargetChain;
@"UIKeyboardSceneDelegate<_UIKeyboardFocusAssistantDelegate>" _keyboardSceneDelegate;
@"BKSHIDEventDeliveryPolicyObserver" _eventDeliveryPolicyObserver;
@"<_UIDeferralPolicyTask>" _deferralPolicyTask;
@"<BSInvalidatable>" _activeInputAssertion;
@"BKSHIDEventDeferringToken" _tokenForActiveInputAssertion;
@"UIResponder" _responderForReadyTask;
@"UIResponder" _responderForMeanwhileTask;
```

## Properties

```
@property (T@"BKSHIDEventDeliveryManager",R,N) deliveryManager;
@property (T@"BKSHIDEventDeliveryPolicyObserver",&,N,V_eventDeliveryPolicyObserver) eventDeliveryPolicyObserver;
@property (T@"<_UIDeferralPolicyTask>",&,N,V_deferralPolicyTask) deferralPolicyTask;
@property (TB,N,V_isFinalSceneInDeferringTargetChain) isFinalSceneInDeferringTargetChain;
@property (TB,N,V_isAncestorOfDeferringTargetChain) isAncestorOfDeferringTargetChain;
@property (T@"<BSInvalidatable>",&,N,V_activeInputAssertion) activeInputAssertion;
@property (T@"BKSHIDEventDeferringToken",&,N,V_tokenForActiveInputAssertion) tokenForActiveInputAssertion;
@property (T@"UIResponder",W,N,V_responderForReadyTask) responderForReadyTask;
@property (T@"UIResponder",W,N,V_responderForMeanwhileTask) responderForMeanwhileTask;
@property (T@"UIKeyboardSceneDelegate<_UIKeyboardFocusAssistantDelegate>",W,N,V_keyboardSceneDelegate) keyboardSceneDelegate;
@property (TB,R,N) hasKeyboardFocus;
@property (TB,R,N) isAncestorOfKeyboardFocusTarget;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIKeyboardFocusAssistant startMonitoring];
-[_UIKeyboardFocusAssistant observerDeliveryPolicyDidChange:];
-[_UIKeyboardFocusAssistant setResponderForMeanwhileTask:];
-[_UIKeyboardFocusAssistant _beginActiveInputForResponder:];
-[_UIKeyboardFocusAssistant setEventDeliveryPolicyObserver:];
-[_UIKeyboardFocusAssistant hasKeyboardFocus];
-[_UIKeyboardFocusAssistant isAncestorOfKeyboardFocusTarget];
-[_UIKeyboardFocusAssistant deferralPolicyTask];
-[_UIKeyboardFocusAssistant eventDeliveryPolicyObserver];
-[_UIKeyboardFocusAssistant setActiveInputAssertion:];
-[_UIKeyboardFocusAssistant _endActiveInputForResponder:];
-[_UIKeyboardFocusAssistant _shouldCancelDeferralPolicyTask:forRunnableTaskWithResponder:needsFocus:isReentrant:];
-[_UIKeyboardFocusAssistant setKeyboardSceneDelegate:];
-[_UIKeyboardFocusAssistant dealloc];
-[_UIKeyboardFocusAssistant tokenForActiveInputAssertion];
-[_UIKeyboardFocusAssistant performWhenReadyForResponder:needsFocus:reason:readyTask:meanwhileTask:];
-[_UIKeyboardFocusAssistant _requestKeyboardFocusWithProvenance:];
-[_UIKeyboardFocusAssistant _configureEventDeliveryPolicyObserver];
-[_UIKeyboardFocusAssistant stopMonitoring];
-[_UIKeyboardFocusAssistant _enqueueSelectionRequestForProvenance:];
-[_UIKeyboardFocusAssistant _responderWantsActiveInputMode:];
-[_UIKeyboardFocusAssistant storeProvenanceForActiveInputModality:];
-[_UIKeyboardFocusAssistant activeInputAssertion];
-[_UIKeyboardFocusAssistant updateActiveInputAssertionForResponder:];
-[_UIKeyboardFocusAssistant keyboardSceneDelegate];
-[_UIKeyboardFocusAssistant monitoringDeferringToken];
-[_UIKeyboardFocusAssistant hasActiveInputAssertion];
-[_UIKeyboardFocusAssistant isAncestorOfDeferringTargetChain];
-[_UIKeyboardFocusAssistant setDeferralPolicyTask:];
-[_UIKeyboardFocusAssistant isFinalSceneInDeferringTargetChain];
-[_UIKeyboardFocusAssistant responderNeedsKeyboardFocus:];
-[_UIKeyboardFocusAssistant setIsAncestorOfDeferringTargetChain:];
-[_UIKeyboardFocusAssistant deliveryManager];
-[_UIKeyboardFocusAssistant performWhenReadyForResponder:needsFocus:precedence:reason:readyTask:meanwhileTask:];
-[_UIKeyboardFocusAssistant enqueueRequestKeyboardFocusWithProvenance:];
-[_UIKeyboardFocusAssistant _newEventDeliveryPolicyObserver];
-[_UIKeyboardFocusAssistant readyForTaskWithResponder:needsFocus:];
-[_UIKeyboardFocusAssistant responderForMeanwhileTask];
-[_UIKeyboardFocusAssistant _handleObserverDeliveryPolicyDidChange];
-[_UIKeyboardFocusAssistant setIsFinalSceneInDeferringTargetChain:];
-[_UIKeyboardFocusAssistant setTokenForActiveInputAssertion:];
-[_UIKeyboardFocusAssistant responderForReadyTask];
-[_UIKeyboardFocusAssistant setResponderForReadyTask:];
```
