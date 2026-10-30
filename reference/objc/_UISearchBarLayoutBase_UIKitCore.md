# `_UISearchBarLayoutBase`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 9 instance variables, 9 properties, 23 instance methods, 0 class methods

## Instance variables

```
B _isLayoutValid;
B _layoutRTL;
B _hostedByNavigationBar;
B _shouldApplyContainerSafeAreaInsets;
@"UIView" _associatedView;
q _barMetrics;
{CGSize="width"d"height"d} _layoutSize;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _contentInset;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _containerSafeAreaInsets;
```

## Properties

```
@property (T@"UIView",W,N,V_associatedView) associatedView;
@property (Tq,N,V_barMetrics) barMetrics;
@property (T{UIEdgeInsets=dddd},N,V_contentInset) contentInset;
@property (TB,N,GisLayoutRTL,V_layoutRTL) layoutRTL;
@property (TB,N,GisHostedByNavigationBar,V_hostedByNavigationBar) hostedByNavigationBar;
@property (TB,N,V_shouldApplyContainerSafeAreaInsets) shouldApplyContainerSafeAreaInsets;
@property (T{UIEdgeInsets=dddd},N,V_containerSafeAreaInsets) containerSafeAreaInsets;
@property (T{CGSize=dd},N,V_layoutSize) layoutSize;
@property (TB,R,N,GisLayoutValid) layoutValid;
```

## Instance methods

```
-[_UISearchBarLayoutBase updateLayoutIfNeeded];
-[_UISearchBarLayoutBase applyLayout];
-[_UISearchBarLayoutBase updateLayout];
-[_UISearchBarLayoutBase layoutSize];
-[_UISearchBarLayoutBase setContentInset:];
-[_UISearchBarLayoutBase setLayoutRTL:];
-[_UISearchBarLayoutBase barMetrics];
-[_UISearchBarLayoutBase setHostedByNavigationBar:];
-[_UISearchBarLayoutBase associatedView];
-[_UISearchBarLayoutBase setAssociatedView:];
-[_UISearchBarLayoutBase description];
-[_UISearchBarLayoutBase containerSafeAreaInsets];
-[_UISearchBarLayoutBase invalidateLayout];
-[_UISearchBarLayoutBase copyWithZone:];
-[_UISearchBarLayoutBase setBarMetrics:];
-[_UISearchBarLayoutBase contentInset];
-[_UISearchBarLayoutBase isHostedByNavigationBar];
-[_UISearchBarLayoutBase isLayoutRTL];
-[_UISearchBarLayoutBase isLayoutValid];
-[_UISearchBarLayoutBase setContainerSafeAreaInsets:];
-[_UISearchBarLayoutBase setLayoutSize:];
-[_UISearchBarLayoutBase setShouldApplyContainerSafeAreaInsets:];
-[_UISearchBarLayoutBase shouldApplyContainerSafeAreaInsets];
```
