# `UICollectionViewSupplementaryRegistration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 8 properties, 9 instance methods, 2 class methods

## Instance variables

```
# _supplementaryClass;
@"UINib" _supplementaryNib;
@"NSString" _elementKind;
@? _configurationHandler;
@"UICollectionView" __collectionViewRequestingViewWhenCreated;
@"NSString" _reuseIdentifier;
```

## Properties

```
@property (T@"UICollectionView",R,W,N,V__collectionViewRequestingViewWhenCreated) _collectionViewRequestingViewWhenCreated;
@property (T@"NSString",R,N,V_reuseIdentifier) reuseIdentifier;
@property (TB,R,N) hasSupplementaryClass;
@property (TB,R,N) hasSupplementaryNib;
@property (T#,R,N,V_supplementaryClass) supplementaryClass;
@property (T@"UINib",R,N,V_supplementaryNib) supplementaryNib;
@property (T@"NSString",R,N,V_elementKind) elementKind;
@property (T@?,R,N,V_configurationHandler) configurationHandler;
```

## Class methods

```
+[UICollectionViewSupplementaryRegistration registrationWithSupplementaryClass:elementKind:configurationHandler:];
+[UICollectionViewSupplementaryRegistration registrationWithSupplementaryNib:elementKind:configurationHandler:];
```

## Instance methods

```
-[UICollectionViewSupplementaryRegistration supplementaryNib];
-[UICollectionViewSupplementaryRegistration hasSupplementaryClass];
-[UICollectionViewSupplementaryRegistration configurationHandler];
-[UICollectionViewSupplementaryRegistration supplementaryClass];
-[UICollectionViewSupplementaryRegistration hasSupplementaryNib];
-[UICollectionViewSupplementaryRegistration elementKind];
-[UICollectionViewSupplementaryRegistration reuseIdentifier];
-[UICollectionViewSupplementaryRegistration _collectionViewRequestingViewWhenCreated];
-[UICollectionViewSupplementaryRegistration initWithSupplementaryClass:supplementaryNib:elementKind:configurationHandler:reuseIdentifier:];
```
