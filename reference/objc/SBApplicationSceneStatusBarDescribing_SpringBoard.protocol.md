# `SBApplicationSceneStatusBarDescribing` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 15 properties, 16 instance methods, 0 class methods

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
```

## Instance methods

```
-[SBApplicationSceneStatusBarDescribing statusBarAlpha];
-[SBApplicationSceneStatusBarDescribing statusBarAvoidanceFrame];
-[SBApplicationSceneStatusBarDescribing statusBarSceneIdentifier];
-[SBApplicationSceneStatusBarDescribing statusBarHidden];
-[SBApplicationSceneStatusBarDescribing breadcrumbProvider];
-[SBApplicationSceneStatusBarDescribing classicApplicationSceneHandleIfExists];
-[SBApplicationSceneStatusBarDescribing sceneToHandleStatusBarTapIfExists];
-[SBApplicationSceneStatusBarDescribing backgroundActivitiesToSuppress];
-[SBApplicationSceneStatusBarDescribing preferredStatusBarAxis];
-[SBApplicationSceneStatusBarDescribing overlayStatusBarData];
-[SBApplicationSceneStatusBarDescribing statusBarOrientation];
-[SBApplicationSceneStatusBarDescribing sceneWantsDeviceOrientationEventsEnabled];
-[SBApplicationSceneStatusBarDescribing statusBarAxis];
-[SBApplicationSceneStatusBarDescribing statusBarStyle];
-[SBApplicationSceneStatusBarDescribing defaultStatusBarStyle];
-[SBApplicationSceneStatusBarDescribing statusBarStyleForPartWithIdentifier:];
```
