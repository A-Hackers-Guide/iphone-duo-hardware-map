# `_UICircleProgressLayer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CALayer`
- 6 instance variables, 6 properties, 13 instance methods, 1 class methods

## Instance variables

```
d _progressLineWidth;
d _oneFullRotation;
B _showProgressTray;
q _progressStartPoint;
@"UIColor" _progressColor;
@"UIColor" _progressBackgroundColor;
```

## Properties

```
@property (Tq,N,V_progressStartPoint) progressStartPoint;
@property (T@"UIColor",&,N,V_progressColor) progressColor;
@property (T@"UIColor",&,N,V_progressBackgroundColor) progressBackgroundColor;
@property (Td,N,V_progressLineWidth) progressLineWidth;
@property (TB,N,V_showProgressTray) showProgressTray;
@property (Td,D,N) progress;
```

## Class methods

```
+[_UICircleProgressLayer needsDisplayForKey:];
```

## Instance methods

```
-[_UICircleProgressLayer drawInContext:];
-[_UICircleProgressLayer init];
-[_UICircleProgressLayer setProgressColor:];
-[_UICircleProgressLayer initWithLayer:];
-[_UICircleProgressLayer progressColor];
-[_UICircleProgressLayer progressBackgroundColor];
-[_UICircleProgressLayer progressLineWidth];
-[_UICircleProgressLayer progressStartPoint];
-[_UICircleProgressLayer setProgressBackgroundColor:];
-[_UICircleProgressLayer setProgressLineWidth:];
-[_UICircleProgressLayer setProgressStartPoint:];
-[_UICircleProgressLayer setShowProgressTray:];
-[_UICircleProgressLayer showProgressTray];
```
