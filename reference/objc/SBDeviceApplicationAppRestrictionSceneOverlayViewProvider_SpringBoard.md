# `SBDeviceApplicationAppRestrictionSceneOverlayViewProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDeviceApplicationSceneOverlayViewProvider`
- Protocols: `ALRFBScenePreflightObserver`, `FBSceneObserver`, `SBDeviceApplicationSceneHandleObserver`
- 6 instance variables, 4 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"NSString" _sceneIdentifier;
@"FBScene" _scene;
@"UIViewController" _appRestrictionViewController;
B _requiresPreflight;
@"FBScene" _activePreflightScene;
@"<BSInvalidatable>" _keyboardRedirectionAssertion;
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
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider sceneHandle:didDestroyScene:];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider sceneHandle:didCreateScene:];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider priority];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider scene:requiresPreflight:];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider scene:clientDidConnect:];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider _realOverlayViewController];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider noteLiveContentDisableReasonsChanged];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider supportedInterfaceOrientations];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider contentWantsSimplifiedOrientationBehavior];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider _hostWouldPresentLiveContentIfReady];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider initWithSceneHandle:delegate:];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider _activateIfPossible];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider invalidate];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider noteDisplayModeChange:];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider _preflightSupportedInterfaceOrientations];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider _updateActivation];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider _configureForScene:];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider _deactivateIfPossible];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider scene:updatedActivePreflightScene:];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider _makePreflightViewController];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider shouldFollowSceneOrientation];
-[SBDeviceApplicationAppRestrictionSceneOverlayViewProvider _updateKeyboardDeferringRules];
```
