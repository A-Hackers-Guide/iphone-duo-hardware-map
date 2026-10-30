# `SBAppSwitcherReusableSnapshotView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherWallpaperPageContentView`
- Protocols: `SBAppSwitcherSnapshotImageCacheObserver`, `SBApplicationAppProtectionAssistantObserver`, `SBReusableView`, `SBAppSwitcherPageContentView`
- 27 instance variables, 13 properties, 66 instance methods, 0 class methods

## Instance variables

```
@"BSUIOrientationTransformWrapperView" _orientationWrapper;
@"SBSwitcherSnapshotImageView" _imageView;
@"UIViewController" _containerViewController;
@"<SBAppSwitcherReusableSnapshotViewDelegate>" _delegate;
@"SBAppSwitcherSnapshotViewState" _snapshotViewState;
@"STBlockingViewController" _blockingViewController;
@"UIViewController" _appProtectionShieldViewController;
@"UIView" _solidColorBackstopView;
@"SBAppSwitcherSnapshotImageCache" _snapshotCache;
@"SBAppSwitcherSnapshotLockoutViewControllerProvider" _lockoutVCProvider;
@"SBAppClipOverlayCoordinator" _appClipOverlayCoordinator;
@"SBAppClipOverlayViewController" _appClipOverlayViewController;
@"SBAppSwitcherSettings" _settings;
@"SBSwitcherWindowManagementContext" _windowManagementContext;
B _shouldUseBrightMaterial;
B _showingIconOverlayView;
B _shouldStretchToBounds;
B _usesNonuniformScaling;
@"NSMutableArray" _deferredSnapshotCrossfadeQueue;
@"SBApplicationController" _applicationController;
@"SBCrossfadeView" _snapshotCrossfadeView;
@"SBSwitcherSnapshotImageView" _fromSnapshotImageView;
@"SBSwitcherSnapshotImageView" _toSnapshotImageView;
@"SBSwitcherItemContainerContentViewBlurAnimator" _snapshotBlurAnimator;
B _active;
B _visible;
@"SBAppLayout" _appLayout;
```

## Properties

```
@property (T@"SBAppLayout",&,N,V_appLayout) appLayout;
@property (TB,N,V_shouldUseBrightMaterial) shouldUseBrightMaterial;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Td,N) cornerRadius;
@property (TQ,N) maskedCorners;
@property (T{CACornerRadii={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}},N) cornerRadii;
@property (Tq,N) orientation;
@property (TB,R,N) contentRequiresGroupOpacity;
@property (TB,N,GisActive,V_active) active;
@property (TB,N,GisVisible,V_visible) visible;
```

## Instance methods

```
-[SBAppSwitcherReusableSnapshotView setOrientation:];
-[SBAppSwitcherReusableSnapshotView _updateCornerRadius];
-[SBAppSwitcherReusableSnapshotView shouldUseBrightMaterial];
-[SBAppSwitcherReusableSnapshotView setVisible:];
-[SBAppSwitcherReusableSnapshotView _configureSnapshotImageView:cacheEntry:];
-[SBAppSwitcherReusableSnapshotView _doNonUniformScalingForApplication:];
-[SBAppSwitcherReusableSnapshotView _setCacheEntry:];
-[SBAppSwitcherReusableSnapshotView contentRequiresGroupOpacity];
-[SBAppSwitcherReusableSnapshotView _addAppProtectionShieldIfNeeded];
-[SBAppSwitcherReusableSnapshotView setAppLayout:];
-[SBAppSwitcherReusableSnapshotView appLayout];
-[SBAppSwitcherReusableSnapshotView _contentOrientationForSnapshotCacheEntry:];
-[SBAppSwitcherReusableSnapshotView _removeAppProtectionShield];
-[SBAppSwitcherReusableSnapshotView dealloc];
-[SBAppSwitcherReusableSnapshotView _presentedContentSizeForSnapshot:];
-[SBAppSwitcherReusableSnapshotView _frameInLayoutSpaceForRole:inAppLayout:inOrientation:];
-[SBAppSwitcherReusableSnapshotView setShouldStretchToBounds:];
-[SBAppSwitcherReusableSnapshotView setShowingIconOverlayView:];
-[SBAppSwitcherReusableSnapshotView isVisible];
-[SBAppSwitcherReusableSnapshotView _isAnimatingTransition];
-[SBAppSwitcherReusableSnapshotView didUpdateCacheEntry:];
-[SBAppSwitcherReusableSnapshotView layoutSubviews];
-[SBAppSwitcherReusableSnapshotView _addOrRemoveAppProtectionShieldForApplication:];
-[SBAppSwitcherReusableSnapshotView _contentModeForApplication:];
-[SBAppSwitcherReusableSnapshotView setActive:];
-[SBAppSwitcherReusableSnapshotView _isLetterboxedMixedOrientationApplication:];
-[SBAppSwitcherReusableSnapshotView _updateToNewSnapshotImageUsingCacheEntry:];
-[SBAppSwitcherReusableSnapshotView _removeAppClipOverlay];
-[SBAppSwitcherReusableSnapshotView _sceneHandle];
-[SBAppSwitcherReusableSnapshotView hasSceneOverlayView];
-[SBAppSwitcherReusableSnapshotView _handleInstalledAppsChanged:];
-[SBAppSwitcherReusableSnapshotView invalidate];
-[SBAppSwitcherReusableSnapshotView _snapshotUpdateAnimationDuration];
-[SBAppSwitcherReusableSnapshotView appProtectionAssistantShouldShieldDidChange:];
-[SBAppSwitcherReusableSnapshotView _updateContentOrientation];
-[SBAppSwitcherReusableSnapshotView _updateCornerRadiusIfNecessaryForSnapshotImageView:cacheEntry:];
-[SBAppSwitcherReusableSnapshotView prepareForReuse];
-[SBAppSwitcherReusableSnapshotView _cornerRadiiInContentOrientation:];
-[SBAppSwitcherReusableSnapshotView _setAnimatingTransition:];
-[SBAppSwitcherReusableSnapshotView _removeAppLockoutOverlay];
-[SBAppSwitcherReusableSnapshotView initWithDelegate:snapshotCache:lockoutVCProvider:appClipOverlayCoordinator:containerViewController:applicationController:];
-[SBAppSwitcherReusableSnapshotView _supportsMixedOrientation];
-[SBAppSwitcherReusableSnapshotView _cacheEntry];
-[SBAppSwitcherReusableSnapshotView _addAppLockoutOverlayIfNecessary];
-[SBAppSwitcherReusableSnapshotView description];
-[SBAppSwitcherReusableSnapshotView setShouldUseBrightMaterial:];
-[SBAppSwitcherReusableSnapshotView _setSceneHandle:];
-[SBAppSwitcherReusableSnapshotView setUsesNonuniformScaling:];
-[SBAppSwitcherReusableSnapshotView _requestFreshImages];
-[SBAppSwitcherReusableSnapshotView _windowManagementStyleDidChange:];
-[SBAppSwitcherReusableSnapshotView _updateSceneHandle];
-[SBAppSwitcherReusableSnapshotView isActive];
-[SBAppSwitcherReusableSnapshotView _performDeferredSnapshotUpdatesIfNecessary];
-[SBAppSwitcherReusableSnapshotView _addAppClipOverlayForBundleIdentifier:sceneIdentifier:];
-[SBAppSwitcherReusableSnapshotView _reservedStrip];
-[SBAppSwitcherReusableSnapshotView _isSnapshotSuspendSnapshot:];
-[SBAppSwitcherReusableSnapshotView _currentSnapshotImageFrame];
-[SBAppSwitcherReusableSnapshotView setWallpaperStyle:];
-[SBAppSwitcherReusableSnapshotView _updateCornerRadiusIfNecessaryForOverlayView:matchCurrentImageView:];
-[SBAppSwitcherReusableSnapshotView _addOverlayViewControllerToOrientationWrapper:];
-[SBAppSwitcherReusableSnapshotView _effectiveWindowScene];
-[SBAppSwitcherReusableSnapshotView _frameForClassicContentOfSize:inRect:];
-[SBAppSwitcherReusableSnapshotView setBlurRadius:withAnimationSettings:updateMode:];
-[SBAppSwitcherReusableSnapshotView setRequiresAnimatableSnapshotUpdates:];
-[SBAppSwitcherReusableSnapshotView _frameForBackstopLayer];
-[SBAppSwitcherReusableSnapshotView _updateTranslucency];
```
