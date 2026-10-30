# `PKSelectionController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDropInteractionDelegate_Private`, `PKSelectionRenderingDelegate`, `PKSelectionObserving`
- 26 instance variables, 5 properties, 26 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _dropPosition;
@"<PKDrawingUUID>" _previousDrawingUUIDForSelection;
i _selectionViewCount;
q _currentIntersectionAlgorithm;
@"PKTranscriptionController" _transcriptionController;
@"NSObject<OS_dispatch_queue>" _intersectionQueue;
@"NSObject<OS_dispatch_queue>" _selectionHullQueue;
@? _intersectStrokesBetweenLollipopBlock;
@"NSString" _cachedReflowTranscription;
@"UIDropInteraction" _dropInteraction;
B _isChangingColor;
@? _deferredChangingColorBlock;
@"PKImageGenerationController" _imageGenerationController;
B _isClearingSelection;
B _shouldClampInputPoints;
B _isWritingToolsManagingSelection;
B _insertSpaceEnabled;
B _isCurrentlyAddingSpace;
@"PKTiledView" _tiledView;
@"PKStrokeSelection" _currentStrokeSelection;
@"UIPasteboard" _currentPasteboard;
@"NSUUID" _selectionAdditionalStrokesHandle;
@"PKSpaceInsertionController" _spaceInsertionController;
@"PKSelectionView" _selectionView;
@"PKSelectionGestureView" _selectionGestureView;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _selectionTransform;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSObject<OS_dispatch_queue>",&,D,N) selectionHullQueue;
```

## Instance methods

```
-[PKSelectionController dropInteraction:sessionDidEnter:];
-[PKSelectionController dropInteraction:sessionDidUpdate:];
-[PKSelectionController _dropInteraction:dataOwnerForSession:];
-[PKSelectionController dropInteraction:performDrop:];
-[PKSelectionController dropInteraction:canHandleSession:];
-[PKSelectionController dealloc];
-[PKSelectionController _lastStrokesInStrokes:];
-[PKSelectionController dropInteraction:sessionDidExit:];
-[PKSelectionController selectionColor];
-[PKSelectionController isRTL];
-[PKSelectionController dropInteraction:previewForDroppingItem:withDefault:];
-[PKSelectionController _firstStrokesInStrokes:];
-[PKSelectionController didEndScroll];
-[PKSelectionController _addItemsToPasteboard:];
-[PKSelectionController attachmentBoundsForDrawing:];
-[PKSelectionController currentIntersectionAlgorithm];
-[PKSelectionController didBeginModifyDrawing];
-[PKSelectionController didBeginSpaceInsertionWithLassoStroke:drawing:addDefaultSpace:strokesAbove:strokesBelow:externalElements:];
-[PKSelectionController didEndModifyDrawing];
-[PKSelectionController didSelect:lassoStroke:transform:drawing:];
-[PKSelectionController didSelect:lassoStroke:transform:drawing:selectionType:completion:];
-[PKSelectionController didSelectStrokesNotification:];
-[PKSelectionController scaleForDrawing:];
-[PKSelectionController selectionHullQueue];
-[PKSelectionController transformFromStrokeSpaceToViewInDrawing:];
-[PKSelectionController updateLiveSelectionForStrokesInLayer:inDrawing:];
```
