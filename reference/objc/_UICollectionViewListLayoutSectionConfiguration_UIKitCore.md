# `_UICollectionViewListLayoutSectionConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 26 instance variables, 30 properties, 80 instance methods, 1 class methods

## Instance variables

```
B _stylesFirstItemAsHeader;
B _sectionHeaderHugsContent;
B _hasCompactSectionSpacing;
B __apiVersion;
@"_UIListSeparatorConfiguration" _separatorConfiguration;
@? _itemSeparatorHandler;
q _appearanceStyle;
d _cornerRadius;
d _rowHeight;
d _sectionHeaderHeight;
d _sectionFooterHeight;
d _estimatedRowHeight;
d _estimatedSectionHeaderHeight;
d _estimatedSectionFooterHeight;
d _headerTopPadding;
q _separatorStyle;
@? _separatorInsetProvider;
@? _leadingSwipeActionsConfigurationProvider;
@? _trailingSwipeActionsConfigurationProvider;
@? _willBeginSwipingHandler;
@? _didEndSwipingHandler;
@"UICollectionView" _collectionView;
@"<NSCollectionLayoutEnvironment_Private>" _layoutEnvironment;
@"NSString" __headerElementKind;
@"NSString" __footerElementKind;
@"UIColor" __backgroundColor;
```

## Properties

```
@property (T@"UICollectionView",R,W,N,G_collectionView,V_collectionView) collectionView;
@property (T@"<NSCollectionLayoutEnvironment_Private>",R,N,G_layoutEnvironment,V_layoutEnvironment) layoutEnvironment;
@property (T@"<UITableConstants>",R,N,G_constants) constants;
@property (T@"_UIListSeparatorConfiguration",R,N,G_separatorConfigurationNoCopy) _separatorConfigurationNoCopy;
@property (TB,R,N,G_wantsSwipeActions) wantsSwipeActions;
@property (TB,N,G_isAPIVersion,V__apiVersion) _apiVersion;
@property (T@"NSString",C,N,V__headerElementKind) _headerElementKind;
@property (T@"NSString",C,N,V__footerElementKind) _footerElementKind;
@property (T@"UIColor",&,N,V__backgroundColor) _backgroundColor;
@property (T@?,C,N,G_itemSeparatorHandler,S_setItemSeparatorHandler:,V_itemSeparatorHandler) _itemSeparatorHandler;
@property (Tq,N,V_appearanceStyle) appearanceStyle;
@property (Td,N,V_cornerRadius) cornerRadius;
@property (TB,N,V_stylesFirstItemAsHeader) stylesFirstItemAsHeader;
@property (Td,N,V_rowHeight) rowHeight;
@property (Td,N,V_sectionHeaderHeight) sectionHeaderHeight;
@property (Td,N,V_sectionFooterHeight) sectionFooterHeight;
@property (Td,N,V_estimatedRowHeight) estimatedRowHeight;
@property (Td,N,V_estimatedSectionHeaderHeight) estimatedSectionHeaderHeight;
@property (Td,N,V_estimatedSectionFooterHeight) estimatedSectionFooterHeight;
@property (TB,N,V_sectionHeaderHugsContent) sectionHeaderHugsContent;
@property (TB,N,V_hasCompactSectionSpacing) hasCompactSectionSpacing;
@property (Td,N,V_headerTopPadding) headerTopPadding;
@property (T@"_UIListSeparatorConfiguration",C,N,G_separatorConfiguration,S_setSeparatorConfiguration:,V_separatorConfiguration) _separatorConfiguration;
@property (Tq,N,V_separatorStyle) separatorStyle;
@property (T{NSDirectionalEdgeInsets=dddd},N) separatorInset;
@property (T@?,C,N,V_separatorInsetProvider) separatorInsetProvider;
@property (T@?,C,N,V_leadingSwipeActionsConfigurationProvider) leadingSwipeActionsConfigurationProvider;
@property (T@?,C,N,V_trailingSwipeActionsConfigurationProvider) trailingSwipeActionsConfigurationProvider;
@property (T@?,C,N,V_willBeginSwipingHandler) willBeginSwipingHandler;
@property (T@?,C,N,V_didEndSwipingHandler) didEndSwipingHandler;
```

## Class methods

```
+[_UICollectionViewListLayoutSectionConfiguration new];
```

## Instance methods

```
-[_UICollectionViewListLayoutSectionConfiguration _wantsSwipeActions];
-[_UICollectionViewListLayoutSectionConfiguration estimatedSectionFooterHeight];
-[_UICollectionViewListLayoutSectionConfiguration initWithCollectionView:];
-[_UICollectionViewListLayoutSectionConfiguration separatorInset];
-[_UICollectionViewListLayoutSectionConfiguration _sectionSpacingStyle];
-[_UICollectionViewListLayoutSectionConfiguration _effectiveEstimatedSectionHeaderHeight];
-[_UICollectionViewListLayoutSectionConfiguration headerTopPadding];
-[_UICollectionViewListLayoutSectionConfiguration setHeaderTopPadding:];
-[_UICollectionViewListLayoutSectionConfiguration stylesFirstItemAsHeader];
-[_UICollectionViewListLayoutSectionConfiguration _setItemSeparatorHandler:];
-[_UICollectionViewListLayoutSectionConfiguration _effectiveEstimatedRowHeight];
-[_UICollectionViewListLayoutSectionConfiguration _backgroundColor];
-[_UICollectionViewListLayoutSectionConfiguration setDidEndSwipingHandler:];
-[_UICollectionViewListLayoutSectionConfiguration setSeparatorStyle:];
-[_UICollectionViewListLayoutSectionConfiguration setSectionHeaderHugsContent:];
-[_UICollectionViewListLayoutSectionConfiguration estimatedRowHeight];
-[_UICollectionViewListLayoutSectionConfiguration setSeparatorInsetProvider:];
-[_UICollectionViewListLayoutSectionConfiguration init];
-[_UICollectionViewListLayoutSectionConfiguration _separatorHeight];
-[_UICollectionViewListLayoutSectionConfiguration initWithAppearanceStyle:layoutEnvironment:];
-[_UICollectionViewListLayoutSectionConfiguration setRowHeight:];
-[_UICollectionViewListLayoutSectionConfiguration separatorInsetProvider];
-[_UICollectionViewListLayoutSectionConfiguration set_footerElementKind:];
-[_UICollectionViewListLayoutSectionConfiguration set_headerElementKind:];
-[_UICollectionViewListLayoutSectionConfiguration _effectiveEstimatedSectionFooterHeight];
-[_UICollectionViewListLayoutSectionConfiguration _separatorConfiguration];
-[_UICollectionViewListLayoutSectionConfiguration setSeparatorInset:];
-[_UICollectionViewListLayoutSectionConfiguration _constants];
-[_UICollectionViewListLayoutSectionConfiguration _separatorConfigurationNoCopy];
-[_UICollectionViewListLayoutSectionConfiguration _setSeparatorConfiguration:];
-[_UICollectionViewListLayoutSectionConfiguration appearanceStyle];
-[_UICollectionViewListLayoutSectionConfiguration sectionFooterHeight];
-[_UICollectionViewListLayoutSectionConfiguration _createSeparatorForBottom:];
-[_UICollectionViewListLayoutSectionConfiguration set_backgroundColor:];
-[_UICollectionViewListLayoutSectionConfiguration _setDefaultBackgroundColor:];
-[_UICollectionViewListLayoutSectionConfiguration _defaultSectionHeaderHeight];
-[_UICollectionViewListLayoutSectionConfiguration setCornerRadius:];
-[_UICollectionViewListLayoutSectionConfiguration trailingSwipeActionsConfigurationProvider];
-[_UICollectionViewListLayoutSectionConfiguration _createSwipeActionsContainer];
-[_UICollectionViewListLayoutSectionConfiguration didEndSwipingHandler];
-[_UICollectionViewListLayoutSectionConfiguration _shouldSupplementariesFollowSectionInsets];
-[_UICollectionViewListLayoutSectionConfiguration setEstimatedSectionHeaderHeight:];
-[_UICollectionViewListLayoutSectionConfiguration sectionHeaderHeight];
-[_UICollectionViewListLayoutSectionConfiguration setStylesFirstItemAsHeader:];
-[_UICollectionViewListLayoutSectionConfiguration _footerElementKind];
-[_UICollectionViewListLayoutSectionConfiguration setSectionHeaderHeight:];
-[_UICollectionViewListLayoutSectionConfiguration setEstimatedRowHeight:];
-[_UICollectionViewListLayoutSectionConfiguration _addSupplementaryItemsToLayout:headerFooterPinningBehavior:];
-[_UICollectionViewListLayoutSectionConfiguration setWillBeginSwipingHandler:];
-[_UICollectionViewListLayoutSectionConfiguration _hasSupplementaryAsHeader];
-[_UICollectionViewListLayoutSectionConfiguration willBeginSwipingHandler];
-[_UICollectionViewListLayoutSectionConfiguration set_apiVersion:];
-[_UICollectionViewListLayoutSectionConfiguration setEstimatedSectionFooterHeight:];
-[_UICollectionViewListLayoutSectionConfiguration cornerRadius];
-[_UICollectionViewListLayoutSectionConfiguration _itemSeparatorHandler];
-[_UICollectionViewListLayoutSectionConfiguration _usesSectionBackgroundDecoration];
-[_UICollectionViewListLayoutSectionConfiguration leadingSwipeActionsConfigurationProvider];
-[_UICollectionViewListLayoutSectionConfiguration _hasFooter];
-[_UICollectionViewListLayoutSectionConfiguration _generateLayoutGroup:];
-[_UICollectionViewListLayoutSectionConfiguration rowHeight];
-[_UICollectionViewListLayoutSectionConfiguration _traitCollection];
-[_UICollectionViewListLayoutSectionConfiguration estimatedSectionHeaderHeight];
-[_UICollectionViewListLayoutSectionConfiguration _sectionPosition];
-[_UICollectionViewListLayoutSectionConfiguration _listGeometry];
-[_UICollectionViewListLayoutSectionConfiguration hasCompactSectionSpacing];
-[_UICollectionViewListLayoutSectionConfiguration setAppearanceStyle:];
-[_UICollectionViewListLayoutSectionConfiguration _collectionView];
-[_UICollectionViewListLayoutSectionConfiguration _defaultSectionFooterHeight];
-[_UICollectionViewListLayoutSectionConfiguration setSectionFooterHeight:];
-[_UICollectionViewListLayoutSectionConfiguration setHasCompactSectionSpacing:];
-[_UICollectionViewListLayoutSectionConfiguration _hasHeaderOrFirstItemStyledAsHeader];
-[_UICollectionViewListLayoutSectionConfiguration copyWithZone:];
-[_UICollectionViewListLayoutSectionConfiguration _isAPIVersion];
-[_UICollectionViewListLayoutSectionConfiguration _headerElementKind];
-[_UICollectionViewListLayoutSectionConfiguration separatorStyle];
-[_UICollectionViewListLayoutSectionConfiguration setTrailingSwipeActionsConfigurationProvider:];
-[_UICollectionViewListLayoutSectionConfiguration sectionHeaderHugsContent];
-[_UICollectionViewListLayoutSectionConfiguration _defaultRowHeight];
-[_UICollectionViewListLayoutSectionConfiguration setLeadingSwipeActionsConfigurationProvider:];
-[_UICollectionViewListLayoutSectionConfiguration _layoutEnvironment];
```
