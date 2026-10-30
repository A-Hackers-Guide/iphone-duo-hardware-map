# `_SBButterflyAppsLayoutModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWindowingModifier`
- 2 instance variables, 0 properties, 86 instance methods, 0 class methods

## Instance variables

```
@"SBAppLayout" _activeAppLayout;
@"NSUUID" _homeAffordanceReuseIdentifier;
```

## Instance methods

```
-[_SBButterflyAppsLayoutModifier jetsamModeForAppLayout:];
-[_SBButterflyAppsLayoutModifier homeScreenScale];
-[_SBButterflyAppsLayoutModifier isContainerStatusBarVisible];
-[_SBButterflyAppsLayoutModifier foregroundAppLayouts];
-[_SBButterflyAppsLayoutModifier homeScreenBackdropBlurProgress];
-[_SBButterflyAppsLayoutModifier homeScreenDimmingAlpha];
-[_SBButterflyAppsLayoutModifier initWithActiveAppLayout:homeAffordanceReuseIdentifier:];
-[_SBButterflyAppsLayoutModifier isSwitcherWindowUserInteractionEnabled];
-[_SBButterflyAppsLayoutModifier homeScreenAlpha];
-[_SBButterflyAppsLayoutModifier isHomeScreenContentRequired];
-[_SBButterflyAppsLayoutModifier touchBehaviorForLayoutRole:inAppLayout:];
-[_SBButterflyAppsLayoutModifier clipsToUnobscuredMarginAtIndex:];
-[_SBButterflyAppsLayoutModifier shouldScaleOverlayToFillBoundsAtIndex:];
-[_SBButterflyAppsLayoutModifier visibleSplitViewHandleNubViews];
-[_SBButterflyAppsLayoutModifier homeScreenBackdropBlurType];
-[_SBButterflyAppsLayoutModifier dockProgress];
-[_SBButterflyAppsLayoutModifier visibleHomeAffordanceLayoutElements];
-[_SBButterflyAppsLayoutModifier isSwitcherWindowVisible];
-[_SBButterflyAppsLayoutModifier activityModeForAppLayout:];
-[_SBButterflyAppsLayoutModifier appLayoutsToCacheSnapshots];
-[_SBButterflyAppsLayoutModifier shouldScrollViewBlockTouches];
-[_SBButterflyAppsLayoutModifier isWallpaperRequiredForSwitcher];
-[_SBButterflyAppsLayoutModifier wantsDockBehaviorAssertion];
-[_SBButterflyAppsLayoutModifier isContentStatusBarVisibleForIndex:];
-[_SBButterflyAppsLayoutModifier shouldAccessoryDrawShadowForAppLayout:];
-[_SBButterflyAppsLayoutModifier dockUpdateMode];
-[_SBButterflyAppsLayoutModifier shouldAllowContentViewTouchesForLayoutRole:inAppLayout:];
-[_SBButterflyAppsLayoutModifier visibleCornersForTouchResizeForLayoutRole:inAppLayout:];
-[_SBButterflyAppsLayoutModifier isScrollEnabled];
-[_SBButterflyAppsLayoutModifier isIndexRubberbandableForSwipeToKill:];
-[_SBButterflyAppsLayoutModifier wallpaperStyle];
-[_SBButterflyAppsLayoutModifier activeLeafAppLayoutsReachableByKeyboardShortcut];
-[_SBButterflyAppsLayoutModifier wallpaperScale];
-[_SBButterflyAppsLayoutModifier destinationAppLayoutForDismissingCurrentMode];
-[_SBButterflyAppsLayoutModifier backgroundOpacityForIndex:];
-[_SBButterflyAppsLayoutModifier keyboardSuppressionMode];
-[_SBButterflyAppsLayoutModifier neighboringAppLayoutsForFocusedAppLayout:];
-[_SBButterflyAppsLayoutModifier visibleMarginForItemContainerAtIndex:];
-[_SBButterflyAppsLayoutModifier wallpaperOverlayAlphaForIndex:];
-[_SBButterflyAppsLayoutModifier identifiersInStrip];
-[_SBButterflyAppsLayoutModifier indexToScrollToAfterRemovingIndex:];
-[_SBButterflyAppsLayoutModifier shadowForItem:];
-[_SBButterflyAppsLayoutModifier visibleItems];
-[_SBButterflyAppsLayoutModifier cornersForItem:];
-[_SBButterflyAppsLayoutModifier regionDividerOpacity];
-[_SBButterflyAppsLayoutModifier activeCornersForTouchResizeForLayoutRole:inAppLayout:];
-[_SBButterflyAppsLayoutModifier isFocusEnabledForAppLayout:];
-[_SBButterflyAppsLayoutModifier isItemResizingAllowedForLayoutRole:inAppLayout:];
-[_SBButterflyAppsLayoutModifier shouldUseBrightMaterialForIndex:];
-[_SBButterflyAppsLayoutModifier isLayoutRoleKillable:inAppLayout:atIndex:];
-[_SBButterflyAppsLayoutModifier canPerformKeyboardShortcutAction:forBundleIdentifier:];
-[_SBButterflyAppsLayoutModifier isLayoutRoleEligibleForContentDragSpringLoading:inAppLayout:];
-[_SBButterflyAppsLayoutModifier frameForSplitViewHandleNubView:];
-[_SBButterflyAppsLayoutModifier preferredAppLayoutToReuseAccessoryForAppLayout:fromAppLayouts:];
-[_SBButterflyAppsLayoutModifier indexToScrollToAfterInsertingAtIndex:];
-[_SBButterflyAppsLayoutModifier isItemContainerPointerInteractionEnabled];
-[_SBButterflyAppsLayoutModifier regionDividerCenter];
-[_SBButterflyAppsLayoutModifier appLayoutsToResignActive];
-[_SBButterflyAppsLayoutModifier shelfBackgroundBlurOpacity];
-[_SBButterflyAppsLayoutModifier animationAttributesForItem:];
-[_SBButterflyAppsLayoutModifier isLayoutRoleSelectable:inAppLayout:];
-[_SBButterflyAppsLayoutModifier opacityForItem:];
-[_SBButterflyAppsLayoutModifier appLayoutForReceivingHardwareButtonEvents];
-[_SBButterflyAppsLayoutModifier dimmingAlphaForItem:];
-[_SBButterflyAppsLayoutModifier shouldSuppressHighlightEffectForLayoutRole:inAppLayout:];
-[_SBButterflyAppsLayoutModifier wantsRegionDivider];
-[_SBButterflyAppsLayoutModifier lighteningAlphaForIndex:];
-[_SBButterflyAppsLayoutModifier preferredStatusBarAxis];
-[_SBButterflyAppsLayoutModifier shelfBackgroundBlurFrame];
-[_SBButterflyAppsLayoutModifier asyncRenderingAttributesForAppLayout:];
-[_SBButterflyAppsLayoutModifier wantsHomeScreenPointerInteractions];
-[_SBButterflyAppsLayoutModifier shouldConfigureInAppDockHiddenAssertion];
-[_SBButterflyAppsLayoutModifier regionDividerOptions];
-[_SBButterflyAppsLayoutModifier preferredSnapshotOrientationForAppLayout:];
-[_SBButterflyAppsLayoutModifier topMostItems];
-[_SBButterflyAppsLayoutModifier visibleAppSpaces];
-[_SBButterflyAppsLayoutModifier shouldBringCardToFrontDuringInsertionOrRemoval];
-[_SBButterflyAppsLayoutModifier supportsHomeAffordanceForItem:];
-[_SBButterflyAppsLayoutModifier frameForItem:];
-[_SBButterflyAppsLayoutModifier shouldAnimateInsertionOrRemovalOfAppLayout:atIndex:];
-[_SBButterflyAppsLayoutModifier wantsAsynchronousSurfaceRetentionAssertion];
-[_SBButterflyAppsLayoutModifier titleStyleForItem:];
-[_SBButterflyAppsLayoutModifier appLayoutsToCacheFullsizeSnapshots];
-[_SBButterflyAppsLayoutModifier isLayoutRoleDraggable:inAppLayout:];
-[_SBButterflyAppsLayoutModifier preferredSwitcherScreenRegionForAppLayout:];
-[_SBButterflyAppsLayoutModifier _isAppsRegionFullScreen];
```
