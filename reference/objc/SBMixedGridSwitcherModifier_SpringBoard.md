# `SBMixedGridSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- Protocols: `SBMixedGridSwitcherProviding`
- 23 instance variables, 11 properties, 110 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _previousContentOffset;
B _isScrollingForward;
@"SBSwitcherModifier" _gridModifier;
B _hasForegroundFullScreenApp;
B _isSwitcherVisible;
B _cachedVisibleAppsRangeIsValid;
{_NSRange="location"Q"length"Q} _cachedVisibleAppsRange;
B _isScrolling;
Q _lastAppLayoutsGenerationCount;
Q _cachedIndexOfFirstMainAppLayout;
d _cachedFullScreenCardScale;
{CGSize="width"d"height"d} _cachedContentSize;
@"NSMutableDictionary" _cachedFrameForIndex;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _cachedCenterCardFrame;
q _lastInterfaceOrientation;
{?="cachedIndexOfFirstMainAppLayoutIsValid"b1"cachedFullScreenCardScaleIsValid"b1"cachedContentSizeIsValid"b1"cachedFrameForIndexIsValid"b1"cachedCenterCardFrameIsValid"b1} _cachesValidity;
B _reversesFloatingCardDirection;
B _supportsCenterModalAppLayouts;
B _disableFullScreenCardScaleRounding;
Q _lowDensityGridLayoutAlignment;
Q _maximumNumberOfFullScreenCardsForSingleRow;
{CGSize="width"d"height"d} _fullScreenCardSize;
{CGSize="width"d"height"d} _floatingCardSize;
```

## Properties

```
@property (TB,N,V_disableFullScreenCardScaleRounding) disableFullScreenCardScaleRounding;
@property (T{CGSize=dd},R,N,V_fullScreenCardSize) fullScreenCardSize;
@property (T{CGSize=dd},R,N,V_floatingCardSize) floatingCardSize;
@property (TB,N,V_supportsCenterModalAppLayouts) supportsCenterModalAppLayouts;
@property (TQ,N,V_lowDensityGridLayoutAlignment) lowDensityGridLayoutAlignment;
@property (TQ,N,V_maximumNumberOfFullScreenCardsForSingleRow) maximumNumberOfFullScreenCardsForSingleRow;
@property (TB,N,V_reversesFloatingCardDirection) reversesFloatingCardDirection;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBMixedGridSwitcherModifier contentViewScale];
-[SBMixedGridSwitcherModifier scaleForIndex:];
-[SBMixedGridSwitcherModifier titleOpacityForIndex:];
-[SBMixedGridSwitcherModifier adjustedOffsetForOffset:translation:startPoint:locationInView:horizontalVelocity:verticalVelocity:];
-[SBMixedGridSwitcherModifier didMoveToParentModifier:];
-[SBMixedGridSwitcherModifier cornerRadiiForIndex:];
-[SBMixedGridSwitcherModifier clipsToUnobscuredMarginAtIndex:];
-[SBMixedGridSwitcherModifier animationAttributesForLayoutElement:];
-[SBMixedGridSwitcherModifier adjustedAppLayoutsForAppLayouts:];
-[SBMixedGridSwitcherModifier topMostLayoutElements];
-[SBMixedGridSwitcherModifier titleAndIconOpacityForIndex:];
-[SBMixedGridSwitcherModifier appLayoutsToCacheSnapshots];
-[SBMixedGridSwitcherModifier handleTransitionEvent:];
-[SBMixedGridSwitcherModifier visibleAppLayouts];
-[SBMixedGridSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBMixedGridSwitcherModifier shadowOpacityForLayoutRole:atIndex:];
-[SBMixedGridSwitcherModifier contentOffsetForIndex:alignment:];
-[SBMixedGridSwitcherModifier headerStyleForIndex:];
-[SBMixedGridSwitcherModifier isIndexRubberbandableForSwipeToKill:];
-[SBMixedGridSwitcherModifier frameForIndex:];
-[SBMixedGridSwitcherModifier activeLeafAppLayoutsReachableByKeyboardShortcut];
-[SBMixedGridSwitcherModifier adjustedContinuousExposeIdentifiersInStripFromPreviousIdentifiersInStrip:];
-[SBMixedGridSwitcherModifier destinationAppLayoutForDismissingCurrentMode];
-[SBMixedGridSwitcherModifier backgroundOpacityForIndex:];
-[SBMixedGridSwitcherModifier neighboringAppLayoutsForFocusedAppLayout:];
-[SBMixedGridSwitcherModifier visibleMarginForItemContainerAtIndex:];
-[SBMixedGridSwitcherModifier indexToScrollToAfterRemovingIndex:];
-[SBMixedGridSwitcherModifier distanceToLeadingEdgeOfLeadingCardFromTrailingEdgeOfScreenWithVisibleIndexToStartSearch:];
-[SBMixedGridSwitcherModifier restingOffsetForScrollOffset:velocity:];
-[SBMixedGridSwitcherModifier regionDividerOpacity];
-[SBMixedGridSwitcherModifier resetAdjustedScrollingState];
-[SBMixedGridSwitcherModifier snapshotScaleForLayoutRole:inAppLayout:];
-[SBMixedGridSwitcherModifier isLayoutRoleKillable:inAppLayout:atIndex:];
-[SBMixedGridSwitcherModifier indexToScrollToAfterInsertingAtIndex:];
-[SBMixedGridSwitcherModifier _contentSize];
-[SBMixedGridSwitcherModifier slideOverTongueDirection];
-[SBMixedGridSwitcherModifier regionDividerCenter];
-[SBMixedGridSwitcherModifier blurViewIconScaleForIndex:];
-[SBMixedGridSwitcherModifier inactiveAppLayoutsReachableByKeyboardShortcut];
-[SBMixedGridSwitcherModifier shouldTetherItemsAndAccessoriesInAppLayout:];
-[SBMixedGridSwitcherModifier handleScrollEvent:];
-[SBMixedGridSwitcherModifier shouldSuppressHighlightEffectForLayoutRole:inAppLayout:];
-[SBMixedGridSwitcherModifier wantsRegionDivider];
-[SBMixedGridSwitcherModifier scrollViewAttributes];
-[SBMixedGridSwitcherModifier shadowOffsetForIndex:];
-[SBMixedGridSwitcherModifier _cardCornerRadiusInSwitcher];
-[SBMixedGridSwitcherModifier shadowStyleForLayoutRole:inAppLayout:];
-[SBMixedGridSwitcherModifier copyWithZone:];
-[SBMixedGridSwitcherModifier minimumTranslationToKillIndex:];
-[SBMixedGridSwitcherModifier regionDividerOptions];
-[SBMixedGridSwitcherModifier adjustedContinuousExposeIdentifiersInSwitcherFromPreviousIdentifiersInSwitcher:identifiersInStrip:];
-[SBMixedGridSwitcherModifier shouldBringCardToFrontDuringInsertionOrRemoval];
-[SBMixedGridSwitcherModifier _visibleAppLayoutRangeForContentOffset:];
-[SBMixedGridSwitcherModifier shouldAnimateInsertionOrRemovalOfAppLayout:atIndex:];
-[SBMixedGridSwitcherModifier canFocusableAppLayoutBeEffectivelyObscured:];
-[SBMixedGridSwitcherModifier contentPageViewScaleForAppLayout:withScale:];
-[SBMixedGridSwitcherModifier appLayoutsToCacheFullsizeSnapshots];
-[SBMixedGridSwitcherModifier _forwardingTargetForUpdate];
-[SBMixedGridSwitcherModifier isLayoutRoleDraggable:inAppLayout:];
-[SBMixedGridSwitcherModifier _verticalSpacing];
-[SBMixedGridSwitcherModifier isIndexVisible:];
-[SBMixedGridSwitcherModifier _adjustedFrame:forFloatingAppIndex:];
-[SBMixedGridSwitcherModifier _cacheKeyForLayoutRole:inAppLayout:];
-[SBMixedGridSwitcherModifier _cachedCenterCardFrame];
-[SBMixedGridSwitcherModifier _cachedFullScreenCardScale];
-[SBMixedGridSwitcherModifier _cardHeaderHeight];
-[SBMixedGridSwitcherModifier _fittedContentSize];
-[SBMixedGridSwitcherModifier _fittedFloatingContentSize];
-[SBMixedGridSwitcherModifier _fittedFullScreenContentSize];
-[SBMixedGridSwitcherModifier _floatingAppsStackRange];
-[SBMixedGridSwitcherModifier _floatingCardScale];
-[SBMixedGridSwitcherModifier _frameForIndex:applyScrollViewContentOffset:];
-[SBMixedGridSwitcherModifier _fullScreenCardScale];
-[SBMixedGridSwitcherModifier _horizontalSpacing];
-[SBMixedGridSwitcherModifier _indexOfFirstFloatingLayoutFromAppLayouts:];
-[SBMixedGridSwitcherModifier _indexOfLeadingCard];
-[SBMixedGridSwitcherModifier _invalidateCachesIfNeeded];
-[SBMixedGridSwitcherModifier _isDoubleStackingFullScreenCards];
-[SBMixedGridSwitcherModifier _isIndexFullScreenOrCenterModal:];
-[SBMixedGridSwitcherModifier _minimumFullScreenContentSize];
-[SBMixedGridSwitcherModifier _numberOfFloatingColumns];
-[SBMixedGridSwitcherModifier _numberOfFullScreenAppLayouts];
-[SBMixedGridSwitcherModifier _numberOfFullScreenColumns];
-[SBMixedGridSwitcherModifier _numberOfFullScreenRows];
-[SBMixedGridSwitcherModifier _numberOfOffScreenTrailingFloatingCardsForContentOffset:];
-[SBMixedGridSwitcherModifier _numberOfOffScreenTrailingFullScreenCardsForContentOffset:];
-[SBMixedGridSwitcherModifier _scaledCardSizeForIndex:];
-[SBMixedGridSwitcherModifier _subtreeIndexForIndex:indexOfFirstMainAppLayout:];
-[SBMixedGridSwitcherModifier _unpaddedCoplanarFrameForIndex:doubleStack:count:cardSize:scale:contentWidth:];
-[SBMixedGridSwitcherModifier _visibleAppLayoutRangeForContentOffset:lastVisibleIndex:];
-[SBMixedGridSwitcherModifier disableFullScreenCardScaleRounding];
-[SBMixedGridSwitcherModifier firstFloatingCardPeekingWidth];
-[SBMixedGridSwitcherModifier floatingCardSize];
-[SBMixedGridSwitcherModifier fullScreenCardSize];
-[SBMixedGridSwitcherModifier indexOfFirstMainAppLayoutFromAppLayouts:];
-[SBMixedGridSwitcherModifier initWithFullScreenCardSize:floatingCardSize:];
-[SBMixedGridSwitcherModifier isIndexFullyVisible:];
-[SBMixedGridSwitcherModifier lowDensityGridLayoutAlignment];
-[SBMixedGridSwitcherModifier maximumNumberOfFullScreenCardsForSingleRow];
-[SBMixedGridSwitcherModifier numberOfFloatingAppLayouts];
-[SBMixedGridSwitcherModifier rangeOfVisibleAppLayouts];
-[SBMixedGridSwitcherModifier responseForProposedChildResponse:childModifier:event:];
-[SBMixedGridSwitcherModifier reversesFloatingCardDirection];
-[SBMixedGridSwitcherModifier setDisableFullScreenCardScaleRounding:];
-[SBMixedGridSwitcherModifier setLowDensityGridLayoutAlignment:];
-[SBMixedGridSwitcherModifier setMaximumNumberOfFullScreenCardsForSingleRow:];
-[SBMixedGridSwitcherModifier setReversesFloatingCardDirection:];
-[SBMixedGridSwitcherModifier setSupportsCenterModalAppLayouts:];
-[SBMixedGridSwitcherModifier supportsCenterModalAppLayouts];
-[SBMixedGridSwitcherModifier unadjustedScaleForIndex:];
```
