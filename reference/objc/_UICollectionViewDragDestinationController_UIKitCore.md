# `_UICollectionViewDragDestinationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDropInteractionDelegate_Private`
- 8 instance variables, 4 properties, 37 instance methods, 0 class methods

## Instance variables

```
@"UICollectionView" _collectionView;
@"UIDropInteraction" _dropInteraction;
@"_UICollectionViewDragAndDropController" _delegate;
@"CADisplayLink" _reorderDisplayLink;
@"_UIDragDestinationControllerSessionState" _sessionState;
@"_UIDragDestinationControllerReorderingState" _reorderingState;
@"_UIDragDestinationControllerDropProposalState" _dropProposalState;
Q _dropSuspensionCount;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UICollectionViewDragDestinationController _beginOrResumeDropSession:];
-[_UICollectionViewDragDestinationController dropInteraction:sessionDidEnter:];
-[_UICollectionViewDragDestinationController dropInteraction:sessionDidUpdate:];
-[_UICollectionViewDragDestinationController _dropInteraction:dataOwnerForSession:];
-[_UICollectionViewDragDestinationController dropInteraction:concludeDrop:];
-[_UICollectionViewDragDestinationController _cancelInteractiveReorderingIfNeeded];
-[_UICollectionViewDragDestinationController _queryClientForPreviewParametersForItemAtIndexPath:];
-[_UICollectionViewDragDestinationController _resumeReorderingDisplayLink];
-[_UICollectionViewDragDestinationController _shouldQueryDropActionForIndexPath:];
-[_UICollectionViewDragDestinationController dropInteraction:performDrop:];
-[_UICollectionViewDragDestinationController _configureInteraction];
-[_UICollectionViewDragDestinationController dropInteraction:canHandleSession:];
-[_UICollectionViewDragDestinationController _dropDelegateActual];
-[_UICollectionViewDragDestinationController dealloc];
-[_UICollectionViewDragDestinationController _dropDelegateProxy];
-[_UICollectionViewDragDestinationController _endInteractiveReorderingIfNeeded];
-[_UICollectionViewDragDestinationController _commitCurrentInteractiveReordering];
-[_UICollectionViewDragDestinationController dropInteraction:item:willAnimateDropWithAnimator:];
-[_UICollectionViewDragDestinationController _isLocalInteractiveMove];
-[_UICollectionViewDragDestinationController initWithCollectionView:delegate:];
-[_UICollectionViewDragDestinationController _updateDropProposalByQueryingClientIfNeeded:indicatorLayoutAttributes:];
-[_UICollectionViewDragDestinationController hasPerformedReordering];
-[_UICollectionViewDragDestinationController _computeNextItemAttributesStartingFromItemAttributes:withCurrentDragLocation:];
-[_UICollectionViewDragDestinationController _dragDestinationDelegateActual];
-[_UICollectionViewDragDestinationController _dragDestinationDelegateProxy];
-[_UICollectionViewDragDestinationController dropInteraction:sessionDidExit:];
-[_UICollectionViewDragDestinationController _isMultiItemSource];
-[_UICollectionViewDragDestinationController description];
-[_UICollectionViewDragDestinationController _effectiveDropProposalForProposal:];
-[_UICollectionViewDragDestinationController dropInteraction:sessionDidEnd:];
-[_UICollectionViewDragDestinationController _configureReorderingDisplayLinkIfNeeded];
-[_UICollectionViewDragDestinationController _commitCurrentDragAndDropSession];
-[_UICollectionViewDragDestinationController _pauseReorderingDisplayLink];
-[_UICollectionViewDragDestinationController _cancelCurrentInteractiveReorder];
-[_UICollectionViewDragDestinationController _hasGapLargeEnoughToRequireDropActionCallForCurrentItemAttributes:proposedNextItemAttributes:];
-[_UICollectionViewDragDestinationController dropInteraction:previewForDroppingItem:withDefault:];
-[_UICollectionViewDragDestinationController _reorderingDisplayLinkDidTick];
```
