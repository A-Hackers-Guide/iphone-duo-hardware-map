# `UISelectionGrabberCustomPath`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 6 properties, 12 instance methods, 0 class methods

## Instance variables

```
d _lineWidth;
{CGPoint="x"d"y"d} _topPoint;
{CGPoint="x"d"y"d} _bottomPoint;
```

## Properties

```
@property (T{CGPoint=dd},N,V_topPoint) topPoint;
@property (T{CGPoint=dd},N,V_bottomPoint) bottomPoint;
@property (Td,N,V_lineWidth) lineWidth;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) boundingRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) boundingEdgeRect;
@property (TB,R,N) containsZeroPoint;
```

## Instance methods

```
-[UISelectionGrabberCustomPath boundingRect];
-[UISelectionGrabberCustomPath lineWidth];
-[UISelectionGrabberCustomPath setLineWidth:];
-[UISelectionGrabberCustomPath summaryDescription];
-[UISelectionGrabberCustomPath description];
-[UISelectionGrabberCustomPath setBottomPoint:];
-[UISelectionGrabberCustomPath bezierPathForHostView:targetView:];
-[UISelectionGrabberCustomPath bottomPoint];
-[UISelectionGrabberCustomPath boundingEdgeRect];
-[UISelectionGrabberCustomPath containsZeroPoint];
-[UISelectionGrabberCustomPath setTopPoint:];
-[UISelectionGrabberCustomPath topPoint];
```
