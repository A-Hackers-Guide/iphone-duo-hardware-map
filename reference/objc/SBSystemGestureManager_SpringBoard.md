# `SBSystemGestureManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `UIPointerInteractionDelegate`, `UIPencilInteractionDelegatePrivate`, `BSDescriptionProviding`, `BSInvalidatable`
- 24 instance variables, 11 properties, 52 instance methods, 2 class methods

## Instance variables

```
@"FBSDisplayIdentity" _displayIdentity;
@"NSMutableDictionary" _typeToGesture;
@"NSMutableDictionary" _gestureToType;
@"NSMutableDictionary" _typeToState;
@"NSMapTable" _recognizingTouchGestures;
@"NSMutableSet" _touchGestures;
@"NSMutableSet" _gesturesDisabledAssertions;
@"NSSet" _gestureTypesAllowedWhileDisableAssertionsExist;
@"<BSInvalidatable>" _systemGestureSymbolicRule;
@"<BSInvalidatable>" _systemGestureEventDeferringRule;
@"<BSInvalidatable>" _pointerEventRoutingAssertion;
I _lastSystemGestureWindowContextId;
@"<BSInvalidatable>" _systemGesturesAllowedToken;
@"UIPointerInteraction" _systemPointerInteraction;
@"<BSInvalidatable>" _systemPointerContextIDAssertion;
@"NSMapTable" _ignoreHIDEdgeFlagsAssertions;
@"BSCompoundAssertion" _ignoreHIDEdgeFlagsAssertion;
@"UIPencilInteraction" _systemPencilInteraction;
B _isInvalidated;
B _systemGesturesDisabledForAccessibility;
@"SBIndirectTouchLifecycleMonitor" _indirectTouchLifecycleMonitor;
q _touchInterfaceOrientation;
@"_UISystemGestureManager" _systemGestureManager;
@"<SBSystemUIPointerInteractionDelegate>" _systemPointerInteractionDelegate;
```

## Properties

```
@property (T@"_UISystemGestureManager",W,N,V_systemGestureManager) systemGestureManager;
@property (T@"<SBSystemUIPointerInteractionDelegate>",W,N,V_systemPointerInteractionDelegate) systemPointerInteractionDelegate;
@property (TB,R,N,GisAnyTouchGestureRunning) anyTouchGestureRunning;
@property (TB,N,GareSystemGesturesDisabledForAccessibility,V_systemGesturesDisabledForAccessibility) systemGesturesDisabledForAccessibility;
@property (T@"SBIndirectTouchLifecycleMonitor",&,N,V_indirectTouchLifecycleMonitor) indirectTouchLifecycleMonitor;
@property (TB,R,N,GisValid) valid;
@property (Tq,N,V_touchInterfaceOrientation) touchInterfaceOrientation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSystemGestureManager _attributesForGestureType:];
+[SBSystemGestureManager gestureTypesWithAttributes:];
```

## Instance methods

```
-[SBSystemGestureManager setSystemGestureManager:];
-[SBSystemGestureManager debugDescription];
-[SBSystemGestureManager pointerInteraction:styleForRegion:];
-[SBSystemGestureManager succinctDescriptionBuilder];
-[SBSystemGestureManager init];
-[SBSystemGestureManager pointerInteraction:willEnterRegion:animator:];
-[SBSystemGestureManager pointerInteraction:willExitRegion:animator:];
-[SBSystemGestureManager descriptionWithMultilinePrefix:];
-[SBSystemGestureManager succinctDescription];
-[SBSystemGestureManager invalidate];
-[SBSystemGestureManager systemGestureManager];
-[SBSystemGestureManager removeGestureRecognizer:];
-[SBSystemGestureManager isValid];
-[SBSystemGestureManager pointerInteraction:regionForRequest:defaultRegion:];
-[SBSystemGestureManager windowForSystemGestures];
-[SBSystemGestureManager description];
-[SBSystemGestureManager _evaluateEnablement];
-[SBSystemGestureManager descriptionBuilderWithMultilinePrefix:];
-[SBSystemGestureManager _pencilInteraction:didReceiveSqueeze:];
-[SBSystemGestureManager _disableSystemGesture:withType:];
-[SBSystemGestureManager _configureForNewSystemGestureWindowIfNecessary];
-[SBSystemGestureManager _enableSystemGesture:withType:];
-[SBSystemGestureManager _initWithDisplayIdentity:];
-[SBSystemGestureManager _invalidateIgnoreHidEdgeFlagsAssertionForRemovedRecognizer:];
-[SBSystemGestureManager _isGestureWithTypeAllowed:];
-[SBSystemGestureManager _isTouchGestureWithType:];
-[SBSystemGestureManager _recognitionEventForTouchGestureType:];
-[SBSystemGestureManager _shouldEnableSystemGestureWithType:];
-[SBSystemGestureManager _systemGestureChanged:];
-[SBSystemGestureManager _updateIgnoreHIDEdgeFlagsAssertions];
-[SBSystemGestureManager acquireSystemEdgeGesturesIgnoreHIDEdgeFlagsForReason:];
-[SBSystemGestureManager acquireSystemGestureDisableAssertionForReason:exceptSystemGestureTypes:];
-[SBSystemGestureManager acquireSystemGestureDisableAssertionForReason:forSystemGestureTypes:];
-[SBSystemGestureManager addGestureRecognizer:withType:];
-[SBSystemGestureManager areSystemGesturesDisabledForAccessibility];
-[SBSystemGestureManager cancelGestureRecognizerOfType:reason:];
-[SBSystemGestureManager gestureRecognizerOfType:shouldBeRequiredToFailByGestureRecognizer:];
-[SBSystemGestureManager gestureRecognizerOfType:shouldRequireFailureOfGestureRecognizer:];
-[SBSystemGestureManager ignoreScreenEdgeTouchWithIdentifier:];
-[SBSystemGestureManager indirectTouchLifecycleMonitor];
-[SBSystemGestureManager isAnyTouchGestureRunning];
-[SBSystemGestureManager isGestureWithTypeAllowed:];
-[SBSystemGestureManager isSystemGestureRecognizer:];
-[SBSystemGestureManager setIndirectTouchLifecycleMonitor:];
-[SBSystemGestureManager setSystemGesturesDisabledForAccessibility:];
-[SBSystemGestureManager setSystemPointerInteractionDelegate:];
-[SBSystemGestureManager setTouchInterfaceOrientation:];
-[SBSystemGestureManager shouldEnableSystemGestureWithType:];
-[SBSystemGestureManager shouldSystemGestureReceiveTouchWithLocation:];
-[SBSystemGestureManager systemPointerInteractionDelegate];
-[SBSystemGestureManager touchInterfaceOrientation];
-[SBSystemGestureManager typeOfSystemGesture:];
```
