# `_UICollectionLayoutContainer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCollectionLayoutContainer`
- 6 instance variables, 9 properties, 9 instance methods, 0 class methods

## Instance variables

```
{?="adaptedToRegion"b1} _containerFlags;
@"_UIContentInsetsEnvironment" _insetsEnvironment;
@? _boundaryRegionProvider;
{CGSize="width"d"height"d} _contentSize;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _boundaryRegion;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _contentInsets;
```

## Properties

```
@property (T{CGSize=dd},N,V_contentSize) contentSize;
@property (T{NSDirectionalEdgeInsets=dddd},N,V_contentInsets) contentInsets;
@property (T@"_UIContentInsetsEnvironment",&,N,V_insetsEnvironment) insetsEnvironment;
@property (T{CGSize=dd},R,N) effectiveContentSize;
@property (T{NSDirectionalEdgeInsets=dddd},R,N) effectiveContentInsets;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UICollectionLayoutContainer effectiveContentSize];
-[_UICollectionLayoutContainer effectiveContentInsets];
-[_UICollectionLayoutContainer setContentInsets:];
-[_UICollectionLayoutContainer contentSize];
-[_UICollectionLayoutContainer setInsetsEnvironment:];
-[_UICollectionLayoutContainer contentInsets];
-[_UICollectionLayoutContainer setContentSize:];
-[_UICollectionLayoutContainer description];
-[_UICollectionLayoutContainer isEqual:];
```
