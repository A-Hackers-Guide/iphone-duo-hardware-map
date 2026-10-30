# `SBFullScreenToHomeIconZoomSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransitionSwitcherModifier`
- 28 instance variables, 9 properties, 82 instance methods, 0 class methods

## Instance variables

```
Q _direction;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _homeScreenIconFrame;
d _homeScreenIconCornerRadius;
d _homeScreenIconScale;
B _homeScreenIconLocationIsFloatingDock;
B _homeScreenIconIsWidget;
B _homeScreenIconIsSmallWidget;
B _itemContainerOverlapsDock;
B _wantsDockWindowLevelAssertion;
@"SBCoplanarSwitcherModifier" _coplanarModifier;
B _shouldAcceleratedHomeButtonPressBegin;
B _isHidingDockIcon;
B _genieEnabled;
B _isAddingToStage;
B _isMinimizing;
@"SBAppLayout" _fromAppLayout;
@"SBAppLayout" _toAppLayout;
B _hasResetCornerRadius;
B _isWaitingForGlassHighlightDelay;
B _shouldUpdateIconViewVisibility;
B _shouldMatchMoveToIconView;
B _canAddVelocityKickToHurdleDock;
B _shouldForceDefaultAnchorPointForTransition;
B _shouldDockOrderFrontDuringTransition;
B _shouldDisableAsyncRendering;
B _genieDisabled;
B _supportsGlassHighlight;
@"SBAppLayout" _appLayout;
```

## Properties

```
@property (TB,N,V_shouldUpdateIconViewVisibility) shouldUpdateIconViewVisibility;
@property (TB,N,V_shouldMatchMoveToIconView) shouldMatchMoveToIconView;
@property (TB,N,V_canAddVelocityKickToHurdleDock) canAddVelocityKickToHurdleDock;
@property (TB,N,V_shouldForceDefaultAnchorPointForTransition) shouldForceDefaultAnchorPointForTransition;
@property (TB,N,V_shouldDockOrderFrontDuringTransition) shouldDockOrderFrontDuringTransition;
@property (TB,N,V_shouldDisableAsyncRendering) shouldDisableAsyncRendering;
@property (TB,N,GisGenieDisabled,V_genieDisabled) genieDisabled;
@property (TB,N,V_supportsGlassHighlight) supportsGlassHighlight;
@property (T@"SBAppLayout",R,N,V_appLayout) appLayout;
```

## Instance methods

```
-[SBFullScreenToHomeIconZoomSwitcherModifier scaleForIndex:];
-[SBFullScreenToHomeIconZoomSwitcherModifier anchorPointForIndex:];
-[SBFullScreenToHomeIconZoomSwitcherModifier isSwitcherWindowUserInteractionEnabled];
-[SBFullScreenToHomeIconZoomSwitcherModifier dockWindowLevelPriority];
-[SBFullScreenToHomeIconZoomSwitcherModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBFullScreenToHomeIconZoomSwitcherModifier homeScreenAlpha];
-[SBFullScreenToHomeIconZoomSwitcherModifier maskedCornersForIndex:];
-[SBFullScreenToHomeIconZoomSwitcherModifier dockWindowLevel];
-[SBFullScreenToHomeIconZoomSwitcherModifier isHomeScreenContentRequired];
-[SBFullScreenToHomeIconZoomSwitcherModifier didMoveToParentModifier:];
-[SBFullScreenToHomeIconZoomSwitcherModifier shouldForceDefaultAnchorPointForTransition];
-[SBFullScreenToHomeIconZoomSwitcherModifier cornerRadiiForIndex:];
-[SBFullScreenToHomeIconZoomSwitcherModifier adjustedSpaceAccessoryViewAnchorPoint:forAppLayout:];
-[SBFullScreenToHomeIconZoomSwitcherModifier shouldAsyncRenderUntilDelay:];
-[SBFullScreenToHomeIconZoomSwitcherModifier shouldFireTransitionCompletionInDefaultRunLoopMode];
-[SBFullScreenToHomeIconZoomSwitcherModifier shouldScaleOverlayToFillBoundsAtIndex:];
-[SBFullScreenToHomeIconZoomSwitcherModifier animationAttributesForLayoutElement:];
-[SBFullScreenToHomeIconZoomSwitcherModifier setShouldForceDefaultAnchorPointForTransition:];
-[SBFullScreenToHomeIconZoomSwitcherModifier homeScreenBackdropBlurType];
-[SBFullScreenToHomeIconZoomSwitcherModifier _layoutSettings];
-[SBFullScreenToHomeIconZoomSwitcherModifier dockProgress];
-[SBFullScreenToHomeIconZoomSwitcherModifier adjustedSpaceAccessoryViewFrame:forAppLayout:];
-[SBFullScreenToHomeIconZoomSwitcherModifier topMostLayoutElements];
-[SBFullScreenToHomeIconZoomSwitcherModifier isSwitcherWindowVisible];
-[SBFullScreenToHomeIconZoomSwitcherModifier appLayoutsForContinuousExposeIdentifier:];
-[SBFullScreenToHomeIconZoomSwitcherModifier appLayoutsToCacheSnapshots];
-[SBFullScreenToHomeIconZoomSwitcherModifier _normalizedHomeScreenTargetZoomPercentBetweenCenterAndEdge:];
-[SBFullScreenToHomeIconZoomSwitcherModifier wantsDockWindowLevelAssertion];
-[SBFullScreenToHomeIconZoomSwitcherModifier presentationAttributesForShelf:];
-[SBFullScreenToHomeIconZoomSwitcherModifier handleTransitionEvent:];
-[SBFullScreenToHomeIconZoomSwitcherModifier canAddVelocityKickToHurdleDock];
-[SBFullScreenToHomeIconZoomSwitcherModifier shouldPinLayoutRolesToSpace:];
-[SBFullScreenToHomeIconZoomSwitcherModifier transitionWillUpdate];
-[SBFullScreenToHomeIconZoomSwitcherModifier adjustedSpaceAccessoryViewScale:forAppLayout:];
-[SBFullScreenToHomeIconZoomSwitcherModifier isWallpaperRequiredForSwitcher];
-[SBFullScreenToHomeIconZoomSwitcherModifier visibleAppLayouts];
-[SBFullScreenToHomeIconZoomSwitcherModifier setShouldDisableAsyncRendering:];
-[SBFullScreenToHomeIconZoomSwitcherModifier perspectiveAngleForLayoutRole:inAppLayout:withPerspectiveAngle:];
-[SBFullScreenToHomeIconZoomSwitcherModifier wantsDockBehaviorAssertion];
-[SBFullScreenToHomeIconZoomSwitcherModifier dockUpdateMode];
-[SBFullScreenToHomeIconZoomSwitcherModifier fadeInDelayForSplitViewHandles];
-[SBFullScreenToHomeIconZoomSwitcherModifier perspectiveAngleForIndex:];
-[SBFullScreenToHomeIconZoomSwitcherModifier appLayout];
-[SBFullScreenToHomeIconZoomSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBFullScreenToHomeIconZoomSwitcherModifier transitionDidEnd];
-[SBFullScreenToHomeIconZoomSwitcherModifier shouldAcceleratedHomeButtonPressBegin];
-[SBFullScreenToHomeIconZoomSwitcherModifier handleTimerEvent:];
-[SBFullScreenToHomeIconZoomSwitcherModifier _genieCounterScaleIfNeeded];
-[SBFullScreenToHomeIconZoomSwitcherModifier shadowOpacityForLayoutRole:atIndex:];
-[SBFullScreenToHomeIconZoomSwitcherModifier _settingsByInterpolatingBetween:and:progress:];
-[SBFullScreenToHomeIconZoomSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBFullScreenToHomeIconZoomSwitcherModifier shouldDockOrderFrontDuringTransition];
-[SBFullScreenToHomeIconZoomSwitcherModifier wallpaperStyle];
-[SBFullScreenToHomeIconZoomSwitcherModifier adjustedSpaceAccessoryViewPerspectiveAngle:forAppLayout:];
-[SBFullScreenToHomeIconZoomSwitcherModifier containerLeafAppLayoutForShelf:];
-[SBFullScreenToHomeIconZoomSwitcherModifier frameForIndex:];
-[SBFullScreenToHomeIconZoomSwitcherModifier transitionWillBegin];
-[SBFullScreenToHomeIconZoomSwitcherModifier genieAttributesForAppLayout:];
-[SBFullScreenToHomeIconZoomSwitcherModifier wallpaperScale];
-[SBFullScreenToHomeIconZoomSwitcherModifier supportsGlassHighlight];
-[SBFullScreenToHomeIconZoomSwitcherModifier _numberOfPeekingItemsAboveDisplayItem:zOrderedItems:];
-[SBFullScreenToHomeIconZoomSwitcherModifier isGenieDisabled];
-[SBFullScreenToHomeIconZoomSwitcherModifier setGenieDisabled:];
-[SBFullScreenToHomeIconZoomSwitcherModifier setShouldUpdateIconViewVisibility:];
-[SBFullScreenToHomeIconZoomSwitcherModifier shouldMatchMoveToIconView];
-[SBFullScreenToHomeIconZoomSwitcherModifier initWithTransitionID:appLayout:direction:];
-[SBFullScreenToHomeIconZoomSwitcherModifier _isIndexZoomAppLayout:];
-[SBFullScreenToHomeIconZoomSwitcherModifier fullyPresentedFrameForAppLayout:frame:];
-[SBFullScreenToHomeIconZoomSwitcherModifier _normalizedHomeScreenIconZoomPercentBetweenTopAndBottom:];
-[SBFullScreenToHomeIconZoomSwitcherModifier asyncRenderingDisabled];
-[SBFullScreenToHomeIconZoomSwitcherModifier setShouldMatchMoveToIconView:];
-[SBFullScreenToHomeIconZoomSwitcherModifier _flexibleAutoLayoutSpaceForZoomingAppLayout];
-[SBFullScreenToHomeIconZoomSwitcherModifier _homeScreenFrameForZoomingIndex:ignoringGenie:];
-[SBFullScreenToHomeIconZoomSwitcherModifier shouldUpdateIconViewVisibility];
-[SBFullScreenToHomeIconZoomSwitcherModifier initWithTransitionID:targetFrame:appLayout:direction:];
-[SBFullScreenToHomeIconZoomSwitcherModifier layoutSettingsForTargetCenter:];
-[SBFullScreenToHomeIconZoomSwitcherModifier setShouldDockOrderFrontDuringTransition:];
-[SBFullScreenToHomeIconZoomSwitcherModifier _isEffectivelyHome];
-[SBFullScreenToHomeIconZoomSwitcherModifier setSupportsGlassHighlight:];
-[SBFullScreenToHomeIconZoomSwitcherModifier shouldDisableAsyncRendering];
-[SBFullScreenToHomeIconZoomSwitcherModifier descriptionBuilderWithMultilinePrefix:];
-[SBFullScreenToHomeIconZoomSwitcherModifier setCanAddVelocityKickToHurdleDock:];
```
