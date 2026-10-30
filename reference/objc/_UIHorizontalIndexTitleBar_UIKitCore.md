# `_UIHorizontalIndexTitleBar`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UICollectionViewDelegate`, `UICollectionViewDataSource`, `UICollectionViewDelegate`
- 10 instance variables, 14 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _entries;
@"UICollectionView" _collectionView;
@"UICollectionViewCompositionalLayout" _layout;
@"UIFocusGuide" _horizontalIndexTitleBarFocusGuide;
@"_UIFocusFastScrollingIndexBarEntry" _selectedEntry;
@"NSIndexPath" _selectedEntryIndexPath;
@"_UIHorizontalIndexTitleBarCell" _focusedCell;
@"<_UIHorizontalIndexTitleBarDelegate>" _delegate;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _sectionInset;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _parentContentInset;
```

## Properties

```
@property (T@"UICollectionView",&,N,V_collectionView) collectionView;
@property (T@"UICollectionViewCompositionalLayout",&,N,V_layout) layout;
@property (T@"UIFocusGuide",&,N,V_horizontalIndexTitleBarFocusGuide) horizontalIndexTitleBarFocusGuide;
@property (T@"NSArray",&,N,V_entries) entries;
@property (T@"_UIFocusFastScrollingIndexBarEntry",&,N,V_selectedEntry) selectedEntry;
@property (T@"NSIndexPath",&,N,V_selectedEntryIndexPath) selectedEntryIndexPath;
@property (T@"_UIHorizontalIndexTitleBarCell",W,N,V_focusedCell) focusedCell;
@property (T@"<_UIHorizontalIndexTitleBarDelegate>",W,N,V_delegate) delegate;
@property (T{UIEdgeInsets=dddd},N,G_parentContentInset,S_setParentContentInset:,V_parentContentInset) parentContentInset;
@property (T{UIEdgeInsets=dddd},N,V_sectionInset) sectionInset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIHorizontalIndexTitleBar commonInit];
-[_UIHorizontalIndexTitleBar entries];
-[_UIHorizontalIndexTitleBar indexPathForPreferredFocusedViewInCollectionView:];
-[_UIHorizontalIndexTitleBar collectionView:numberOfItemsInSection:];
-[_UIHorizontalIndexTitleBar setEntries:];
-[_UIHorizontalIndexTitleBar init];
-[_UIHorizontalIndexTitleBar collectionView:didSelectItemAtIndexPath:];
-[_UIHorizontalIndexTitleBar didUpdateFocusInContext:withAnimationCoordinator:];
-[_UIHorizontalIndexTitleBar collectionView:cellForItemAtIndexPath:];
-[_UIHorizontalIndexTitleBar numberOfSectionsInCollectionView:];
-[_UIHorizontalIndexTitleBar collectionView];
-[_UIHorizontalIndexTitleBar setCollectionView:];
-[_UIHorizontalIndexTitleBar setDelegate:];
-[_UIHorizontalIndexTitleBar delegate];
-[_UIHorizontalIndexTitleBar preferredFocusEnvironments];
-[_UIHorizontalIndexTitleBar layout];
-[_UIHorizontalIndexTitleBar shouldUpdateFocusInContext:];
-[_UIHorizontalIndexTitleBar setLayout:];
-[_UIHorizontalIndexTitleBar setFocusedCell:];
-[_UIHorizontalIndexTitleBar _cancelDelayedFocusAction];
-[_UIHorizontalIndexTitleBar _combinedSectionInset];
-[_UIHorizontalIndexTitleBar _currentlyFocusedCell];
-[_UIHorizontalIndexTitleBar _existingCellForSelectedIndexPath];
-[_UIHorizontalIndexTitleBar _flipIfRightToLeft];
-[_UIHorizontalIndexTitleBar _isViewEntryCell:];
-[_UIHorizontalIndexTitleBar _parentContentInset];
-[_UIHorizontalIndexTitleBar _selectEntryForTitleIndex:];
-[_UIHorizontalIndexTitleBar _selectFocusedCell];
-[_UIHorizontalIndexTitleBar _sendDelayedFocusActionIfNecessary];
-[_UIHorizontalIndexTitleBar _setParentContentInset:];
-[_UIHorizontalIndexTitleBar _updateWithEntries:];
-[_UIHorizontalIndexTitleBar focusedCell];
-[_UIHorizontalIndexTitleBar horizontalIndexTitleBarFocusGuide];
-[_UIHorizontalIndexTitleBar sectionInset];
-[_UIHorizontalIndexTitleBar selectedEntry];
-[_UIHorizontalIndexTitleBar selectedEntryIndexPath];
-[_UIHorizontalIndexTitleBar setHorizontalIndexTitleBarFocusGuide:];
-[_UIHorizontalIndexTitleBar setSectionInset:];
-[_UIHorizontalIndexTitleBar setSelectedEntry:];
-[_UIHorizontalIndexTitleBar setSelectedEntryIndexPath:];
```
