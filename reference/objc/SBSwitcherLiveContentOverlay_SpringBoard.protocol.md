# `SBSwitcherLiveContentOverlay` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `SBSDisplayLayoutElementProviding`, `SBTopAffordanceControlling`
- 0 instance variables, 14 properties, 54 instance methods, 0 class methods

## Properties

```
@property (T@"<SBSwitcherLiveContentOverlayDelegate>",W,N) delegate;
@property (T@"UIView",R,N) contentOverlayView;
@property (TB,R,N,GisAsyncRenderingEnabled) asyncRenderingEnabled;
@property (TB,N) wantsEnhancedWindowingEnabled;
@property (TB,N) resizesHostedContext;
@property (TB,N) shouldPreventFlatteningUnoccludedScenes;
@property (TB,N) disableFlattening;
@property (Tq,N) preferredLandscapeSceneBarPosition;
@property (TQ,N) preferredHingeEdge;
@property (TB,R,N) requiresLegacyRotationSupport;
@property (Tq,R,N) touchBehavior;
@property (TB,N,GisMaximized) maximized;
@property (T{UIRectCornerRadii=dddd},N) cornerRadii;
@property (Tq,N) activeAppearance;
```

## Instance methods

```
-[SBSwitcherLiveContentOverlay cornerRadii];
-[SBSwitcherLiveContentOverlay resizesHostedContext];
-[SBSwitcherLiveContentOverlay setUsesBrightSceneViewBackgroundMaterial:];
-[SBSwitcherLiveContentOverlay noteKeyboardFocusDidChangeToSceneID:];
-[SBSwitcherLiveContentOverlay setOcclusionState:inSteadyState:];
-[SBSwitcherLiveContentOverlay setWantsEnhancedWindowingEnabled:];
-[SBSwitcherLiveContentOverlay preferredInterfaceOrientation];
-[SBSwitcherLiveContentOverlay isMaximized];
-[SBSwitcherLiveContentOverlay setResizesHostedContext:];
-[SBSwitcherLiveContentOverlay setPreferredHingeEdge:];
-[SBSwitcherLiveContentOverlay noteGeometryMayHaveChanged];
-[SBSwitcherLiveContentOverlay overlaySceneHandle];
-[SBSwitcherLiveContentOverlay preferredHingeEdge];
-[SBSwitcherLiveContentOverlay supportedInterfaceOrientations];
-[SBSwitcherLiveContentOverlay setShouldPreventFlatteningUnoccludedScenes:];
-[SBSwitcherLiveContentOverlay setPreferredLandscapeSceneBarPosition:];
-[SBSwitcherLiveContentOverlay isAsyncRenderingEnabled];
-[SBSwitcherLiveContentOverlay activeAppearance];
-[SBSwitcherLiveContentOverlay setCornerRadii:];
-[SBSwitcherLiveContentOverlay setMatchMovedToScene:];
-[SBSwitcherLiveContentOverlay liveSceneIdentityToken];
-[SBSwitcherLiveContentOverlay prepareOverlayForContentRotation];
-[SBSwitcherLiveContentOverlay setAsyncRenderingEnabled:withMinificationFilterEnabled:];
-[SBSwitcherLiveContentOverlay setBlurViewIconScale:];
-[SBSwitcherLiveContentOverlay preferredLandscapeSceneBarPosition];
-[SBSwitcherLiveContentOverlay contentOverlayView];
-[SBSwitcherLiveContentOverlay setDelegate:];
-[SBSwitcherLiveContentOverlay setDimmed:];
-[SBSwitcherLiveContentOverlay touchBehavior];
-[SBSwitcherLiveContentOverlay setStatusBarHidden:nubViewHidden:animator:];
-[SBSwitcherLiveContentOverlay disableFlattening];
-[SBSwitcherLiveContentOverlay wantsEnhancedWindowingEnabled];
-[SBSwitcherLiveContentOverlay isContentUpdating];
-[SBSwitcherLiveContentOverlay delegate];
-[SBSwitcherLiveContentOverlay setDisableFlattening:];
-[SBSwitcherLiveContentOverlay backgroundActivitiesToSuppress];
-[SBSwitcherLiveContentOverlay leadingStatusBarStyle];
-[SBSwitcherLiveContentOverlay currentStatusBarStyleAttributes];
-[SBSwitcherLiveContentOverlay disableAsynchronousRenderingForNextCommit];
-[SBSwitcherLiveContentOverlay setTouchBehavior:];
-[SBSwitcherLiveContentOverlay currentStatusBarHeight];
-[SBSwitcherLiveContentOverlay setLiveContentBlurEnabled:duration:blurDelay:iconViewScale:began:completion:];
-[SBSwitcherLiveContentOverlay trailingStatusBarStyle];
-[SBSwitcherLiveContentOverlay shouldPreventFlatteningUnoccludedScenes];
-[SBSwitcherLiveContentOverlay setActiveAppearance:];
-[SBSwitcherLiveContentOverlay setMaximized:];
-[SBSwitcherLiveContentOverlay requiresLegacyRotationSupport];
-[SBSwitcherLiveContentOverlay newSnapshotView];
-[SBSwitcherLiveContentOverlay bestHomeAffordanceOrientationForOrientation:];
-[SBSwitcherLiveContentOverlay hitTestedToTopAffordance:window:];
-[SBSwitcherLiveContentOverlay newPortaledLiveContentOverlayView];
-[SBSwitcherLiveContentOverlay setContentReferenceSize:interfaceOrientation:];
-[SBSwitcherLiveContentOverlay setStatusBarPartAlphas:nubViewHidden:animator:];
-[SBSwitcherLiveContentOverlay updateAppNameVisibilityInActiveLeadingStatusBarWithBlock:];
```
