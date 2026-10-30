# `SBActivityViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `ACUISActivityHostViewControllerDelegate`
- 7 instance variables, 14 properties, 38 instance methods, 0 class methods

## Instance variables

```
Q _presentationMode;
Q _visibility;
@"<SBActivityViewControllerDelegate>" _delegate;
@"SBActivityItem" _activityItem;
@"ACUISActivityHostViewController" _activityHostViewController;
@"<ACUISActivityMetricsProvider>" _metricsProvider;
@"<BSInvalidatable>" _activeIdleTimerAssertion;
```

## Properties

```
@property (T@"ACUISActivityHostViewController",&,N,V_activityHostViewController) activityHostViewController;
@property (T@"<BSInvalidatable>",&,N,V_activeIdleTimerAssertion) activeIdleTimerAssertion;
@property (T@"<SBActivityViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"SBActivityItem",R,N,V_activityItem) activityItem;
@property (T{CGSize=dd},R,N) preferredActivityContentSize;
@property (T@"<ACUISActivityMetricsProvider>",&,N,V_metricsProvider) metricsProvider;
@property (TB,R,N) wantsIdleTimerDisabled;
@property (T@"NSSet",R,N) audioCategoriesDisablingVolumeHUD;
@property (TQ,N,V_presentationMode) presentationMode;
@property (TQ,N,V_visibility) visibility;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBActivityViewController presentationMode];
-[SBActivityViewController setPresentationMode:];
-[SBActivityViewController setVisibility:];
-[SBActivityViewController _unlockAndLaunchAppIfPossible:withAction:];
-[SBActivityViewController visibility];
-[SBActivityViewController ensureContent:queue:completion:];
-[SBActivityViewController dealloc];
-[SBActivityViewController audioCategoriesDisablingVolumeHUD];
-[SBActivityViewController viewDidLoad];
-[SBActivityViewController metricsProvider];
-[SBActivityViewController viewWillAppear:];
-[SBActivityViewController invalidate];
-[SBActivityViewController setDelegate:];
-[SBActivityViewController delegate];
-[SBActivityViewController viewWillLayoutSubviews];
-[SBActivityViewController handleActivityWillDismissFromBottomSwipeGesture];
-[SBActivityViewController viewDidDisappear:];
-[SBActivityViewController setMetricsProvider:];
-[SBActivityViewController _preferredContentSizeDidChangeForChildViewController:];
-[SBActivityViewController activityItem];
-[SBActivityViewController initWithActivityItem:];
-[SBActivityViewController wantsIdleTimerDisabled];
-[SBActivityViewController _viewWillLayoutSubviews];
-[SBActivityViewController activityHostViewController:didSetIdleTimerDisabled:];
-[SBActivityViewController activityHostViewController:requestsLaunchWithAction:];
-[SBActivityViewController activityHostViewControllerAudioCategoriesDisablingVolumeHUDDidChange:];
-[SBActivityViewController activityHostViewControllerBackgroundTintColorDidChange:];
-[SBActivityViewController activityHostViewControllerHostShouldCancelTouches:];
-[SBActivityViewController activeIdleTimerAssertion];
-[SBActivityViewController activityHostViewController];
-[SBActivityViewController initWithActivityItem:sceneType:payloadID:];
-[SBActivityViewController initWithActivityItem:sceneType:payloadID:targetBundleIdentifier:];
-[SBActivityViewController initWithActivityItem:sceneType:payloadID:targetBundleIdentifier:windowScene:];
-[SBActivityViewController initWithActivityItem:sceneType:payloadID:windowScene:];
-[SBActivityViewController initWithActivityItem:viewController:];
-[SBActivityViewController preferredActivityContentSize];
-[SBActivityViewController setActiveIdleTimerAssertion:];
-[SBActivityViewController setActivityHostViewController:];
```
