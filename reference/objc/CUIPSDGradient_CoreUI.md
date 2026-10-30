# `CUIPSDGradient`

- Image: [`/System/Library/PrivateFrameworks/CoreUI.framework/CoreUI`](../userland/System__Library__PrivateFrameworks__CoreUI.framework__CoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 3 class methods

## Instance variables

```
@"CUIPSDGradientEvaluator" evaluator;
d drawingAngle;
I gradientStyle;
```

## Properties

```
@property (T@"CUIPSDGradientEvaluator",&,Vevaluator) evaluator;
@property (Td,VdrawingAngle) drawingAngle;
@property (TI,VgradientStyle) gradientStyle;
```

## Class methods

```
+[CUIPSDGradient cuiPSDGradientWithColors:locations:midpointLocations:angle:isRadial:];
+[CUIPSDGradient cuiPSDGradientWithColors:locations:midpointLocations:angle:style:];
+[CUIPSDGradient getMidpointLocationFromArray:atIndex:withPolicy:];
```

## Instance methods

```
-[CUIPSDGradient dealloc];
-[CUIPSDGradient evaluator];
-[CUIPSDGradient setEvaluator:];
-[CUIPSDGradient drawingAngle];
-[CUIPSDGradient gradientStyle];
-[CUIPSDGradient initWithEvaluator:drawingAngle:gradientStyle:];
-[CUIPSDGradient setDrawingAngle:];
-[CUIPSDGradient setGradientStyle:];
```
