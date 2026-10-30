# `SBLockScreenDeviceMotionEffectController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PTSettingsKeyPathObserver`, `SBBacklightControllerObserver`, `PRUISDeviceMotionControllerDelegate`, `PRUISDeviceMotionDisablementAssertionManagerObserver`, `FBSDisplayLayoutPublisherObserving`, `PBUIWallpaperObserver`
- 26 instance variables, 16 properties, 50 instance methods, 1 class methods

## Instance variables

```
@"SBBacklightController" _backlightController;
@"PRUISDeviceMotionDisablementAssertionManager" _deviceMotionDisableAssertionManager;
@"<BSInvalidatable>" _wallpaperNotVisibleDeviceMotionDisableAssertion;
@"<BSInvalidatable>" _wallpaperObscuredDeviceMotionDisableAssertion;
@"<BSInvalidatable>" _posterDeviceMotionDisableAssertion;
@"<BSInvalidatable>" _backlightDeviceMotionDisableAssertion;
@"<BSInvalidatable>" _reducedMotionDeviceMotionDisableAssertion;
@"<BSInvalidatable>" _lowPowerDeviceMotionDisableAssertion;
@"<BSInvalidatable>" _backlightChangeSourceDisableAssertion;
@"<BSInvalidatable>" _userPresenceDisableAssertion;
@"<BSInvalidatable>" _coverSheetNotVisibleDisableAssertion;
@"SBMiscellaneousDefaults" _miscellaneousDefaults;
@"SBLockScreenDefaults" _lockScreenDefaults;
@"<BSDefaultObserver>" _defaultObserverToken;
B _wallpaperVisible;
B _wallpaperObscured;
B _posterClientWantsMotionEvents;
B _userPresenceDetected;
B _coverSheetVisible;
d _motionUpdateInterval;
Q _posterClientDeviceMotionMode;
@"SBWallpaperController" _wallpaperController;
@"SBDeviceMotionEffectSettings" _deviceMotionEffectPrototypeSettings;
@"<FBSDisplayLayoutPublishing>" _displayLayoutPublisher;
@"NSObject<OS_dispatch_queue>" _performanceOptimizationUpdateQueue;
@"PRUISDeviceMotionController" _posterDeviceMotionController;
```

## Properties

```
@property (T@"SBWallpaperController",W,N,V_wallpaperController) wallpaperController;
@property (T@"SBDeviceMotionEffectSettings",&,N,V_deviceMotionEffectPrototypeSettings) deviceMotionEffectPrototypeSettings;
@property (T@"<FBSDisplayLayoutPublishing>",&,N,V_displayLayoutPublisher) displayLayoutPublisher;
@property (TB,N,GisCoverSheetVisible,V_coverSheetVisible) coverSheetVisible;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_performanceOptimizationUpdateQueue) performanceOptimizationUpdateQueue;
@property (T@"PRUISDeviceMotionController",&,N,G_posterDeviceMotionController,S_setPosterDeviceMotionController:,V_posterDeviceMotionController) posterDeviceMotionController;
@property (TB,N,GisWallpaperVisible,V_wallpaperVisible) wallpaperVisible;
@property (TB,N,GisWallpaperObscured,V_wallpaperObscured) wallpaperObscured;
@property (TB,N,V_posterClientWantsMotionEvents) posterClientWantsMotionEvents;
@property (Td,N,V_motionUpdateInterval) motionUpdateInterval;
@property (TB,N,GisUserPresenceDetected,V_userPresenceDetected) userPresenceDetected;
@property (TQ,N,V_posterClientDeviceMotionMode) posterClientDeviceMotionMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBLockScreenDeviceMotionEffectController new];
```

## Instance methods

```
-[SBLockScreenDeviceMotionEffectController backlightController:didTransitionToBacklightState:source:];
-[SBLockScreenDeviceMotionEffectController _acquireWallpaperNotVisibleDeviceMotionDisableAssertion];
-[SBLockScreenDeviceMotionEffectController setWallpaperObscured:];
-[SBLockScreenDeviceMotionEffectController wallpaperController];
-[SBLockScreenDeviceMotionEffectController isUserPresenceDetected];
-[SBLockScreenDeviceMotionEffectController setDeviceMotionEffectPrototypeSettings:];
-[SBLockScreenDeviceMotionEffectController isWallpaperObscured];
-[SBLockScreenDeviceMotionEffectController deviceMotionController:didUpdateMotionWithRotation:];
-[SBLockScreenDeviceMotionEffectController posterClientWantsMotionEvents];
-[SBLockScreenDeviceMotionEffectController _updatePerformanceOptimizationState];
-[SBLockScreenDeviceMotionEffectController setMotionUpdateInterval:];
-[SBLockScreenDeviceMotionEffectController isCoverSheetVisible];
-[SBLockScreenDeviceMotionEffectController init];
-[SBLockScreenDeviceMotionEffectController _isPerformanceOptimizationDisabled];
-[SBLockScreenDeviceMotionEffectController setPerformanceOptimizationUpdateQueue:];
-[SBLockScreenDeviceMotionEffectController _acquirePosterClientDeviceMotionDisableAssertion];
-[SBLockScreenDeviceMotionEffectController dealloc];
-[SBLockScreenDeviceMotionEffectController deviceMotionControllerDidUpdateDeviceMotionSettings:];
-[SBLockScreenDeviceMotionEffectController _acquireBacklightDeviceMotionDisableAssertion];
-[SBLockScreenDeviceMotionEffectController publisher:didUpdateLayout:withTransition:];
-[SBLockScreenDeviceMotionEffectController wallpaperDidUpdatePreferredDeviceMotionUpdateInterval:];
-[SBLockScreenDeviceMotionEffectController _acquireWallpaperObscuredDeviceMotionDisableAssertion];
-[SBLockScreenDeviceMotionEffectController setCoverSheetVisible:];
-[SBLockScreenDeviceMotionEffectController _acquireCoverSheetNotVisibleDeviceMotionDisableAssertion];
-[SBLockScreenDeviceMotionEffectController initWithScene:];
-[SBLockScreenDeviceMotionEffectController motionUpdateInterval];
-[SBLockScreenDeviceMotionEffectController _setPosterDeviceMotionController:];
-[SBLockScreenDeviceMotionEffectController isWallpaperVisible];
-[SBLockScreenDeviceMotionEffectController _posterDeviceMotionController];
-[SBLockScreenDeviceMotionEffectController _acquireReducedMotionDeviceMotionDisableAssertion];
-[SBLockScreenDeviceMotionEffectController _acquireBacklightChangeSourceDeviceMotionDisableAssertion];
-[SBLockScreenDeviceMotionEffectController posterClientDeviceMotionMode];
-[SBLockScreenDeviceMotionEffectController setDisplayLayoutPublisher:];
-[SBLockScreenDeviceMotionEffectController _acquireDisableAssertionForReason:optimizationEnabled:];
-[SBLockScreenDeviceMotionEffectController displayLayoutPublisher];
-[SBLockScreenDeviceMotionEffectController setUserPresenceDetected:];
-[SBLockScreenDeviceMotionEffectController deviceMotionEffectPrototypeSettings];
-[SBLockScreenDeviceMotionEffectController setPosterClientDeviceMotionMode:];
-[SBLockScreenDeviceMotionEffectController _acquireNoUserPresenceDeviceMotionDisableAssertion];
-[SBLockScreenDeviceMotionEffectController _updateClientWantsMotionEventState];
-[SBLockScreenDeviceMotionEffectController setPosterClientWantsMotionEvents:];
-[SBLockScreenDeviceMotionEffectController initWithWallpaperController:backlightController:displayLayoutPublisher:deviceMotionDisableAssertionManager:];
-[SBLockScreenDeviceMotionEffectController performanceOptimizationUpdateQueue];
-[SBLockScreenDeviceMotionEffectController deviceMotionDisableAssertionManager:didDisableDeviceMotion:];
-[SBLockScreenDeviceMotionEffectController setWallpaperController:];
-[SBLockScreenDeviceMotionEffectController posterDidUpdateWantsMotionEvents:];
-[SBLockScreenDeviceMotionEffectController settings:changedValueForKeyPath:];
-[SBLockScreenDeviceMotionEffectController _acquireLowPowerDeviceMotionDisableAssertion];
-[SBLockScreenDeviceMotionEffectController setWallpaperVisible:];
-[SBLockScreenDeviceMotionEffectController posterDidUpdateDeviceMotionMode:];
```
