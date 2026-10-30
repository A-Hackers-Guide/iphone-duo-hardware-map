# `SBManagedDisplayController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBacklightControllerObserver`, `SBDisplayContentModeTransitionObserver`, `SBRecordingIndicatorDisplayPowerManagerDelegate`, `SBWindowSceneAttachmentObserving`
- 3 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"SBRecordingIndicatorDisplayPowerManager" _indicatorDisplayPowerManager;
@"NSNumber" _maximumFrameRate;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (T@"NSNumber",C,N,V_maximumFrameRate) maximumFrameRate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBManagedDisplayController backlightController:didTransitionToBacklightState:source:];
-[SBManagedDisplayController setMaximumFrameRate:];
-[SBManagedDisplayController maximumFrameRate];
-[SBManagedDisplayController setWindowScene:];
-[SBManagedDisplayController windowSceneDidDisconnect:];
-[SBManagedDisplayController displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBManagedDisplayController displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBManagedDisplayController windowSceneDidConnect:];
-[SBManagedDisplayController windowScene];
-[SBManagedDisplayController _updateDisplayPreferences];
-[SBManagedDisplayController indicatorDisplayPowerManager:didChangeDisplayPowerRequired:];
-[SBManagedDisplayController initWithIndicatorDisplayPowerManager:];
```
