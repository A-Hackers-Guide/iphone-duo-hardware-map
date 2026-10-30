# `SBWindowSceneStatusBarManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIStatusBarManager`
- Protocols: `PBUIWallpaperObserver`, `PTSettingsKeyObserver`, `BSDescriptionProviding`, `SBWindowSceneAttachmentObserving`
- 15 instance variables, 19 properties, 67 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
@"UIStatusBarWindow" _statusBarWindow;
@"UIStatusBar" _statusBar;
@"UITapGestureRecognizer" _statusBarSingleTapGestureRecognizer;
@"NSMutableDictionary" _globalAvoidanceFrames;
@"NSMapTable" _instanceAvoidanceFrames;
@"NSMutableDictionary" _globalOcclusionFrames;
@"NSMapTable" _instanceOcclusionFrames;
@"NSHashTable" _observers;
@"NSHashTable" _homeScreenLegibilityObservers;
@"_UILegibilitySettings" _currentHomeScreenLegibilitySettings;
@"SBWindowSceneStatusBarSettingsAssertion" _currentHomeScreenLegibilitySettingsAssertion;
@"SBWindowSceneStatusBarAssertionManager" _assertionManager;
@"SBWindowSceneStatusBarLayoutManager" _layoutManager;
@"SBStatusBarReusePool" _reusePool;
```

## Properties

```
@property (T@"NSHashTable",R,N,G_homeScreenLegibilityObservers) homeScreenLegibilityObservers;
@property (T@"_UILegibilitySettings",&,N,G_currentHomeScreenLegibilitySettings,S_setCurrentHomeScreenLegibilitySettings:) currentHomeScreenLegibilitySettings;
@property (T@"SBWindowSceneStatusBarSettingsAssertion",&,N,G_currentHomeScreenLegibilitySettingsAssertion,S_setCurrentHomeScreenLegibilitySettingsAssertion:) currentHomeScreenLegibilitySettingsAssertion;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIStatusBarWindow",R,N,V_statusBarWindow) statusBarWindow;
@property (T@"UIStatusBar",R,N,V_statusBar) statusBar;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) statusBarWindowFrame;
@property (T@"SBWindowSceneStatusBarAssertionManager",R,N,V_assertionManager) assertionManager;
@property (T@"SBWindowSceneStatusBarLayoutManager",R,N,V_layoutManager) layoutManager;
@property (T@"SBStatusBarReusePool",R,N,V_reusePool) reusePool;
@property (Tq,N) statusBarOrientation;
@property (TB,R,N,GisStatusBarEffectivelyHidden) statusBarEffectivelyHidden;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBWindowSceneStatusBarManager wallpaperDidChangeForVariant:];
-[SBWindowSceneStatusBarManager statusBar];
-[SBWindowSceneStatusBarManager setStatusBarOrientation:];
-[SBWindowSceneStatusBarManager defaultStatusBarFrame];
-[SBWindowSceneStatusBarManager _updateLegibility];
-[SBWindowSceneStatusBarManager statusBarEdgeInOrientation:];
-[SBWindowSceneStatusBarManager statusBarFrameWithinBounds:extent:inOrientation:];
-[SBWindowSceneStatusBarManager wallpaperController];
-[SBWindowSceneStatusBarManager sbf_addObserver:];
-[SBWindowSceneStatusBarManager leadingStatusBarStyleRequest];
-[SBWindowSceneStatusBarManager trailingStatusBarStyleRequest];
-[SBWindowSceneStatusBarManager assertionManager];
-[SBWindowSceneStatusBarManager statusBarLayoutFrameWithinBounds:extent:inOrientation:];
-[SBWindowSceneStatusBarManager _setCurrentHomeScreenLegibilitySettingsAssertion:];
-[SBWindowSceneStatusBarManager succinctDescriptionBuilder];
-[SBWindowSceneStatusBarManager updateHomeScreenStatusBarLegibility];
-[SBWindowSceneStatusBarManager statusBarAxisForPreferredAxis:inOrientation:];
-[SBWindowSceneStatusBarManager addHomeScreenStatusBarLegibilityObserver:];
-[SBWindowSceneStatusBarManager _stopObservingLegibilityChanges];
-[SBWindowSceneStatusBarManager sbf_requestLockScreenStatusBarModeAssertionWithReason:isForAOD:];
-[SBWindowSceneStatusBarManager windowSceneDidDisconnect:];
-[SBWindowSceneStatusBarManager layoutManager];
-[SBWindowSceneStatusBarManager reusePool];
-[SBWindowSceneStatusBarManager statusBarLayoutFrameInOrientation:];
-[SBWindowSceneStatusBarManager _combineFrame:withFrame:];
-[SBWindowSceneStatusBarManager _legibilitySettings];
-[SBWindowSceneStatusBarManager removeHomeScreenStatusBarLegibilityObserver:];
-[SBWindowSceneStatusBarManager statusBarAxisForPreferredAxis:];
-[SBWindowSceneStatusBarManager descriptionWithMultilinePrefix:];
-[SBWindowSceneStatusBarManager _setCurrentHomeScreenLegibilitySettings:];
-[SBWindowSceneStatusBarManager initWithScene:];
-[SBWindowSceneStatusBarManager settings:changedValueForKey:];
-[SBWindowSceneStatusBarManager _statusBarSingleTapped:];
-[SBWindowSceneStatusBarManager frontmostStatusBarStyleRequest];
-[SBWindowSceneStatusBarManager statusBarWindowFrame];
-[SBWindowSceneStatusBarManager succinctDescription];
-[SBWindowSceneStatusBarManager _homeScreenLegibilityObservers];
-[SBWindowSceneStatusBarManager occlusionFrameForStatusBar:];
-[SBWindowSceneStatusBarManager statusBarInsetsForExtent:inOrientation:];
-[SBWindowSceneStatusBarManager _preferredContentSizeDidChange:];
-[SBWindowSceneStatusBarManager sbf_supportsObservation];
-[SBWindowSceneStatusBarManager setOcclusionFrame:reason:statusBar:animationSettings:options:];
-[SBWindowSceneStatusBarManager isStatusBarEffectivelyHidden];
-[SBWindowSceneStatusBarManager _preferredStatusBarAutoresizingMask];
-[SBWindowSceneStatusBarManager _isEmbeddedDisplay];
-[SBWindowSceneStatusBarManager setOcclusionFrame:reason:statusBar:animationSettings:];
-[SBWindowSceneStatusBarManager _transientOverlayPresentationManagerActiveStatusBarStyleRequest];
-[SBWindowSceneStatusBarManager _globalOcclusionFrame];
-[SBWindowSceneStatusBarManager _avoidanceFrameClampedToMaximumOcclusionFrame:];
-[SBWindowSceneStatusBarManager description];
-[SBWindowSceneStatusBarManager _startObservingLegibilityChanges];
-[SBWindowSceneStatusBarManager statusBarOrientation];
-[SBWindowSceneStatusBarManager _setUpStatusBarSingleTapGestureRecognizerIfNeeded];
-[SBWindowSceneStatusBarManager statusBarFrame];
-[SBWindowSceneStatusBarManager sbf_removeObserver:];
-[SBWindowSceneStatusBarManager _applyAvoidanceFrameToStatusBar:withGlobalAvoidanceFrame:animationSettings:reason:options:];
-[SBWindowSceneStatusBarManager windowSceneDidConnect:];
-[SBWindowSceneStatusBarManager statusBarWindow];
-[SBWindowSceneStatusBarManager _currentHomeScreenLegibilitySettingsAssertion];
-[SBWindowSceneStatusBarManager _currentHomeScreenLegibilitySettings];
-[SBWindowSceneStatusBarManager wallpaperLegibilitySettingsDidChange:forVariant:];
-[SBWindowSceneStatusBarManager setAvoidanceFrame:reason:statusBar:animationSettings:];
-[SBWindowSceneStatusBarManager avoidanceFrameForStatusBar:];
-[SBWindowSceneStatusBarManager defaultStatusBarLayoutFrame];
-[SBWindowSceneStatusBarManager _globalAvoidanceFrame];
-[SBWindowSceneStatusBarManager descriptionBuilderWithMultilinePrefix:];
-[SBWindowSceneStatusBarManager setAvoidanceFrame:reason:statusBar:animationSettings:options:];
```
