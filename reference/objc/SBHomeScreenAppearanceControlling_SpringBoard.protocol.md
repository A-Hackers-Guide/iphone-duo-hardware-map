# `SBHomeScreenAppearanceControlling` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 25 instance methods, 0 class methods

## Properties

```
@property (T@"SBWindow",R,N) window;
@property (T@"SBWindow",R,N) folderWindow;
@property (TB,R,N,GisRotationSupported) rotationSupported;
@property (T@"UIView",R,N) homeScreenContentView;
@property (T@"UIView",R,N) homeScreenScalingView;
@property (TB,R,N,GisHomeScreenScaleOwnedByPulldownGesture) homeScreenScaleOwnedByPulldownGesture;
```

## Instance methods

```
-[SBHomeScreenAppearanceControlling endRequiringBackdropViewForReason:];
-[SBHomeScreenAppearanceControlling beginRequiringLiveBackdropViewForReason:];
-[SBHomeScreenAppearanceControlling isHomeScreenScaleOwnedByPulldownGesture];
-[SBHomeScreenAppearanceControlling endRequiringLiveBackdropViewForReason:];
-[SBHomeScreenAppearanceControlling beginRequiringBackdropViewForReason:];
-[SBHomeScreenAppearanceControlling setHomeScreenDimmingAlpha:settings:behaviorMode:completion:];
-[SBHomeScreenAppearanceControlling cancelInProcessAnimations];
-[SBHomeScreenAppearanceControlling homeScreenContentView];
-[SBHomeScreenAppearanceControlling endRequiringContentForReason:];
-[SBHomeScreenAppearanceControlling beginRequiringContentForReason:options:];
-[SBHomeScreenAppearanceControlling beginRequiringContentForReason:];
-[SBHomeScreenAppearanceControlling setHomeScreenBackdropBlurMaterialRecipeName:behaviorMode:completion:];
-[SBHomeScreenAppearanceControlling window];
-[SBHomeScreenAppearanceControlling restoreContentAndUnscatterIconsAnimated:withCompletion:];
-[SBHomeScreenAppearanceControlling setHomeScreenScale:settings:behaviorMode:completion:];
-[SBHomeScreenAppearanceControlling folderWindow];
-[SBHomeScreenAppearanceControlling setHomeScreenBlurProgress:behaviorMode:completion:];
-[SBHomeScreenAppearanceControlling isBackdropVisible];
-[SBHomeScreenAppearanceControlling isRotationSupported];
-[SBHomeScreenAppearanceControlling setHomeScreenAlpha:dockAlpha:includeDock:behaviorMode:completion:];
-[SBHomeScreenAppearanceControlling restoreContentAndUnscatterIconsAnimated:];
-[SBHomeScreenAppearanceControlling homeScreenScalingView];
-[SBHomeScreenAppearanceControlling restoreContentAndUnscatterIconsAnimated:afterDelay:withCompletion:];
-[SBHomeScreenAppearanceControlling setHomeScreenTranslation:behaviorMode:completion:];
-[SBHomeScreenAppearanceControlling isIconListViewTornDown];
```
