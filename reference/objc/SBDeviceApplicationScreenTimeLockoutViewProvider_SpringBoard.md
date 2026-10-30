# `SBDeviceApplicationScreenTimeLockoutViewProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDeviceApplicationSceneOverlayViewProvider`
- Protocols: `SBDeviceApplicationSceneHandleObserver`
- 3 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"STBlockingViewController" _blockingViewController;
B _waitingForPreflight;
B _isActive;
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
-[SBDeviceApplicationScreenTimeLockoutViewProvider sceneHandle:clientConnectedForScene:];
-[SBDeviceApplicationScreenTimeLockoutViewProvider priority];
-[SBDeviceApplicationScreenTimeLockoutViewProvider _realOverlayViewController];
-[SBDeviceApplicationScreenTimeLockoutViewProvider hideContentWithAnimation:completionHandler:];
-[SBDeviceApplicationScreenTimeLockoutViewProvider dealloc];
-[SBDeviceApplicationScreenTimeLockoutViewProvider initWithSceneHandle:delegate:];
-[SBDeviceApplicationScreenTimeLockoutViewProvider _activateIfPossible];
-[SBDeviceApplicationScreenTimeLockoutViewProvider _handleInstalledAppsChanged:];
-[SBDeviceApplicationScreenTimeLockoutViewProvider showContentWithAnimation:completionHandler:];
-[SBDeviceApplicationScreenTimeLockoutViewProvider _blockingViewControllerDismissedItself];
-[SBDeviceApplicationScreenTimeLockoutViewProvider _deactivateIfPossibleRespectingAppBlockedState:];
-[SBDeviceApplicationScreenTimeLockoutViewProvider _newBlockingViewControllerWithBundleIdentifier:];
```
