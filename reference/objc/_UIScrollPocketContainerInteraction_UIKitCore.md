# `_UIScrollPocketContainerInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction`, `UIInteraction_Internal`, `UIInteraction_Private`
- 1 instance variables, 7 properties, 22 instance methods, 1 class methods

## Instance variables

```
implementation;
```

## Properties

```
@property (T@"UIScrollView",N,W) _scrollView;
@property (T@"_UIScrollPocketCollectorInteraction",N,W) _collectorInteraction;
@property (TQ,N) _edge;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) _elementInteractionRect;
@property (TB,N) _active;
@property (TB,N) _findsParentScrollView;
@property (T@"UIView",N,R) view;
```

## Class methods

```
+[_UIScrollPocketContainerInteraction _lumaUserInterfaceStyleSpringDuration];
```

## Instance methods

```
-[_UIScrollPocketContainerInteraction _scrollView];
-[_UIScrollPocketContainerInteraction _isActive];
-[_UIScrollPocketContainerInteraction initWithEdge:];
-[_UIScrollPocketContainerInteraction init];
-[_UIScrollPocketContainerInteraction _updateProperties];
-[_UIScrollPocketContainerInteraction _elementInteractionRect];
-[_UIScrollPocketContainerInteraction _setActive:];
-[_UIScrollPocketContainerInteraction _setHostSharedLuminanceAggregatorProxy:];
-[_UIScrollPocketContainerInteraction _setFindsParentScrollView:];
-[_UIScrollPocketContainerInteraction _setScrollView:];
-[_UIScrollPocketContainerInteraction view];
-[_UIScrollPocketContainerInteraction _findsParentScrollView];
-[_UIScrollPocketContainerInteraction _setEdge:];
-[_UIScrollPocketContainerInteraction willMoveToView:];
-[_UIScrollPocketContainerInteraction _viewVisibilityDidChange];
-[_UIScrollPocketContainerInteraction initWithScrollView:edge:];
-[_UIScrollPocketContainerInteraction _collectorInteraction];
-[_UIScrollPocketContainerInteraction _viewTraitCollectionDidChange:];
-[_UIScrollPocketContainerInteraction _setCollectorInteraction:];
-[_UIScrollPocketContainerInteraction _setElementInteractionRect:];
-[_UIScrollPocketContainerInteraction didMoveToView:];
-[_UIScrollPocketContainerInteraction _edge];
```
