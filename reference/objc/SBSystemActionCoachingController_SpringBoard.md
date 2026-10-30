# `SBSystemActionCoachingController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PTSettingsKeyObserver`, `SBBacklightControllerObserver`, `SBSystemActionCoachingHUDViewControllerDelegate`, `SBSystemGestureRecognizerDelegate`, `SBSystemActionPreviewCoordinatorObserving`
- 15 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<SBSystemActionCoachingControllerDelegate>" _delegate;
@"<SBHUDControlling>" _HUDController;
@"SBRingerControl" _ringerControl;
@"SBActivityManager" _activityManager;
@"SBApplicationController" _applicationController;
@"SBDoNotDisturbStateMonitor" _doNotDisturbStateMonitor;
@"SBFlashlightActivityManager" _flashlightActivityManager;
@"SBFocusActivityManager" _focusActivityManager;
@"SBBannerManager" _bannerManager;
@"SBSystemGestureManager" _systemGestureManager;
@"SBSystemActionCoachingSettings" _settings;
@"<SBSystemActionCoachingPolicy>" _policy;
@"NSArray" _systemApertureFrames;
@"SBFailingSystemGestureRecognizer" _dismissGestureRecognizer;
@"<BSInvalidatable>" _bannerWindowLevelAssertion;
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
-[SBSystemActionCoachingController backlightController:didTransitionToBacklightState:source:];
-[SBSystemActionCoachingController _gestureRecognizerFailed:];
-[SBSystemActionCoachingController dealloc];
-[SBSystemActionCoachingController settings:changedValueForKey:];
-[SBSystemActionCoachingController viewForSystemGestureRecognizer:];
-[SBSystemActionCoachingController _volumeButtonPressed:];
-[SBSystemActionCoachingController systemActionCoachingHUDViewController:didBeginTransitionToState:];
-[SBSystemActionCoachingController _systemApertureLayoutChanged:];
-[SBSystemActionCoachingController systemActionPreviewCoordinator:didBeginPreview:forAction:];
-[SBSystemActionCoachingController systemActionPreviewCoordinator:didEndPreview:forAction:withResult:];
-[SBSystemActionCoachingController systemActionPreviewCoordinator:didInvalidateExpansionOfPreview:forAction:withResult:];
```
