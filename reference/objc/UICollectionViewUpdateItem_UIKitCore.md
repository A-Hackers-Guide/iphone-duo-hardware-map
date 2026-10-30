# `UICollectionViewUpdateItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `_CVCCollectionUpdateItem`
- 8 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
{_UICollectionUpdateIndexPair="section"q"item"q} _initialIndexPair;
{_UICollectionUpdateIndexPair="section"q"item"q} _finalIndexPair;
{_UICollectionUpdateIndexPair="section"q"item"q} _indexPairForAction;
{?="isAppendingSectionInsert"b1"shouldReconfigure"b1} _updateItemFlags;
@"NSIndexPath" _initialIndexPath;
@"NSIndexPath" _finalIndexPath;
q _updateAction;
@"NSUUID" _identifier;
```

## Properties

```
@property (T@"NSIndexPath",R,N,V_initialIndexPath) indexPathBeforeUpdate;
@property (T@"NSIndexPath",R,N,V_finalIndexPath) indexPathAfterUpdate;
@property (Tq,R,N,V_updateAction) updateAction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UICollectionViewUpdateItem compareIndexPathsForMoves:];
-[UICollectionViewUpdateItem indexPathBeforeUpdate];
-[UICollectionViewUpdateItem updateAction];
-[UICollectionViewUpdateItem indexPathAfterUpdate];
-[UICollectionViewUpdateItem inverseCompareIndexPaths:];
-[UICollectionViewUpdateItem initWithAction:forIndexPath:];
-[UICollectionViewUpdateItem description];
-[UICollectionViewUpdateItem compareIndexPaths:];
-[UICollectionViewUpdateItem copyWithZone:];
-[UICollectionViewUpdateItem isEqual:];
-[UICollectionViewUpdateItem initWithInitialIndexPath:finalIndexPath:updateAction:];
```
