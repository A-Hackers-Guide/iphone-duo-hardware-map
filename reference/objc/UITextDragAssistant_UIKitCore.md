# `UITextDragAssistant`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDragInteractionDelegate_Private`, `UIDropInteractionDelegate_Private`, `_UITextPasteProgressSupport`, `UITextPasteSessionDelegate`, `UITextDragDropSupport`
- 26 instance variables, 10 properties, 81 instance methods, 0 class methods

## Instance variables

```
{?="viewSupportsGhostedRanges"b1"geometrySupportsSameViewOperations"b1"shouldRestoreFirstResponder"b1"draggingOngoing"b1"handledCancelAnimation"b1"restoreNonEditableAfterDrop"b1"restoreSelectableAfterDrop"b1"wasSelectableBeforeDrop"b1"forceEditable"b1"delegateSupportsProposalForDrop"b1"delegateSupportsSessionDidUpdate"b1"delegateSupportsRangeForDrop"b1"delegateSupportsPositionForDrop"b1"delegateSupportsWillMoveCaret"b1"delegateSupportsDidMoveCaret"b1"viewSupportsTextStorage"b1"textStorageDidChange"b1"dropPerformed"b1"defaultDropHandling"b1"didHandleSameViewDropOperation"b1} _flags;
@"<UITextDraggableGeometry>" _geometry;
@"<UIDragSession>" _currentDragSession;
@"UIDragInteraction" _currentDragInteraction;
@"NSArray" _draggedTextRanges;
@"UITextRange" _initialDragSelectedRange;
{CGPoint="x"d"y"d} _initialDragLocation;
@"NSArray" _movedItemsInView;
@"NSMapTable" _targetedPreviewProviders;
@"NSMapTable" _previewProviders;
@"NSTextStorage" _observingStorage;
@"<UIDropSession>" _currentDropSession;
@"_UITextDragCaretView" _dropCaret;
@"UITextRange" _currentDropRange;
@"UIDragItem" _topmostDropItem;
@"UITargetedDragPreview" _topmostDropPreview;
@"UITextDropProposal" _currentDropProposal;
@"UITextRange" _preDropSelectionRange;
@"<UITextDraggableGeometrySameViewDropOperation>" _sameViewDropOperation;
@"UITextDraggableGeometrySameViewDropOperationResult" _sameViewDropOperationResult;
@"UITextPasteController" _dropPasteController;
@"<UITextDropPasteSession>" _dropPasteSession;
@? _delayedPreviewProvider;
@"UIView<UITextDragSupporting><UITextDropSupporting>" _view;
@"UIDragInteraction" _dragInteraction;
@"UIDropInteraction" _dropInteraction;
```

## Properties

```
@property (T@"UIView<UITextDragSupporting><UITextDropSupporting>",R,W,N,V_view) view;
@property (T@"<UITextDraggableGeometry>",R,N) geometry;
@property (T@"UIDragInteraction",R,W,N,V_dragInteraction) dragInteraction;
@property (T@"UIDropInteraction",R,W,N,V_dropInteraction) dropInteraction;
@property (TB,R,N,GisDragActive) dragActive;
@property (TB,R,N,GisDropActive) dropActive;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UITextDragAssistant dragInteraction:previewForLiftingItem:session:];
-[UITextDragAssistant dragInteraction:itemsForBeginningSession:];
-[UITextDragAssistant dragInteraction:previewForCancellingItem:withDefault:];
-[UITextDragAssistant dragInteraction:item:willAnimateCancelWithAnimator:];
-[UITextDragAssistant dropInteraction:sessionDidEnter:];
-[UITextDragAssistant dragInteraction:sessionDidMove:];
-[UITextDragAssistant dropInteraction:sessionDidUpdate:];
-[UITextDragAssistant dragInteraction:session:didEndWithOperation:];
-[UITextDragAssistant _dropInteraction:dataOwnerForSession:];
-[UITextDragAssistant isDragActive];
-[UITextDragAssistant dragInteraction:sessionWillBegin:];
-[UITextDragAssistant dragInteraction:prefersFullSizePreviewsForSession:];
-[UITextDragAssistant dropInteraction:concludeDrop:];
-[UITextDragAssistant _addDraggedTextRangeForItems:defaultRange:];
-[UITextDragAssistant _accessibilityDraggableRanges];
-[UITextDragAssistant _dragInteraction:competingGestureRecognizerShouldDelayLift:];
-[UITextDragAssistant notifyTextInteraction];
-[UITextDragAssistant dragInteraction:session:willEndWithOperation:];
-[UITextDragAssistant dropInteraction:performDrop:];
-[UITextDragAssistant _textPasteSelectableRangeForResult:fromRange:];
-[UITextDragAssistant dropInteraction];
-[UITextDragAssistant textPasteSessionWillHidePasteResult:];
-[UITextDragAssistant dragInteraction:sessionForAddingItems:withTouchAtPoint:];
-[UITextDragAssistant dragInteraction];
-[UITextDragAssistant dropInteraction:canHandleSession:];
-[UITextDragAssistant _textRangeForDraggingFromPoint:];
-[UITextDragAssistant textPasteSessionWillBeginPasting:];
-[UITextDragAssistant _forDraggedTextRangesDo:];
-[UITextDragAssistant _dragInteraction:dataOwnerForSession:];
-[UITextDragAssistant initWithView:];
-[UITextDragAssistant _shrinkingPreview:toPosition:];
-[UITextDragAssistant _viewHasOtherDragInteraction];
-[UITextDragAssistant _closestPositionToPoint:];
-[UITextDragAssistant _performSameViewOperation:];
-[UITextDragAssistant _initializeDragSession:withInteraction:];
-[UITextDragAssistant _dataOwnerForSession:atPoint:];
-[UITextDragAssistant installDragInteractionIfNeeded];
-[UITextDragAssistant _positionInSession:];
-[UITextDragAssistant _dropRequestWithRange:inSession:];
-[UITextDragAssistant _clearDraggedTextRanges];
-[UITextDragAssistant _performDropToRange:inSession:];
-[UITextDragAssistant _dropRequestWithRange:suggestedProposal:inSession:];
-[UITextDragAssistant _updateDropCaretToRange:session:];
-[UITextDragAssistant dropInteraction:item:willAnimateDropWithAnimator:];
-[UITextDragAssistant _restoreResponderIfNeededForOperation:];
-[UITextDragAssistant geometry];
-[UITextDragAssistant isDropActive];
-[UITextDragAssistant view];
-[UITextDragAssistant _dragInteraction:dataOwnerForAddingToSession:withTouchAtPoint:];
-[UITextDragAssistant textPasteSessionDidRevealPasteResult:];
-[UITextDragAssistant _applyOptionsToGeometry];
-[UITextDragAssistant _cleanupDrop];
-[UITextDragAssistant _dragInteractionShouldBecomeDraggingSourceDelegate:];
-[UITextDragAssistant initWithView:geometry:];
-[UITextDragAssistant invalidateDropCaret];
-[UITextDragAssistant _suggestedProposalForRequest:];
-[UITextDragAssistant _updateCurrentDropProposalInSession:usingRequest:];
-[UITextDragAssistant _rangeInSession:];
-[UITextDragAssistant _hasDraggedTextRange:];
-[UITextDragAssistant dropInteraction:sessionDidExit:];
-[UITextDragAssistant _liftOrDrag:didEndWithOperation:];
-[UITextDragAssistant dragInteraction:itemsForAddingToSession:withTouchAtPoint:];
-[UITextDragAssistant _containerViewForDropPreviews];
-[UITextDragAssistant _previewForIrrelevantItemFromPreview:];
-[UITextDragAssistant installDropInteractionIfNeeded];
-[UITextDragAssistant _textPasteRangeBehavior];
-[UITextDragAssistant _containerViewForLiftPreviews];
-[UITextDragAssistant _ghostDraggedTextRanges:];
-[UITextDragAssistant _itemsForDraggedRange:];
-[UITextDragAssistant _textStorageDidProcessEditing];
-[UITextDragAssistant _prepareSameViewOperation:forItems:fromRanges:toRange:];
-[UITextDragAssistant dragInteraction:willAnimateLiftWithAnimator:session:];
-[UITextDragAssistant dropInteraction:sessionDidEnd:];
-[UITextDragAssistant _stopObservingTextStorage];
-[UITextDragAssistant initWithDraggableOnlyView:];
-[UITextDragAssistant accessibilityCanDrag];
-[UITextDragAssistant _previewForTopmostItem:];
-[UITextDragAssistant _dropInteraction:delayedPreviewProviderForDroppingItem:previewProvider:];
-[UITextDragAssistant textPasteSessionDidEndPasting:];
-[UITextDragAssistant _dragInteraction:shouldDelayCompetingGestureRecognizer:];
-[UITextDragAssistant dropInteraction:previewForDroppingItem:withDefault:];
```
