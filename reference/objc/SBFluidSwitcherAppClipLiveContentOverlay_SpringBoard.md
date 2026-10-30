# `SBFluidSwitcherAppClipLiveContentOverlay`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBUISizeObservingViewDelegate`, `SBFullScreenSwitcherSceneLiveContentOverlay`, `SBSDisplayLayoutElementProviding`
- 21 instance variables, 21 properties, 67 instance methods, 0 class methods

## Instance variables

```
@"NSString" _bundleIdentifier;
@"NSString" _sceneIdentifier;
@"SBAppClipOverlayViewController" _placeholderViewController;
@"UIStatusBar" _statusBar;
@"SBUISizeObservingView" _containerView;
B _isPendingUpdate;
@"SBSDisplayLayoutElement" _displayLayoutElement;
@"<BSInvalidatable>" _displayLayoutElementAssertion;
@"SBApplicationController" _applicationController;
B _asyncRenderingEnabled;
B _resizesHostedContext;
B _shouldPreventFlatteningUnoccludedScenes;
B _disableFlattening;
B _wantsEnhancedWindowingEnabled;
B _maximized;
q _preferredLandscapeSceneBarPosition;
Q _preferredHingeEdge;
@"<SBSwitcherLiveContentOverlayDelegate>" _delegate;
q _activeAppearance;
@"SBWindowScene" _sbWindowScene;
{UIRectCornerRadii="topLeft"d"bottomLeft"d"bottomRight"d"topRight"d} _cornerRadii;
```

## Properties

```
@property (T@"SBWindowScene",R,W,N,G_sbWindowScene,V_sbWindowScene) sbWindowScene;
@property (T@"UIViewController",R,N) contentViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBSwitcherLiveContentOverlayDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView",R,N) contentOverlayView;
@property (TB,R,N,GisAsyncRenderingEnabled,V_asyncRenderingEnabled) asyncRenderingEnabled;
@property (TB,N,V_wantsEnhancedWindowingEnabled) wantsEnhancedWindowingEnabled;
@property (TB,N,V_resizesHostedContext) resizesHostedContext;
@property (TB,N,V_shouldPreventFlatteningUnoccludedScenes) shouldPreventFlatteningUnoccludedScenes;
@property (TB,N,V_disableFlattening) disableFlattening;
@property (Tq,N,V_preferredLandscapeSceneBarPosition) preferredLandscapeSceneBarPosition;
@property (TQ,N,V_preferredHingeEdge) preferredHingeEdge;
@property (TB,R,N) requiresLegacyRotationSupport;
@property (Tq,R,N) touchBehavior;
@property (TB,N,GisMaximized,V_maximized) maximized;
@property (T{UIRectCornerRadii=dddd},N,V_cornerRadii) cornerRadii;
@property (Tq,N,V_activeAppearance) activeAppearance;
@property (TB,N,GisDisplayLayoutElementActive) displayLayoutElementActive;
```

## Instance methods

```
-[SBFluidSwitcherAppClipLiveContentOverlay cornerRadii];
-[SBFluidSwitcherAppClipLiveContentOverlay resizesHostedContext];
-[SBFluidSwitcherAppClipLiveContentOverlay setUsesBrightSceneViewBackgroundMaterial:];
-[SBFluidSwitcherAppClipLiveContentOverlay setDisplayLayoutElementActive:];
-[SBFluidSwitcherAppClipLiveContentOverlay noteKeyboardFocusDidChangeToSceneID:];
-[SBFluidSwitcherAppClipLiveContentOverlay setOcclusionState:inSteadyState:];
-[SBFluidSwitcherAppClipLiveContentOverlay setWantsEnhancedWindowingEnabled:];
-[SBFluidSwitcherAppClipLiveContentOverlay preferredInterfaceOrientation];
-[SBFluidSwitcherAppClipLiveContentOverlay updateDisplayLayoutElementWithBuilder:];
-[SBFluidSwitcherAppClipLiveContentOverlay isMaximized];
-[SBFluidSwitcherAppClipLiveContentOverlay setResizesHostedContext:];
-[SBFluidSwitcherAppClipLiveContentOverlay setPreferredHingeEdge:];
-[SBFluidSwitcherAppClipLiveContentOverlay noteGeometryMayHaveChanged];
-[SBFluidSwitcherAppClipLiveContentOverlay _installedApplicationsDidChange:];
-[SBFluidSwitcherAppClipLiveContentOverlay overlaySceneHandle];
-[SBFluidSwitcherAppClipLiveContentOverlay preferredHingeEdge];
-[SBFluidSwitcherAppClipLiveContentOverlay supportedInterfaceOrientations];
-[SBFluidSwitcherAppClipLiveContentOverlay setShouldPreventFlatteningUnoccludedScenes:];
-[SBFluidSwitcherAppClipLiveContentOverlay setPreferredLandscapeSceneBarPosition:];
-[SBFluidSwitcherAppClipLiveContentOverlay contentViewController];
-[SBFluidSwitcherAppClipLiveContentOverlay _statusBarReusePool];
-[SBFluidSwitcherAppClipLiveContentOverlay isAsyncRenderingEnabled];
-[SBFluidSwitcherAppClipLiveContentOverlay dealloc];
-[SBFluidSwitcherAppClipLiveContentOverlay activeAppearance];
-[SBFluidSwitcherAppClipLiveContentOverlay setCornerRadii:];
-[SBFluidSwitcherAppClipLiveContentOverlay setMatchMovedToScene:];
-[SBFluidSwitcherAppClipLiveContentOverlay liveSceneIdentityToken];
-[SBFluidSwitcherAppClipLiveContentOverlay prepareOverlayForContentRotation];
-[SBFluidSwitcherAppClipLiveContentOverlay setAsyncRenderingEnabled:withMinificationFilterEnabled:];
-[SBFluidSwitcherAppClipLiveContentOverlay setBlurViewIconScale:];
-[SBFluidSwitcherAppClipLiveContentOverlay preferredLandscapeSceneBarPosition];
-[SBFluidSwitcherAppClipLiveContentOverlay updateWindowControlsLayout:];
-[SBFluidSwitcherAppClipLiveContentOverlay updateTopAffordanceContextMenuWithOptions:selectedActionType:layout:hidden:interfaceOrientation:];
-[SBFluidSwitcherAppClipLiveContentOverlay invalidate];
-[SBFluidSwitcherAppClipLiveContentOverlay contentOverlayView];
-[SBFluidSwitcherAppClipLiveContentOverlay setDelegate:];
-[SBFluidSwitcherAppClipLiveContentOverlay setDimmed:];
-[SBFluidSwitcherAppClipLiveContentOverlay _sbWindowScene];
-[SBFluidSwitcherAppClipLiveContentOverlay touchBehavior];
-[SBFluidSwitcherAppClipLiveContentOverlay setStatusBarHidden:nubViewHidden:animator:];
-[SBFluidSwitcherAppClipLiveContentOverlay disableFlattening];
-[SBFluidSwitcherAppClipLiveContentOverlay wantsEnhancedWindowingEnabled];
-[SBFluidSwitcherAppClipLiveContentOverlay isContentUpdating];
-[SBFluidSwitcherAppClipLiveContentOverlay configureWithWorkspaceEntity:referenceFrame:contentOrientation:containerOrientation:layoutRole:sbsDisplayLayoutRole:zOrderIndex:spaceConfiguration:floatingConfiguration:hasClassicAppOrientationMismatch:sizingPolicy:resetsSceneViewDisplayMode:];
-[SBFluidSwitcherAppClipLiveContentOverlay delegate];
-[SBFluidSwitcherAppClipLiveContentOverlay setDisableFlattening:];
-[SBFluidSwitcherAppClipLiveContentOverlay backgroundActivitiesToSuppress];
-[SBFluidSwitcherAppClipLiveContentOverlay windowControlsView];
-[SBFluidSwitcherAppClipLiveContentOverlay leadingStatusBarStyle];
-[SBFluidSwitcherAppClipLiveContentOverlay currentStatusBarStyleAttributes];
-[SBFluidSwitcherAppClipLiveContentOverlay isDisplayLayoutElementActive];
-[SBFluidSwitcherAppClipLiveContentOverlay disableAsynchronousRenderingForNextCommit];
-[SBFluidSwitcherAppClipLiveContentOverlay setTouchBehavior:];
-[SBFluidSwitcherAppClipLiveContentOverlay currentStatusBarHeight];
-[SBFluidSwitcherAppClipLiveContentOverlay setLiveContentBlurEnabled:duration:blurDelay:iconViewScale:began:completion:];
-[SBFluidSwitcherAppClipLiveContentOverlay trailingStatusBarStyle];
-[SBFluidSwitcherAppClipLiveContentOverlay shouldPreventFlatteningUnoccludedScenes];
-[SBFluidSwitcherAppClipLiveContentOverlay setActiveAppearance:];
-[SBFluidSwitcherAppClipLiveContentOverlay overlayType];
-[SBFluidSwitcherAppClipLiveContentOverlay setMaximized:];
-[SBFluidSwitcherAppClipLiveContentOverlay requiresLegacyRotationSupport];
-[SBFluidSwitcherAppClipLiveContentOverlay sizeObservingView:didChangeSize:];
-[SBFluidSwitcherAppClipLiveContentOverlay _beginPollingUpdateStillAvailable];
-[SBFluidSwitcherAppClipLiveContentOverlay _createAndConfigureStatusBar];
-[SBFluidSwitcherAppClipLiveContentOverlay _launchApplication:];
-[SBFluidSwitcherAppClipLiveContentOverlay initWithPlaceholderEntity:windowScene:applicationController:];
-[SBFluidSwitcherAppClipLiveContentOverlay setContentReferenceSize:interfaceOrientation:];
```
