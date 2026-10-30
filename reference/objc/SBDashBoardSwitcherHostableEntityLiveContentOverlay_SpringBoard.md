# `SBDashBoardSwitcherHostableEntityLiveContentOverlay`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFullScreenSwitcherSceneLiveContentOverlay`
- 17 instance variables, 19 properties, 62 instance methods, 0 class methods

## Instance variables

```
@"SBWorkspaceEntity" _entity;
@"SBWindowScene" _sbWindowScene;
@"SBSDisplayLayoutElement" _displayLayoutElement;
@"<BSInvalidatable>" _displayLayoutElementAssertion;
@"<CSHostableEntity>" _hostableEntity;
@"UIViewController<CSHostableEntityContentContaining>" _contentViewController;
B _maximized;
B _asyncRenderingEnabled;
B _wantsEnhancedWindowingEnabled;
B _resizesHostedContext;
B _shouldPreventFlatteningUnoccludedScenes;
B _disableFlattening;
@"<SBSwitcherLiveContentOverlayDelegate>" _delegate;
q _preferredLandscapeSceneBarPosition;
Q _preferredHingeEdge;
q _activeAppearance;
{UIRectCornerRadii="topLeft"d"bottomLeft"d"bottomRight"d"topRight"d} _cornerRadii;
```

## Properties

```
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
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay _sceneIfExists];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay cornerRadii];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay _hostedEntityViewController];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay resizesHostedContext];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setUsesBrightSceneViewBackgroundMaterial:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setDisplayLayoutElementActive:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay noteKeyboardFocusDidChangeToSceneID:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setOcclusionState:inSteadyState:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setWantsEnhancedWindowingEnabled:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay preferredInterfaceOrientation];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay updateDisplayLayoutElementWithBuilder:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay isMaximized];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setResizesHostedContext:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setPreferredHingeEdge:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay noteGeometryMayHaveChanged];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay overlaySceneHandle];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay preferredHingeEdge];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay supportedInterfaceOrientations];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setShouldPreventFlatteningUnoccludedScenes:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setPreferredLandscapeSceneBarPosition:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay contentViewController];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay initWithEntity:windowScene:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay isAsyncRenderingEnabled];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay activeAppearance];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setCornerRadii:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setMatchMovedToScene:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay liveSceneIdentityToken];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay prepareOverlayForContentRotation];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setAsyncRenderingEnabled:withMinificationFilterEnabled:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setBlurViewIconScale:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay preferredLandscapeSceneBarPosition];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay updateWindowControlsLayout:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay updateTopAffordanceContextMenuWithOptions:selectedActionType:layout:hidden:interfaceOrientation:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay invalidate];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay contentOverlayView];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setDelegate:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setDimmed:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay touchBehavior];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setStatusBarHidden:nubViewHidden:animator:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay disableFlattening];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay wantsEnhancedWindowingEnabled];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay isContentUpdating];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay configureWithWorkspaceEntity:referenceFrame:contentOrientation:containerOrientation:layoutRole:sbsDisplayLayoutRole:zOrderIndex:spaceConfiguration:floatingConfiguration:hasClassicAppOrientationMismatch:sizingPolicy:resetsSceneViewDisplayMode:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay delegate];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setDisableFlattening:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay backgroundActivitiesToSuppress];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay windowControlsView];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay leadingStatusBarStyle];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay currentStatusBarStyleAttributes];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay isDisplayLayoutElementActive];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay disableAsynchronousRenderingForNextCommit];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setTouchBehavior:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay currentStatusBarHeight];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setLiveContentBlurEnabled:duration:blurDelay:iconViewScale:began:completion:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay trailingStatusBarStyle];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay shouldPreventFlatteningUnoccludedScenes];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setActiveAppearance:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay overlayType];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay _hostedSceneID];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay _sceneHandleIfExists];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay setMaximized:];
-[SBDashBoardSwitcherHostableEntityLiveContentOverlay requiresLegacyRotationSupport];
```
