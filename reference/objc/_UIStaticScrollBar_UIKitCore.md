# `_UIStaticScrollBar`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIScrollAccessory`
- 9 instance variables, 7 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"UIView" _dividerLine;
@"NSInvocation" _invocation;
@"NSArray" _constraints;
@"_UIScrollPocketInteraction" _scrollPocketInteraction;
B _shouldInsetButtonsForIndex;
@"UIScrollView" _scrollView;
q _edge;
@"UIButton" _upButton;
@"UIButton" _downButton;
```

## Properties

```
@property (T@"UIButton",R,N,V_upButton) upButton;
@property (T@"UIButton",R,N,V_downButton) downButton;
@property (TB,N,V_shouldInsetButtonsForIndex) shouldInsetButtonsForIndex;
@property (Tq,R,N) desiredAccessoryEdge;
@property (T@"UIScrollView",W,N,V_scrollView) scrollView;
@property (Tq,N,V_edge) edge;
@property (TB,R,N) overlay;
```

## Instance methods

```
-[_UIStaticScrollBar setEdge:];
-[_UIStaticScrollBar edge];
-[_UIStaticScrollBar update];
-[_UIStaticScrollBar scrollView];
-[_UIStaticScrollBar layoutSubviews];
-[_UIStaticScrollBar setScrollView:];
-[_UIStaticScrollBar buttonTapped:];
-[_UIStaticScrollBar sizeThatFits:];
-[_UIStaticScrollBar overlay];
-[_UIStaticScrollBar willMoveToWindow:];
-[_UIStaticScrollBar _axis];
-[_UIStaticScrollBar updateConstraints];
-[_UIStaticScrollBar initWithFrame:];
-[_UIStaticScrollBar centeringBounds];
-[_UIStaticScrollBar _constraintsForEdge:];
-[_UIStaticScrollBar _setupSubviewsIfNeeded];
-[_UIStaticScrollBar _updateScrollPocketIfNecessary];
-[_UIStaticScrollBar desiredAccessoryEdge];
-[_UIStaticScrollBar downButton];
-[_UIStaticScrollBar setShouldInsetButtonsForIndex:];
-[_UIStaticScrollBar shouldInsetButtonsForIndex];
-[_UIStaticScrollBar upButton];
```
