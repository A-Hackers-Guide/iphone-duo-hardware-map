# `SBInCallBannerPresentableViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBDeviceApplicationSceneHandleObserver`, `SBBannerManagerPresentable`, `SBButtonEventsHandler`, `BSInvalidatable`
- 9 instance variables, 19 properties, 45 instance methods, 2 class methods

## Instance variables

```
B _didCrossDefaultDraggingThreshold;
@"<BNPanGestureProxy>" _lastGestureProxy;
@"SBDeviceApplicationSceneViewController" _sceneViewController;
@"SBSceneViewStatusBarAssertion" _statusBarHiddenAssertion;
@"SBSUIInCallSceneClientSettingsDiffInspector" _inCallSceneClientSettingsDiffInspector;
B _presented;
@"<SBInCallBannerPresentableViewControllerDelegate>" _delegate;
@"SBDeviceApplicationSceneHandle" _sceneHandle;
{CGSize="width"d"height"d} _preferredBannerContentSize;
```

## Properties

```
@property (T@"<SBInCallBannerPresentableViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T{CGSize=dd},N,V_preferredBannerContentSize) preferredBannerContentSize;
@property (T@"SBDeviceApplicationSceneHandle",R,N,V_sceneHandle) sceneHandle;
@property (TB,R,N,GisCallConnected) callConnected;
@property (TB,R,N,GisPresented,V_presented) presented;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
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
```

## Class methods

```
+[SBInCallBannerPresentableViewController requesterIdentifier];
+[SBInCallBannerPresentableViewController cornerRadius];
```

## Instance methods

```
-[SBInCallBannerPresentableViewController isTouchOutsideDismissalEnabled];
-[SBInCallBannerPresentableViewController sceneHandle:didUpdateClientSettings:];
-[SBInCallBannerPresentableViewController isDraggingInteractionEnabled];
-[SBInCallBannerPresentableViewController isPresented];
-[SBInCallBannerPresentableViewController handleVolumeDownButtonPress];
-[SBInCallBannerPresentableViewController sceneHandle];
-[SBInCallBannerPresentableViewController presentableDidAppearAsBanner:];
-[SBInCallBannerPresentableViewController handleHomeButtonLongPress];
-[SBInCallBannerPresentableViewController requestIdentifier];
-[SBInCallBannerPresentableViewController isDraggingDismissalEnabled];
-[SBInCallBannerPresentableViewController handleVoiceCommandButtonPress];
-[SBInCallBannerPresentableViewController dealloc];
-[SBInCallBannerPresentableViewController preferredContentSizeWithPresentationSize:containerSize:];
-[SBInCallBannerPresentableViewController handleHeadsetButtonPress:];
-[SBInCallBannerPresentableViewController viewDidLoad];
-[SBInCallBannerPresentableViewController initWithSceneHandle:];
-[SBInCallBannerPresentableViewController handleLockButtonPress];
-[SBInCallBannerPresentableViewController viewDidLayoutSubviews];
-[SBInCallBannerPresentableViewController requesterIdentifier];
-[SBInCallBannerPresentableViewController handleVolumeUpButtonPress];
-[SBInCallBannerPresentableViewController viewController];
-[SBInCallBannerPresentableViewController handleHomeButtonDoublePress];
-[SBInCallBannerPresentableViewController invalidate];
-[SBInCallBannerPresentableViewController _canShowWhileLocked];
-[SBInCallBannerPresentableViewController setDelegate:];
-[SBInCallBannerPresentableViewController userInteractionWillBeginForBannerForPresentable:];
-[SBInCallBannerPresentableViewController userInteractionDidEndForBannerForPresentable:];
-[SBInCallBannerPresentableViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBInCallBannerPresentableViewController presentableWillAppearAsBanner:];
-[SBInCallBannerPresentableViewController delegate];
-[SBInCallBannerPresentableViewController _inCallSceneClientSettingsDiffInspector];
-[SBInCallBannerPresentableViewController presentableDidDisappearAsBanner:withReason:];
-[SBInCallBannerPresentableViewController handleHomeButtonPress];
-[SBInCallBannerPresentableViewController presentableWillDisappearAsBanner:withReason:];
-[SBInCallBannerPresentableViewController isCallConnected];
-[SBInCallBannerPresentableViewController draggingDidBeginWithGestureProxy:];
-[SBInCallBannerPresentableViewController translationInCoordinateSpace:];
-[SBInCallBannerPresentableViewController velocityInCoordinateSpace:];
-[SBInCallBannerPresentableViewController visualTranslationInCoordinateSpace:];
-[SBInCallBannerPresentableViewController _handlePanGestureProxyAction:];
-[SBInCallBannerPresentableViewController _callConnectedStatusChanged];
-[SBInCallBannerPresentableViewController _handleTapAction:];
-[SBInCallBannerPresentableViewController preferredBannerContentSize];
-[SBInCallBannerPresentableViewController setPreferredBannerContentSize:];
-[SBInCallBannerPresentableViewController shouldDismissForReason:];
```
