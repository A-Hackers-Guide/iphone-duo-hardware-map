# `SBDeviceApplicationSceneStatusBarStateProvider_Base`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBApplicationSceneStatusBarDescribingInternal`, `SBDeviceApplicationSceneStatusBarStateProviderBaseSubclassesMustOverride`, `SBApplicationSceneStatusBarDescribing`
- 1 instance variables, 19 properties, 41 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _observers;
```

## Properties

```
@property (Tq,R,N) statusBarStyle;
@property (Tq,R,N) defaultStatusBarStyle;
@property (TB,R,N) statusBarHidden;
@property (Td,R,N) statusBarAlpha;
@property (Tq,R,N) statusBarOrientation;
@property (T@"NSSet",R,N) backgroundActivitiesToSuppress;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) statusBarAvoidanceFrame;
@property (TB,R,N) sceneWantsDeviceOrientationEventsEnabled;
@property (T@"NSString",R,N) statusBarSceneIdentifier;
@property (Tq,R,N) statusBarAxis;
@property (Tq,R,N) preferredStatusBarAxis;
@property (T@"_UIStatusBarData",R,N) overlayStatusBarData;
@property (T@"SBDeviceApplicationSceneStatusBarBreadcrumbProvider",R,N) breadcrumbProvider;
@property (T@"SBDeviceApplicationSceneHandle",R,N) classicApplicationSceneHandleIfExists;
@property (T@"FBScene",R,N) sceneToHandleStatusBarTapIfExists;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDeviceApplicationSceneStatusBarStateProvider_Base statusBarAlpha];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base statusBarAvoidanceFrame];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base statusBarSceneIdentifier];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base succinctDescriptionBuilder];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base statusBarHidden];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base init];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base breadcrumbProvider];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base _statusBarAlpha];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base _suppressInheritedPartStyles];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base enumerateObserversWithBlock:];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base descriptionWithMultilinePrefix:];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base _allObservers];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base _statusBarPartStyles];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base classicApplicationSceneHandleIfExists];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base succinctDescription];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base _statusBarAppearsOutsideOfAJailedApp];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base sceneToHandleStatusBarTapIfExists];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base _defaultStatusBarStyle];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base backgroundActivitiesToSuppress];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base description];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base preferredStatusBarAxis];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base overlayStatusBarData];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base statusBarOrientation];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base sceneWantsDeviceOrientationEventsEnabled];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base _statusBarOrientationGivenFallbackOrientation:];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base _statusBarStyleForPartWithIdentifier:suppressingInherited:];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base statusBarAxis];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base statusBarStyle];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base _fallbackInterfaceOrientation];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base _statusBarStyle];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base _jailedAppControlsVisibilityOfStatusBarAppearingOutside];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base _statusBarAxis];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base _statusBarHiddenGivenFallbackOrientation:];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base defaultStatusBarStyle];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base descriptionBuilderWithMultilinePrefix:];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base statusBarPartStyles];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base SB_conformsToSBApplicationSceneStatusBarDescribing];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base _observerRecords];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base addStatusBarObserver:];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base removeStatusBarObserver:];
-[SBDeviceApplicationSceneStatusBarStateProvider_Base statusBarStyleForPartWithIdentifier:];
```
