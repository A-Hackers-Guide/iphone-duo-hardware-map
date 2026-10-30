# `UIPointerInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIPointerInteractionDriverSink`, `UIInteraction_Internal`, `UIInteraction`
- 12 instance variables, 14 properties, 44 instance methods, 0 class methods

## Instance variables

```
{?="regionForRequest"B"styleForRegion"B"willEnterRegionAnimator"B"willExitRegionAnimator"B"asyncRegionForRequest"B"targetRegionForDeceleratingPointerWithRequests"B} _delegateImplements;
Q _generationID;
B _observingPresentationNotification;
B _enabled;
B _pausesPointerUpdatesWhilePanning;
@"UIView" _view;
@"UIPointerRegion" _defaultRegion;
@"<UIPointerInteractionDelegate>" _delegate;
@"NSArray" _drivers;
@"UIPointerRegion" _currentRegion;
@"UIPointerRegion" _mostRecentRegion;
q _currentModifiers;
```

## Properties

```
@property (T@"NSArray",C,N,V_drivers) drivers;
@property (T@"UIPointerRegion",C,N,V_currentRegion) currentRegion;
@property (T@"UIPointerRegion",C,N,V_mostRecentRegion) mostRecentRegion;
@property (Tq,N,V_currentModifiers) currentModifiers;
@property (T@"UIPointerRegion",R,N,V_defaultRegion) defaultRegion;
@property (TB,N,G_pausesPointerUpdatesWhilePanning,S_setPausesPointerUpdatesWhilePanning:,V_pausesPointerUpdatesWhilePanning) pausesPointerUpdatesWhilePanning;
@property (T@"<UIPointerInteractionDelegate>",R,W,N,V_delegate) delegate;
@property (TB,N,GisEnabled,V_enabled) enabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<UIInteractionEffect>",?,&,N) interactionEffect;
@property (T@"UIView",R,W,N,V_view) view;
```

## Instance methods

```
-[UIPointerInteraction drivers];
-[UIPointerInteraction driver:willAttachHoverGestureRecognizer:toView:];
-[UIPointerInteraction _queryDelegateForRegionWithRequest:completion:forceSynchronous:];
-[UIPointerInteraction initWithDelegate:];
-[UIPointerInteraction _notifyDelegate_willExitRegion:];
-[UIPointerInteraction init];
-[UIPointerInteraction currentRegion];
-[UIPointerInteraction driverDidExit:];
-[UIPointerInteraction mostRecentRegion];
-[UIPointerInteraction setCurrentRegion:];
-[UIPointerInteraction dealloc];
-[UIPointerInteraction _pointerRegionAtPoint:modifiers:];
-[UIPointerInteraction _applyPointerStyle:forRegion:animator:];
-[UIPointerInteraction driver:didIssueUpdate:];
-[UIPointerInteraction _pointerStyleForRegion:];
-[UIPointerInteraction setCurrentModifiers:];
-[UIPointerInteraction _setPausesPointerUpdatesWhilePanning:];
-[UIPointerInteraction _supportsAssociation];
-[UIPointerInteraction isEnabled];
-[UIPointerInteraction _handlePresentationNotification:];
-[UIPointerInteraction invalidate];
-[UIPointerInteraction view];
-[UIPointerInteraction _targetedPreviewForContinuingEffectWithPreview:];
-[UIPointerInteraction setEnabled:];
-[UIPointerInteraction willMoveToView:];
-[UIPointerInteraction delegate];
-[UIPointerInteraction setMostRecentRegion:];
-[UIPointerInteraction _updateInteractionIsEnabled];
-[UIPointerInteraction _notifyDelegate_willEnterRegion:];
-[UIPointerInteraction _updateCurrentRegionIfNecessary:update:];
-[UIPointerInteraction _pausesPointerUpdatesWhilePanning];
-[UIPointerInteraction setDrivers:];
-[UIPointerInteraction currentModifiers];
-[UIPointerInteraction _pointerDidEnterRegion:update:];
-[UIPointerInteraction _updatePointerStyleForRegion:update:animator:];
-[UIPointerInteraction _regionContainsCurrentHoverLocation:];
-[UIPointerInteraction _updateDebugUIForRegionIfEnabled:];
-[UIPointerInteraction _viewTraitCollectionDidChange:];
-[UIPointerInteraction _pointerDidExitRegion:willEnterNewRegion:];
-[UIPointerInteraction _runAlongsideAnimator:];
-[UIPointerInteraction didMoveToView:];
-[UIPointerInteraction defaultRegion];
-[UIPointerInteraction _modifiersDidChangeInRegion:update:];
-[UIPointerInteraction _pointerDidExit];
```
