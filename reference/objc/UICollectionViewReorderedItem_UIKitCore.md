# `UICollectionViewReorderedItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"UICollectionViewCell" _cell;
@"NSIndexPath" _originalIndexPath;
@"NSIndexPath" _targetIndexPath;
B _isUncommitted;
@"NSIndexPath" _lastCommittedIndexPath;
```

## Properties

```
@property (T@"UICollectionViewCell",R,N,V_cell) cell;
@property (T@"NSIndexPath",&,N,V_originalIndexPath) originalIndexPath;
@property (T@"NSIndexPath",&,N,V_targetIndexPath) targetIndexPath;
@property (T@"NSIndexPath",R,N,V_lastCommittedIndexPath) lastCommittedIndexPath;
@property (TB,R,N,V_isUncommitted) isUncommitted;
```

## Instance methods

```
-[UICollectionViewReorderedItem description];
-[UICollectionViewReorderedItem targetIndexPath];
-[UICollectionViewReorderedItem cell];
-[UICollectionViewReorderedItem commitTargetIndexPath];
-[UICollectionViewReorderedItem expectedCellIndexPath];
-[UICollectionViewReorderedItem initWithCell:indexPath:];
-[UICollectionViewReorderedItem isNOOP];
-[UICollectionViewReorderedItem isUncommitted];
-[UICollectionViewReorderedItem lastCommittedIndexPath];
-[UICollectionViewReorderedItem originalIndexPath];
-[UICollectionViewReorderedItem setOriginalIndexPath:];
-[UICollectionViewReorderedItem setTargetIndexPath:];
```
