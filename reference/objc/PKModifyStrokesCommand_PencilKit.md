# `PKModifyStrokesCommand`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKUndoCommand`
- 2 instance variables, 2 properties, 6 instance methods, 4 class methods

## Instance variables

```
B _hide;
@"NSArray" _strokes;
```

## Properties

```
@property (T@"NSArray",R,N,V_strokes) strokes;
@property (TB,R,N,V_hide) hide;
```

## Class methods

```
+[PKModifyStrokesCommand commandForErasingAllStrokesInDrawing:];
+[PKModifyStrokesCommand commandForErasingStrokes:drawing:];
+[PKModifyStrokesCommand commandForMakingStrokeVisible:drawing:hiding:];
+[PKModifyStrokesCommand commandForMakingStrokesVisible:drawing:hiding:];
```

## Instance methods

```
-[PKModifyStrokesCommand hide];
-[PKModifyStrokesCommand description];
-[PKModifyStrokesCommand strokes];
-[PKModifyStrokesCommand applyToDrawing:];
-[PKModifyStrokesCommand initWithStrokes:drawingUUID:actionName:hiding:];
-[PKModifyStrokesCommand invertedInDrawing:];
```
