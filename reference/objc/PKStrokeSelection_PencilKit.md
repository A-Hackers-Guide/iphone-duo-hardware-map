# `PKStrokeSelection`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSItemProviderReading`, `NSItemProviderWriting`
- 8 instance variables, 14 properties, 28 instance methods, 6 class methods

## Instance variables

```
@"NSOrderedSet" _strokes;
@"NSSet" _strokeIdentifiers;
@"PKStroke" _lassoStroke;
@"PKStrokeSelectionImage" _strokeImage;
@"PKStrokeSelectionImage" _strokeImageWithHighlight;
@"PKDrawing" _drawing;
@"NSOrderedSet" _externalElements;
@"NSItemProvider" _externalElementsItemProvider;
```

## Properties

```
@property (T@"NSOrderedSet",R,N,V_strokes) strokes;
@property (T@"NSSet",R,N,V_strokeIdentifiers) strokeIdentifiers;
@property (T@"PKStroke",R,N,V_lassoStroke) lassoStroke;
@property (T@"PKStrokeSelectionImage",C,N,V_strokeImage) strokeImage;
@property (T@"PKStrokeSelectionImage",C,N,V_strokeImageWithHighlight) strokeImageWithHighlight;
@property (T@"PKDrawing",R,N,V_drawing) drawing;
@property (Tq,R,N) requiredContentVersion;
@property (T@"NSOrderedSet",C,N,V_externalElements) externalElements;
@property (T@"NSItemProvider",C,N,V_externalElementsItemProvider) externalElementsItemProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSArray",?,R,C,N) writableTypeIdentifiersForItemProvider;
```

## Class methods

```
+[PKStrokeSelection writableTypeIdentifiersForItemProvider];
+[PKStrokeSelection readableTypeIdentifiersForItemProvider];
+[PKStrokeSelection objectWithItemProviderData:typeIdentifier:error:];
+[PKStrokeSelection objectWithItemProviderData:typeIdentifier:drawingClass:error:];
+[PKStrokeSelection strokeSelectionFromData:];
+[PKStrokeSelection strokeSelectionFromData:forDrawingClass:];
```

## Instance methods

```
-[PKStrokeSelection drawing];
-[PKStrokeSelection writableTypeIdentifiersForItemProvider];
-[PKStrokeSelection requiredContentVersion];
-[PKStrokeSelection bounds];
-[PKStrokeSelection description];
-[PKStrokeSelection loadDataWithTypeIdentifier:forItemProviderCompletionHandler:];
-[PKStrokeSelection strokes];
-[PKStrokeSelection strokeIdentifiers];
-[PKStrokeSelection setStrokeImage:];
-[PKStrokeSelection strokeImage];
-[PKStrokeSelection _newDrawingWithStrokes];
-[PKStrokeSelection boundsWithoutLasso];
-[PKStrokeSelection containsBitmapData];
-[PKStrokeSelection externalElements];
-[PKStrokeSelection externalElementsBounds];
-[PKStrokeSelection externalElementsItemProvider];
-[PKStrokeSelection generateImageWithConfig:fullSizeConfig:selectionInteraction:withCompletion:];
-[PKStrokeSelection imageDataForSelection];
-[PKStrokeSelection initWithStrokes:externalElements:lassoStroke:drawing:];
-[PKStrokeSelection initWithStrokes:lassoStroke:drawing:];
-[PKStrokeSelection lassoStroke];
-[PKStrokeSelection legacyStrokeDataForSelection];
-[PKStrokeSelection newExternalElementsCGImageFromCGImage:withConfig:selectionInteraction:renderImage:withCompletion:];
-[PKStrokeSelection setExternalElements:];
-[PKStrokeSelection setExternalElementsItemProvider:];
-[PKStrokeSelection setStrokeImageWithHighlight:];
-[PKStrokeSelection strokeDataForSelection];
-[PKStrokeSelection strokeImageWithHighlight];
```
