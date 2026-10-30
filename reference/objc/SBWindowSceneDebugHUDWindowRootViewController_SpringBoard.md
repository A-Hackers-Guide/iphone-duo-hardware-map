# `SBWindowSceneDebugHUDWindowRootViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBDisplayContentModeTransitionObserver`, `SBBacklightControllerObserver`, `SBFDevicePoseProviderObserver`
- 8 instance variables, 7 properties, 31 instance methods, 0 class methods

## Instance variables

```
@"SBDebugHUDDefaults" _debugHUDDefaults;
d _debugLabelMaxWidth;
@"UIView" _hingeAngleHUDView;
@"UIView" _zStackHUDView;
@"SBScreenBrightnessDebugHUDView" _brightnessHUDView;
@"SBWindowScene" _windowScene;
@"SBWindowScene" _otherWindowScene;
@"UILabel" _debugLabel;
```

## Properties

```
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (T@"SBWindowScene",W,N,V_otherWindowScene) otherWindowScene;
@property (T@"UILabel",R,N,V_debugLabel) debugLabel;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBWindowSceneDebugHUDWindowRootViewController debugLabel];
-[SBWindowSceneDebugHUDWindowRootViewController backlightController:didTransitionToBacklightState:source:];
-[SBWindowSceneDebugHUDWindowRootViewController backlightController:didUpdateDigitizerDisabled:tapToWakeEnabled:];
-[SBWindowSceneDebugHUDWindowRootViewController setWindowScene:];
-[SBWindowSceneDebugHUDWindowRootViewController displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBWindowSceneDebugHUDWindowRootViewController displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBWindowSceneDebugHUDWindowRootViewController viewDidLoad];
-[SBWindowSceneDebugHUDWindowRootViewController viewDidLayoutSubviews];
-[SBWindowSceneDebugHUDWindowRootViewController poseProvider:didUpdateFromPose:toPose:];
-[SBWindowSceneDebugHUDWindowRootViewController _canShowWhileLocked];
-[SBWindowSceneDebugHUDWindowRootViewController windowScene];
-[SBWindowSceneDebugHUDWindowRootViewController _showsZStackHUD];
-[SBWindowSceneDebugHUDWindowRootViewController _descriptionForScene:orientation:];
-[SBWindowSceneDebugHUDWindowRootViewController _isHingeAngleHUDEnabled];
-[SBWindowSceneDebugHUDWindowRootViewController _layoutBrightnessHUDView];
-[SBWindowSceneDebugHUDWindowRootViewController _layoutHingeAngleHUDView];
-[SBWindowSceneDebugHUDWindowRootViewController _layoutZStackHUDView];
-[SBWindowSceneDebugHUDWindowRootViewController _setUpBrightnessHUDView];
-[SBWindowSceneDebugHUDWindowRootViewController _setUpHingeAngleHUDView];
-[SBWindowSceneDebugHUDWindowRootViewController _setUpZStackHUDView];
-[SBWindowSceneDebugHUDWindowRootViewController _showsBrightnessHUD];
-[SBWindowSceneDebugHUDWindowRootViewController _showsDevicePoseHUD];
-[SBWindowSceneDebugHUDWindowRootViewController _tearDownBrightnessHUDView];
-[SBWindowSceneDebugHUDWindowRootViewController _tearDownDebugLabel];
-[SBWindowSceneDebugHUDWindowRootViewController _tearDownHingeAngleHUDView];
-[SBWindowSceneDebugHUDWindowRootViewController _tearDownZStackHUDView];
-[SBWindowSceneDebugHUDWindowRootViewController _updateDebugLabel];
-[SBWindowSceneDebugHUDWindowRootViewController initWithDebugHUDDefaults:];
-[SBWindowSceneDebugHUDWindowRootViewController otherWindowScene];
-[SBWindowSceneDebugHUDWindowRootViewController setOtherWindowScene:];
-[SBWindowSceneDebugHUDWindowRootViewController updateHUDsForCurrentDefaults];
```
