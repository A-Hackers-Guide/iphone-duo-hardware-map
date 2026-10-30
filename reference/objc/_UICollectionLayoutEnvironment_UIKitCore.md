# `_UICollectionLayoutEnvironment`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCollectionLayoutEnvironment_Private`
- 5 instance variables, 9 properties, 12 instance methods, 0 class methods

## Instance variables

```
B __wantsCollapsedTopSpacing;
@"_UICollectionLayoutContainer" _container;
@"UITraitCollection" _traitCollection;
@"<_UIDataSourceSnapshotTranslating>" __dataSourceSnapshot;
q __sectionIndex;
```

## Properties

```
@property (T@"_UICollectionLayoutContainer",&,N,V_container) container;
@property (T@"UITraitCollection",&,N,V_traitCollection) traitCollection;
@property (T@"<_UIDataSourceSnapshotTranslating>",&,N,V__dataSourceSnapshot) _dataSourceSnapshot;
@property (Tq,N,V__sectionIndex) _sectionIndex;
@property (TB,N,V__wantsCollapsedTopSpacing) _wantsCollapsedTopSpacing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UICollectionLayoutEnvironment setTraitCollection:];
-[_UICollectionLayoutEnvironment traitCollection];
-[_UICollectionLayoutEnvironment set_dataSourceSnapshot:];
-[_UICollectionLayoutEnvironment initWithContainer:traitCollection:dataSourceSnapshot:sectionIndex:wantsCollapsedTopSpacing:];
-[_UICollectionLayoutEnvironment _sectionIndex];
-[_UICollectionLayoutEnvironment set_wantsCollapsedTopSpacing:];
-[_UICollectionLayoutEnvironment setContainer:];
-[_UICollectionLayoutEnvironment _dataSourceSnapshot];
-[_UICollectionLayoutEnvironment initWithContainer:traitCollection:dataSourceSnapshot:];
-[_UICollectionLayoutEnvironment _wantsCollapsedTopSpacing];
-[_UICollectionLayoutEnvironment set_sectionIndex:];
-[_UICollectionLayoutEnvironment container];
```
