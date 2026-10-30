# `PKSmartSelectionController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKSelectionInteractionDelegate`, `PKStrokeSpatialCacheDelegate`
- 11 instance variables, 10 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"<PKSmartSelectionControllerDelegate>" _delegate;
@"PKTiledView" _tiledView;
@"<PKAttachment>" _currentAttachment;
@"NSMutableDictionary" _uuidToStrokeSpatialCacheDict;
@"PKSelectionController" _selectionController;
@"PKRecognitionController" _recognitionController;
@"PKRecognitionSessionManager" _sessionManager;
{CGPoint="x"d"y"d} _lastTapLocation;
d _lastTapTimestamp;
q _currentTapCount;
@"UIGestureRecognizer" _gestureRecognizer;
```

## Properties

```
@property (T@"PKDrawing",R,N) currentDrawing;
@property (T@"NSArray",R,C,N) currentSelectedStrokes;
@property (Tq,R,N) currentSelectionType;
@property (T@"<PKAttachment>",R,N) currentAttachment;
@property (T@"UIView",R,N) selectionView;
@property (T@"PKRecognitionController",R,N) recognitionController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKSmartSelectionController interaction];
-[PKSmartSelectionController currentDrawing];
-[PKSmartSelectionController dealloc];
-[PKSmartSelectionController selectionView];
-[PKSmartSelectionController translate:];
-[PKSmartSelectionController canCopyAsText];
-[PKSmartSelectionController canTranslate];
-[PKSmartSelectionController clearSelectionIfNecessaryWithCompletion:];
-[PKSmartSelectionController contentTypeForIntersectedStrokes:];
-[PKSmartSelectionController copyAsText:];
-[PKSmartSelectionController currentAttachment];
-[PKSmartSelectionController currentSelectedStrokes];
-[PKSmartSelectionController currentSelectionType];
-[PKSmartSelectionController didFinishCalculatingVisibleOnscreenStrokes:drawing:];
-[PKSmartSelectionController fetchIntersectedStrokesAtPoint:selectionType:inputType:visibleOnscreenStrokes:completion:];
-[PKSmartSelectionController fetchIntersectedStrokesBetweenTopPoint:bottomPoint:liveScrollOffset:completion:];
-[PKSmartSelectionController firstStrokesInSelectedStrokes:isRTL:];
-[PKSmartSelectionController handleDoubleTapInputAtPoint:];
-[PKSmartSelectionController handleDoubleTapInputAtPoint:inSelectionView:];
-[PKSmartSelectionController handleTapInputAtPoint:];
-[PKSmartSelectionController initWithDelegate:canvasView:drawing:gestureRecognizer:];
-[PKSmartSelectionController initWithDelegate:canvasView:gestureRecognizer:recognitionController:];
-[PKSmartSelectionController installSelectionViewForCurrentSelection];
-[PKSmartSelectionController invalidateCacheForBounds:inDrawing:];
-[PKSmartSelectionController lastStrokesInSelectedStrokes:isRTL:];
-[PKSmartSelectionController recognitionController];
-[PKSmartSelectionController selectStrokes:forSelectionType:inDrawing:];
-[PKSmartSelectionController selectStrokesWithoutDidSelectStrokesUpdate:inDrawing:];
-[PKSmartSelectionController selectionInteraction:didSelectStrokes:selectionType:inAttachment:];
-[PKSmartSelectionController selectionInteraction:handleTapOnCanvasAtLocation:inAttachment:];
-[PKSmartSelectionController selectionTypeForTapCount:];
-[PKSmartSelectionController setExternalAttachment:];
-[PKSmartSelectionController straighten:completion:];
-[PKSmartSelectionController strokeSpatialCacheForAttachment:];
-[PKSmartSelectionController updateGestureHistoryWithLocation:gesture:];
```
