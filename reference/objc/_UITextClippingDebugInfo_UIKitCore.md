# `_UITextClippingDebugInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 9 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _ignoresResult;
B _leftEdgeClipped;
B _rightEdgeClipped;
B _bottomEdgeClipped;
B _topEdgeClipped;
@"UIView" _clippingView;
Q _edgesClipped;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _visibleBounds;
```

## Properties

```
@property (T@"UIView",W,N,V_clippingView) clippingView;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_visibleBounds) visibleBounds;
@property (TB,N,V_ignoresResult) ignoresResult;
@property (TQ,N,V_edgesClipped) edgesClipped;
@property (TB,R,N) hasClippedEdges;
@property (TB,N,V_leftEdgeClipped) leftEdgeClipped;
@property (TB,N,V_rightEdgeClipped) rightEdgeClipped;
@property (TB,N,V_bottomEdgeClipped) bottomEdgeClipped;
@property (TB,N,V_topEdgeClipped) topEdgeClipped;
```

## Instance methods

```
-[_UITextClippingDebugInfo visibleBounds];
-[_UITextClippingDebugInfo clippingView];
-[_UITextClippingDebugInfo setClippingView:];
-[_UITextClippingDebugInfo setVisibleBounds:];
-[_UITextClippingDebugInfo hasClippedEdges];
-[_UITextClippingDebugInfo leftEdgeClipped];
-[_UITextClippingDebugInfo bottomEdgeClipped];
-[_UITextClippingDebugInfo edgesClipped];
-[_UITextClippingDebugInfo ignoresResult];
-[_UITextClippingDebugInfo initWithClippingView:visibleBounds:ignoresResult:edgesClipped:];
-[_UITextClippingDebugInfo rightEdgeClipped];
-[_UITextClippingDebugInfo setBottomEdgeClipped:];
-[_UITextClippingDebugInfo setEdgesClipped:];
-[_UITextClippingDebugInfo setIgnoresResult:];
-[_UITextClippingDebugInfo setLeftEdgeClipped:];
-[_UITextClippingDebugInfo setRightEdgeClipped:];
-[_UITextClippingDebugInfo setTopEdgeClipped:];
-[_UITextClippingDebugInfo topEdgeClipped];
```
