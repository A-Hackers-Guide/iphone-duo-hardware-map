# `SBDeviceApplicationSceneViewControlling` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `SBApplicationSceneViewControlling`, `SBSceneLayoutStatusBarAssertionProviding`, `SBLayoutStateTransitionObserver`
- 0 instance variables, 11 properties, 34 instance methods, 0 class methods

## Properties

```
@property (T@"UIView<SBApplicationSceneBackgroundView>",&,N) backgroundView;
@property (T@"SBDeviceApplicationSceneHandle",R,N) sceneHandle;
@property (T@"SBHomeGrabberView",R,N) homeGrabberView;
@property (Tq,N) homeGrabberDisplayMode;
@property (T@"NSString",C,N) sceneMinificationFilter;
@property (TB,N) sceneRendersAsynchronously;
@property (TB,N) sceneResizesHostedContext;
@property (TB,N) sceneFullyOccluded;
@property (T@"NSString",C,N) sceneFlattenMode;
@property (T@"UIView",R,N) sceneContentView;
@property (TB,R,N) groupOpacityRequiredForContentAnimation;
```

## Instance methods

```
-[SBDeviceApplicationSceneViewControlling homeGrabberView];
-[SBDeviceApplicationSceneViewControlling sceneHandle];
-[SBDeviceApplicationSceneViewControlling sceneContentView];
-[SBDeviceApplicationSceneViewControlling setSceneFullyOccluded:];
-[SBDeviceApplicationSceneViewControlling didRotateFromInterfaceOrientation:toInterfaceOrientation:];
-[SBDeviceApplicationSceneViewControlling willRotateFromInterfaceOrientation:toInterfaceOrientation:alongsideContainerView:animated:];
-[SBDeviceApplicationSceneViewControlling backgroundView];
-[SBDeviceApplicationSceneViewControlling backgroundActivitiesToSuppress];
-[SBDeviceApplicationSceneViewControlling sceneFullyOccluded];
-[SBDeviceApplicationSceneViewControlling leadingStatusBarStyle];
-[SBDeviceApplicationSceneViewControlling currentStatusBarStyleAttributes];
-[SBDeviceApplicationSceneViewControlling containerDidUpdateTraitsParticipant:];
-[SBDeviceApplicationSceneViewControlling willPerformNonAnimatedTransitionToInterfaceOrientation:];
-[SBDeviceApplicationSceneViewControlling prepareForContentRotation];
-[SBDeviceApplicationSceneViewControlling currentStatusBarHeight];
-[SBDeviceApplicationSceneViewControlling trailingStatusBarStyle];
-[SBDeviceApplicationSceneViewControlling setBackgroundView:];
-[SBDeviceApplicationSceneViewControlling bestHomeAffordanceOrientationForOrientation:];
-[SBDeviceApplicationSceneViewControlling conformsToProtocolSBDeviceApplicationSceneViewControlling];
-[SBDeviceApplicationSceneViewControlling groupOpacityRequiredForContentAnimation];
-[SBDeviceApplicationSceneViewControlling homeGrabberDisplayMode];
-[SBDeviceApplicationSceneViewControlling noteSceneFrameInKeyboardReferenceSpaceMayHaveChanged];
-[SBDeviceApplicationSceneViewControlling prepareForSceneContentMovingToWindowScene:];
-[SBDeviceApplicationSceneViewControlling sceneFlattenMode];
-[SBDeviceApplicationSceneViewControlling sceneMinificationFilter];
-[SBDeviceApplicationSceneViewControlling sceneRendersAsynchronously];
-[SBDeviceApplicationSceneViewControlling sceneResizesHostedContext];
-[SBDeviceApplicationSceneViewControlling scrollToTopXPositionForGestureRecognizer:];
-[SBDeviceApplicationSceneViewControlling setHomeGrabberDisplayMode:];
-[SBDeviceApplicationSceneViewControlling setSceneFlattenMode:];
-[SBDeviceApplicationSceneViewControlling setSceneMinificationFilter:];
-[SBDeviceApplicationSceneViewControlling setSceneRendersAsynchronously:];
-[SBDeviceApplicationSceneViewControlling setSceneResizesHostedContext:];
-[SBDeviceApplicationSceneViewControlling updateAppNameVisibilityInActiveLeadingStatusBarWithBlock:];
```
