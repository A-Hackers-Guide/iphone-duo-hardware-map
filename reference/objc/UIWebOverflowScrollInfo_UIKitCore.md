# `UIWebOverflowScrollInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _isUserScroll;
@"DOMNode" _node;
{CGPoint="x"d"y"d} _offset;
```

## Properties

```
@property (T@"DOMNode",&,N,V_node) node;
@property (T{CGPoint=dd},N,V_offset) offset;
@property (TB,N,V_isUserScroll) isUserScroll;
```

## Instance methods

```
-[UIWebOverflowScrollInfo dealloc];
-[UIWebOverflowScrollInfo setNode:];
-[UIWebOverflowScrollInfo node];
-[UIWebOverflowScrollInfo setOffset:];
-[UIWebOverflowScrollInfo offset];
-[UIWebOverflowScrollInfo coalesceScrollForNode:offset:isUserScroll:];
-[UIWebOverflowScrollInfo initWithNode:offset:isUserScroll:];
-[UIWebOverflowScrollInfo isUserScroll];
-[UIWebOverflowScrollInfo setIsUserScroll:];
```
