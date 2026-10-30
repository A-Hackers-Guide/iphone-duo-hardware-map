# `PKAttachment` (protocol)

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 11 properties, 33 instance methods, 0 class methods

## Properties

```
@property (T@"PKDrawing",C,N) drawing;
@property (T@"PKRecognitionController",R,N) recognitionController;
@property (T{CGAffineTransform=dddddd},R,N) drawingTransform;
@property (T@"PKStrokeSpatialCache",R,N) strokeSpatialCache;
@property (T@"UIView",R,N) tileMaskView;
@property (T@"UIView",R,N) tileContainerView;
@property (T@"UIView",R,N) attachmentContainerView;
@property (T@"UIView",R,N) viewRep;
@property (T@"PKAttachmentView",R,N) attachmentView;
@property (TB,R,N) isAtEndOfDocument;
@property (TB,R,N) isExternalAttachment;
```

## Instance methods

```
-[PKAttachment drawing];
-[PKAttachment setDrawing:];
-[PKAttachment attachmentView];
-[PKAttachment _firstStrokesInSelectedStrokes:];
-[PKAttachment viewRep];
-[PKAttachment visibleOnscreenBoundsDidChange:];
-[PKAttachment _handleSingleTapAtDrawingLocation:];
-[PKAttachment _lastStrokesInSelectedStrokes:];
-[PKAttachment attachmentContainerView];
-[PKAttachment contentTypeForIntersectedStrokes:];
-[PKAttachment drawingTransform];
-[PKAttachment fetchIntersectedStrokesAtPoint:selectionType:inputType:visibleOnscreenStrokes:completion:];
-[PKAttachment fetchIntersectedStrokesBetweenTopPoint:bottomPoint:liveScrollOffset:completion:];
-[PKAttachment hitByTouchLocation:bounds:];
-[PKAttachment isAtEndOfDocument];
-[PKAttachment isExternalAttachment];
-[PKAttachment recognitionController];
-[PKAttachment strokeSpatialCache];
-[PKAttachment tileContainerView];
-[PKAttachment tileMaskView];
-[PKAttachment _handleSingleTapAtDrawingLocation:fromTapStroke:];
-[PKAttachment autoRefineTaskCoordinator];
-[PKAttachment contentScaledCoordinateSpace];
-[PKAttachment contentUnscaledCoordinateSpace];
-[PKAttachment contentWindowCoordinateSpace];
-[PKAttachment didDeselectAllStrokes];
-[PKAttachment didSelectPreviouslySelectedStrokes:];
-[PKAttachment externalAttachmentDidChangeDrawing:];
-[PKAttachment installSelectionView:];
-[PKAttachment strokeDataUUIDsNonInteractiveFromAttachment];
-[PKAttachment translationDidFinishedInViewController:];
-[PKAttachment updateLiveSelectionForStrokesInLayer:inDrawing:];
-[PKAttachment viewScaleForExternalAttachment];
```
