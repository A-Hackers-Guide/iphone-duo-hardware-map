# `_UISceneEventDeferringClientComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `BSDescriptionStreaming`, `_UISceneEventDeferringClient`, `FBSSceneObserver`
- 9 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
{?="isTrackingFirstResponder"b1"hasRequestedInitialSelection"b1} _flags;
@"<BSInvalidatable>" _reachabilityAssertion;
@"BKSHIDEventDeferringReachabilityStatus" _reachabilityStatus;
q _pendingSelectionRequestIgnoringModalities;
@"BSAbsoluteMachTimer" _pendingSelectionRequestTimer;
@"BSCompoundAssertion" _constraintInterestCompoundAssertion;
@"<BSCompoundAssertionState>" _constraintInterestAssertionState;
@"<BSInvalidatable>" _constraintAssertionForFirstResponder;
@"BKSHIDEventDeferringToken" _overrideDeferringToken;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"BKSHIDEventDeferringToken",&,N,V_overrideDeferringToken) overrideDeferringToken;
```

## Instance methods

```
-[_UISceneEventDeferringClientComponent debugDescription];
-[_UISceneEventDeferringClientComponent overrideDeferringToken];
-[_UISceneEventDeferringClientComponent setScene:];
-[_UISceneEventDeferringClientComponent imposeConstraintForReason:];
-[_UISceneEventDeferringClientComponent succinctDescription];
-[_UISceneEventDeferringClientComponent invalidate];
-[_UISceneEventDeferringClientComponent firstResponderDidChange:];
-[_UISceneEventDeferringClientComponent performSelectionRequestIgnoringModalities:];
-[_UISceneEventDeferringClientComponent setOverrideDeferringToken:];
-[_UISceneEventDeferringClientComponent description];
-[_UISceneEventDeferringClientComponent appendDescriptionToStream:];
-[_UISceneEventDeferringClientComponent wantsKeyboardEvents:];
```
