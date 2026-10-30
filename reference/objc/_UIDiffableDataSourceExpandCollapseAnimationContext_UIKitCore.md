# `_UIDiffableDataSourceExpandCollapseAnimationContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UICollectionViewUpdateExpandCollapseAnimationContext`
- 10 instance variables, 4 properties, 4 instance methods, 0 class methods

## Instance variables

```
q _sectionIndex;
@"__UIDiffableDataSourceSnapshot" _initialSnapshot;
@"NSDiffableDataSourceSectionSnapshot" _initialSectionSnapshot;
@"NSDiffableDataSourceSectionSnapshot" _finalSectionSnapshot;
@"NSOrderedSet" _initialIdentifiers;
@"NSOrderedSet" _finalIdentifiers;
@"NSOrderedSet" _initialVisibleIdentifiers;
@"NSOrderedSet" _finalVisibleIdentifiers;
@"NSArray" _identifiersOfExpandedItems;
@"NSArray" _identifiersOfCollapsedItems;
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
-[_UIDiffableDataSourceExpandCollapseAnimationContext indexPathsForChildItemsInCollapsingParent:];
-[_UIDiffableDataSourceExpandCollapseAnimationContext indexPathsForChildItemsInExpandingParent:];
-[_UIDiffableDataSourceExpandCollapseAnimationContext indexPathsForCollapsedParentItems];
-[_UIDiffableDataSourceExpandCollapseAnimationContext indexPathsForExpandedParentItems];
```
