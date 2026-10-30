# `PKTransformStrokesCommand`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKUndoCommand`
- 3 instance variables, 3 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _strokes;
@"NSArray" _strokeTransforms;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _strokeTransform;
```

## Properties

```
@property (T@"NSArray",R,N,V_strokes) strokes;
@property (T{CGAffineTransform=dddddd},R,N,V_strokeTransform) strokeTransform;
@property (T@"NSArray",R,N,V_strokeTransforms) strokeTransforms;
```

## Class methods

```
+[PKTransformStrokesCommand commandForTransforming:drawing:strokeTransform:];
+[PKTransformStrokesCommand commandForTransforming:drawing:strokeTransforms:];
```

## Instance methods

```
-[PKTransformStrokesCommand strokeTransform];
-[PKTransformStrokesCommand description];
-[PKTransformStrokesCommand strokes];
-[PKTransformStrokesCommand applyToDrawing:];
-[PKTransformStrokesCommand initWithStrokes:drawingUUID:actionName:strokeTransform:];
-[PKTransformStrokesCommand initWithStrokes:drawingUUID:actionName:strokeTransforms:];
-[PKTransformStrokesCommand invertedInDrawing:];
-[PKTransformStrokesCommand strokeTransforms];
```
