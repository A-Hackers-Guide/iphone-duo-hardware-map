# `SBShelfCarouselSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- 18 instance variables, 1 properties, 117 instance methods, 0 class methods

## Instance variables

```
Q _fittedContentSize_lastAppLayoutsGenCount;
q _fittedContentSize_lastOrientation;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _fittedContentSize_lastContainerViewBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _fittedContentSize_lastSwitcherViewBounds;
{CGSize="width"d"height"d} _fittedContentSize_lastSize;
Q _visibleRange_lastAppLayoutsGenCount;
q _visibleRange_lastOrientation;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _visibleRange_lastContainerViewBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _visibleRange_lastSwitcherViewBounds;
{CGPoint="x"d"y"d} _visibleRange_lastContentOffset;
{_NSRange="location"Q"length"Q} _visibleRange_lastRange;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _centerCardSize_containerViewBounds;
{CGSize="width"d"height"d} _centerCardSize_landscapeCardSize;
{CGSize="width"d"height"d} _centerCardSize_portraitCardSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _floatingCardSize_containerViewBounds;
{CGSize="width"d"height"d} _floatingCardSize_landscapeCardSize;
{CGSize="width"d"height"d} _floatingCardSize_portraitCardSize;
B _hasReceivedInitialSetupEvent;
```

## Properties

```
@property (T@"NSArray",R,C,N) orderedVisibleAppLayouts;
```

## Instance methods

```
-[SBShelfCarouselSwitcherModifier jetsamModeForAppLayout:];
-[SBShelfCarouselSwitcherModifier scaleForIndex:];
-[SBShelfCarouselSwitcherModifier anchorPointForIndex:];
-[SBShelfCarouselSwitcherModifier titleOpacityForIndex:];
-[SBShelfCarouselSwitcherModifier homeScreenScale];
-[SBShelfCarouselSwitcherModifier isContainerStatusBarVisible];
-[SBShelfCarouselSwitcherModifier foregroundAppLayouts];
-[SBShelfCarouselSwitcherModifier homeScreenBackdropBlurProgress];
-[SBShelfCarouselSwitcherModifier homeScreenDimmingAlpha];
-[SBShelfCarouselSwitcherModifier clippingFrameForIndex:withBounds:];
-[SBShelfCarouselSwitcherModifier isSwitcherWindowUserInteractionEnabled];
-[SBShelfCarouselSwitcherModifier homeScreenAlpha];
-[SBShelfCarouselSwitcherModifier isHomeScreenContentRequired];
-[SBShelfCarouselSwitcherModifier adjustedOffsetForOffset:translation:startPoint:locationInView:horizontalVelocity:verticalVelocity:];
-[SBShelfCarouselSwitcherModifier touchBehaviorForLayoutRole:inAppLayout:];
-[SBShelfCarouselSwitcherModifier cornerRadiiForIndex:];
-[SBShelfCarouselSwitcherModifier _isIndexVisible:];
-[SBShelfCarouselSwitcherModifier clipsToUnobscuredMarginAtIndex:];
-[SBShelfCarouselSwitcherModifier shouldScaleOverlayToFillBoundsAtIndex:];
-[SBShelfCarouselSwitcherModifier animationAttributesForLayoutElement:];
-[SBShelfCarouselSwitcherModifier adjustedAppLayoutsForAppLayouts:];
-[SBShelfCarouselSwitcherModifier clippingFrameForLayoutRole:inAppLayout:atIndex:withBounds:];
-[SBShelfCarouselSwitcherModifier homeScreenBackdropBlurType];
-[SBShelfCarouselSwitcherModifier dockProgress];
-[SBShelfCarouselSwitcherModifier visibleHomeAffordanceLayoutElements];
-[SBShelfCarouselSwitcherModifier topMostLayoutElements];
-[SBShelfCarouselSwitcherModifier isSwitcherWindowVisible];
-[SBShelfCarouselSwitcherModifier titleAndIconOpacityForIndex:];
-[SBShelfCarouselSwitcherModifier activityModeForAppLayout:];
-[SBShelfCarouselSwitcherModifier appLayoutsToCacheSnapshots];
-[SBShelfCarouselSwitcherModifier shouldScrollViewBlockTouches];
-[SBShelfCarouselSwitcherModifier isWallpaperRequiredForSwitcher];
-[SBShelfCarouselSwitcherModifier visibleAppLayouts];
-[SBShelfCarouselSwitcherModifier init];
-[SBShelfCarouselSwitcherModifier wantsDockBehaviorAssertion];
-[SBShelfCarouselSwitcherModifier isContentStatusBarVisibleForIndex:];
-[SBShelfCarouselSwitcherModifier shouldAccessoryDrawShadowForAppLayout:];
-[SBShelfCarouselSwitcherModifier dockUpdateMode];
-[SBShelfCarouselSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBShelfCarouselSwitcherModifier shouldAllowContentViewTouchesForLayoutRole:inAppLayout:];
-[SBShelfCarouselSwitcherModifier visibleCornersForTouchResizeForLayoutRole:inAppLayout:];
-[SBShelfCarouselSwitcherModifier isScrollEnabled];
-[SBShelfCarouselSwitcherModifier shadowOpacityForLayoutRole:atIndex:];
-[SBShelfCarouselSwitcherModifier frameForLayoutRole:inAppLayout:withBounds:];
-[SBShelfCarouselSwitcherModifier contentOffsetForIndex:alignment:];
-[SBShelfCarouselSwitcherModifier headerStyleForIndex:];
-[SBShelfCarouselSwitcherModifier isIndexRubberbandableForSwipeToKill:];
-[SBShelfCarouselSwitcherModifier wallpaperStyle];
-[SBShelfCarouselSwitcherModifier frameForIndex:];
-[SBShelfCarouselSwitcherModifier activeLeafAppLayoutsReachableByKeyboardShortcut];
-[SBShelfCarouselSwitcherModifier wallpaperScale];
-[SBShelfCarouselSwitcherModifier adjustedContinuousExposeIdentifiersInStripFromPreviousIdentifiersInStrip:];
-[SBShelfCarouselSwitcherModifier multipleWindowsIndicatorLayoutRolesForAppLayout:];
-[SBShelfCarouselSwitcherModifier destinationAppLayoutForDismissingCurrentMode];
-[SBShelfCarouselSwitcherModifier backgroundOpacityForIndex:];
-[SBShelfCarouselSwitcherModifier keyboardSuppressionMode];
-[SBShelfCarouselSwitcherModifier neighboringAppLayoutsForFocusedAppLayout:];
-[SBShelfCarouselSwitcherModifier visibleMarginForItemContainerAtIndex:];
-[SBShelfCarouselSwitcherModifier wallpaperOverlayAlphaForIndex:];
-[SBShelfCarouselSwitcherModifier identifiersInStrip];
-[SBShelfCarouselSwitcherModifier indexToScrollToAfterRemovingIndex:];
-[SBShelfCarouselSwitcherModifier distanceToLeadingEdgeOfLeadingCardFromTrailingEdgeOfScreenWithVisibleIndexToStartSearch:];
-[SBShelfCarouselSwitcherModifier restingOffsetForScrollOffset:velocity:];
-[SBShelfCarouselSwitcherModifier regionDividerOpacity];
-[SBShelfCarouselSwitcherModifier activeCornersForTouchResizeForLayoutRole:inAppLayout:];
-[SBShelfCarouselSwitcherModifier resetAdjustedScrollingState];
-[SBShelfCarouselSwitcherModifier snapshotScaleForLayoutRole:inAppLayout:];
-[SBShelfCarouselSwitcherModifier isFocusEnabledForAppLayout:];
-[SBShelfCarouselSwitcherModifier isItemResizingAllowedForLayoutRole:inAppLayout:];
-[SBShelfCarouselSwitcherModifier shouldUseBrightMaterialForIndex:];
-[SBShelfCarouselSwitcherModifier isLayoutRoleKillable:inAppLayout:atIndex:];
-[SBShelfCarouselSwitcherModifier canPerformKeyboardShortcutAction:forBundleIdentifier:];
-[SBShelfCarouselSwitcherModifier handleTapAppLayoutEvent:];
-[SBShelfCarouselSwitcherModifier isLayoutRoleEligibleForContentDragSpringLoading:inAppLayout:];
-[SBShelfCarouselSwitcherModifier indexToScrollToAfterInsertingAtIndex:];
-[SBShelfCarouselSwitcherModifier _contentSize];
-[SBShelfCarouselSwitcherModifier isItemContainerPointerInteractionEnabled];
-[SBShelfCarouselSwitcherModifier regionDividerCenter];
-[SBShelfCarouselSwitcherModifier appLayoutsToResignActive];
-[SBShelfCarouselSwitcherModifier shelfBackgroundBlurOpacity];
-[SBShelfCarouselSwitcherModifier shouldTetherItemsAndAccessoriesInAppLayout:];
-[SBShelfCarouselSwitcherModifier isLayoutRoleSelectable:inAppLayout:];
-[SBShelfCarouselSwitcherModifier appLayoutForReceivingHardwareButtonEvents];
-[SBShelfCarouselSwitcherModifier wantsRegionDivider];
-[SBShelfCarouselSwitcherModifier scrollViewAttributes];
-[SBShelfCarouselSwitcherModifier lighteningAlphaForIndex:];
-[SBShelfCarouselSwitcherModifier preferredStatusBarAxis];
-[SBShelfCarouselSwitcherModifier shelfBackgroundBlurFrame];
-[SBShelfCarouselSwitcherModifier asyncRenderingAttributesForAppLayout:];
-[SBShelfCarouselSwitcherModifier shadowStyleForLayoutRole:inAppLayout:];
-[SBShelfCarouselSwitcherModifier wantsHomeScreenPointerInteractions];
-[SBShelfCarouselSwitcherModifier shouldConfigureInAppDockHiddenAssertion];
-[SBShelfCarouselSwitcherModifier minimumTranslationToKillIndex:];
-[SBShelfCarouselSwitcherModifier regionDividerOptions];
-[SBShelfCarouselSwitcherModifier preferredSnapshotOrientationForAppLayout:];
-[SBShelfCarouselSwitcherModifier adjustedContinuousExposeIdentifiersInSwitcherFromPreviousIdentifiersInSwitcher:identifiersInStrip:];
-[SBShelfCarouselSwitcherModifier iconOpacityForIndex:];
-[SBShelfCarouselSwitcherModifier shouldBringCardToFrontDuringInsertionOrRemoval];
-[SBShelfCarouselSwitcherModifier isHomeAffordanceSupportedForAppLayout:];
-[SBShelfCarouselSwitcherModifier shouldAnimateInsertionOrRemovalOfAppLayout:atIndex:];
-[SBShelfCarouselSwitcherModifier contentPageViewScaleForAppLayout:withScale:];
-[SBShelfCarouselSwitcherModifier wantsAsynchronousSurfaceRetentionAssertion];
-[SBShelfCarouselSwitcherModifier appLayoutsToCacheFullsizeSnapshots];
-[SBShelfCarouselSwitcherModifier _forwardingTargetForUpdate];
-[SBShelfCarouselSwitcherModifier isLayoutRoleDraggable:inAppLayout:];
-[SBShelfCarouselSwitcherModifier _cardSizeForAppLayout:];
-[SBShelfCarouselSwitcherModifier _cardSizeForIndex:];
-[SBShelfCarouselSwitcherModifier _centerCardSizeForOrientation:];
-[SBShelfCarouselSwitcherModifier _effectiveMaxCarouselWidth];
-[SBShelfCarouselSwitcherModifier _fittedContentSize];
-[SBShelfCarouselSwitcherModifier _floatingCardSizeForOrientation:];
-[SBShelfCarouselSwitcherModifier _frameForIndex:applyCarousel:];
-[SBShelfCarouselSwitcherModifier _orderedVisibleAppLayouts];
-[SBShelfCarouselSwitcherModifier _visibleRange];
-[SBShelfCarouselSwitcherModifier handleInitialSetupEvent:];
-[SBShelfCarouselSwitcherModifier handleShelfFocusedDisplayItemsChangedEvent:];
-[SBShelfCarouselSwitcherModifier orderedVisibleAppLayouts];
```
