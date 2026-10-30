# `PKModifyStrokesGroupIDCommand`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKUndoCommand`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _strokes;
@"NSUUID" _groupID;
@"NSUUID" _oldGroupID;
```

## Properties

```
@property (T@"NSArray",R,N,V_strokes) strokes;
@property (T@"NSUUID",R,N,V_groupID) groupID;
@property (T@"NSUUID",R,N,V_oldGroupID) oldGroupID;
```

## Class methods

```
+[PKModifyStrokesGroupIDCommand commandForModifyingStrokes:drawing:groupID:actionName:];
```

## Instance methods

```
-[PKModifyStrokesGroupIDCommand groupID];
-[PKModifyStrokesGroupIDCommand description];
-[PKModifyStrokesGroupIDCommand strokes];
-[PKModifyStrokesGroupIDCommand applyToDrawing:];
-[PKModifyStrokesGroupIDCommand applyToDrawingReturnInverted:];
-[PKModifyStrokesGroupIDCommand initWithStrokes:drawingUUID:actionName:groupID:oldGroupID:];
-[PKModifyStrokesGroupIDCommand invertedInDrawing:];
-[PKModifyStrokesGroupIDCommand oldGroupID];
```
