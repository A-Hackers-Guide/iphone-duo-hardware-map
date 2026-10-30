# `_UIScrollPocketInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction`, `UIInteraction_Internal`, `UIInteraction_Private`, `BSDescriptionStreaming`
- 1 instance variables, 10 properties, 27 instance methods, 0 class methods

## Instance variables

```
implementation;
```

## Properties

```
@property (T@"UIScrollView",N,W) _scrollView;
@property (T@"_UIScrollPocketCollectorInteraction",N,W) _collectorInteraction;
@property (TQ,N) _edge;
@property (Tq,N) _style;
@property (TB,N) _requiresPocket;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) _rect;
@property (T{UIEdgeInsets=dddd},N) _insets;
@property (T@"NSValue",N,&) _cornerRadii;
@property (T@"UIView",N,R) view;
@property (T@"NSString",N,R) description;
```

## Instance methods

```
-[_UIScrollPocketInteraction _insets];
-[_UIScrollPocketInteraction _scrollView];
-[_UIScrollPocketInteraction _setInsets:];
-[_UIScrollPocketInteraction init];
-[_UIScrollPocketInteraction _updateProperties];
-[_UIScrollPocketInteraction _cornerRadii];
-[_UIScrollPocketInteraction initWithStyle:];
-[_UIScrollPocketInteraction _rect];
-[_UIScrollPocketInteraction _didMoveFromWindow:toWindow:];
-[_UIScrollPocketInteraction _setScrollView:];
-[_UIScrollPocketInteraction view];
-[_UIScrollPocketInteraction _setStyle:];
-[_UIScrollPocketInteraction _setEdge:];
-[_UIScrollPocketInteraction willMoveToView:];
-[_UIScrollPocketInteraction initWithScrollView:edge:style:];
-[_UIScrollPocketInteraction _setCornerRadii:];
-[_UIScrollPocketInteraction description];
-[_UIScrollPocketInteraction _style];
-[_UIScrollPocketInteraction _setRequiresPocket:];
-[_UIScrollPocketInteraction appendDescriptionToStream:];
-[_UIScrollPocketInteraction _setRect:];
-[_UIScrollPocketInteraction _viewVisibilityDidChange];
-[_UIScrollPocketInteraction _collectorInteraction];
-[_UIScrollPocketInteraction _setCollectorInteraction:];
-[_UIScrollPocketInteraction didMoveToView:];
-[_UIScrollPocketInteraction _edge];
-[_UIScrollPocketInteraction _requiresPocket];
```
