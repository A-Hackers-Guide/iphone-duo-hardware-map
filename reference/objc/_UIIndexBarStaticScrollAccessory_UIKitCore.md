# `_UIIndexBarStaticScrollAccessory`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStaticScrollBar`
- Protocols: `UIScrollAccessory`
- 7 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"UIIndexBarAccessoryView" _indexBarView;
@"UIView" _containerView;
@"_UIScrollPocketInteraction" _scrollPocketInteraction;
B _overlay;
B _showIndexBar;
q _edge;
@"UIScrollView" _scrollView;
```

## Properties

```
@property (TB,N,V_showIndexBar) showIndexBar;
@property (T@"UIIndexBarAccessoryView",R,N,V_indexBarView) indexBarView;
@property (TB,D,N) shouldInsetButtonsForIndex;
@property (T@"UIScrollView",W,N,V_scrollView) scrollView;
@property (Tq,N,V_edge) edge;
@property (TB,R,N,V_overlay) overlay;
```

## Instance methods

```
-[_UIIndexBarStaticScrollAccessory setEdge:];
-[_UIIndexBarStaticScrollAccessory edge];
-[_UIIndexBarStaticScrollAccessory update];
-[_UIIndexBarStaticScrollAccessory scrollView];
-[_UIIndexBarStaticScrollAccessory layoutSubviews];
-[_UIIndexBarStaticScrollAccessory setScrollView:];
-[_UIIndexBarStaticScrollAccessory overlay];
-[_UIIndexBarStaticScrollAccessory _installScrollPocketInteractionIfNecessary];
-[_UIIndexBarStaticScrollAccessory indexBarView];
-[_UIIndexBarStaticScrollAccessory setShowIndexBar:];
-[_UIIndexBarStaticScrollAccessory showIndexBar];
```
