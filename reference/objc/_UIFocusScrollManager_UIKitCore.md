# `_UIFocusScrollManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"UIScreen" _screen;
@"_UIFocusDisplayLinkScrollAnimator" _scrollAnimator;
@"NSHashTable" _stackVisitedScrollingContainers;
```

## Properties

```
@property (T@"_UIFocusDisplayLinkScrollAnimator",R,N,V_scrollAnimator) scrollAnimator;
@property (T@"NSHashTable",R,N,V_stackVisitedScrollingContainers) stackVisitedScrollingContainers;
@property (T@"UIScreen",R,W,N,V_screen) screen;
```

## Instance methods

```
-[_UIFocusScrollManager initWithScreen:];
-[_UIFocusScrollManager screen];
-[_UIFocusScrollManager isScrollingScrollableContainer:];
-[_UIFocusScrollManager stackVisitedScrollingContainers];
-[_UIFocusScrollManager _ensureFocusItemIsOnscreenForScrollRequest:];
-[_UIFocusScrollManager _scrollWithScrollRequest:onlyIfNecessary:];
-[_UIFocusScrollManager adjustTargetContentOffsetForScrollableContainer:byDelta:];
-[_UIFocusScrollManager animateOffsetOfEnvironmentScrollableContainer:toShowFocusItem:];
-[_UIFocusScrollManager animateOffsetOfScrollableContainersInParentEnvironmentContainer:toShowFocusItem:];
-[_UIFocusScrollManager cancelScrollingForScrollableContainer:];
-[_UIFocusScrollManager contentOffsetForEnvironmentScrollableContainer:toShowFocusItem:targetOffset:];
-[_UIFocusScrollManager contentOffsetForEnvironmentScrollableContainer:toShowRect:targetOffset:];
-[_UIFocusScrollManager currentVelocityForScrollableContainer:];
-[_UIFocusScrollManager performScrollingIfNeededForFocusUpdateInContext:];
-[_UIFocusScrollManager scrollAnimator];
-[_UIFocusScrollManager targetContentOffsetForScrollableContainer:];
```
