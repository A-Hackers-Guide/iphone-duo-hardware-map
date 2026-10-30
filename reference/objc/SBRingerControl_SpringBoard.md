# `SBRingerControl`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAVSystemControllerCacheObserver`, `SBControlCenterObserver`, `SBRingerHUDViewControllerDelegate`, `SBRingerAlertElementDelegate`
- 11 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _avscOperationsQueue;
B _ringerMuted;
f _volume;
@"SBBannerManager" _bannerManager;
@"SBSoundController" _soundController;
@"SBAVSystemControllerCache" _avCache;
@"SBControlCenterCoordinator" _controlCenterCoordinator;
@"SBLockScreenCoordinator" _lockScreenCoordinator;
@"SBRingerHUDViewController" _ringerHUDViewController;
@"SBSystemActionCompoundPreviewAssertion" _compoundPreviewAssertion;
@"SBRingerAlertElement" _ringerAlertElement;
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
-[SBRingerControl dealloc];
-[SBRingerControl _accessibilityIsRingerMuted];
-[SBRingerControl cache:didUpdateRingerMuted:];
-[SBRingerControl controlCenter:didDismissOnWindowScene:];
-[SBRingerControl controlCenter:willPresentOnWindowScene:];
-[SBRingerControl observeRingerMutedWithBlock:];
-[SBRingerControl previewRingerStateForReason:];
-[SBRingerControl ringerAlertElementWantsToBeDismissed:forReason:];
-[SBRingerControl ringerAlertElementWantsToBePresented:];
-[SBRingerControl ringerAlertElementWantsToResetAutomaticInvalidationTimer:];
-[SBRingerControl ringerHUDViewControllerWantsToBeDismissed:];
-[SBRingerControl ringerHUDViewControllerWantsToBePresented:];
-[SBRingerControl setRingerMuted:withFeedback:reason:clientType:];
-[SBRingerControl soundForRingerMuted:];
```
