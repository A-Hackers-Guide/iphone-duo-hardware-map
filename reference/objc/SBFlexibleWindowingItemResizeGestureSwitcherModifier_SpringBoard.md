# `SBFlexibleWindowingItemResizeGestureSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBGestureSwitcherModifier`
- 33 instance variables, 1 properties, 36 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _currentAppLayout;
q _selectedLayoutRole;
Q _selectedEdge;
Q _resizeAnchor;
@"SBDisplayItem" _selectedDisplayItem;
{CGPoint="x"d"y"d} _location;
{CGPoint="x"d"y"d} _locationEdgeAdjustment;
B _dockAwareIfCenterAnchored;
B _needsCenterAnchoringPerOptionModifier;
B _selectedItemWasInitiallyInDefaultPosition;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _initialFrameInScreenCoordinates;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _currentFrameForDrawingInScreenCoordinates;
{CGSize="width"d"height"d} _currentSceneSize;
B _needsSceneSizeUpdate;
d _amountInitiallyOffScreenToLeft;
d _amountInitiallyOffScreenToRight;
d _amountInitiallyOffScreenToBottom;
@"SBDisplayItemLayoutGrid" _layoutGrid;
@"SBFlexibleWindowingAutoLayoutController" _autoLayoutController;
@"SBFlexibleWindowingAutoLayoutSpace" _autoLayoutSpaceWithDraggedItemExcluded;
Q _currentActiveResizeCorner;
@"SBGestureSwitcherModifierEvent" _lastGestureEvent;
q _delayedSceneSizeUpdateGeneration;
@"NSString" _delayedSceneSizeUpdateReason;
{SBWindowControlsLayout="style"q"underlapsStatusBar"B"margin"{CGPoint="x"d"y"d}} _currentWindowControlsLayout;
@"SBDisplayItemGridLayoutRestrictionInfo" _layoutRestrictionInfoForSelectedItem;
B _resizedDisplayItemIntersectsHomeAffordanceArea;
d _effectiveInitialPositionY;
B _selectedItemIsInSlideOver;
B _inLeftPinnedSlideOver;
B _inRightPinnedSlideOver;
d _rubberbandingRangeX;
d _rubberbandingRangeY;
```

## Properties

```
@property (T@"SBAppLayout",R,N,V_currentAppLayout) selectedAppLayout;
```

## Instance methods

```
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier handleGestureEvent:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier homeScreenDimmingAlpha];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier maskedCornersForIndex:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier cornerRadiiForIndex:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier animationAttributesForLayoutElement:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier visibleSplitViewHandleNubViews];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier dockProgress];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier visibleSplitViewHandleDimmingViews];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier topMostLayoutElements];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier handleTransitionEvent:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier wantsDockBehaviorAssertion];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier isContentStatusBarVisibleForIndex:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier visibleCornersForTouchResizeForLayoutRole:inAppLayout:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier handleTimerEvent:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier selectedAppLayout];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier topMostLayoutRolesForAppLayout:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier wantsSceneResizesHostedContextForAppLayout:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier activeCornersForTouchResizeForLayoutRole:inAppLayout:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier cornerRadiiForLayoutRole:inAppLayout:withCornerRadii:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier isItemResizingAllowedForLayoutRole:inAppLayout:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier occlusionStateForLayoutRole:inAppLayout:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier isLayoutRoleMatchMovedToScene:inAppLayout:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier shouldConfigureInAppDockHiddenAssertion];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier maskedCornersForLayoutRole:inAppLayout:withMaskedCorners:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier hiddenContentStatusBarPartsForLayoutRole:inAppLayout:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier _animationSettingsForLayout];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier _convertToSpaceRectFromScreenRect:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier _dockProgressForResizingWindow];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier _initialScaledFrameInScreenCoordinatesForSelectedDisplayItemInAppLayout:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier _isStripVisibleForCurrentAppLayout];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier _responseForGestureUpdateAtGestureEnd:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier _responseForSceneSizeUpdateToSize:center:sceneUpdatesOnly:animated:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier handleSceneReadyEvent:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier initWithGestureID:];
-[SBFlexibleWindowingItemResizeGestureSwitcherModifier layoutRestrictionInfoForItem:];
```
