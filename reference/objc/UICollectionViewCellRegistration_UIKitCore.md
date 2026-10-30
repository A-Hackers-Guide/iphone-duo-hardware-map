# `UICollectionViewCellRegistration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 7 properties, 8 instance methods, 2 class methods

## Instance variables

```
# _cellClass;
@"UINib" _cellNib;
@? _configurationHandler;
@"UICollectionView" __collectionViewRequestingViewWhenCreated;
@"NSString" _reuseIdentifier;
```

## Properties

```
@property (T@"UICollectionView",R,W,N,V__collectionViewRequestingViewWhenCreated) _collectionViewRequestingViewWhenCreated;
@property (T@"NSString",R,N,V_reuseIdentifier) reuseIdentifier;
@property (TB,R,N) hasCellClass;
@property (TB,R,N) hasCellNib;
@property (T#,R,N,V_cellClass) cellClass;
@property (T@"UINib",R,N,V_cellNib) cellNib;
@property (T@?,R,N,V_configurationHandler) configurationHandler;
```

## Class methods

```
+[UICollectionViewCellRegistration registrationWithCellClass:configurationHandler:];
+[UICollectionViewCellRegistration registrationWithCellNib:configurationHandler:];
```

## Instance methods

```
-[UICollectionViewCellRegistration initWithCellClass:cellNib:configurationHandler:reuseIdentifier:];
-[UICollectionViewCellRegistration hasCellClass];
-[UICollectionViewCellRegistration hasCellNib];
-[UICollectionViewCellRegistration configurationHandler];
-[UICollectionViewCellRegistration reuseIdentifier];
-[UICollectionViewCellRegistration cellClass];
-[UICollectionViewCellRegistration _collectionViewRequestingViewWhenCreated];
-[UICollectionViewCellRegistration cellNib];
```
