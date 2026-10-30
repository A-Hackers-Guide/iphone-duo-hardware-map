# `SBShelfLiveContentOverlay`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSwitcherLiveContentOverlay`, `SBSceneViewPresentationConfiguring`, `SBUISizeObservingViewDelegate`
- 17 instance variables, 22 properties, 63 instance methods, 0 class methods

## Instance variables

```
@"SBDeviceApplicationSceneView" _sceneView;
@"SBUISizeObservingView" _sizeObservingView;
B asyncRenderingEnabled;
B resizesHostedContext;
B shouldPreventFlatteningUnoccludedScenes;
B disableFlattening;
B wantsEnhancedWindowingEnabled;
B maximized;
B _pendingSwitcherSnapshotCacheUpdate;
@"UIView" contentOverlayView;
@"<SBSwitcherLiveContentOverlayDelegate>" delegate;
q preferredLandscapeSceneBarPosition;
Q preferredHingeEdge;
q activeAppearance;
@"SBDeviceApplicationSceneHandle" _sceneHandle;
Q _displayMode;
{UIRectCornerRadii="topLeft"d"bottomLeft"d"bottomRight"d"topRight"d} cornerRadii;
```

## Properties

```
@property (T@"SBDeviceApplicationSceneHandle",R,N,V_sceneHandle) sceneHandle;
@property (TQ,N,V_displayMode) displayMode;
@property (TB,N,GisPendingSwitcherSnapshotCacheUpdate,V_pendingSwitcherSnapshotCacheUpdate) pendingSwitcherSnapshotCacheUpdate;
@property (T@"<SBSwitcherLiveContentOverlayDelegate>",W,N,Vdelegate) delegate;
@property (T@"UIView",R,N,VcontentOverlayView) contentOverlayView;
@property (TB,R,N,GisAsyncRenderingEnabled,VasyncRenderingEnabled) asyncRenderingEnabled;
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
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBShelfLiveContentOverlay cornerRadii];
-[SBShelfLiveContentOverlay resizesHostedContext];
-[SBShelfLiveContentOverlay setUsesBrightSceneViewBackgroundMaterial:];
-[SBShelfLiveContentOverlay setDisplayLayoutElementActive:];
-[SBShelfLiveContentOverlay noteKeyboardFocusDidChangeToSceneID:];
-[SBShelfLiveContentOverlay setOcclusionState:inSteadyState:];
-[SBShelfLiveContentOverlay setWantsEnhancedWindowingEnabled:];
-[SBShelfLiveContentOverlay preferredInterfaceOrientation];
-[SBShelfLiveContentOverlay updateDisplayLayoutElementWithBuilder:];
-[SBShelfLiveContentOverlay sceneHandle];
-[SBShelfLiveContentOverlay isMaximized];
-[SBShelfLiveContentOverlay setResizesHostedContext:];
-[SBShelfLiveContentOverlay setPreferredHingeEdge:];
-[SBShelfLiveContentOverlay noteGeometryMayHaveChanged];
-[SBShelfLiveContentOverlay overlaySceneHandle];
-[SBShelfLiveContentOverlay preferredHingeEdge];
-[SBShelfLiveContentOverlay setDisplayMode:];
-[SBShelfLiveContentOverlay supportedInterfaceOrientations];
-[SBShelfLiveContentOverlay setShouldPreventFlatteningUnoccludedScenes:];
-[SBShelfLiveContentOverlay setPreferredLandscapeSceneBarPosition:];
-[SBShelfLiveContentOverlay isAsyncRenderingEnabled];
-[SBShelfLiveContentOverlay displayMode];
-[SBShelfLiveContentOverlay activeAppearance];
-[SBShelfLiveContentOverlay setCornerRadii:];
-[SBShelfLiveContentOverlay setMatchMovedToScene:];
-[SBShelfLiveContentOverlay liveSceneIdentityToken];
-[SBShelfLiveContentOverlay prepareOverlayForContentRotation];
-[SBShelfLiveContentOverlay setAsyncRenderingEnabled:withMinificationFilterEnabled:];
-[SBShelfLiveContentOverlay setBlurViewIconScale:];
-[SBShelfLiveContentOverlay preferredLandscapeSceneBarPosition];
-[SBShelfLiveContentOverlay updateWindowControlsLayout:];
-[SBShelfLiveContentOverlay updateTopAffordanceContextMenuWithOptions:selectedActionType:layout:hidden:interfaceOrientation:];
-[SBShelfLiveContentOverlay contentOverlayView];
-[SBShelfLiveContentOverlay setDelegate:];
-[SBShelfLiveContentOverlay setDimmed:];
-[SBShelfLiveContentOverlay touchBehavior];
-[SBShelfLiveContentOverlay setStatusBarHidden:nubViewHidden:animator:];
-[SBShelfLiveContentOverlay disableFlattening];
-[SBShelfLiveContentOverlay wantsEnhancedWindowingEnabled];
-[SBShelfLiveContentOverlay isContentUpdating];
-[SBShelfLiveContentOverlay delegate];
-[SBShelfLiveContentOverlay setDisableFlattening:];
-[SBShelfLiveContentOverlay backgroundActivitiesToSuppress];
-[SBShelfLiveContentOverlay windowControlsView];
-[SBShelfLiveContentOverlay leadingStatusBarStyle];
-[SBShelfLiveContentOverlay sceneViewPresentationPriority:];
-[SBShelfLiveContentOverlay currentStatusBarStyleAttributes];
-[SBShelfLiveContentOverlay isDisplayLayoutElementActive];
-[SBShelfLiveContentOverlay disableAsynchronousRenderingForNextCommit];
-[SBShelfLiveContentOverlay setTouchBehavior:];
-[SBShelfLiveContentOverlay currentStatusBarHeight];
-[SBShelfLiveContentOverlay setLiveContentBlurEnabled:duration:blurDelay:iconViewScale:began:completion:];
-[SBShelfLiveContentOverlay trailingStatusBarStyle];
-[SBShelfLiveContentOverlay shouldPreventFlatteningUnoccludedScenes];
-[SBShelfLiveContentOverlay setActiveAppearance:];
-[SBShelfLiveContentOverlay setMaximized:];
-[SBShelfLiveContentOverlay requiresLegacyRotationSupport];
-[SBShelfLiveContentOverlay sizeObservingView:didChangeSize:];
-[SBShelfLiveContentOverlay sceneViewPresentationIdentifier:];
-[SBShelfLiveContentOverlay _updateSceneViewInSideSizeObservingViewIfNecessary];
-[SBShelfLiveContentOverlay initWithSceneHandle:referenceSize:contentOrientation:containerOrientation:livePortalView:];
-[SBShelfLiveContentOverlay isPendingSwitcherSnapshotCacheUpdate];
-[SBShelfLiveContentOverlay setPendingSwitcherSnapshotCacheUpdate:];
```
