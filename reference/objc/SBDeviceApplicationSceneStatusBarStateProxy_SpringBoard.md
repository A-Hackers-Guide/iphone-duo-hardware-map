# `SBDeviceApplicationSceneStatusBarStateProxy`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDeviceApplicationSceneStatusBarStateProvider_Base`
- Protocols: `SBDeviceApplicationSceneStatusBarStateObserver`, `SBDeviceApplicationSceneStatusBarStateProviderBaseSubclassesMustOverride`, `BSInvalidatable`
- 2 instance variables, 4 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"SBDeviceApplicationSceneStatusBarStateProvider" _stateProvider;
@"SBDeviceApplicationSceneHandle" _deviceApplicationSceneHandle;
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
-[SBDeviceApplicationSceneStatusBarStateProxy sceneWithIdentifier:didChangeBackgroundActivitiesToSuppressTo:];
-[SBDeviceApplicationSceneStatusBarStateProxy statusBarAvoidanceFrame];
-[SBDeviceApplicationSceneStatusBarStateProxy sceneWithIdentifier:didChangeStatusBarAlphaTo:];
-[SBDeviceApplicationSceneStatusBarStateProxy sceneWithIdentifier:didChangeStatusBarStyleTo:];
-[SBDeviceApplicationSceneStatusBarStateProxy statusBarSceneIdentifier];
-[SBDeviceApplicationSceneStatusBarStateProxy breadcrumbProvider];
-[SBDeviceApplicationSceneStatusBarStateProxy _statusBarAlpha];
-[SBDeviceApplicationSceneStatusBarStateProxy sceneWithIdentifier:didChangeStatusBarStyleTo:forPartWithIdentifier:];
-[SBDeviceApplicationSceneStatusBarStateProxy _suppressInheritedPartStyles];
-[SBDeviceApplicationSceneStatusBarStateProxy sceneWithIdentifier:didChangeSceneInterfaceOrientationTo:];
-[SBDeviceApplicationSceneStatusBarStateProxy _statusBarPartStyles];
-[SBDeviceApplicationSceneStatusBarStateProxy _anyObserverWants:];
-[SBDeviceApplicationSceneStatusBarStateProxy classicApplicationSceneHandleIfExists];
-[SBDeviceApplicationSceneStatusBarStateProxy invalidate];
-[SBDeviceApplicationSceneStatusBarStateProxy _statusBarAppearsOutsideOfAJailedApp];
-[SBDeviceApplicationSceneStatusBarStateProxy sceneWithIdentifier:didChangeStatusBarAvoidanceFrameTo:];
-[SBDeviceApplicationSceneStatusBarStateProxy sceneWithIdentifier:didChangeStatusBarOrientationTo:];
-[SBDeviceApplicationSceneStatusBarStateProxy sceneToHandleStatusBarTapIfExists];
-[SBDeviceApplicationSceneStatusBarStateProxy _defaultStatusBarStyle];
-[SBDeviceApplicationSceneStatusBarStateProxy backgroundActivitiesToSuppress];
-[SBDeviceApplicationSceneStatusBarStateProxy overlayStatusBarData];
-[SBDeviceApplicationSceneStatusBarStateProxy sceneWantsDeviceOrientationEventsEnabled];
-[SBDeviceApplicationSceneStatusBarStateProxy _statusBarOrientationGivenFallbackOrientation:];
-[SBDeviceApplicationSceneStatusBarStateProxy _statusBarStyleForPartWithIdentifier:suppressingInherited:];
-[SBDeviceApplicationSceneStatusBarStateProxy didInvalidateStatusBarDescriptionForSceneWithIdentifier:];
-[SBDeviceApplicationSceneStatusBarStateProxy sceneWithIdentifier:didChangeStatusBarHiddenTo:withAnimation:];
-[SBDeviceApplicationSceneStatusBarStateProxy _fallbackInterfaceOrientation];
-[SBDeviceApplicationSceneStatusBarStateProxy _statusBarStyle];
-[SBDeviceApplicationSceneStatusBarStateProxy _jailedAppControlsVisibilityOfStatusBarAppearingOutside];
-[SBDeviceApplicationSceneStatusBarStateProxy _statusBarAxis];
-[SBDeviceApplicationSceneStatusBarStateProxy invalidateStatusBarSettings];
-[SBDeviceApplicationSceneStatusBarStateProxy _statusBarHiddenGivenFallbackOrientation:];
-[SBDeviceApplicationSceneStatusBarStateProxy initWithDeviceApplicationSceneHandle:];
-[SBDeviceApplicationSceneStatusBarStateProxy sceneWithIdentifier:didChangeStatusBarAxisTo:withAnimationParameters:];
```
