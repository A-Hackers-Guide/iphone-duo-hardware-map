# `SBExposeWindowingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 13 instance variables, 5 properties, 134 instance methods, 0 class methods

## Instance variables

```
B _overrideContextToBuildAppLayoutsInExpose;
Q _ongoingAppLayoutRemovals;
@"NSArray" _pilesInExpose;
@"NSArray" _allAppLayouts;
@"NSSet" _visibleItems;
@"NSArray" _topMostItems;
{CGSize="width"d"height"d} _fittedContentSize;
@"NSArray" _effectiveRecentAppLayouts;
B _handlesTapAppLayoutEvents;
B _handlesTapAppLayoutHeaderEvents;
d _scaleFactor;
d _horizontalEdgeSpacingScaleFactor;
@"SBAppLayout" _organicExposeAppLayout;
```

## Properties

```
@property (TB,N,V_handlesTapAppLayoutEvents) handlesTapAppLayoutEvents;
@property (TB,N,V_handlesTapAppLayoutHeaderEvents) handlesTapAppLayoutHeaderEvents;
@property (Td,N,V_scaleFactor) scaleFactor;
@property (Td,N,V_horizontalEdgeSpacingScaleFactor) horizontalEdgeSpacingScaleFactor;
@property (T@"SBAppLayout",R,N,V_organicExposeAppLayout) organicExposeAppLayout;
```

## Instance methods

```
-[SBExposeWindowingModifier jetsamModeForAppLayout:];
-[SBExposeWindowingModifier homeScreenScale];
-[SBExposeWindowingModifier isContainerStatusBarVisible];
-[SBExposeWindowingModifier foregroundAppLayouts];
-[SBExposeWindowingModifier homeScreenBackdropBlurProgress];
-[SBExposeWindowingModifier homeScreenDimmingAlpha];
-[SBExposeWindowingModifier clippingFrameForIndex:withBounds:];
-[SBExposeWindowingModifier isSwitcherWindowUserInteractionEnabled];
-[SBExposeWindowingModifier shouldUseAnchorPointToPinLayoutRolesToSpace:];
-[SBExposeWindowingModifier homeScreenAlpha];
-[SBExposeWindowingModifier isHomeScreenContentRequired];
-[SBExposeWindowingModifier adjustedOffsetForOffset:translation:startPoint:locationInView:horizontalVelocity:verticalVelocity:];
-[SBExposeWindowingModifier touchBehaviorForLayoutRole:inAppLayout:];
-[SBExposeWindowingModifier clipsToUnobscuredMarginAtIndex:];
-[SBExposeWindowingModifier shouldScaleOverlayToFillBoundsAtIndex:];
-[SBExposeWindowingModifier adjustedAppLayoutsForAppLayouts:];
-[SBExposeWindowingModifier visibleSplitViewHandleNubViews];
-[SBExposeWindowingModifier displayItemsToExcludeFromStrip];
-[SBExposeWindowingModifier clippingFrameForLayoutRole:inAppLayout:atIndex:withBounds:];
-[SBExposeWindowingModifier homeScreenBackdropBlurType];
-[SBExposeWindowingModifier dockProgress];
-[SBExposeWindowingModifier windowManagementContext];
-[SBExposeWindowingModifier visibleHomeAffordanceLayoutElements];
-[SBExposeWindowingModifier visibleSplitViewHandleDimmingViews];
-[SBExposeWindowingModifier isSwitcherWindowVisible];
-[SBExposeWindowingModifier activityModeForAppLayout:];
-[SBExposeWindowingModifier appLayoutsToCacheSnapshots];
-[SBExposeWindowingModifier shouldPinLayoutRolesToSpace:];
-[SBExposeWindowingModifier shouldScrollViewBlockTouches];
-[SBExposeWindowingModifier transitionDidUpdate:];
-[SBExposeWindowingModifier isWallpaperRequiredForSwitcher];
-[SBExposeWindowingModifier layoutViewModelsIfNeeded];
-[SBExposeWindowingModifier init];
-[SBExposeWindowingModifier wantsDockBehaviorAssertion];
-[SBExposeWindowingModifier isContentStatusBarVisibleForIndex:];
-[SBExposeWindowingModifier shouldAccessoryDrawShadowForAppLayout:];
-[SBExposeWindowingModifier dockUpdateMode];
-[SBExposeWindowingModifier setScaleFactor:];
-[SBExposeWindowingModifier appLayout];
-[SBExposeWindowingModifier shouldAllowContentViewTouchesForLayoutRole:inAppLayout:];
-[SBExposeWindowingModifier visibleCornersForTouchResizeForLayoutRole:inAppLayout:];
-[SBExposeWindowingModifier isScrollEnabled];
-[SBExposeWindowingModifier scaleForLayoutRole:inAppLayout:];
-[SBExposeWindowingModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBExposeWindowingModifier contentOffsetForIndex:alignment:];
-[SBExposeWindowingModifier isIndexRubberbandableForSwipeToKill:];
-[SBExposeWindowingModifier wallpaperStyle];
-[SBExposeWindowingModifier activeLeafAppLayoutsReachableByKeyboardShortcut];
-[SBExposeWindowingModifier recentAppLayouts];
-[SBExposeWindowingModifier wallpaperScale];
-[SBExposeWindowingModifier adjustedContinuousExposeIdentifiersInStripFromPreviousIdentifiersInStrip:];
-[SBExposeWindowingModifier destinationAppLayoutForDismissingCurrentMode];
-[SBExposeWindowingModifier backgroundOpacityForIndex:];
-[SBExposeWindowingModifier keyboardSuppressionMode];
-[SBExposeWindowingModifier useItemContainerFooterViewsForAppLayout:];
-[SBExposeWindowingModifier neighboringAppLayoutsForFocusedAppLayout:];
-[SBExposeWindowingModifier visibleMarginForItemContainerAtIndex:];
-[SBExposeWindowingModifier wallpaperOverlayAlphaForIndex:];
-[SBExposeWindowingModifier identifiersInStrip];
-[SBExposeWindowingModifier indexToScrollToAfterRemovingIndex:];
-[SBExposeWindowingModifier shadowForItem:];
-[SBExposeWindowingModifier distanceToLeadingEdgeOfLeadingCardFromTrailingEdgeOfScreenWithVisibleIndexToStartSearch:];
-[SBExposeWindowingModifier visibleItems];
-[SBExposeWindowingModifier cornersForItem:];
-[SBExposeWindowingModifier restingOffsetForScrollOffset:velocity:];
-[SBExposeWindowingModifier regionDividerOpacity];
-[SBExposeWindowingModifier activeCornersForTouchResizeForLayoutRole:inAppLayout:];
-[SBExposeWindowingModifier resetAdjustedScrollingState];
-[SBExposeWindowingModifier snapshotScaleForLayoutRole:inAppLayout:];
-[SBExposeWindowingModifier isFocusEnabledForAppLayout:];
-[SBExposeWindowingModifier shouldRemoveProlongedCursorGestureFloatingDockBehaviorAssertion];
-[SBExposeWindowingModifier isItemResizingAllowedForLayoutRole:inAppLayout:];
-[SBExposeWindowingModifier shouldUseBrightMaterialForIndex:];
-[SBExposeWindowingModifier isLayoutRoleKillable:inAppLayout:atIndex:];
-[SBExposeWindowingModifier canPerformKeyboardShortcutAction:forBundleIdentifier:];
-[SBExposeWindowingModifier isLayoutRoleEligibleForContentDragSpringLoading:inAppLayout:];
-[SBExposeWindowingModifier scaleFactor];
-[SBExposeWindowingModifier indexToScrollToAfterInsertingAtIndex:];
-[SBExposeWindowingModifier _contentSize];
-[SBExposeWindowingModifier isItemContainerPointerInteractionEnabled];
-[SBExposeWindowingModifier regionDividerCenter];
-[SBExposeWindowingModifier appLayoutsToResignActive];
-[SBExposeWindowingModifier shelfBackgroundBlurOpacity];
-[SBExposeWindowingModifier animationAttributesForItem:];
-[SBExposeWindowingModifier isLayoutRoleSelectable:inAppLayout:];
-[SBExposeWindowingModifier appLayoutForReceivingHardwareButtonEvents];
-[SBExposeWindowingModifier wantsSpaceAccessoryViewPointerInteractionsForAppLayout:];
-[SBExposeWindowingModifier wantsRegionDivider];
-[SBExposeWindowingModifier contentPageViewScaleForLayoutRole:inAppLayout:withContentPageViewScale:];
-[SBExposeWindowingModifier scrollViewAttributes];
-[SBExposeWindowingModifier lighteningAlphaForIndex:];
-[SBExposeWindowingModifier preferredStatusBarAxis];
-[SBExposeWindowingModifier shelfBackgroundBlurFrame];
-[SBExposeWindowingModifier asyncRenderingAttributesForAppLayout:];
-[SBExposeWindowingModifier shadowStyleForLayoutRole:inAppLayout:];
-[SBExposeWindowingModifier wantsHomeScreenPointerInteractions];
-[SBExposeWindowingModifier shouldConfigureInAppDockHiddenAssertion];
-[SBExposeWindowingModifier minimumTranslationToKillIndex:];
-[SBExposeWindowingModifier regionDividerOptions];
-[SBExposeWindowingModifier preferredSnapshotOrientationForAppLayout:];
-[SBExposeWindowingModifier topMostItems];
-[SBExposeWindowingModifier adjustedContinuousExposeIdentifiersInSwitcherFromPreviousIdentifiersInSwitcher:identifiersInStrip:];
-[SBExposeWindowingModifier shouldBringCardToFrontDuringInsertionOrRemoval];
-[SBExposeWindowingModifier supportsHomeAffordanceForItem:];
-[SBExposeWindowingModifier frameForItem:];
-[SBExposeWindowingModifier shouldAnimateInsertionOrRemovalOfAppLayout:atIndex:];
-[SBExposeWindowingModifier contentPageViewScaleForAppLayout:withScale:];
-[SBExposeWindowingModifier wantsAsynchronousSurfaceRetentionAssertion];
-[SBExposeWindowingModifier titleStyleForItem:];
-[SBExposeWindowingModifier appLayoutsToCacheFullsizeSnapshots];
-[SBExposeWindowingModifier isLayoutRoleDraggable:inAppLayout:];
-[SBExposeWindowingModifier strip];
-[SBExposeWindowingModifier handlesTapAppLayoutHeaderEvents];
-[SBExposeWindowingModifier _captureModelForOverflowAndManualModeIfNeeded];
-[SBExposeWindowingModifier _effectiveIndexInRecencyOfAppLayout:];
-[SBExposeWindowingModifier _fittedContentSize];
-[SBExposeWindowingModifier _heightForCardInSwitcherWithScaleFactor:];
-[SBExposeWindowingModifier _indexOfLeadingAppLayout];
-[SBExposeWindowingModifier _visibleSwitcherBoundsIncludingShadow];
-[SBExposeWindowingModifier appLayoutContainingAppLayout:];
-[SBExposeWindowingModifier appLayoutHeaderTapped:];
-[SBExposeWindowingModifier appLayoutTapped:];
-[SBExposeWindowingModifier groupsWindowsByApp];
-[SBExposeWindowingModifier handlesTapAppLayoutEvents];
-[SBExposeWindowingModifier horizontalEdgeSpacingScaleFactor];
-[SBExposeWindowingModifier itemInserted:];
-[SBExposeWindowingModifier itemRemoved:];
-[SBExposeWindowingModifier organicExposeAppLayout];
-[SBExposeWindowingModifier setHandlesTapAppLayoutEvents:];
-[SBExposeWindowingModifier setHandlesTapAppLayoutHeaderEvents:];
-[SBExposeWindowingModifier setHorizontalEdgeSpacingScaleFactor:];
-[SBExposeWindowingModifier shouldConfigureInAppDockVisibleAssertion];
-[SBExposeWindowingModifier tappedOutsideToDismiss:];
-[SBExposeWindowingModifier windowingConfigurationForInterfaceOrientation:];
```
