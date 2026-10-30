# `SBBannerSourceListenerHostedPresentableViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BNBannerSourceListenerHostedPresentableViewController`
- Protocols: `SBBarSwipeAffordanceObserver`, `SBPresentableSystemDragCancelling`, `SBBannerPhysicalButtonTarget`, `SBBannerManagerPresentable`, `SBUIPresentableLocalHomeGestureParticipant`, `SBButtonEventsHandler`, `SBBannerLayoutCustomizing`
- 9 instance variables, 17 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"SBWindowSceneStatusBarSettingsAssertion" _appStatusBarSettingsAssertion;
@"NSMutableArray" _wantsHomeAffordanceActionsAwaitingResponse;
@"SBBannerGestureRecognizerPriorityAssertion" _gestureRecognizerPriorityAssertion;
@"NSMutableDictionary" _buttonEventsToActions;
@"SBBarSwipeAffordanceView" _barSwipeAffordanceView;
B _supportsCancellingSystemDragGesture;
@"SBBannerCustomTransitioningDelegate" _customTransitioningDelegate;
@"<SBPresentableSystemDragCancellationHandler>" _systemDragCancellationHandler;
@"<SBUIPresentableHomeGestureContext>" _homeGestureContext;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBPresentableSystemDragCancellationHandler>",W,N,V_systemDragCancellationHandler) systemDragCancellationHandler;
@property (Tq,?,R,N) presentableBehavior;
@property (T@"<BNPresentableContext>",?,W,N) presentableContext;
@property (T@"NSSet",?,R,C,N) preferredBackgroundActivitiesToSuppress;
@property (TB,?,R,N,GisDraggingDismissalEnabled) draggingDismissalEnabled;
@property (TB,?,R,N,GisDraggingInteractionEnabled) draggingInteractionEnabled;
@property (TB,?,R,N,GisTouchOutsideDismissalEnabled) touchOutsideDismissalEnabled;
@property (T@"UIViewController",?,R,N) viewController;
@property (Tq,?,R,N) presentableType;
@property (T@"NSString",R,C,N) requesterIdentifier;
@property (T@"NSString",R,C,N) requestIdentifier;
@property (T@"<SBUIPresentableHomeGestureContext>",W,N,V_homeGestureContext) homeGestureContext;
@property (T{UIEdgeInsets=dddd},?,R,N) bannerContentOutsets;
```

## Instance methods

```
-[SBBannerSourceListenerHostedPresentableViewController isDraggingInteractionEnabled];
-[SBBannerSourceListenerHostedPresentableViewController handleVolumeDownButtonPress];
-[SBBannerSourceListenerHostedPresentableViewController bannerContentOutsets];
-[SBBannerSourceListenerHostedPresentableViewController presentableDidAppearAsBanner:];
-[SBBannerSourceListenerHostedPresentableViewController _updateAppStatusBarSettingsAssertion];
-[SBBannerSourceListenerHostedPresentableViewController handleHomeButtonLongPress];
-[SBBannerSourceListenerHostedPresentableViewController scene:handleActions:];
-[SBBannerSourceListenerHostedPresentableViewController setSystemDragCancellationHandler:];
-[SBBannerSourceListenerHostedPresentableViewController systemDragCancellationHandler];
-[SBBannerSourceListenerHostedPresentableViewController isDraggingDismissalEnabled];
-[SBBannerSourceListenerHostedPresentableViewController handleVoiceCommandButtonPress];
-[SBBannerSourceListenerHostedPresentableViewController dealloc];
-[SBBannerSourceListenerHostedPresentableViewController homeGestureContext];
-[SBBannerSourceListenerHostedPresentableViewController handleHeadsetButtonPress:];
-[SBBannerSourceListenerHostedPresentableViewController handleLockButtonPress];
-[SBBannerSourceListenerHostedPresentableViewController handleVolumeUpButtonPress];
-[SBBannerSourceListenerHostedPresentableViewController homeGesturePerformedForBarSwipeAffordanceView:];
-[SBBannerSourceListenerHostedPresentableViewController shouldDismissForReason:outReason:];
-[SBBannerSourceListenerHostedPresentableViewController handleHomeButtonDoublePress];
-[SBBannerSourceListenerHostedPresentableViewController setHomeGestureContext:];
-[SBBannerSourceListenerHostedPresentableViewController presentableWillAppearAsBanner:];
-[SBBannerSourceListenerHostedPresentableViewController homeGestureOwnershipDidChange:];
-[SBBannerSourceListenerHostedPresentableViewController _invalidateAllButtonEventActions];
-[SBBannerSourceListenerHostedPresentableViewController targetSceneForPhysicalButtonInteraction];
-[SBBannerSourceListenerHostedPresentableViewController presentableDidDisappearAsBanner:withReason:];
-[SBBannerSourceListenerHostedPresentableViewController transitioningDelegate];
-[SBBannerSourceListenerHostedPresentableViewController shouldDisableTouchCancellationForTouch:event:];
-[SBBannerSourceListenerHostedPresentableViewController scene:didUpdateClientSettings:];
-[SBBannerSourceListenerHostedPresentableViewController handleHomeButtonPress];
-[SBBannerSourceListenerHostedPresentableViewController presentableWillDisappearAsBanner:withReason:];
```
