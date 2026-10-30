# `PKSpaceInsertionController`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 27 instance variables, 6 properties, 38 instance methods, 0 class methods

## Instance variables

```
@"NSMutableOrderedSet" _strokesBelow;
@"NSMutableOrderedSet" _strokesAbove;
@"UIView" _tapToDismissView;
@"PKSpaceInsertionView" _topInsertionView;
@"PKSpaceInsertionView" _bottomInsertionView;
{CGPoint="x"d"y"d} _beginDragLocation;
{CGPoint="x"d"y"d} _initialViewLocation;
@"UIPanGestureRecognizer" _dragTopLollipopGR;
@"UIPanGestureRecognizer" _dragBottomLollipopGR;
@"PKStrokeSelection" _bottomStrokeSelection;
@"PKStrokeSelection" _topStrokeSelection;
@"PKImageView" _topImageView;
@"PKImageView" _bottomImageView;
B _topHandleRemovesWhitespace;
@"PKStrokeSelection" _strokeSelectionBeforeInsertingSpace;
q _selectionTypeBeforeInsertingSpace;
@"PKStrokeSelection" _cachedStrokeSelection;
@"NSOrderedSet" _cachedStrokesBelow;
@"NSOrderedSet" _cachedStrokesAbove;
B _shouldUseCachedStrokes;
B _insertSpaceAffordancePanDidEnd;
B _isCurrentlyAddingSpace;
B _didMoveStrokes;
@"PKStroke" _lassoStroke;
@"PKDrawing" _drawing;
@"PKSelectionController" _selectionController;
@"NSOrderedSet" _externalElements;
```

## Properties

```
@property (TB,N,V_isCurrentlyAddingSpace) isCurrentlyAddingSpace;
@property (T@"PKStroke",&,N,V_lassoStroke) lassoStroke;
@property (T@"PKDrawing",&,N,V_drawing) drawing;
@property (T@"PKSelectionController",R,W,N,V_selectionController) selectionController;
@property (TB,R,N,V_didMoveStrokes) didMoveStrokes;
@property (T@"NSOrderedSet",C,N,V_externalElements) externalElements;
```

## Instance methods

```
-[PKSpaceInsertionController drawing];
-[PKSpaceInsertionController setDrawing:];
-[PKSpaceInsertionController selectionController];
-[PKSpaceInsertionController initWithSelectionController:];
-[PKSpaceInsertionController _didGrabInsertSpaceAffordance:];
-[PKSpaceInsertionController didScroll:];
-[PKSpaceInsertionController setLassoStroke:];
-[PKSpaceInsertionController _addSpacingViewsWithFrame:];
-[PKSpaceInsertionController _blitStrokesToViewForSpaceInsertionType:withCompletion:];
-[PKSpaceInsertionController _didEndCreatingSpace];
-[PKSpaceInsertionController _dismissHandlesAndReselectExistingSelectionInDrawing:];
-[PKSpaceInsertionController _dismissSpacingResizeHandles];
-[PKSpaceInsertionController _dragLollipop:];
-[PKSpaceInsertionController _initalBufferBetweenLollipops];
-[PKSpaceInsertionController _layoutViewsIfNecessary];
-[PKSpaceInsertionController _makeSpaceWithOffset:spaceInsertionType:];
-[PKSpaceInsertionController _panGestureDidBegin:];
-[PKSpaceInsertionController _panGestureDidCancelOrFail:];
-[PKSpaceInsertionController _panGestureDidChange:];
-[PKSpaceInsertionController _panGestureDidEnd:];
-[PKSpaceInsertionController _sortStrokesAboveOrBelowWithStrokesAbove:strokesBelow:];
-[PKSpaceInsertionController _temporarilyShiftStrokesWithOffset:spaceInsertionType:];
-[PKSpaceInsertionController _visibleStrokesOnPage:];
-[PKSpaceInsertionController commitSpacingResize];
-[PKSpaceInsertionController didBeginCreatingSpaceWithLassoStroke:drawing:addDefaultSpace:strokesAbove:strokesBelow:externalElements:];
-[PKSpaceInsertionController didMoveStrokes];
-[PKSpaceInsertionController externalElements];
-[PKSpaceInsertionController fetchStrokesAmbiguouslyBelowAndAboveInsertSpaceHandleWithStrokes:inDrawing:completion:];
-[PKSpaceInsertionController initTopAndBottomSelectionIfNecessary];
-[PKSpaceInsertionController insertDefaultSpace:];
-[PKSpaceInsertionController invalidateCachedStrokes];
-[PKSpaceInsertionController isCurrentlyAddingSpace];
-[PKSpaceInsertionController lassoStroke];
-[PKSpaceInsertionController offsetInStrokeSpaceFromViewOffset:inDrawing:];
-[PKSpaceInsertionController projectPath:toEndOfFrame:];
-[PKSpaceInsertionController setExternalElements:];
-[PKSpaceInsertionController setIsCurrentlyAddingSpace:];
-[PKSpaceInsertionController shiftStrokesWithOffset:];
```
