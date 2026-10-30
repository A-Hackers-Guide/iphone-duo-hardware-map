# `_UICollectionViewCompositionLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewLayout`
- 1 instance variables, 1 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _sublayoutsDict;
```

## Properties

```
@property (T@"NSArray",R,N) sublayouts;
```

## Class methods

```
+[_UICollectionViewCompositionLayout invalidationContextClass];
```

## Instance methods

```
-[_UICollectionViewCompositionLayout layoutAttributesForSupplementaryViewOfKind:atIndexPath:];
-[_UICollectionViewCompositionLayout init];
-[_UICollectionViewCompositionLayout layoutAttributesForDecorationViewOfKind:atIndexPath:];
-[_UICollectionViewCompositionLayout invalidateLayoutWithContext:];
-[_UICollectionViewCompositionLayout invalidationContextForBoundsChange:];
-[_UICollectionViewCompositionLayout collectionViewContentSize];
-[_UICollectionViewCompositionLayout prepareLayout];
-[_UICollectionViewCompositionLayout layoutAttributesForItemAtIndexPath:];
-[_UICollectionViewCompositionLayout layoutAttributesForElementsInRect:];
-[_UICollectionViewCompositionLayout _prepareLayout:];
-[_UICollectionViewCompositionLayout _frameForLayout:offset:relativeToEdges:fromSiblingLayout:];
-[_UICollectionViewCompositionLayout _originConvertedSublayoutAttributesForAttributes:inLayout:];
-[_UICollectionViewCompositionLayout addSublayout:forElementKinds:];
-[_UICollectionViewCompositionLayout addSublayout:forItems:inSection:offset:relativeToEdges:fromSiblingLayout:];
-[_UICollectionViewCompositionLayout addSublayout:forRect:];
-[_UICollectionViewCompositionLayout addSublayout:forSections:offset:relativeToEdges:fromSiblingLayout:];
-[_UICollectionViewCompositionLayout invalidationContextForPreferredLayoutAttributes:withOriginalAttributes:];
-[_UICollectionViewCompositionLayout removeSublayout:];
-[_UICollectionViewCompositionLayout shouldInvalidateLayoutForPreferredLayoutAttributes:withOriginalAttributes:];
-[_UICollectionViewCompositionLayout sublayouts];
```
