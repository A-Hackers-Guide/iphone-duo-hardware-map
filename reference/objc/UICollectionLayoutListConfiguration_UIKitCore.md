# `UICollectionLayoutListConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 15 instance variables, 16 properties, 35 instance methods, 0 class methods

## Instance variables

```
B _hasCompactSectionSpacing;
B _showsSeparators;
@"UIListSeparatorConfiguration" _separatorConfiguration;
d _cornerRadius;
@? _willBeginSwipingHandler;
@? _didEndSwipingHandler;
q _appearance;
@? _itemSeparatorHandler;
@"UIColor" _backgroundColor;
@? _leadingSwipeActionsConfigurationProvider;
@? _trailingSwipeActionsConfigurationProvider;
q _headerMode;
q _footerMode;
d _headerTopPadding;
Q _contentHuggingElements;
```

## Properties

```
@property (Td,N,G_cornerRadius,S_setCornerRadius:,V_cornerRadius) _cornerRadius;
@property (T@?,C,N,G_willBeginSwipingHandler,S_setWillBeginSwipingHandler:,V_willBeginSwipingHandler) _willBeginSwipingHandler;
@property (T@?,C,N,G_didEndSwipingHandler,S_setDidEndSwipingHandler:,V_didEndSwipingHandler) _didEndSwipingHandler;
@property (TB,N,S_setSectionHeaderHugsContent:) _sectionHeaderHugsContent;
@property (TB,N,S_setHasCompactSectionSpacing:,V_hasCompactSectionSpacing) _hasCompactSectionSpacing;
@property (Tq,R,N,V_appearance) appearance;
@property (TB,N,V_showsSeparators) showsSeparators;
@property (T@"UIListSeparatorConfiguration",C,N,V_separatorConfiguration) separatorConfiguration;
@property (T@?,C,N,V_itemSeparatorHandler) itemSeparatorHandler;
@property (T@"UIColor",&,N,V_backgroundColor) backgroundColor;
@property (T@?,C,N,V_leadingSwipeActionsConfigurationProvider) leadingSwipeActionsConfigurationProvider;
@property (T@?,C,N,V_trailingSwipeActionsConfigurationProvider) trailingSwipeActionsConfigurationProvider;
@property (Tq,N,V_headerMode) headerMode;
@property (Tq,N,V_footerMode) footerMode;
@property (Td,N,V_headerTopPadding) headerTopPadding;
@property (TQ,N,V_contentHuggingElements) contentHuggingElements;
```

## Instance methods

```
-[UICollectionLayoutListConfiguration _setCornerRadius:];
-[UICollectionLayoutListConfiguration setSeparatorConfiguration:];
-[UICollectionLayoutListConfiguration headerTopPadding];
-[UICollectionLayoutListConfiguration setHeaderTopPadding:];
-[UICollectionLayoutListConfiguration separatorConfiguration];
-[UICollectionLayoutListConfiguration setHeaderMode:];
-[UICollectionLayoutListConfiguration _cornerRadius];
-[UICollectionLayoutListConfiguration init];
-[UICollectionLayoutListConfiguration _setHasCompactSectionSpacing:];
-[UICollectionLayoutListConfiguration _setDidEndSwipingHandler:];
-[UICollectionLayoutListConfiguration footerMode];
-[UICollectionLayoutListConfiguration _sectionHeaderHugsContent];
-[UICollectionLayoutListConfiguration _willBeginSwipingHandler];
-[UICollectionLayoutListConfiguration setContentHuggingElements:];
-[UICollectionLayoutListConfiguration _setWillBeginSwipingHandler:];
-[UICollectionLayoutListConfiguration trailingSwipeActionsConfigurationProvider];
-[UICollectionLayoutListConfiguration setBackgroundColor:];
-[UICollectionLayoutListConfiguration _spiConfiguration];
-[UICollectionLayoutListConfiguration setShowsSeparators:];
-[UICollectionLayoutListConfiguration headerMode];
-[UICollectionLayoutListConfiguration leadingSwipeActionsConfigurationProvider];
-[UICollectionLayoutListConfiguration setItemSeparatorHandler:];
-[UICollectionLayoutListConfiguration backgroundColor];
-[UICollectionLayoutListConfiguration showsSeparators];
-[UICollectionLayoutListConfiguration appearance];
-[UICollectionLayoutListConfiguration _setSectionHeaderHugsContent:];
-[UICollectionLayoutListConfiguration copyWithZone:];
-[UICollectionLayoutListConfiguration setFooterMode:];
-[UICollectionLayoutListConfiguration _hasCompactSectionSpacing];
-[UICollectionLayoutListConfiguration contentHuggingElements];
-[UICollectionLayoutListConfiguration itemSeparatorHandler];
-[UICollectionLayoutListConfiguration setTrailingSwipeActionsConfigurationProvider:];
-[UICollectionLayoutListConfiguration initWithAppearance:];
-[UICollectionLayoutListConfiguration setLeadingSwipeActionsConfigurationProvider:];
-[UICollectionLayoutListConfiguration _didEndSwipingHandler];
```
