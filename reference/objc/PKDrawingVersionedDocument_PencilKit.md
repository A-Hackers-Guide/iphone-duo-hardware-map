# `PKDrawingVersionedDocument`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKVersionedDocument`
- 3 instance variables, 3 properties, 12 instance methods, 2 class methods

## Instance variables

```
B _loadNonInkingStrokes;
@"PKDrawingConcrete" _drawing;
# _drawingClass;
```

## Properties

```
@property (T@"PKDrawingConcrete",&,N,V_drawing) drawing;
@property (T#,&,N,V_drawingClass) drawingClass;
@property (TB,N,V_loadNonInkingStrokes) loadNonInkingStrokes;
```

## Class methods

```
+[PKDrawingVersionedDocument minimumSupportedVersion];
+[PKDrawingVersionedDocument serializationVersion];
```

## Instance methods

```
-[PKDrawingVersionedDocument drawing];
-[PKDrawingVersionedDocument setDrawing:];
-[PKDrawingVersionedDocument initWithDrawing:];
-[PKDrawingVersionedDocument mergeVersion:fromData:];
-[PKDrawingVersionedDocument serializeCurrentVersion:];
-[PKDrawingVersionedDocument drawingClass];
-[PKDrawingVersionedDocument initWithDrawingClass:];
-[PKDrawingVersionedDocument loadNonInkingStrokes];
-[PKDrawingVersionedDocument loadUnzippedData:];
-[PKDrawingVersionedDocument mergeWithDrawingVersionedDocument:];
-[PKDrawingVersionedDocument setDrawingClass:];
-[PKDrawingVersionedDocument setLoadNonInkingStrokes:];
```
