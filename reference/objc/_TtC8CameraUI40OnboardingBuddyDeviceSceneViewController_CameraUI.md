# `_TtC8CameraUI40OnboardingBuddyDeviceSceneViewController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SCNSceneRendererDelegate`, `CAStateControllerDelegate`
- 19 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
CameraUI.OnboardingBuddySetupViewModel viewModel;
CameraUI.Stopwatch renderStopwatch;
_$sSo7SCNViewC sceneView;
_$sSo7SCNNodeC cameraNode;
_$sSo7SCNNodeC deviceModelNode;
_$sSo7SCNNodeC buttonRippleEffectOverlayNode;
_$sSD -> CameraUI.OnboardingBuddyDeviceSceneViewController.AnimationStateDescription _$sSo7CAStateC animationStates;
_$sSo17CAStateControllerCSg buttonHighlightStateController;
_$sSo17CAStateControllerCSg demoLoopAnimationStateController;
_$sSo17CAStateControllerCSg buttonGlowAccentAnimationStateController;
_$sSo15CAGradientLayerC graduatedNeutralDensityLayer;
Swift.Bool hasInitialRenderOccurred;
Swift.Bool demoLoopHasStarted;
Swift.Bool paused;
_$sSo8CAFilterCSg progressiveBlurFilter;
_$sSa -> Dispatch.DispatchWorkItem pendingAnimationTimeouts;
_$sSi buttonAnimationCallCount;
_$sSd lastButtonAnimationTime;
_$sSi maxAnimationCallsPerSecond;
```

## Instance methods

```
-[_TtC8CameraUI40OnboardingBuddyDeviceSceneViewController stateController:transitionDidStart:speed:];
-[_TtC8CameraUI40OnboardingBuddyDeviceSceneViewController viewDidLoad];
-[_TtC8CameraUI40OnboardingBuddyDeviceSceneViewController initWithNibName:bundle:];
-[_TtC8CameraUI40OnboardingBuddyDeviceSceneViewController viewDidAppear:];
-[_TtC8CameraUI40OnboardingBuddyDeviceSceneViewController viewDidDisappear:];
-[_TtC8CameraUI40OnboardingBuddyDeviceSceneViewController initWithCoder:];
-[_TtC8CameraUI40OnboardingBuddyDeviceSceneViewController renderer:didRenderScene:atTime:];
```
