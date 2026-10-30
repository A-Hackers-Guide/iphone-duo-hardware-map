# `SBDockToStageZoomWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 10 instance variables, 1 properties, 58 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _transitionID;
@"SBAppLayout" _appLayout;
d _iconCornerRadius;
d _iconScale;
B _wantsResignActiveAndAsyncRenderingAssertions;
B _isAddingToStage;
B _itemContainerOverlapsDock;
B _isHidingDockIcon;
B _shouldDodgeDock;
@"SBAppLayout" _launchingOverDesktopSpaceAppLayout;
```

## Properties

```
@property (T@"SBAppLayout",&,N,V_launchingOverDesktopSpaceAppLayout) launchingOverDesktopSpaceAppLayout;
```

## Instance methods

```
-[SBDockToStageZoomWindowingModifier scaleForIndex:];
-[SBDockToStageZoomWindowingModifier anchorPointForIndex:];
-[SBDockToStageZoomWindowingModifier dockWindowLevelPriority];
-[SBDockToStageZoomWindowingModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBDockToStageZoomWindowingModifier maskedCornersForIndex:];
-[SBDockToStageZoomWindowingModifier dockWindowLevel];
-[SBDockToStageZoomWindowingModifier cornerRadiiForIndex:];
-[SBDockToStageZoomWindowingModifier adjustedSpaceAccessoryViewAnchorPoint:forAppLayout:];
-[SBDockToStageZoomWindowingModifier shouldScaleOverlayToFillBoundsAtIndex:];
-[SBDockToStageZoomWindowingModifier animationAttributesForLayoutElement:];
-[SBDockToStageZoomWindowingModifier adjustedAppLayoutsForAppLayouts:];
-[SBDockToStageZoomWindowingModifier _layoutSettings];
-[SBDockToStageZoomWindowingModifier dockProgress];
-[SBDockToStageZoomWindowingModifier adjustedSpaceAccessoryViewFrame:forAppLayout:];
-[SBDockToStageZoomWindowingModifier topMostLayoutElements];
-[SBDockToStageZoomWindowingModifier appLayoutsForContinuousExposeIdentifier:];
-[SBDockToStageZoomWindowingModifier appLayoutsToCacheSnapshots];
-[SBDockToStageZoomWindowingModifier _normalizedHomeScreenTargetZoomPercentBetweenCenterAndEdge:];
-[SBDockToStageZoomWindowingModifier wantsDockWindowLevelAssertion];
-[SBDockToStageZoomWindowingModifier presentationAttributesForShelf:];
-[SBDockToStageZoomWindowingModifier shouldPinLayoutRolesToSpace:];
-[SBDockToStageZoomWindowingModifier transitionDidUpdate:];
-[SBDockToStageZoomWindowingModifier visibleAppLayouts];
-[SBDockToStageZoomWindowingModifier wantsDockBehaviorAssertion];
-[SBDockToStageZoomWindowingModifier dockUpdateMode];
-[SBDockToStageZoomWindowingModifier fadeInDelayForSplitViewHandles];
-[SBDockToStageZoomWindowingModifier perspectiveAngleForIndex:];
-[SBDockToStageZoomWindowingModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBDockToStageZoomWindowingModifier shadowOpacityForLayoutRole:atIndex:];
-[SBDockToStageZoomWindowingModifier _settingsByInterpolatingBetween:and:progress:];
-[SBDockToStageZoomWindowingModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBDockToStageZoomWindowingModifier containerLeafAppLayoutForShelf:];
-[SBDockToStageZoomWindowingModifier frameForIndex:];
-[SBDockToStageZoomWindowingModifier genieAttributesForAppLayout:];
-[SBDockToStageZoomWindowingModifier complete];
-[SBDockToStageZoomWindowingModifier keyboardSuppressionMode];
-[SBDockToStageZoomWindowingModifier transitionWillBegin:];
-[SBDockToStageZoomWindowingModifier _isIndexZoomAppLayout:];
-[SBDockToStageZoomWindowingModifier fullyPresentedFrameForAppLayout:frame:];
-[SBDockToStageZoomWindowingModifier _normalizedHomeScreenIconZoomPercentBetweenTopAndBottom:];
-[SBDockToStageZoomWindowingModifier _flexibleAutoLayoutSpaceForZoomingAppLayout];
-[SBDockToStageZoomWindowingModifier asyncRenderingAttributesForAppLayout:];
-[SBDockToStageZoomWindowingModifier shouldConfigureInAppDockHiddenAssertion];
-[SBDockToStageZoomWindowingModifier timerFired:];
-[SBDockToStageZoomWindowingModifier maskedCornersForLayoutRole:inAppLayout:withMaskedCorners:];
-[SBDockToStageZoomWindowingModifier _isEffectivelyHome];
-[SBDockToStageZoomWindowingModifier wantsSpaceAccessoryViewGenieForAppLayout:];
-[SBDockToStageZoomWindowingModifier wantsAsynchronousSurfaceRetentionAssertion];
-[SBDockToStageZoomWindowingModifier wantsDockPortalViewLayoutElement];
-[SBDockToStageZoomWindowingModifier _layoutSettingsForTargetCenter:];
-[SBDockToStageZoomWindowingModifier _appLayoutForIcon];
-[SBDockToStageZoomWindowingModifier _frameForZoomingIndex:isEffectivelyHome:ignoringGenie:];
-[SBDockToStageZoomWindowingModifier _iconFrame];
-[SBDockToStageZoomWindowingModifier initWithAppLayout:addingToStage:];
-[SBDockToStageZoomWindowingModifier launchingOverDesktopSpaceAppLayout];
-[SBDockToStageZoomWindowingModifier setLaunchingOverDesktopSpaceAppLayout:];
-[SBDockToStageZoomWindowingModifier shouldInterruptForActivity:];
-[SBDockToStageZoomWindowingModifier transitionDidComplete:];
```
