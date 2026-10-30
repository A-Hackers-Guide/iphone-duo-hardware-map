# `_UICollectionViewMultiSelectController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIMultiSelectInteractionDelegate_Internal`
- 6 instance variables, 10 properties, 67 instance methods, 0 class methods

## Instance variables

```
q _computedAxisConstraint;
{?="visibleCellsDirtied"b1"prewarmingCellCache"b1"updatingSelection"b1} _flags;
@"UICollectionView" _collectionView;
@"UIMultiSelectInteraction" _multiSelectInteraction;
@"UIMultiSelectInteractionState" _selectionState;
@"NSMapTable" _contentMaskCache;
```

## Properties

```
@property (T@"UICollectionView",W,N,V_collectionView) collectionView;
@property (T@"UIMultiSelectInteraction",&,N,V_multiSelectInteraction) multiSelectInteraction;
@property (T@"UIMultiSelectInteractionState",&,N,V_selectionState) selectionState;
@property (T@"NSMapTable",&,N,V_contentMaskCache) contentMaskCache;
@property (TB,N,GisEnabled) enabled;
@property (TB,R,N,GisInMultiselectInteraction) inMultiselectInteraction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UICollectionViewMultiSelectController shouldAllowSelectionExtensionAtPoint:];
-[_UICollectionViewMultiSelectController multiSelectInteraction:extendSelectionInDirection:];
-[_UICollectionViewMultiSelectController supportsMultiSelectInteraction:];
-[_UICollectionViewMultiSelectController didCancelMultiSelectInteraction:atPoint:];
-[_UICollectionViewMultiSelectController keyCommandsForSelectionExtension];
-[_UICollectionViewMultiSelectController isInMultiSelectMode];
-[_UICollectionViewMultiSelectController initWithCollectionView:];
-[_UICollectionViewMultiSelectController _isUsingTableLayoutSPI];
-[_UICollectionViewMultiSelectController _shouldBeginInteractionAtIndexPath:];
-[_UICollectionViewMultiSelectController multiSelectInteraction:toggleSelectionStateUpToPoint:];
-[_UICollectionViewMultiSelectController targetForKeyCommands];
-[_UICollectionViewMultiSelectController multiSelectInteraction];
-[_UICollectionViewMultiSelectController shouldAllowSelectionExtensionAtIndexPath:];
-[_UICollectionViewMultiSelectController interaction:shouldAutomaticallyTransitionToMultiSelectModeAtPoint:withVelocity:];
-[_UICollectionViewMultiSelectController multiSelectInteraction:appendSelectionAtPoint:];
-[_UICollectionViewMultiSelectController collectionViewDidUpdateVisibleCells];
-[_UICollectionViewMultiSelectController _collectionViewDelegate];
-[_UICollectionViewMultiSelectController multiSelectInteraction:selectItemsWithinRect:leadingPoint:];
-[_UICollectionViewMultiSelectController _boundingScrollViewForIndexPath:];
-[_UICollectionViewMultiSelectController _allowsBandSelectionStartingAtPoint:multiSelectInteraction:];
-[_UICollectionViewMultiSelectController _testTouchPolicyAtPoint:withVelocity:];
-[_UICollectionViewMultiSelectController _point:liesBeyondFrame:inDirection:];
-[_UICollectionViewMultiSelectController dealloc];
-[_UICollectionViewMultiSelectController collectionView];
-[_UICollectionViewMultiSelectController noteProgrammaticSelectionChangeAtIndexPath:];
-[_UICollectionViewMultiSelectController _selectIndexPaths:];
-[_UICollectionViewMultiSelectController _indexPathsWithinRect:];
-[_UICollectionViewMultiSelectController multiSelectInteraction:toggleSelectionWithinRect:leadingPoint:];
-[_UICollectionViewMultiSelectController setSelectionState:];
-[_UICollectionViewMultiSelectController _allowsPanningAcrossConstrainedAxisToBeginMultiSelectInteractionAtPoint:];
-[_UICollectionViewMultiSelectController willBeginMultiSelectInteraction:atPoint:keepCurrentSelection:];
-[_UICollectionViewMultiSelectController multiSelectInteraction:shouldStartBandSelectionAtPoint:];
-[_UICollectionViewMultiSelectController didEndMultiSelectInteraction:atPoint:];
-[_UICollectionViewMultiSelectController _updateContentMasksForVisibleCells];
-[_UICollectionViewMultiSelectController shouldAllowSelectionAppendageAtPoint:];
-[_UICollectionViewMultiSelectController isInMultiselectInteraction];
-[_UICollectionViewMultiSelectController isEnabled];
-[_UICollectionViewMultiSelectController _deselectIndexPaths:];
-[_UICollectionViewMultiSelectController setCollectionView:];
-[_UICollectionViewMultiSelectController _antecedentIndexPathsForLayoutAttributes:inDirection:];
-[_UICollectionViewMultiSelectController _extendSelectionToPoint:];
-[_UICollectionViewMultiSelectController _autoScrollAtIndexPaths:fromPoint:];
-[_UICollectionViewMultiSelectController supportsKeyboardSelectionExtension];
-[_UICollectionViewMultiSelectController clearSelectionState];
-[_UICollectionViewMultiSelectController multiSelectInteraction:shouldShowBandForSelectionStartingAtPoint:];
-[_UICollectionViewMultiSelectController setMultiSelectInteraction:];
-[_UICollectionViewMultiSelectController setEnabled:];
-[_UICollectionViewMultiSelectController indexPathsBetweenIndexPath:andIndexPath:];
-[_UICollectionViewMultiSelectController uninstallFromCollectionView];
-[_UICollectionViewMultiSelectController shouldBeginMultiSelectInteraction:ofType:atPoint:withVelocity:];
-[_UICollectionViewMultiSelectController _shouldBeginInteractionAtPoint:];
-[_UICollectionViewMultiSelectController _hitTestForSystemEditControlAtPoint:];
-[_UICollectionViewMultiSelectController automaticallyTransitionToMultiSelectModeKeepingCurrentSelection:];
-[_UICollectionViewMultiSelectController childScrollViewAtLocation:];
-[_UICollectionViewMultiSelectController updateSelectedIndexPaths:];
-[_UICollectionViewMultiSelectController selectionStartIndexPath];
-[_UICollectionViewMultiSelectController contentMaskCache];
-[_UICollectionViewMultiSelectController _autoScrollAssistantForIndexPaths:];
-[_UICollectionViewMultiSelectController selectionEndIndexPath];
-[_UICollectionViewMultiSelectController selectedIndexPathsChanged:];
-[_UICollectionViewMultiSelectController _performWithPrewarmingCache:];
-[_UICollectionViewMultiSelectController axisConstraintForSingleFingerPanGestureAtPoint:];
-[_UICollectionViewMultiSelectController axisConstraintAtPoint:];
-[_UICollectionViewMultiSelectController selectionState];
-[_UICollectionViewMultiSelectController multiSelectInteractionGestureShouldPreventDragLiftGesture:];
-[_UICollectionViewMultiSelectController setContentMaskCache:];
-[_UICollectionViewMultiSelectController axisConstraintAtIndexPath:];
```
