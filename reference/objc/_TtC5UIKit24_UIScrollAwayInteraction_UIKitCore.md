# `_TtC5UIKit24_UIScrollAwayInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction`, `_UIScrollViewScrollObserver_Internal`
- 9 instance variables, 1 properties, 10 instance methods, 0 class methods

## Instance variables

```
_$sSo6UIViewCSgXw view;
(objc_protocol 0x1864376d0) ? delegate;
CoreGraphics.CGFloat activationDistanceThreshold;
CoreGraphics.CGFloat activeDistance;
UIKit._UIScrollAwayInteraction.Direction direction;
CoreGraphics.CGFloat progress;
UIKit._UIScrollAwayInteraction.State state;
_$sSo12UIScrollViewCSgXw contentScrollView;
__C.CGPoint lastContentOffset;
```

## Properties

```
@property (T@"UIView",N,W,Vview) view;
```

## Instance methods

```
-[_TtC5UIKit24_UIScrollAwayInteraction _observeScrollViewDidEndDecelerating:];
-[_TtC5UIKit24_UIScrollAwayInteraction _observeScrollViewDidScroll:];
-[_TtC5UIKit24_UIScrollAwayInteraction _observeScrollViewDidEndDragging:willDecelerate:];
-[_TtC5UIKit24_UIScrollAwayInteraction init];
-[_TtC5UIKit24_UIScrollAwayInteraction setView:];
-[_TtC5UIKit24_UIScrollAwayInteraction view];
-[_TtC5UIKit24_UIScrollAwayInteraction willMoveToView:];
-[_TtC5UIKit24_UIScrollAwayInteraction _observeScrollViewWillScrollToTop:];
-[_TtC5UIKit24_UIScrollAwayInteraction _observeScrollViewWillBeginDragging:];
-[_TtC5UIKit24_UIScrollAwayInteraction didMoveToView:];
```
