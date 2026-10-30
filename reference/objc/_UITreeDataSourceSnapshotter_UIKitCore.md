# `_UITreeDataSourceSnapshotter`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UITreeDataSourceSnapshotter`, `NSCopying`
- 3 instance variables, 1 properties, 55 instance methods, 0 class methods

## Instance variables

```
{vector<_UIOutlineNode, std::allocator<_UIOutlineNode>>="__begin_"^{_UIOutlineNode}"__end_"^{_UIOutlineNode}""{?="__cap_"^{_UIOutlineNode}}} _nodes;
q _count;
@"NSMutableIndexSet" _expandedIndexes;
```

## Properties

```
@property (Tq,N,V_count) count;
```

## Instance methods

```
-[_UITreeDataSourceSnapshotter childrenForParentAtIndex:];
-[_UITreeDataSourceSnapshotter rootIndexes];
-[_UITreeDataSourceSnapshotter _insertCount:beforeIndex:];
-[_UITreeDataSourceSnapshotter collapseIndexes:];
-[_UITreeDataSourceSnapshotter _nodeIndexForGlobalIndex:];
-[_UITreeDataSourceSnapshotter insertCount:afterIndex:];
-[_UITreeDataSourceSnapshotter setCount:];
-[_UITreeDataSourceSnapshotter snapshotterRepresentingSubtreeForIndex:includingParent:];
-[_UITreeDataSourceSnapshotter _indexForInsertingAfterIndex:];
-[_UITreeDataSourceSnapshotter _allIndexes];
-[_UITreeDataSourceSnapshotter _deleteChildNodesForParentNodeIndex:];
-[_UITreeDataSourceSnapshotter init];
-[_UITreeDataSourceSnapshotter appendChildItemsWithCount:toParentIndex:];
-[_UITreeDataSourceSnapshotter _binarySearchForGlobalIndex:startIndex:endIndex:];
-[_UITreeDataSourceSnapshotter count];
-[_UITreeDataSourceSnapshotter visibleIndexes];
-[_UITreeDataSourceSnapshotter indexIsVisible:];
-[_UITreeDataSourceSnapshotter initWithNodes:count:expandedIndexes:];
-[_UITreeDataSourceSnapshotter hasChildrenForParentAtIndex:];
-[_UITreeDataSourceSnapshotter visualDescription];
-[_UITreeDataSourceSnapshotter snapshotterRepresentingSubtreeForIndex:];
-[_UITreeDataSourceSnapshotter deleteIndexes:];
-[_UITreeDataSourceSnapshotter expandedIndexes];
-[_UITreeDataSourceSnapshotter deleteIndexes:orphanDisposition:];
-[_UITreeDataSourceSnapshotter indexIsExpanded:];
-[_UITreeDataSourceSnapshotter _insertSubtreeFromSnapshotter:atIndex:adjustedIndex:];
-[_UITreeDataSourceSnapshotter levelForIndex:];
-[_UITreeDataSourceSnapshotter _recomputeRangeOffsetForGlobalIndex:];
-[_UITreeDataSourceSnapshotter parentForChildAtIndex:];
-[_UITreeDataSourceSnapshotter replaceChildItemsFromSnapshotter:forParentIndex:];
-[_UITreeDataSourceSnapshotter _shouldSplitNodeAtInsertionIndex:];
-[_UITreeDataSourceSnapshotter insertSubtreeFromSnapshotter:beforeIndex:];
-[_UITreeDataSourceSnapshotter insertCount:beforeIndex:];
-[_UITreeDataSourceSnapshotter _snapshotterByNormalizingRangeOffsets];
-[_UITreeDataSourceSnapshotter _recomputeExpandedIndexesForInsertedRange:];
-[_UITreeDataSourceSnapshotter childrenForParentAtIndex:recursive:];
-[_UITreeDataSourceSnapshotter description];
-[_UITreeDataSourceSnapshotter expandIndexes:];
-[_UITreeDataSourceSnapshotter _childrenForParent:];
-[_UITreeDataSourceSnapshotter _splitNodeAtInsertionIndex:];
-[_UITreeDataSourceSnapshotter indexesForLevel:];
-[_UITreeDataSourceSnapshotter _snapshotterByShiftingIndexesByCount:];
-[_UITreeDataSourceSnapshotter _nextNodeForNodeIndex:];
-[_UITreeDataSourceSnapshotter _parentNodeIndexForNodeIndex:];
-[_UITreeDataSourceSnapshotter appendChildItemsWithCount:];
-[_UITreeDataSourceSnapshotter _nodeForGlobalIndex:];
-[_UITreeDataSourceSnapshotter copyWithZone:];
-[_UITreeDataSourceSnapshotter _childNodeIndexForGloalIndex:];
-[_UITreeDataSourceSnapshotter isEqual:];
-[_UITreeDataSourceSnapshotter _insertCount:afterIndex:];
-[_UITreeDataSourceSnapshotter insertSubtreeFromSnapshotter:afterIndex:];
-[_UITreeDataSourceSnapshotter _isNodeIndexVisible:];
-[_UITreeDataSourceSnapshotter isFlat];
-[_UITreeDataSourceSnapshotter insertCount:afterIndex:insertionMode:];
-[_UITreeDataSourceSnapshotter _recomputeExpandedIndexesForDeletedIndexes:];
```
