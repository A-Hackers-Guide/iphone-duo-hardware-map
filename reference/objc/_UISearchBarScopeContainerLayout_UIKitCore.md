# `_UISearchBarScopeContainerLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISearchBarLayoutBase`
- 14 instance variables, 16 properties, 33 instance methods, 0 class methods

## Instance variables

```
B _collapsed;
B _hasScopeBar;
B _combinedScopeBar;
B _hostedInlineInNavigationBar;
B _independentFromSearchBarLayout;
@"<_UISearchBarContainerSublayoutDelegate>" _delegate;
@"_UISearchBarSearchContainerLayout" _neighboringSearchLayout;
@"UIView" _scopeBar;
Q _numberOfScopeTitles;
@? _hostedScopeBarHeightForBarMetrics;
@? _hostedScopeBarTopInsetForBarMetrics;
d _scopeBarOpacity;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _scopeBarLayoutFrame;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _defaultScopeBarInsets;
```

## Properties

```
@property (T@"<_UISearchBarContainerSublayoutDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisCollapsed,V_collapsed) collapsed;
@property (T@"_UISearchBarSearchContainerLayout",&,N,V_neighboringSearchLayout) neighboringSearchLayout;
@property (T@"UIView",&,N,V_scopeBar) scopeBar;
@property (TB,N,V_hasScopeBar) hasScopeBar;
@property (TB,N,V_combinedScopeBar) combinedScopeBar;
@property (TB,N,V_hostedInlineInNavigationBar) hostedInlineInNavigationBar;
@property (TB,N,V_independentFromSearchBarLayout) independentFromSearchBarLayout;
@property (TQ,N,V_numberOfScopeTitles) numberOfScopeTitles;
@property (T{UIEdgeInsets=dddd},N,V_defaultScopeBarInsets) defaultScopeBarInsets;
@property (T@?,C,N,V_hostedScopeBarHeightForBarMetrics) hostedScopeBarHeightForBarMetrics;
@property (T@?,C,N,V_hostedScopeBarTopInsetForBarMetrics) hostedScopeBarTopInsetForBarMetrics;
@property (T{UIEdgeInsets=dddd},R,N) containerSpecificInsets;
@property (Td,R,N) naturalContainerHeight;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_scopeBarLayoutFrame) scopeBarLayoutFrame;
@property (Td,R,N,V_scopeBarOpacity) scopeBarOpacity;
```

## Instance methods

```
-[_UISearchBarScopeContainerLayout combinedScopeBar];
-[_UISearchBarScopeContainerLayout setCollapsed:];
-[_UISearchBarScopeContainerLayout setScopeBar:];
-[_UISearchBarScopeContainerLayout setDefaultScopeBarInsets:];
-[_UISearchBarScopeContainerLayout hostedScopeBarHeightForBarMetrics];
-[_UISearchBarScopeContainerLayout applyLayout];
-[_UISearchBarScopeContainerLayout hasScopeBar];
-[_UISearchBarScopeContainerLayout defaultScopeBarInsets];
-[_UISearchBarScopeContainerLayout scopeBar];
-[_UISearchBarScopeContainerLayout setCombinedScopeBar:];
-[_UISearchBarScopeContainerLayout updateLayout];
-[_UISearchBarScopeContainerLayout hostedScopeBarTopInsetForBarMetrics];
-[_UISearchBarScopeContainerLayout setHostedInlineInNavigationBar:];
-[_UISearchBarScopeContainerLayout setHostedScopeBarHeightForBarMetrics:];
-[_UISearchBarScopeContainerLayout setNumberOfScopeTitles:];
-[_UISearchBarScopeContainerLayout hostedInlineInNavigationBar];
-[_UISearchBarScopeContainerLayout naturalContainerHeight];
-[_UISearchBarScopeContainerLayout setHasScopeBar:];
-[_UISearchBarScopeContainerLayout setDelegate:];
-[_UISearchBarScopeContainerLayout setIndependentFromSearchBarLayout:];
-[_UISearchBarScopeContainerLayout neighboringSearchLayout];
-[_UISearchBarScopeContainerLayout scopeControlHeight];
-[_UISearchBarScopeContainerLayout isCollapsed];
-[_UISearchBarScopeContainerLayout setHostedScopeBarTopInsetForBarMetrics:];
-[_UISearchBarScopeContainerLayout scopeBarLayoutFrame];
-[_UISearchBarScopeContainerLayout delegate];
-[_UISearchBarScopeContainerLayout numberOfScopeTitles];
-[_UISearchBarScopeContainerLayout setNeighboringSearchLayout:];
-[_UISearchBarScopeContainerLayout description];
-[_UISearchBarScopeContainerLayout scopeBarOpacity];
-[_UISearchBarScopeContainerLayout independentFromSearchBarLayout];
-[_UISearchBarScopeContainerLayout copyWithZone:];
-[_UISearchBarScopeContainerLayout containerSpecificInsets];
```
