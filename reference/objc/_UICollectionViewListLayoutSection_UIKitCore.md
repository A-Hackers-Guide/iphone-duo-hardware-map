# `_UICollectionViewListLayoutSection`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSCollectionLayoutSection`
- Protocols: `_UICollectionLayoutSectionCallback`
- 8 instance variables, 11 properties, 61 instance methods, 0 class methods

## Instance variables

```
@"_UICollectionViewListLayoutSectionConfiguration" _configuration;
{?="hasCustomizedContentInsets"b1} _sectionFlags;
q _headerFooterPinningBehavior;
d _paddingToBoundarySupplementaries;
@"<NSCollectionLayoutEnvironment_Private>" _layoutEnvironment;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _defaultSectionContentInsets;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _defaultDirectionalLayoutMargins;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _defaultSeparatorInsets;
```

## Properties

```
@property (T@"<NSCollectionLayoutEnvironment_Private>",R,N,G_layoutEnvironment,V_layoutEnvironment) layoutEnvironment;
@property (T@"_UICollectionLayoutContainer",R,N) _layoutContainer;
@property (Tq,R,N,V_headerFooterPinningBehavior) _headerFooterPinningBehavior;
@property (T{NSDirectionalEdgeInsets=dddd},R,N,V_defaultSectionContentInsets) _defaultSectionContentInsets;
@property (Td,R,N,V_paddingToBoundarySupplementaries) _paddingToBoundarySupplementaries;
@property (T{NSDirectionalEdgeInsets=dddd},R,N,V_defaultDirectionalLayoutMargins) _defaultDirectionalLayoutMargins;
@property (T{NSDirectionalEdgeInsets=dddd},R,N,V_defaultSeparatorInsets) _defaultSeparatorInsets;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UICollectionViewListLayoutSection _wantsSwipeActions];
-[_UICollectionViewListLayoutSection _enrichLayoutAttributes:interactionState:];
-[_UICollectionViewListLayoutSection _defaultSeparatorInsets];
-[_UICollectionViewListLayoutSection _isRTL];
-[_UICollectionViewListLayoutSection _effectiveSectionSupplementaryHorizontalInsets];
-[_UICollectionViewListLayoutSection _hasHorizontalInsets];
-[_UICollectionViewListLayoutSection _maskedCornersForBackgroundOfItemWithSelectionGrouping:];
-[_UICollectionViewListLayoutSection _transformFittingLayoutAttributes:interactionState:];
-[_UICollectionViewListLayoutSection _defaultSectionContentInsets];
-[_UICollectionViewListLayoutSection _defaultSectionContentInsetsForSectionMetrics:];
-[_UICollectionViewListLayoutSection setContentInsets:];
-[_UICollectionViewListLayoutSection _effectiveBoundarySeparatorInsets:];
-[_UICollectionViewListLayoutSection _defaultDirectionalLayoutMargins];
-[_UICollectionViewListLayoutSection _shouldDrawSeparatorAtBottom:ofSection:interactionState:];
-[_UICollectionViewListLayoutSection _willBeginSwiping];
-[_UICollectionViewListLayoutSection _shouldHideTopSeparatorAtIndexPath:interactionState:];
-[_UICollectionViewListLayoutSection _preferredContainerBackgroundColor];
-[_UICollectionViewListLayoutSection _trailingSwipeActionsConfigurationForIndexPath:];
-[_UICollectionViewListLayoutSection _constants];
-[_UICollectionViewListLayoutSection _defaultLayoutMarginsInsideSection];
-[_UICollectionViewListLayoutSection _shouldInvalidateForScrollViewLayoutAdjustmentsChange];
-[_UICollectionViewListLayoutSection _descriptionProperties];
-[_UICollectionViewListLayoutSection initWithConfiguration:];
-[_UICollectionViewListLayoutSection _configureLayoutAttributesForSidebarPlainCell:];
-[_UICollectionViewListLayoutSection __isLastItemInSection:];
-[_UICollectionViewListLayoutSection _configureLayoutAttributesForBackgroundDecoration:];
-[_UICollectionViewListLayoutSection shouldRestrictOrthogonalAxisDuringInteractiveMovement];
-[_UICollectionViewListLayoutSection _separatorConfigurationForItemAtIndexPath:withSelectionGrouping:considerNextCellGrouping:interactionState:];
-[_UICollectionViewListLayoutSection _transformPreferredLayoutAttributes:interactionState:];
-[_UICollectionViewListLayoutSection _configureLayoutAttributesWithInsetGroupedMasking:stylesFirstItemAsHeader:];
-[_UICollectionViewListLayoutSection _defaultLayoutMarginsForHeaderFooterViewWithLayoutAttributes:];
-[_UICollectionViewListLayoutSection _useRoundedSwipeActions];
-[_UICollectionViewListLayoutSection _configureLayoutAttributesWithDefaultMasking:];
-[_UICollectionViewListLayoutSection _separatorInsetBehaviorAtBottom:indexPath:interactionState:];
-[_UICollectionViewListLayoutSection _wantsBandSelectionVisuals];
-[_UICollectionViewListLayoutSection _leadingSwipeActionsConfigurationForIndexPath:];
-[_UICollectionViewListLayoutSection _extensionBehavior];
-[_UICollectionViewListLayoutSection _updateMaxWidthForLayoutAttributes:];
-[_UICollectionViewListLayoutSection _configureLayoutAttributes:forSeparatorAtBottom:preferredConfiguration:interactionState:];
-[_UICollectionViewListLayoutSection contentInsets];
-[_UICollectionViewListLayoutSection _callback];
-[_UICollectionViewListLayoutSection _hasHeaderFooterBelowLastItemInSection:interactionState:];
-[_UICollectionViewListLayoutSection _effectiveCornerRadius];
-[_UICollectionViewListLayoutSection _configureLayoutAttributesForPlainSupplementaryView:];
-[_UICollectionViewListLayoutSection _sectionPreferredBottomSeparatorInsetsForIndexPath:];
-[_UICollectionViewListLayoutSection _shouldHideBottomSeparatorAtIndexPath:forGrouping:considerNextCellGrouping:interactionState:];
-[_UICollectionViewListLayoutSection copyWithZone:];
-[_UICollectionViewListLayoutSection _paddingToBoundarySupplementaries];
-[_UICollectionViewListLayoutSection _headerFooterPinningBehavior];
-[_UICollectionViewListLayoutSection _invalidationContextForCellBackgroundOrBottomSeparatorChangeAtIndexPath:interactionState:separatorOnly:];
-[_UICollectionViewListLayoutSection _sectionPreferredTopSeparatorInsetsWithBottomInsets:hasCustomInsets:];
-[_UICollectionViewListLayoutSection _effectiveSectionHorizontalInsets];
-[_UICollectionViewListLayoutSection _generateListSectionDataForLayoutAttributes:interactionState:];
-[_UICollectionViewListLayoutSection _adjustsLayoutToDrawTopSeparatorInSection:interactionState:];
-[_UICollectionViewListLayoutSection _configureLayoutAttributesForSwipeActionMasking:interactionState:];
-[_UICollectionViewListLayoutSection _didEndSwiping];
-[_UICollectionViewListLayoutSection _layoutContainer];
-[_UICollectionViewListLayoutSection _updateStyleForSwipeActionsConfiguration:];
-[_UICollectionViewListLayoutSection initWithConfiguration:layoutEnvironment:];
-[_UICollectionViewListLayoutSection _layoutEnvironment];
-[_UICollectionViewListLayoutSection _configureLayoutAttributesForPlainCell:];
```
