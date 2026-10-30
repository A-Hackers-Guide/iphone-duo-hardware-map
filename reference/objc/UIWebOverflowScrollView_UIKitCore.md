# `UIWebOverflowScrollView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIScrollView`
- 6 instance variables, 6 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _beingRemoved;
@"UIWebBrowserView" _webBrowserView;
@"UIWebOverflowScrollListener" _scrollListener;
@"UIWebOverflowContentView" _overflowContentView;
@"DOMNode" _node;
@"CALayer" _webLayer;
```

## Properties

```
@property (T@"UIWebBrowserView",N,V_webBrowserView) webBrowserView;
@property (T@"UIWebOverflowScrollListener",&,N,V_scrollListener) scrollListener;
@property (T@"UIWebOverflowContentView",&,N,V_overflowContentView) overflowContentView;
@property (T@"CALayer",&,N,V_webLayer) webLayer;
@property (T@"DOMNode",&,N,V_node) node;
@property (TB,N,GisBeingRemoved,V_beingRemoved) beingRemoved;
```

## Instance methods

```
-[UIWebOverflowScrollView setContentOffset:];
-[UIWebOverflowScrollView dealloc];
-[UIWebOverflowScrollView setNode:];
-[UIWebOverflowScrollView node];
-[UIWebOverflowScrollView fixUpViewAfterInsertion];
-[UIWebOverflowScrollView initWithLayer:node:webBrowserView:];
-[UIWebOverflowScrollView isBeingRemoved];
-[UIWebOverflowScrollView overflowContentView];
-[UIWebOverflowScrollView replaceLayer:];
-[UIWebOverflowScrollView scrollListener];
-[UIWebOverflowScrollView setBeingRemoved:];
-[UIWebOverflowScrollView setOverflowContentView:];
-[UIWebOverflowScrollView setScrollListener:];
-[UIWebOverflowScrollView setWebBrowserView:];
-[UIWebOverflowScrollView setWebLayer:];
-[UIWebOverflowScrollView superview];
-[UIWebOverflowScrollView webBrowserView];
-[UIWebOverflowScrollView webLayer];
-[UIWebOverflowScrollView willBeRemoved];
```
