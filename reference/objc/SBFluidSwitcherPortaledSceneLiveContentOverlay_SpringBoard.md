# `SBFluidSwitcherPortaledSceneLiveContentOverlay`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBUISizeObservingViewDelegate`, `SBFullScreenSwitcherSceneLiveContentOverlay`, `SBSceneViewPresentationConfiguring`
- 17 instance variables, 26 properties, 68 instance methods, 0 class methods

## Instance variables

```
B wantsEnhancedWindowingEnabled;
B resizesHostedContext;
B shouldPreventFlatteningUnoccludedScenes;
B disableFlattening;
B maximized;
@"<SBSwitcherLiveContentOverlayDelegate>" delegate;
q preferredLandscapeSceneBarPosition;
Q preferredHingeEdge;
q activeAppearance;
@"SBDeviceApplicationSceneHandle" _sceneHandle;
q _contentOrientation;
q _containerOrientation;
@"UIView" _livePortalView;
@"SBDeviceApplicationSceneView" _sceneView;
@"SBUISizeObservingView" _sizeObservingView;
{CGSize="width"d"height"d} _referenceSize;
{UIRectCornerRadii="topLeft"d"bottomLeft"d"bottomRight"d"topRight"d} cornerRadii;
```

## Properties

```
@property (T@"SBUISizeObservingView",R,N,V_sizeObservingView) sizeObservingView;
@property (T@"SBDeviceApplicationSceneHandle",R,N,V_sceneHandle) sceneHandle;
@property (T{CGSize=dd},R,N,V_referenceSize) referenceSize;
@property (Tq,R,N,V_contentOrientation) contentOrientation;
@property (Tq,R,N,V_containerOrientation) containerOrientation;
@property (T@"UIView",R,N,V_livePortalView) livePortalView;
@property (T@"SBDeviceApplicationSceneView",R,N,V_sceneView) sceneView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBSwitcherLiveContentOverlayDelegate>",W,N,Vdelegate) delegate;
@property (T@"UIView",R,N) contentOverlayView;
@property (TB,R,N,GisAsyncRenderingEnabled) asyncRenderingEnabled;
@property (TB,N,VwantsEnhancedWindowingEnabled) wantsEnhancedWindowingEnabled;
@property (TB,N,VresizesHostedContext) resizesHostedContext;
@property (TB,N,VshouldPreventFlatteningUnoccludedScenes) shouldPreventFlatteningUnoccludedScenes;
@property (TB,N,VdisableFlattening) disableFlattening;
@property (Tq,N,VpreferredLandscapeSceneBarPosition) preferredLandscapeSceneBarPosition;
@property (TQ,N,VpreferredHingeEdge) preferredHingeEdge;
@property (TB,R,N) requiresLegacyRotationSupport;
@property (Tq,R,N) touchBehavior;
@property (TB,N,GisMaximized,Vmaximized) maximized;
@property (T{UIRectCornerRadii=dddd},N,VcornerRadii) cornerRadii;
@property (Tq,N,VactiveAppearance) activeAppearance;
@property (TB,N,GisDisplayLayoutElementActive) displayLayoutElementActive;
```

## Instance methods

```
-[SBFluidSwitcherPortaledSceneLiveContentOverlay cornerRadii];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay containerOrientation];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay resizesHostedContext];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setUsesBrightSceneViewBackgroundMaterial:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setDisplayLayoutElementActive:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay noteKeyboardFocusDidChangeToSceneID:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setOcclusionState:inSteadyState:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setWantsEnhancedWindowingEnabled:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay preferredInterfaceOrientation];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay updateDisplayLayoutElementWithBuilder:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay sceneHandle];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay isMaximized];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setResizesHostedContext:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setPreferredHingeEdge:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay noteGeometryMayHaveChanged];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay overlaySceneHandle];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay preferredHingeEdge];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay supportedInterfaceOrientations];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setShouldPreventFlatteningUnoccludedScenes:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setPreferredLandscapeSceneBarPosition:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay contentViewController];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay isAsyncRenderingEnabled];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay contentOrientation];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay activeAppearance];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setCornerRadii:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setMatchMovedToScene:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay liveSceneIdentityToken];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay prepareOverlayForContentRotation];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setAsyncRenderingEnabled:withMinificationFilterEnabled:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay sceneView];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay referenceSize];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setBlurViewIconScale:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay preferredLandscapeSceneBarPosition];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay updateWindowControlsLayout:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay updateTopAffordanceContextMenuWithOptions:selectedActionType:layout:hidden:interfaceOrientation:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay invalidate];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay contentOverlayView];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setDelegate:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setDimmed:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay touchBehavior];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setStatusBarHidden:nubViewHidden:animator:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay disableFlattening];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay wantsEnhancedWindowingEnabled];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay isContentUpdating];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay configureWithWorkspaceEntity:referenceFrame:contentOrientation:containerOrientation:layoutRole:sbsDisplayLayoutRole:zOrderIndex:spaceConfiguration:floatingConfiguration:hasClassicAppOrientationMismatch:sizingPolicy:resetsSceneViewDisplayMode:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay delegate];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setDisableFlattening:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay backgroundActivitiesToSuppress];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay windowControlsView];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay leadingStatusBarStyle];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay sceneViewPresentationPriority:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay currentStatusBarStyleAttributes];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay isDisplayLayoutElementActive];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay disableAsynchronousRenderingForNextCommit];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setTouchBehavior:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay currentStatusBarHeight];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setLiveContentBlurEnabled:duration:blurDelay:iconViewScale:began:completion:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay trailingStatusBarStyle];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay shouldPreventFlatteningUnoccludedScenes];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setActiveAppearance:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay overlayType];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay setMaximized:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay requiresLegacyRotationSupport];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay sizeObservingView:didChangeSize:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay sceneViewPresentationIdentifier:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay initWithSceneHandle:referenceSize:contentOrientation:containerOrientation:livePortalView:];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay livePortalView];
-[SBFluidSwitcherPortaledSceneLiveContentOverlay sizeObservingView];
```
