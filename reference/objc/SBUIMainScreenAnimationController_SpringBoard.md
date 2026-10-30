# `SBUIMainScreenAnimationController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBUIWorkspaceAnimationController`
- 2 instance variables, 7 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"<BSInvalidatable>" _wallpaperRequiredAssertion;
@"<BSInvalidatable>" _bannerSuppressionAssertion;
```

## Properties

```
@property (T@"<BSInvalidatable>",&,N,V_wallpaperRequiredAssertion) wallpaperRequiredAssertion;
@property (T@"<BSInvalidatable>",&,N,V_bannerSuppressionAssertion) bannerSuppressionAssertion;
@property (T@"SBWorkspaceTransitionRequest",R,N) transitionRequest;
@property (T@"NSSet",R,C,D,N) toApplicationSceneEntities;
@property (T@"SBDeviceApplicationSceneEntity",R,N) toApplicationSceneEntity;
@property (T@"NSSet",R,C,D,N) fromApplicationSceneEntities;
@property (T@"SBDeviceApplicationSceneEntity",R,N) fromApplicationSceneEntity;
```

## Instance methods

```
-[SBUIMainScreenAnimationController _windowScene];
-[SBUIMainScreenAnimationController _begin];
-[SBUIMainScreenAnimationController initWithTransitionContextProvider:];
-[SBUIMainScreenAnimationController _cleanupAnimation];
-[SBUIMainScreenAnimationController setBannerSuppressionAssertion:];
-[SBUIMainScreenAnimationController bannerSuppressionAssertion];
-[SBUIMainScreenAnimationController __startAnimation];
-[SBUIMainScreenAnimationController __wantsInitialProgressStateChange];
-[SBUIMainScreenAnimationController _dismissBannerAnimated:];
-[SBUIMainScreenAnimationController _getTransitionWindow];
-[SBUIMainScreenAnimationController _primaryAppOrAnyAppFromSet:];
-[SBUIMainScreenAnimationController _shouldDismissBanner];
-[SBUIMainScreenAnimationController fromApplicationSceneEntity];
-[SBUIMainScreenAnimationController initWithWorkspaceTransitionRequest:];
-[SBUIMainScreenAnimationController setWallpaperRequiredAssertion:];
-[SBUIMainScreenAnimationController toApplicationSceneEntity];
-[SBUIMainScreenAnimationController transitionRequest];
-[SBUIMainScreenAnimationController wallpaperRequiredAssertion];
```
