# `UICollectionViewDiffableDataSourceReorderingHandlers`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
@? _canReorderItemHandler;
@? _willReorderHandler;
@? _didReorderHandler;
```

## Properties

```
@property (T@?,C,N,V_canReorderItemHandler) canReorderItemHandler;
@property (T@?,C,N,V_willReorderHandler) willReorderHandler;
@property (T@?,C,N,V_didReorderHandler) didReorderHandler;
```

## Instance methods

```
-[UICollectionViewDiffableDataSourceReorderingHandlers initWithCanReorderItemHandler:willReorderItemHandler:didReorderItemHandler:];
-[UICollectionViewDiffableDataSourceReorderingHandlers setWillReorderHandler:];
-[UICollectionViewDiffableDataSourceReorderingHandlers setDidReorderHandler:];
-[UICollectionViewDiffableDataSourceReorderingHandlers canReorderItemHandler];
-[UICollectionViewDiffableDataSourceReorderingHandlers willReorderHandler];
-[UICollectionViewDiffableDataSourceReorderingHandlers didReorderHandler];
-[UICollectionViewDiffableDataSourceReorderingHandlers setCanReorderItemHandler:];
-[UICollectionViewDiffableDataSourceReorderingHandlers copyWithZone:];
```
