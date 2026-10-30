# `_UISceneEventDeferringHostComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `_UISceneRelationshipManagementHostComponentObserver`, `_UISceneHostKeyboardSuppressionControllerObserver`, `_UISceneHostingEventDeferringHostProviding`, `FBSceneObserver`, `BSDescriptionStreaming`, `_UISceneEventDeferringHost`, `BKSHIDEventDeliveryChainObserving`
- 14 instance variables, 10 properties, 28 instance methods, 0 class methods

## Instance variables

```
{?="hasConfiguredObservers"b1"hasAcquiredTemporaryGrant"b1"hasStaleInterestClientSetting"b1"maintainHostFirstResponderWhenClientWantsKeyboard"b1"clientIsInChain"b1} _flags;
q _pendingSelectionRequestIgnoringModalities;
@"<BSInvalidatable>" _deferringToken;
@"FBSScene" _deferringTokenParentScene;
@"BKSHIDEventDeferringTarget" _deferringTarget;
@"<BSInvalidatable>" _constraintAssertion;
@"BSCompoundAssertion" _constraintInterestCompoundAssertion;
@"<BSCompoundAssertionState>" _constraintInterestAssertionState;
@"<BSInvalidatable>" _alwaysConstraintAssertionIfRequired;
@"<BSInvalidatable>" _clientRequestedConstraintAssertion;
@"BKSHIDEventDeliveryManager" _deliveryManager;
@"BKSHIDEventDeliveryChainObserver" _chainObserver;
@"<BSInvalidatable>" _chainObserverToken;
@"UIResponder" _firstResponderTrackingSelectionPath;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N) maintainHostFirstResponderWhenClientWantsKeyboard;
@property (TB,N) requestEventDeferralForAllFirstResponderChanges;
@property (Tq,N) deferringRuleBehavior;
@property (Tq,N) selectionRequestBehavior;
@property (Tq,N) constraintAssertionBehavior;
@property (Tq,N) grantBehavior;
```

## Instance methods

```
-[_UISceneEventDeferringHostComponent scene:clientDidConnect:];
-[_UISceneEventDeferringHostComponent sceneWillDeactivate:withContext:];
-[_UISceneEventDeferringHostComponent debugDescription];
-[_UISceneEventDeferringHostComponent scene:handleActions:];
-[_UISceneEventDeferringHostComponent sceneDidActivate:];
-[_UISceneEventDeferringHostComponent setScene:];
-[_UISceneEventDeferringHostComponent grantBehavior];
-[_UISceneEventDeferringHostComponent constraintAssertionBehavior];
-[_UISceneEventDeferringHostComponent imposeConstraintForReason:];
-[_UISceneEventDeferringHostComponent selectionRequestBehavior];
-[_UISceneEventDeferringHostComponent setConstraintAssertionBehavior:];
-[_UISceneEventDeferringHostComponent observer:deliveryChainDidUpdate:];
-[_UISceneEventDeferringHostComponent setRequestEventDeferralForAllFirstResponderChanges:];
-[_UISceneEventDeferringHostComponent succinctDescription];
-[_UISceneEventDeferringHostComponent invalidate];
-[_UISceneEventDeferringHostComponent setDeferringRuleBehavior:];
-[_UISceneEventDeferringHostComponent setSelectionRequestBehavior:];
-[_UISceneEventDeferringHostComponent performSelectionRequestIgnoringModalities:];
-[_UISceneEventDeferringHostComponent _scene:isMovingToParent:];
-[_UISceneEventDeferringHostComponent setMaintainHostFirstResponderWhenClientWantsKeyboard:];
-[_UISceneEventDeferringHostComponent maintainHostFirstResponderWhenClientWantsKeyboard];
-[_UISceneEventDeferringHostComponent description];
-[_UISceneEventDeferringHostComponent appendDescriptionToStream:];
-[_UISceneEventDeferringHostComponent deferringRuleBehavior];
-[_UISceneEventDeferringHostComponent setGrantBehavior:];
-[_UISceneEventDeferringHostComponent keyboardSuppressionController:didUpdateSuppression:];
-[_UISceneEventDeferringHostComponent scene:didUpdateClientSettings:];
-[_UISceneEventDeferringHostComponent requestEventDeferralForAllFirstResponderChanges];
```
