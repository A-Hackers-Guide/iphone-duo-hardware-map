# `_UIAutoScrollAssistant`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 11 properties, 27 instance methods, 0 class methods

## Instance variables

```
B _started;
@"UIScrollView" _scrollView;
q _mode;
Q _allowedDirections;
@"CADisplayLink" _displayLink;
d _lastTimestamp;
@"<_UIAutoScrollBehavior>" _behavior;
{CGPoint="x"d"y"d} _point;
{CGPoint="x"d"y"d} _referenceContentOffsetForPoint;
```

## Properties

```
@property (T@"CADisplayLink",&,N,V_displayLink) displayLink;
@property (T{CGPoint=dd},R,N,V_point) point;
@property (T{CGPoint=dd},N,V_referenceContentOffsetForPoint) referenceContentOffsetForPoint;
@property (Td,N,V_lastTimestamp) lastTimestamp;
@property (TB,N,V_started) started;
@property (T@"<_UIAutoScrollBehavior>",&,N,V_behavior) behavior;
@property (T@"UIScrollView",R,W,N,V_scrollView) scrollView;
@property (Tq,N,V_mode) mode;
@property (TB,R,N,GisActive) active;
@property (T{UIEdgeInsets=dddd},N) touchInsets;
@property (TQ,N,V_allowedDirections) allowedDirections;
```

## Instance methods

```
-[_UIAutoScrollAssistant displayLink];
-[_UIAutoScrollAssistant initWithScrollView:];
-[_UIAutoScrollAssistant setStarted:];
-[_UIAutoScrollAssistant _adjustPointToCurrentContentOffset];
-[_UIAutoScrollAssistant setPoint:forContentOffset:];
-[_UIAutoScrollAssistant _handleAutoScrollerWithContentOffset:direction:];
-[_UIAutoScrollAssistant _scrollContinuous];
-[_UIAutoScrollAssistant stop];
-[_UIAutoScrollAssistant scrollView];
-[_UIAutoScrollAssistant setTouchInsets:];
-[_UIAutoScrollAssistant started];
-[_UIAutoScrollAssistant lastTimestamp];
-[_UIAutoScrollAssistant setMode:];
-[_UIAutoScrollAssistant displayLinkFired:];
-[_UIAutoScrollAssistant setDisplayLink:];
-[_UIAutoScrollAssistant setBehavior:];
-[_UIAutoScrollAssistant behavior];
-[_UIAutoScrollAssistant setReferenceContentOffsetForPoint:];
-[_UIAutoScrollAssistant setLastTimestamp:];
-[_UIAutoScrollAssistant autoScrollFromPoint:];
-[_UIAutoScrollAssistant point];
-[_UIAutoScrollAssistant mode];
-[_UIAutoScrollAssistant setAllowedDirections:];
-[_UIAutoScrollAssistant allowedDirections];
-[_UIAutoScrollAssistant touchInsets];
-[_UIAutoScrollAssistant isActive];
-[_UIAutoScrollAssistant referenceContentOffsetForPoint];
```
