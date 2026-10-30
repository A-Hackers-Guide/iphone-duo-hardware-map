# `_UIFloatingTabBarPlatformMetrics`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIVisualStyleProviding`
- 45 instance variables, 46 properties, 93 instance methods, 0 class methods

## Instance variables

```
B _sidebarBorderInsideBounds;
B _showsSidebarTitle;
B _supportsFloatingSidebar;
B _prefersTrailingSidebarButton;
B _sidebarPrefersMacAppearance;
B _sidebarSupportsAnimatedSelections;
B _sidebarSupportsPassthroughInOverlay;
B _supportsCustomizablePlacements;
@"NSArray" _backgroundEffects;
@"<_UIViewMaterial>" _background;
@"UIColor" _borderColor;
d _borderWidth;
@"_UIShadowProperties" _shadowProperties;
d _maximumWidth;
d _maximumExpandedWidth;
d _verticalOffsetInSheetPresentationContext;
d _verticalPaddingToNavigationBar;
@"UIColor" _selectionBackgroundColor;
@"_UIShadowProperties" _selectionShadow;
d _selectionHighlightScale;
d _selectionDistanceThresholdForUnselectedItems;
@"UIFont" _contentFont;
@"UIFont" _selectedContentFont;
@"UIImageSymbolConfiguration" _symbolConfiguration;
@"UIImageSymbolConfiguration" _selectedSymbolConfiguration;
d _maximumContentWidth;
d _imageAndTitleSpacing;
d _safeAreaOffset;
d _minimumEdgeOffset;
d _contentAlphaDistanceThreshold;
@? _contentPaletteProvider;
@"NSArray" _sidebarBackgroundEffects;
d _sidebarBorderWidth;
@"UIColor" _sidebarBorderColor;
@? _sidebarBackgroundProvider;
@"NSString" _overflowButtonImageName;
d _expandedDropTargetInset;
@? _editModeBackgroundShadowProvider;
{CGSize="width"d"height"d} _defaultImageSize;
{UIOffset="horizontal"d"vertical"d} _badgeOffset;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _backgroundInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _titleMargins;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _imageMargins;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _editModeItemMargins;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _editModeTransform;
```

## Properties

```
@property (T@"NSArray",&,N,V_backgroundEffects) backgroundEffects;
@property (T@"<_UIViewMaterial>",&,N,V_background) background;
@property (T{UIEdgeInsets=dddd},N,V_backgroundInsets) backgroundInsets;
@property (T@"UIColor",&,N,V_borderColor) borderColor;
@property (Td,N,V_borderWidth) borderWidth;
@property (T@"_UIShadowProperties",&,N,V_shadowProperties) shadowProperties;
@property (Td,N,V_maximumWidth) maximumWidth;
@property (Td,N,V_maximumExpandedWidth) maximumExpandedWidth;
@property (Td,N,V_verticalOffsetInSheetPresentationContext) verticalOffsetInSheetPresentationContext;
@property (Td,N,V_verticalPaddingToNavigationBar) verticalPaddingToNavigationBar;
@property (T@"UIColor",&,N,V_selectionBackgroundColor) selectionBackgroundColor;
@property (T@"_UIShadowProperties",&,N,V_selectionShadow) selectionShadow;
@property (Td,N,V_selectionHighlightScale) selectionHighlightScale;
@property (Td,N,V_selectionDistanceThresholdForUnselectedItems) selectionDistanceThresholdForUnselectedItems;
@property (T@"UIFont",&,N,V_contentFont) contentFont;
@property (T@"UIFont",&,N,V_selectedContentFont) selectedContentFont;
@property (T@"UIImageSymbolConfiguration",&,N,V_symbolConfiguration) symbolConfiguration;
@property (T@"UIImageSymbolConfiguration",&,N,V_selectedSymbolConfiguration) selectedSymbolConfiguration;
@property (T{CGSize=dd},N,V_defaultImageSize) defaultImageSize;
@property (Td,N,V_maximumContentWidth) maximumContentWidth;
@property (T{UIEdgeInsets=dddd},N,V_titleMargins) titleMargins;
@property (T{UIEdgeInsets=dddd},N,V_imageMargins) imageMargins;
@property (Td,N,V_imageAndTitleSpacing) imageAndTitleSpacing;
@property (Td,N,V_safeAreaOffset) safeAreaOffset;
@property (Td,N,V_minimumEdgeOffset) minimumEdgeOffset;
@property (Td,N,V_contentAlphaDistanceThreshold) contentAlphaDistanceThreshold;
@property (T@?,C,N,V_contentPaletteProvider) contentPaletteProvider;
@property (T{UIOffset=dd},N,V_badgeOffset) badgeOffset;
@property (T@"UIButtonConfiguration",R,C,N) sidebarButtonConfiguration;
@property (T@"NSArray",&,N,V_sidebarBackgroundEffects) sidebarBackgroundEffects;
@property (Td,N,V_sidebarBorderWidth) sidebarBorderWidth;
@property (TB,N,GisSidebarBorderInsideBounds,V_sidebarBorderInsideBounds) sidebarBorderInsideBounds;
@property (T@"UIColor",&,N,V_sidebarBorderColor) sidebarBorderColor;
@property (TB,N,V_showsSidebarTitle) showsSidebarTitle;
@property (TB,N,V_supportsFloatingSidebar) supportsFloatingSidebar;
@property (TB,N,V_prefersTrailingSidebarButton) prefersTrailingSidebarButton;
@property (TB,N,V_sidebarPrefersMacAppearance) sidebarPrefersMacAppearance;
@property (TB,N,V_sidebarSupportsAnimatedSelections) sidebarSupportsAnimatedSelections;
@property (TB,N,V_sidebarSupportsPassthroughInOverlay) sidebarSupportsPassthroughInOverlay;
@property (T@?,C,N,V_sidebarBackgroundProvider) sidebarBackgroundProvider;
@property (T@"NSString",N,V_overflowButtonImageName) overflowButtonImageName;
@property (TB,N,V_supportsCustomizablePlacements) supportsCustomizablePlacements;
@property (T{UIEdgeInsets=dddd},N,V_editModeItemMargins) editModeItemMargins;
@property (T{CGAffineTransform=dddddd},N,V_editModeTransform) editModeTransform;
@property (Td,N,V_expandedDropTargetInset) expandedDropTargetInset;
@property (T@?,C,N,V_editModeBackgroundShadowProvider) editModeBackgroundShadowProvider;
```

## Instance methods

```
-[_UIFloatingTabBarPlatformMetrics maximumWidth];
-[_UIFloatingTabBarPlatformMetrics setBorderColor:];
-[_UIFloatingTabBarPlatformMetrics shadowProperties];
-[_UIFloatingTabBarPlatformMetrics backgroundEffects];
-[_UIFloatingTabBarPlatformMetrics setBorderWidth:];
-[_UIFloatingTabBarPlatformMetrics symbolConfiguration];
-[_UIFloatingTabBarPlatformMetrics setBackground:];
-[_UIFloatingTabBarPlatformMetrics init];
-[_UIFloatingTabBarPlatformMetrics setShadowProperties:];
-[_UIFloatingTabBarPlatformMetrics background];
-[_UIFloatingTabBarPlatformMetrics defaultImageSize];
-[_UIFloatingTabBarPlatformMetrics borderWidth];
-[_UIFloatingTabBarPlatformMetrics setBackgroundEffects:];
-[_UIFloatingTabBarPlatformMetrics setMaximumWidth:];
-[_UIFloatingTabBarPlatformMetrics setBadgeOffset:];
-[_UIFloatingTabBarPlatformMetrics setBackgroundInsets:];
-[_UIFloatingTabBarPlatformMetrics setSymbolConfiguration:];
-[_UIFloatingTabBarPlatformMetrics backgroundInsets];
-[_UIFloatingTabBarPlatformMetrics badgeOffset];
-[_UIFloatingTabBarPlatformMetrics borderColor];
-[_UIFloatingTabBarPlatformMetrics selectionShadow];
-[_UIFloatingTabBarPlatformMetrics setContentFont:];
-[_UIFloatingTabBarPlatformMetrics setSelectedSymbolConfiguration:];
-[_UIFloatingTabBarPlatformMetrics setSidebarPrefersMacAppearance:];
-[_UIFloatingTabBarPlatformMetrics contentAlphaDistanceThreshold];
-[_UIFloatingTabBarPlatformMetrics contentFont];
-[_UIFloatingTabBarPlatformMetrics contentPaletteProvider];
-[_UIFloatingTabBarPlatformMetrics editModeBackgroundShadowProvider];
-[_UIFloatingTabBarPlatformMetrics editModeItemMargins];
-[_UIFloatingTabBarPlatformMetrics editModeTransform];
-[_UIFloatingTabBarPlatformMetrics expandedDropTargetInset];
-[_UIFloatingTabBarPlatformMetrics imageAndTitleSpacing];
-[_UIFloatingTabBarPlatformMetrics imageMargins];
-[_UIFloatingTabBarPlatformMetrics isSidebarBorderInsideBounds];
-[_UIFloatingTabBarPlatformMetrics maximumContentWidth];
-[_UIFloatingTabBarPlatformMetrics maximumExpandedWidth];
-[_UIFloatingTabBarPlatformMetrics minimumEdgeOffset];
-[_UIFloatingTabBarPlatformMetrics overflowButtonImageName];
-[_UIFloatingTabBarPlatformMetrics prefersTrailingSidebarButton];
-[_UIFloatingTabBarPlatformMetrics safeAreaOffset];
-[_UIFloatingTabBarPlatformMetrics scaledImageSizeForTraitCollection:];
-[_UIFloatingTabBarPlatformMetrics selectedContentFont];
-[_UIFloatingTabBarPlatformMetrics selectedSymbolConfiguration];
-[_UIFloatingTabBarPlatformMetrics selectionBackgroundColor];
-[_UIFloatingTabBarPlatformMetrics selectionDistanceThresholdForUnselectedItems];
-[_UIFloatingTabBarPlatformMetrics selectionHighlightScale];
-[_UIFloatingTabBarPlatformMetrics setContentAlphaDistanceThreshold:];
-[_UIFloatingTabBarPlatformMetrics setContentPaletteProvider:];
-[_UIFloatingTabBarPlatformMetrics setDefaultImageSize:];
-[_UIFloatingTabBarPlatformMetrics setEditModeBackgroundShadowProvider:];
-[_UIFloatingTabBarPlatformMetrics setEditModeItemMargins:];
-[_UIFloatingTabBarPlatformMetrics setEditModeTransform:];
-[_UIFloatingTabBarPlatformMetrics setExpandedDropTargetInset:];
-[_UIFloatingTabBarPlatformMetrics setImageAndTitleSpacing:];
-[_UIFloatingTabBarPlatformMetrics setImageMargins:];
-[_UIFloatingTabBarPlatformMetrics setMaximumContentWidth:];
-[_UIFloatingTabBarPlatformMetrics setMaximumExpandedWidth:];
-[_UIFloatingTabBarPlatformMetrics setMinimumEdgeOffset:];
-[_UIFloatingTabBarPlatformMetrics setOverflowButtonImageName:];
-[_UIFloatingTabBarPlatformMetrics setPrefersTrailingSidebarButton:];
-[_UIFloatingTabBarPlatformMetrics setSafeAreaOffset:];
-[_UIFloatingTabBarPlatformMetrics setSelectedContentFont:];
-[_UIFloatingTabBarPlatformMetrics setSelectionBackgroundColor:];
-[_UIFloatingTabBarPlatformMetrics setSelectionDistanceThresholdForUnselectedItems:];
-[_UIFloatingTabBarPlatformMetrics setSelectionHighlightScale:];
-[_UIFloatingTabBarPlatformMetrics setSelectionShadow:];
-[_UIFloatingTabBarPlatformMetrics setShowsSidebarTitle:];
-[_UIFloatingTabBarPlatformMetrics setSidebarBackgroundEffects:];
-[_UIFloatingTabBarPlatformMetrics setSidebarBackgroundProvider:];
-[_UIFloatingTabBarPlatformMetrics setSidebarBorderColor:];
-[_UIFloatingTabBarPlatformMetrics setSidebarBorderInsideBounds:];
-[_UIFloatingTabBarPlatformMetrics setSidebarBorderWidth:];
-[_UIFloatingTabBarPlatformMetrics setSidebarSupportsAnimatedSelections:];
-[_UIFloatingTabBarPlatformMetrics setSidebarSupportsPassthroughInOverlay:];
-[_UIFloatingTabBarPlatformMetrics setSupportsCustomizablePlacements:];
-[_UIFloatingTabBarPlatformMetrics setSupportsFloatingSidebar:];
-[_UIFloatingTabBarPlatformMetrics setTitleMargins:];
-[_UIFloatingTabBarPlatformMetrics setVerticalOffsetInSheetPresentationContext:];
-[_UIFloatingTabBarPlatformMetrics setVerticalPaddingToNavigationBar:];
-[_UIFloatingTabBarPlatformMetrics showsSidebarTitle];
-[_UIFloatingTabBarPlatformMetrics sidebarBackgroundEffects];
-[_UIFloatingTabBarPlatformMetrics sidebarBackgroundProvider];
-[_UIFloatingTabBarPlatformMetrics sidebarBorderColor];
-[_UIFloatingTabBarPlatformMetrics sidebarBorderWidth];
-[_UIFloatingTabBarPlatformMetrics sidebarButtonConfiguration];
-[_UIFloatingTabBarPlatformMetrics sidebarPrefersMacAppearance];
-[_UIFloatingTabBarPlatformMetrics sidebarSupportsAnimatedSelections];
-[_UIFloatingTabBarPlatformMetrics sidebarSupportsPassthroughInOverlay];
-[_UIFloatingTabBarPlatformMetrics supportsCustomizablePlacements];
-[_UIFloatingTabBarPlatformMetrics supportsFloatingSidebar];
-[_UIFloatingTabBarPlatformMetrics titleMargins];
-[_UIFloatingTabBarPlatformMetrics verticalOffsetInSheetPresentationContext];
-[_UIFloatingTabBarPlatformMetrics verticalPaddingToNavigationBar];
```
