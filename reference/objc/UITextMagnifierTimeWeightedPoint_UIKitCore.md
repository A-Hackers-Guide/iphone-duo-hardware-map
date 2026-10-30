# `UITextMagnifierTimeWeightedPoint`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 10 instance methods, 0 class methods

## Instance variables

```
i m_index;
[16{?="point"{CGPoint="x"d"y"d}"time"d}] m_points;
```

## Properties

```
@property (T{CGPoint=dd},R,N) weightedPoint;
```

## Instance methods

```
-[UITextMagnifierTimeWeightedPoint weightedPoint];
-[UITextMagnifierTimeWeightedPoint isPlacedCarefully];
-[UITextMagnifierTimeWeightedPoint displacementInInterval:priorTo:];
-[UITextMagnifierTimeWeightedPoint addPoint:];
-[UITextMagnifierTimeWeightedPoint clearHistory];
-[UITextMagnifierTimeWeightedPoint diffFromLastPoint];
-[UITextMagnifierTimeWeightedPoint displacementInInterval:];
-[UITextMagnifierTimeWeightedPoint distanceCoveredInInterval:];
-[UITextMagnifierTimeWeightedPoint distanceCoveredInInterval:priorTo:];
-[UITextMagnifierTimeWeightedPoint historyCovers:];
```
