# `SBDeviceApplicationSceneStatusBarStateProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDeviceApplicationSceneStatusBarStateProvider_Base`
- Protocols: `SBDeviceApplicationSceneHandleObserver`, `SBDeviceApplicationSceneStatusBarStateProviderBaseSubclassesMustOverride`, `BSInvalidatable`
- 6 instance variables, 4 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"UIApplicationSceneClientSettingsDiffInspector" _appClientSettingsDiffInspector;
@"UIApplicationSceneSettingsDiffInspector" _appSceneSettingsDiffInspector;
@"SBSUIInCallSceneClientSettingsDiffInspector" _inCallSceneClientSettingsDiffInspector;
B _hasAttemptedInCallSceneClientSettingsDiffInspectorCreation;
@"FBSDisplayIdentity" _currentHostedDisplayIdentity;
@"SBDeviceApplicationSceneHandle" _sceneHandle;
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
-[SBDeviceApplicationSceneStatusBarStateProvider sceneHandle:didUpdateClientSettings:];
-[SBDeviceApplicationSceneStatusBarStateProvider statusBarAvoidanceFrame];
-[SBDeviceApplicationSceneStatusBarStateProvider statusBarSceneIdentifier];
-[SBDeviceApplicationSceneStatusBarStateProvider sceneHandle:didChangeBackgroundActivitiesToSuppress:];
-[SBDeviceApplicationSceneStatusBarStateProvider breadcrumbProvider];
-[SBDeviceApplicationSceneStatusBarStateProvider _statusBarAlpha];
-[SBDeviceApplicationSceneStatusBarStateProvider sceneHandle:didUpdateSettingsWithDiff:previousSettings:];
-[SBDeviceApplicationSceneStatusBarStateProvider _statusBarAppearsOutsideOfAJailedAppInOrientation:];
-[SBDeviceApplicationSceneStatusBarStateProvider dealloc];
-[SBDeviceApplicationSceneStatusBarStateProvider _suppressInheritedPartStyles];
-[SBDeviceApplicationSceneStatusBarStateProvider _statusBarPartStyles];
-[SBDeviceApplicationSceneStatusBarStateProvider _anyObserverWants:];
-[SBDeviceApplicationSceneStatusBarStateProvider _handleStatusBarBackgroundActivitiesToSuppressUpdate];
-[SBDeviceApplicationSceneStatusBarStateProvider classicApplicationSceneHandleIfExists];
-[SBDeviceApplicationSceneStatusBarStateProvider _statusBarAppearsOutsideOfAJailedAppCanChange];
-[SBDeviceApplicationSceneStatusBarStateProvider _initWithSceneHandle:];
-[SBDeviceApplicationSceneStatusBarStateProvider invalidate];
-[SBDeviceApplicationSceneStatusBarStateProvider _statusBarAppearsOutsideOfAJailedApp];
-[SBDeviceApplicationSceneStatusBarStateProvider sceneToHandleStatusBarTapIfExists];
-[SBDeviceApplicationSceneStatusBarStateProvider _defaultStatusBarStyle];
-[SBDeviceApplicationSceneStatusBarStateProvider backgroundActivitiesToSuppress];
-[SBDeviceApplicationSceneStatusBarStateProvider overlayStatusBarData];
-[SBDeviceApplicationSceneStatusBarStateProvider sceneWantsDeviceOrientationEventsEnabled];
-[SBDeviceApplicationSceneStatusBarStateProvider _statusBarOrientationGivenFallbackOrientation:];
-[SBDeviceApplicationSceneStatusBarStateProvider _statusBarStyleForPartWithIdentifier:suppressingInherited:];
-[SBDeviceApplicationSceneStatusBarStateProvider _performUpdateWith:actions:];
-[SBDeviceApplicationSceneStatusBarStateProvider _fallbackInterfaceOrientation];
-[SBDeviceApplicationSceneStatusBarStateProvider _statusBarStyle];
-[SBDeviceApplicationSceneStatusBarStateProvider _jailedAppControlsVisibilityOfStatusBarAppearingOutside];
-[SBDeviceApplicationSceneStatusBarStateProvider _statusBarAxis];
-[SBDeviceApplicationSceneStatusBarStateProvider invalidateStatusBarSettings];
-[SBDeviceApplicationSceneStatusBarStateProvider _statusBarHiddenGivenFallbackOrientation:];
```
