# `UIKBMultilingualIntroductionArrowView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 4 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _startPoint;
{CGPoint="x"d"y"d} _endPoint;
@"CAShapeLayer" _arrowTailLayer;
@"CAShapeLayer" _arrowHeadLayer;
```

## Properties

```
@property (T{CGPoint=dd},N,V_startPoint) startPoint;
@property (T{CGPoint=dd},N,V_endPoint) endPoint;
@property (T@"CAShapeLayer",&,N,V_arrowTailLayer) arrowTailLayer;
@property (T@"CAShapeLayer",&,N,V_arrowHeadLayer) arrowHeadLayer;
```

## Instance methods

```
-[UIKBMultilingualIntroductionArrowView init];
-[UIKBMultilingualIntroductionArrowView setStartPoint:];
-[UIKBMultilingualIntroductionArrowView startPoint];
-[UIKBMultilingualIntroductionArrowView endPoint];
-[UIKBMultilingualIntroductionArrowView setEndPoint:];
-[UIKBMultilingualIntroductionArrowView _updatePath];
-[UIKBMultilingualIntroductionArrowView arrowHeadLayer];
-[UIKBMultilingualIntroductionArrowView arrowTailLayer];
-[UIKBMultilingualIntroductionArrowView setArrowHeadLayer:];
-[UIKBMultilingualIntroductionArrowView setArrowTailLayer:];
-[UIKBMultilingualIntroductionArrowView setStartPoint:endPoint:];
```
