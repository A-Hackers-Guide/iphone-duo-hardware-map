# `PKModifyStrokeInkCommand`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKUndoCommand`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _strokes;
@"NSArray" _inks;
@"NSArray" _oldInks;
```

## Properties

```
@property (T@"NSArray",R,N,V_strokes) strokes;
@property (T@"NSArray",R,N,V_inks) inks;
@property (T@"NSArray",R,N,V_oldInks) oldInks;
```

## Class methods

```
+[PKModifyStrokeInkCommand commandForModifyingStrokes:drawing:inks:];
```

## Instance methods

```
-[PKModifyStrokeInkCommand description];
-[PKModifyStrokeInkCommand strokes];
-[PKModifyStrokeInkCommand applyToDrawing:];
-[PKModifyStrokeInkCommand oldInks];
-[PKModifyStrokeInkCommand applyToDrawingReturnInverted:];
-[PKModifyStrokeInkCommand initWithStrokes:drawingUUID:actionName:inks:oldInks:];
-[PKModifyStrokeInkCommand inks];
-[PKModifyStrokeInkCommand invertedInDrawing:];
```
