# `SBDeviceApplicationAppClipOverlayViewProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDeviceApplicationSceneOverlayViewProvider`
- Protocols: `SBDeviceApplicationSceneHandleObserver`
- 2 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"SBAppClipOverlayViewController" _appClipViewController;
@"UIApplicationSceneSettingsDiffInspector" _sceneSettingsDiffInspector;
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
-[SBDeviceApplicationAppClipOverlayViewProvider sceneHandle:clientConnectedForScene:];
-[SBDeviceApplicationAppClipOverlayViewProvider sceneHandle:didChangeEffectiveForegroundness:];
-[SBDeviceApplicationAppClipOverlayViewProvider _realOverlayViewController];
-[SBDeviceApplicationAppClipOverlayViewProvider sceneHandle:didUpdateSettingsWithDiff:previousSettings:];
-[SBDeviceApplicationAppClipOverlayViewProvider dealloc];
-[SBDeviceApplicationAppClipOverlayViewProvider initWithSceneHandle:delegate:];
-[SBDeviceApplicationAppClipOverlayViewProvider _activateIfPossible];
-[SBDeviceApplicationAppClipOverlayViewProvider _deactivateIfPossible];
-[SBDeviceApplicationAppClipOverlayViewProvider wantsResignActiveAssertion];
-[SBDeviceApplicationAppClipOverlayViewProvider shouldSuppressKeyboard];
-[SBDeviceApplicationAppClipOverlayViewProvider _updateOverlaySceneActivationState];
```
