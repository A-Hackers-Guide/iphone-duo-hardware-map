# `_UIEditMenuPlatformMetrics`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIVisualStyleProviding`
- 37 instance variables, 37 properties, 75 instance methods, 0 class methods

## Instance variables

```
B _showsSeparatorBetweenItems;
B _useThinSeparators;
B _prefersHorizontalLayoutForLargeContentSize;
B _derivesAutomaticArrowDirectionsFromAvailableSpace;
B _pageButtonHasInlineAppearance;
B _supportsContextMenuHandoff;
@? _containerViewConfigurator;
@? _menuBackgroundConfigurator;
@"UIVisualEffect" _menuBackgroundEffect;
@"UIVisualEffect" _menuHighlightBackgroundEffect;
@"UIColor" _menuHighlightBackgroundColor;
@"UIVisualEffect" _separatorEffect;
@"UIColor" _separatorEffectColor;
q _overrideUserInterfaceStyle;
d _shadowOpacity;
d _shadowRadius;
d _horizontalMenuMaximumWidth;
d _horizontalMenuCornerRadius;
d _verticalMenuMaximumHeight;
d _verticalMenuCornerRadius;
d _sourceRectMargins;
d _arrowSideRadius;
d _arrowTipRadius;
@? _menuItemMarginsProvider;
@? _cellBackgroundShapeProvider;
@"UIColor" _destructiveColor;
@"UIFont" _menuItemTitleFont;
@"UIButtonConfiguration" _pageButtonConfiguration;
q _pageButtonSymbolScale;
d _pageButtonAlignmentOffset;
d _pageButtonOverlapAmount;
@"UIFont" _pageButtonFont;
d _pageButtonVisibilityMultiplier;
{CGSize="width"d"height"d} _shadowOffset;
{CGSize="width"d"height"d} _arrowSize;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _sectionInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _additionalSeparatorInsets;
```

## Properties

```
@property (T@?,C,N,V_containerViewConfigurator) containerViewConfigurator;
@property (T@?,C,N,V_menuBackgroundConfigurator) menuBackgroundConfigurator;
@property (T@"UIVisualEffect",C,N,V_menuBackgroundEffect) menuBackgroundEffect;
@property (T@"UIVisualEffect",C,N,V_menuHighlightBackgroundEffect) menuHighlightBackgroundEffect;
@property (T@"UIColor",C,N,V_menuHighlightBackgroundColor) menuHighlightBackgroundColor;
@property (T@"UIVisualEffect",C,N,V_separatorEffect) separatorEffect;
@property (T@"UIColor",C,N,V_separatorEffectColor) separatorEffectColor;
@property (TB,N,V_showsSeparatorBetweenItems) showsSeparatorBetweenItems;
@property (TB,N,V_useThinSeparators) useThinSeparators;
@property (TB,N,V_prefersHorizontalLayoutForLargeContentSize) prefersHorizontalLayoutForLargeContentSize;
@property (TB,N,V_derivesAutomaticArrowDirectionsFromAvailableSpace) derivesAutomaticArrowDirectionsFromAvailableSpace;
@property (T{NSDirectionalEdgeInsets=dddd},N,V_sectionInsets) sectionInsets;
@property (T{UIEdgeInsets=dddd},N,V_additionalSeparatorInsets) additionalSeparatorInsets;
@property (Tq,N,V_overrideUserInterfaceStyle) overrideUserInterfaceStyle;
@property (Td,N,V_shadowOpacity) shadowOpacity;
@property (T{CGSize=dd},N,V_shadowOffset) shadowOffset;
@property (Td,N,V_shadowRadius) shadowRadius;
@property (Td,N,V_horizontalMenuMaximumWidth) horizontalMenuMaximumWidth;
@property (Td,N,V_horizontalMenuCornerRadius) horizontalMenuCornerRadius;
@property (Td,N,V_verticalMenuMaximumHeight) verticalMenuMaximumHeight;
@property (Td,N,V_verticalMenuCornerRadius) verticalMenuCornerRadius;
@property (Td,N,V_sourceRectMargins) sourceRectMargins;
@property (T{CGSize=dd},N,V_arrowSize) arrowSize;
@property (Td,N,V_arrowSideRadius) arrowSideRadius;
@property (Td,N,V_arrowTipRadius) arrowTipRadius;
@property (T@?,C,N,V_menuItemMarginsProvider) menuItemMarginsProvider;
@property (T@?,C,N,V_cellBackgroundShapeProvider) cellBackgroundShapeProvider;
@property (T@"UIColor",&,N,V_destructiveColor) destructiveColor;
@property (T@"UIFont",&,N,V_menuItemTitleFont) menuItemTitleFont;
@property (T@"UIButtonConfiguration",C,N,V_pageButtonConfiguration) pageButtonConfiguration;
@property (Tq,N,V_pageButtonSymbolScale) pageButtonSymbolScale;
@property (Td,N,V_pageButtonAlignmentOffset) pageButtonAlignmentOffset;
@property (TB,N,V_pageButtonHasInlineAppearance) pageButtonHasInlineAppearance;
@property (Td,N,V_pageButtonOverlapAmount) pageButtonOverlapAmount;
@property (T@"UIFont",&,N,V_pageButtonFont) pageButtonFont;
@property (Td,N,V_pageButtonVisibilityMultiplier) pageButtonVisibilityMultiplier;
@property (TB,N,V_supportsContextMenuHandoff) supportsContextMenuHandoff;
```

## Instance methods

```
-[_UIEditMenuPlatformMetrics setShadowRadius:];
-[_UIEditMenuPlatformMetrics setShadowOffset:];
-[_UIEditMenuPlatformMetrics init];
-[_UIEditMenuPlatformMetrics separatorEffect];
-[_UIEditMenuPlatformMetrics setSeparatorEffect:];
-[_UIEditMenuPlatformMetrics setOverrideUserInterfaceStyle:];
-[_UIEditMenuPlatformMetrics supportsContextMenuHandoff];
-[_UIEditMenuPlatformMetrics shadowOpacity];
-[_UIEditMenuPlatformMetrics overrideUserInterfaceStyle];
-[_UIEditMenuPlatformMetrics shadowOffset];
-[_UIEditMenuPlatformMetrics setSupportsContextMenuHandoff:];
-[_UIEditMenuPlatformMetrics shadowRadius];
-[_UIEditMenuPlatformMetrics setShadowOpacity:];
-[_UIEditMenuPlatformMetrics arrowSideRadius];
-[_UIEditMenuPlatformMetrics setCellBackgroundShapeProvider:];
-[_UIEditMenuPlatformMetrics additionalSeparatorInsets];
-[_UIEditMenuPlatformMetrics arrowSize];
-[_UIEditMenuPlatformMetrics arrowTipRadius];
-[_UIEditMenuPlatformMetrics cellBackgroundShapeProvider];
-[_UIEditMenuPlatformMetrics containerViewConfigurator];
-[_UIEditMenuPlatformMetrics derivesAutomaticArrowDirectionsFromAvailableSpace];
-[_UIEditMenuPlatformMetrics destructiveColor];
-[_UIEditMenuPlatformMetrics horizontalMenuCornerRadius];
-[_UIEditMenuPlatformMetrics horizontalMenuMaximumWidth];
-[_UIEditMenuPlatformMetrics menuBackgroundConfigurator];
-[_UIEditMenuPlatformMetrics menuBackgroundEffect];
-[_UIEditMenuPlatformMetrics menuHighlightBackgroundColor];
-[_UIEditMenuPlatformMetrics menuHighlightBackgroundEffect];
-[_UIEditMenuPlatformMetrics menuItemMarginsProvider];
-[_UIEditMenuPlatformMetrics menuItemTitleFont];
-[_UIEditMenuPlatformMetrics pageButtonAlignmentOffset];
-[_UIEditMenuPlatformMetrics pageButtonConfiguration];
-[_UIEditMenuPlatformMetrics pageButtonFont];
-[_UIEditMenuPlatformMetrics pageButtonHasInlineAppearance];
-[_UIEditMenuPlatformMetrics pageButtonOverlapAmount];
-[_UIEditMenuPlatformMetrics pageButtonSymbolScale];
-[_UIEditMenuPlatformMetrics pageButtonVisibilityMultiplier];
-[_UIEditMenuPlatformMetrics prefersHorizontalLayoutForLargeContentSize];
-[_UIEditMenuPlatformMetrics sectionInsets];
-[_UIEditMenuPlatformMetrics separatorEffectColor];
-[_UIEditMenuPlatformMetrics setAdditionalSeparatorInsets:];
-[_UIEditMenuPlatformMetrics setArrowSideRadius:];
-[_UIEditMenuPlatformMetrics setArrowSize:];
-[_UIEditMenuPlatformMetrics setArrowTipRadius:];
-[_UIEditMenuPlatformMetrics setContainerViewConfigurator:];
-[_UIEditMenuPlatformMetrics setDerivesAutomaticArrowDirectionsFromAvailableSpace:];
-[_UIEditMenuPlatformMetrics setDestructiveColor:];
-[_UIEditMenuPlatformMetrics setHorizontalMenuCornerRadius:];
-[_UIEditMenuPlatformMetrics setHorizontalMenuMaximumWidth:];
-[_UIEditMenuPlatformMetrics setMenuBackgroundConfigurator:];
-[_UIEditMenuPlatformMetrics setMenuBackgroundEffect:];
-[_UIEditMenuPlatformMetrics setMenuHighlightBackgroundColor:];
-[_UIEditMenuPlatformMetrics setMenuHighlightBackgroundEffect:];
-[_UIEditMenuPlatformMetrics setMenuItemMarginsProvider:];
-[_UIEditMenuPlatformMetrics setMenuItemTitleFont:];
-[_UIEditMenuPlatformMetrics setPageButtonAlignmentOffset:];
-[_UIEditMenuPlatformMetrics setPageButtonConfiguration:];
-[_UIEditMenuPlatformMetrics setPageButtonFont:];
-[_UIEditMenuPlatformMetrics setPageButtonHasInlineAppearance:];
-[_UIEditMenuPlatformMetrics setPageButtonOverlapAmount:];
-[_UIEditMenuPlatformMetrics setPageButtonSymbolScale:];
-[_UIEditMenuPlatformMetrics setPageButtonVisibilityMultiplier:];
-[_UIEditMenuPlatformMetrics setPrefersHorizontalLayoutForLargeContentSize:];
-[_UIEditMenuPlatformMetrics setSectionInsets:];
-[_UIEditMenuPlatformMetrics setSeparatorEffectColor:];
-[_UIEditMenuPlatformMetrics setShowsSeparatorBetweenItems:];
-[_UIEditMenuPlatformMetrics setSourceRectMargins:];
-[_UIEditMenuPlatformMetrics setUseThinSeparators:];
-[_UIEditMenuPlatformMetrics setVerticalMenuCornerRadius:];
-[_UIEditMenuPlatformMetrics setVerticalMenuMaximumHeight:];
-[_UIEditMenuPlatformMetrics showsSeparatorBetweenItems];
-[_UIEditMenuPlatformMetrics sourceRectMargins];
-[_UIEditMenuPlatformMetrics useThinSeparators];
-[_UIEditMenuPlatformMetrics verticalMenuCornerRadius];
-[_UIEditMenuPlatformMetrics verticalMenuMaximumHeight];
```
