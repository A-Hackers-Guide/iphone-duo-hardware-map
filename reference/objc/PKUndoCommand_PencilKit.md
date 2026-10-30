# `PKUndoCommand`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _changesVisibleStrokes;
@"<PKDrawingUUID>" _drawingUUID;
@"NSString" _actionName;
```

## Properties

```
@property (T@"<PKDrawingUUID>",R,N,V_drawingUUID) drawingUUID;
@property (T@"NSString",C,N,V_actionName) actionName;
@property (TB,R,N,V_changesVisibleStrokes) changesVisibleStrokes;
```

## Instance methods

```
-[PKUndoCommand inverted];
-[PKUndoCommand setActionName:];
-[PKUndoCommand strokes];
-[PKUndoCommand actionName];
-[PKUndoCommand applyToDrawing:];
-[PKUndoCommand initWithDrawingUUID:actionName:];
-[PKUndoCommand applyToDrawingReturnInverted:];
-[PKUndoCommand changesVisibleStrokes];
-[PKUndoCommand drawingUUID];
-[PKUndoCommand initWithDrawingUUID:actionName:changesVisibleStrokes:];
-[PKUndoCommand invertedInDrawing:];
-[PKUndoCommand registerWithUndoManager:target:selector:];
```
