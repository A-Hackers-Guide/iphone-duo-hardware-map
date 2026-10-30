# `UICollectionViewFocusUpdateContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIFocusUpdateContext`
- 5 instance variables, 3 properties, 4 instance methods, 2 class methods

## Instance variables

```
B _didSetPreviouslyFocusedIndexPath;
B _didSetNextFocusedIndexPath;
@"NSIndexPath" _previouslyFocusedIndexPath;
@"NSIndexPath" _nextFocusedIndexPath;
@"UICollectionView" _collectionView;
```

## Properties

```
@property (T@"UICollectionView",R,W,N,V_collectionView) collectionView;
@property (T@"NSIndexPath",R,N,V_previouslyFocusedIndexPath) previouslyFocusedIndexPath;
@property (T@"NSIndexPath",R,N,V_nextFocusedIndexPath) nextFocusedIndexPath;
```

## Class methods

```
+[UICollectionViewFocusUpdateContext _contextWithContext:collectionView:];
+[UICollectionViewFocusUpdateContext _contextWithContext:collectionView:cachedPreviouslyFocusedIndexPath:];
```

## Instance methods

```
-[UICollectionViewFocusUpdateContext collectionView];
-[UICollectionViewFocusUpdateContext _initWithContext:collectionView:cachedPreviouslyFocusedIndexPath:];
-[UICollectionViewFocusUpdateContext nextFocusedIndexPath];
-[UICollectionViewFocusUpdateContext previouslyFocusedIndexPath];
```
