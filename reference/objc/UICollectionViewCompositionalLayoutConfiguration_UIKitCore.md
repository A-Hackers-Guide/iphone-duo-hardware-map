# `UICollectionViewCompositionalLayoutConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 4 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
q _scrollDirection;
d _interSectionSpacing;
@"NSArray" _boundarySupplementaryItems;
q _contentInsetsReference;
```

## Properties

```
@property (Tq,N,V_scrollDirection) scrollDirection;
@property (Td,N,V_interSectionSpacing) interSectionSpacing;
@property (T@"NSArray",C,N,V_boundarySupplementaryItems) boundarySupplementaryItems;
@property (Tq,N,V_contentInsetsReference) contentInsetsReference;
```

## Class methods

```
+[UICollectionViewCompositionalLayoutConfiguration defaultConfiguration];
```

## Instance methods

```
-[UICollectionViewCompositionalLayoutConfiguration contentInsetsReference];
-[UICollectionViewCompositionalLayoutConfiguration setInterSectionSpacing:];
-[UICollectionViewCompositionalLayoutConfiguration scrollDirection];
-[UICollectionViewCompositionalLayoutConfiguration init];
-[UICollectionViewCompositionalLayoutConfiguration boundarySupplementaryItems];
-[UICollectionViewCompositionalLayoutConfiguration setContentInsetsReference:];
-[UICollectionViewCompositionalLayoutConfiguration setScrollDirection:];
-[UICollectionViewCompositionalLayoutConfiguration initWithScrollDirection:interSectionSpacing:boundarySupplememtaryItems:contentInsetsReference:];
-[UICollectionViewCompositionalLayoutConfiguration interSectionSpacing];
-[UICollectionViewCompositionalLayoutConfiguration setBoundarySupplementaryItems:];
-[UICollectionViewCompositionalLayoutConfiguration copyWithZone:];
-[UICollectionViewCompositionalLayoutConfiguration differencesFromConfiguration:];
```
