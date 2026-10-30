# `UIDragEvent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIEvent`
- 18 instance variables, 13 properties, 38 instance methods, 2 class methods

## Instance variables

```
@"_UIDragEventSample" _currentSample;
@"UIView" _previousEventView;
@"UIView" _eventView;
@"NSMutableSet" _beginningGestureRecognizers;
@"NSMutableSet" _updatingGestureRecognizers;
@"NSMutableSet" _exitingGestureRecognizers;
@"NSMutableSet" _endingGestureRecognizers;
@"NSMutableSet" _ignoredGestureRecognizers;
@"NSMutableSet" _dynamicGestureRecognizers;
@"NSHashTable" _ownersQueriedForDynamicGestures;
@"NSMutableSet" _dynamicInteractions;
B _ignoreDragEnd;
B _needsHitTestReset;
B _dragFailed;
@? _dragFailedCallback;
I _dragSessionID;
@"_UIInternalDraggingSessionDestination" _sessionDestination;
@"_UIInternalDraggingSessionSource" _sessionSource;
```

## Properties

```
@property (T@"UIView",R,N,G_hitTestedView) hitTestedView;
@property (T@"NSSet",R,N,G_dynamicGestureRecognizers) dynamicGestureRecognizers;
@property (T@"_UIInternalDraggingSessionDestination",R,N,G_sessionDestination,V_sessionDestination) sessionDestination;
@property (T@"_UIInternalDraggingSessionSource",R,N,G_sessionSource,V_sessionSource) sessionSource;
@property (T@"_UIDropSessionImpl",R,N,G_dropSession) dropSession;
@property (T@"UIWindow",R,N) eventWindow;
@property (TB,R,N) isPolicyDriven;
@property (TB,R,N) hasActiveGestureRecognizers;
@property (TI,R,N,G_touchRoutingPolicyContextID) touchRoutingPolicyContextID;
@property (TI,R,N,G_windowServerHitTestContextID) windowServerHitTestContextID;
@property (TI,R,N,V_dragSessionID) dragSessionID;
@property (T{CGPoint=dd},R,N) locationInSceneReferenceSpace;
@property (TB,R,N) isFromAccessibilitySession;
```

## Class methods

```
+[UIDragEvent _invalidateSessionID:];
+[UIDragEvent _isSessionIDValid:];
```

## Instance methods

```
-[UIDragEvent _allWindows];
-[UIDragEvent _setHIDEvent:];
-[UIDragEvent _removeGestureRecognizersSendingCancelledEvent:];
-[UIDragEvent _removeGestureRecognizer:fromComponents:];
-[UIDragEvent _gestureRecognizersForWindow:];
-[UIDragEvent _reset];
-[UIDragEvent _sendEventToGestureRecognizer:];
-[UIDragEvent dealloc];
-[UIDragEvent _wasDeliveredToGestureRecognizers];
-[UIDragEvent locationInView:];
-[UIDragEvent type];
-[UIDragEvent _shouldSkipEventDeliveryWithIgnoreInteractionEvents:];
-[UIDragEvent _shouldSendEvent];
-[UIDragEvent _updatingDropGestureRecognizers];
-[UIDragEvent _dragFailedWithCallback:];
-[UIDragEvent _dropSession];
-[UIDragEvent _dynamicGestureRecognizers];
-[UIDragEvent _hitTestedView];
-[UIDragEvent _ignoreDragEnd];
-[UIDragEvent _ignoreGestureRecognizer:];
-[UIDragEvent _isReadyForReset];
-[UIDragEvent _isTouchRoutingPolicyBased];
-[UIDragEvent _removeQueriedOwnerForDynamicGesturesIfNeeded:];
-[UIDragEvent _sendIfNeeded];
-[UIDragEvent _sessionDestination];
-[UIDragEvent _sessionSource];
-[UIDragEvent _setNeedsHitTestReset];
-[UIDragEvent _touchRoutingPolicyContextID];
-[UIDragEvent _updateFromCurrentSample];
-[UIDragEvent _updateGesturesFromCurrentSample];
-[UIDragEvent _windowServerHitTestContextID];
-[UIDragEvent dragSessionID];
-[UIDragEvent eventWindow];
-[UIDragEvent hasActiveGestureRecognizers];
-[UIDragEvent initWithDragSessionID:environment:];
-[UIDragEvent isFromAccessibilitySession];
-[UIDragEvent isPolicyDriven];
-[UIDragEvent locationInSceneReferenceSpace];
```
