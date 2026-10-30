# `SBFullScreenAlwaysLiveLiveContentOverlay`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`, `SBDeviceApplicationSceneHandleObserver`, `SBSceneViewPresentationConfiguring`, `SBFullScreenSwitcherSceneLiveContentOverlay`
- 14 instance variables, 20 properties, 63 instance methods, 0 class methods

## Instance variables

```
@"BSUIOrientationTransformWrapperView" _transformWrapperView;
@"SBDeviceApplicationSceneHandle" _sceneHandle;
@"UIApplicationSceneSettingsDiffInspector" _sceneSettingsInspector;
@"SBDeviceApplicationSceneView" _sceneView;
{UIRectCornerRadii="topLeft"d"bottomLeft"d"bottomRight"d"topRight"d} _cornerRadii;
B _asyncRenderingEnabled;
B _resizesHostedContext;
B _shouldPreventFlatteningUnoccludedScenes;
B _disableFlattening;
B _wantsEnhancedWindowingEnabled;
B _maximized;
@"<SBSwitcherLiveContentOverlayDelegate>" _delegate;
q _activeAppearance;
q _containerOrientation;
```

## Properties

```
@property (Tq,N,V_containerOrientation) containerOrientation;
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
@property (Tq,N) preferredLandscapeSceneBarPosition;
@property (TQ,N) preferredHingeEdge;
@property (TB,R,N) requiresLegacyRotationSupport;
@property (Tq,R,N) touchBehavior;
@property (TB,N,GisMaximized,V_maximized) maximized;
@property (T{UIRectCornerRadii=dddd},N) cornerRadii;
@property (Tq,N,V_activeAppearance) activeAppearance;
@property (TB,N,GisDisplayLayoutElementActive) displayLayoutElementActive;
```

## Instance methods

```
-[SBFullScreenAlwaysLiveLiveContentOverlay cornerRadii];
-[SBFullScreenAlwaysLiveLiveContentOverlay containerOrientation];
-[SBFullScreenAlwaysLiveLiveContentOverlay resizesHostedContext];
-[SBFullScreenAlwaysLiveLiveContentOverlay setUsesBrightSceneViewBackgroundMaterial:];
-[SBFullScreenAlwaysLiveLiveContentOverlay setDisplayLayoutElementActive:];
-[SBFullScreenAlwaysLiveLiveContentOverlay noteKeyboardFocusDidChangeToSceneID:];
-[SBFullScreenAlwaysLiveLiveContentOverlay setOcclusionState:inSteadyState:];
-[SBFullScreenAlwaysLiveLiveContentOverlay setWantsEnhancedWindowingEnabled:];
-[SBFullScreenAlwaysLiveLiveContentOverlay preferredInterfaceOrientation];
-[SBFullScreenAlwaysLiveLiveContentOverlay updateDisplayLayoutElementWithBuilder:];
-[SBFullScreenAlwaysLiveLiveContentOverlay isMaximized];
-[SBFullScreenAlwaysLiveLiveContentOverlay setResizesHostedContext:];
-[SBFullScreenAlwaysLiveLiveContentOverlay setPreferredHingeEdge:];
-[SBFullScreenAlwaysLiveLiveContentOverlay noteGeometryMayHaveChanged];
-[SBFullScreenAlwaysLiveLiveContentOverlay overlaySceneHandle];
-[SBFullScreenAlwaysLiveLiveContentOverlay preferredHingeEdge];
-[SBFullScreenAlwaysLiveLiveContentOverlay setContainerOrientation:];
-[SBFullScreenAlwaysLiveLiveContentOverlay supportedInterfaceOrientations];
-[SBFullScreenAlwaysLiveLiveContentOverlay setShouldPreventFlatteningUnoccludedScenes:];
-[SBFullScreenAlwaysLiveLiveContentOverlay sceneHandle:didUpdateSettingsWithDiff:previousSettings:];
-[SBFullScreenAlwaysLiveLiveContentOverlay setPreferredLandscapeSceneBarPosition:];
-[SBFullScreenAlwaysLiveLiveContentOverlay contentViewController];
-[SBFullScreenAlwaysLiveLiveContentOverlay isAsyncRenderingEnabled];
-[SBFullScreenAlwaysLiveLiveContentOverlay activeAppearance];
-[SBFullScreenAlwaysLiveLiveContentOverlay setCornerRadii:];
-[SBFullScreenAlwaysLiveLiveContentOverlay setMatchMovedToScene:];
-[SBFullScreenAlwaysLiveLiveContentOverlay liveSceneIdentityToken];
-[SBFullScreenAlwaysLiveLiveContentOverlay prepareOverlayForContentRotation];
-[SBFullScreenAlwaysLiveLiveContentOverlay setAsyncRenderingEnabled:withMinificationFilterEnabled:];
-[SBFullScreenAlwaysLiveLiveContentOverlay setBlurViewIconScale:];
-[SBFullScreenAlwaysLiveLiveContentOverlay preferredLandscapeSceneBarPosition];
-[SBFullScreenAlwaysLiveLiveContentOverlay updateWindowControlsLayout:];
-[SBFullScreenAlwaysLiveLiveContentOverlay updateTopAffordanceContextMenuWithOptions:selectedActionType:layout:hidden:interfaceOrientation:];
-[SBFullScreenAlwaysLiveLiveContentOverlay invalidate];
-[SBFullScreenAlwaysLiveLiveContentOverlay contentOverlayView];
-[SBFullScreenAlwaysLiveLiveContentOverlay setDelegate:];
-[SBFullScreenAlwaysLiveLiveContentOverlay setDimmed:];
-[SBFullScreenAlwaysLiveLiveContentOverlay touchBehavior];
-[SBFullScreenAlwaysLiveLiveContentOverlay setStatusBarHidden:nubViewHidden:animator:];
-[SBFullScreenAlwaysLiveLiveContentOverlay disableFlattening];
-[SBFullScreenAlwaysLiveLiveContentOverlay wantsEnhancedWindowingEnabled];
-[SBFullScreenAlwaysLiveLiveContentOverlay isContentUpdating];
-[SBFullScreenAlwaysLiveLiveContentOverlay configureWithWorkspaceEntity:referenceFrame:contentOrientation:containerOrientation:layoutRole:sbsDisplayLayoutRole:zOrderIndex:spaceConfiguration:floatingConfiguration:hasClassicAppOrientationMismatch:sizingPolicy:resetsSceneViewDisplayMode:];
-[SBFullScreenAlwaysLiveLiveContentOverlay delegate];
-[SBFullScreenAlwaysLiveLiveContentOverlay setDisableFlattening:];
-[SBFullScreenAlwaysLiveLiveContentOverlay backgroundActivitiesToSuppress];
-[SBFullScreenAlwaysLiveLiveContentOverlay windowControlsView];
-[SBFullScreenAlwaysLiveLiveContentOverlay leadingStatusBarStyle];
-[SBFullScreenAlwaysLiveLiveContentOverlay sceneViewPresentationPriority:];
-[SBFullScreenAlwaysLiveLiveContentOverlay currentStatusBarStyleAttributes];
-[SBFullScreenAlwaysLiveLiveContentOverlay isDisplayLayoutElementActive];
-[SBFullScreenAlwaysLiveLiveContentOverlay disableAsynchronousRenderingForNextCommit];
-[SBFullScreenAlwaysLiveLiveContentOverlay setTouchBehavior:];
-[SBFullScreenAlwaysLiveLiveContentOverlay currentStatusBarHeight];
-[SBFullScreenAlwaysLiveLiveContentOverlay setLiveContentBlurEnabled:duration:blurDelay:iconViewScale:began:completion:];
-[SBFullScreenAlwaysLiveLiveContentOverlay trailingStatusBarStyle];
-[SBFullScreenAlwaysLiveLiveContentOverlay shouldPreventFlatteningUnoccludedScenes];
-[SBFullScreenAlwaysLiveLiveContentOverlay setActiveAppearance:];
-[SBFullScreenAlwaysLiveLiveContentOverlay overlayType];
-[SBFullScreenAlwaysLiveLiveContentOverlay setMaximized:];
-[SBFullScreenAlwaysLiveLiveContentOverlay requiresLegacyRotationSupport];
-[SBFullScreenAlwaysLiveLiveContentOverlay sceneViewPresentationIdentifier:];
-[SBFullScreenAlwaysLiveLiveContentOverlay initWithSceneHandle:referenceSize:containerOrientation:];
```
