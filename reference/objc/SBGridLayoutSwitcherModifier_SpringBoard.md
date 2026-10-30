# `SBGridLayoutSwitcherModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifier`
- Protocols: `PTSettingsKeyObserver`
- 4 instance variables, 7 properties, 68 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _previousContentOffset;
B _isScrollingForward;
Q _alignment;
Q _layoutDirection;
```

## Properties

```
@property (TQ,N,V_alignment) alignment;
@property (TQ,N,V_layoutDirection) layoutDirection;
@property (Td,R,N) scale;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBGridLayoutSwitcherModifier contentViewScale];
-[SBGridLayoutSwitcherModifier scaleForIndex:];
-[SBGridLayoutSwitcherModifier titleOpacityForIndex:];
-[SBGridLayoutSwitcherModifier rotationAngleForIndex:];
-[SBGridLayoutSwitcherModifier _applyPrototypeSettings];
-[SBGridLayoutSwitcherModifier adjustedOffsetForOffset:translation:startPoint:locationInView:horizontalVelocity:verticalVelocity:];
-[SBGridLayoutSwitcherModifier didMoveToParentModifier:];
-[SBGridLayoutSwitcherModifier cornerRadiiForIndex:];
-[SBGridLayoutSwitcherModifier _isIndexVisible:];
-[SBGridLayoutSwitcherModifier clipsToUnobscuredMarginAtIndex:];
-[SBGridLayoutSwitcherModifier animationAttributesForLayoutElement:];
-[SBGridLayoutSwitcherModifier visibleHomeAffordanceLayoutElements];
-[SBGridLayoutSwitcherModifier titleAndIconOpacityForIndex:];
-[SBGridLayoutSwitcherModifier appLayoutsToCacheSnapshots];
-[SBGridLayoutSwitcherModifier handleTransitionEvent:];
-[SBGridLayoutSwitcherModifier _cornerRadius];
-[SBGridLayoutSwitcherModifier visibleAppLayouts];
-[SBGridLayoutSwitcherModifier opacityForLayoutRole:inAppLayout:atIndex:];
-[SBGridLayoutSwitcherModifier handleSwitcherSettingsChangedEvent:];
-[SBGridLayoutSwitcherModifier shadowOpacityForLayoutRole:atIndex:];
-[SBGridLayoutSwitcherModifier setLayoutDirection:];
-[SBGridLayoutSwitcherModifier contentOffsetForIndex:alignment:];
-[SBGridLayoutSwitcherModifier frameForIndex:];
-[SBGridLayoutSwitcherModifier adjustedContinuousExposeIdentifiersInStripFromPreviousIdentifiersInStrip:];
-[SBGridLayoutSwitcherModifier layoutDirection];
-[SBGridLayoutSwitcherModifier visibleMarginForItemContainerAtIndex:];
-[SBGridLayoutSwitcherModifier setAlignment:];
-[SBGridLayoutSwitcherModifier indexToScrollToAfterRemovingIndex:];
-[SBGridLayoutSwitcherModifier distanceToLeadingEdgeOfLeadingCardFromTrailingEdgeOfScreenWithVisibleIndexToStartSearch:];
-[SBGridLayoutSwitcherModifier restingOffsetForScrollOffset:velocity:];
-[SBGridLayoutSwitcherModifier regionDividerOpacity];
-[SBGridLayoutSwitcherModifier alignment];
-[SBGridLayoutSwitcherModifier resetAdjustedScrollingState];
-[SBGridLayoutSwitcherModifier snapshotScaleForLayoutRole:inAppLayout:];
-[SBGridLayoutSwitcherModifier scale];
-[SBGridLayoutSwitcherModifier indexToScrollToAfterInsertingAtIndex:];
-[SBGridLayoutSwitcherModifier _contentSize];
-[SBGridLayoutSwitcherModifier regionDividerCenter];
-[SBGridLayoutSwitcherModifier handleScrollEvent:];
-[SBGridLayoutSwitcherModifier wantsRegionDivider];
-[SBGridLayoutSwitcherModifier scrollViewAttributes];
-[SBGridLayoutSwitcherModifier shadowOffsetForIndex:];
-[SBGridLayoutSwitcherModifier minimumTranslationToKillIndex:];
-[SBGridLayoutSwitcherModifier regionDividerOptions];
-[SBGridLayoutSwitcherModifier adjustedContinuousExposeIdentifiersInSwitcherFromPreviousIdentifiersInSwitcher:identifiersInStrip:];
-[SBGridLayoutSwitcherModifier iconOpacityForIndex:];
-[SBGridLayoutSwitcherModifier shouldBringCardToFrontDuringInsertionOrRemoval];
-[SBGridLayoutSwitcherModifier isHomeAffordanceSupportedForAppLayout:];
-[SBGridLayoutSwitcherModifier shouldAnimateInsertionOrRemovalOfAppLayout:atIndex:];
-[SBGridLayoutSwitcherModifier contentPageViewScaleForAppLayout:withScale:];
-[SBGridLayoutSwitcherModifier appLayoutsToCacheFullsizeSnapshots];
-[SBGridLayoutSwitcherModifier _forwardingTargetForUpdate];
-[SBGridLayoutSwitcherModifier _numberOfColumns];
-[SBGridLayoutSwitcherModifier _verticalSpacing];
-[SBGridLayoutSwitcherModifier _columnForIndex:];
-[SBGridLayoutSwitcherModifier _numberOfSpaces];
-[SBGridLayoutSwitcherModifier _scaledCardSize];
-[SBGridLayoutSwitcherModifier _appLayoutIndexForSpaceIndex:];
-[SBGridLayoutSwitcherModifier _cardHeaderHeight];
-[SBGridLayoutSwitcherModifier _firstTrailingIndexForContentOffset:];
-[SBGridLayoutSwitcherModifier _fittedContentSize];
-[SBGridLayoutSwitcherModifier _frameForIndex:ignoringScrollOffset:];
-[SBGridLayoutSwitcherModifier _frameWithScaleAppliedForIndex:ignoringScrollOffset:];
-[SBGridLayoutSwitcherModifier _horizontalSpacing];
-[SBGridLayoutSwitcherModifier _indexOfLeadingCard];
-[SBGridLayoutSwitcherModifier _rowForIndex:];
-[SBGridLayoutSwitcherModifier initWithAlignment:layoutDirection:];
-[SBGridLayoutSwitcherModifier visibleAppLayoutRangeForContentOffset:];
```
