# `CEKWheelScrubberCollectionViewLayout`

- Image: [`/System/Library/PrivateFrameworks/CameraEditKit.framework/CameraEditKit`](../userland/System__Library__PrivateFrameworks__CameraEditKit.framework__CameraEditKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewLayout`
- 7 instance variables, 7 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"<CEKWheelScrubberCollectionViewLayoutDelegate>" _wheelScrubberDelegate;
q _layoutDirection;
q _layoutOrder;
q _cellEffect;
@"NSArray" __cachedLayoutAttributesCells;
{CGSize="width"d"height"d} __cachedContentSize;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _contentInsets;
```

## Properties

```
@property (T{CGSize=dd},N,S_setCachedContentSize:,V__cachedContentSize) _cachedContentSize;
@property (T@"NSArray",&,N,S_setCachedLayoutAttributesCells:,V__cachedLayoutAttributesCells) _cachedLayoutAttributesCells;
@property (T@"<CEKWheelScrubberCollectionViewLayoutDelegate>",W,N,V_wheelScrubberDelegate) wheelScrubberDelegate;
@property (T{UIEdgeInsets=dddd},N,V_contentInsets) contentInsets;
@property (Tq,N,V_layoutDirection) layoutDirection;
@property (Tq,N,V_layoutOrder) layoutOrder;
@property (Tq,N,V_cellEffect) cellEffect;
```

## Instance methods

```
-[CEKWheelScrubberCollectionViewLayout layoutAttributesForSupplementaryViewOfKind:atIndexPath:];
-[CEKWheelScrubberCollectionViewLayout setContentInsets:];
-[CEKWheelScrubberCollectionViewLayout init];
-[CEKWheelScrubberCollectionViewLayout setLayoutOrder:];
-[CEKWheelScrubberCollectionViewLayout setLayoutDirection:];
-[CEKWheelScrubberCollectionViewLayout shouldInvalidateLayoutForBoundsChange:];
-[CEKWheelScrubberCollectionViewLayout layoutDirection];
-[CEKWheelScrubberCollectionViewLayout layoutOrder];
-[CEKWheelScrubberCollectionViewLayout collectionViewContentSize];
-[CEKWheelScrubberCollectionViewLayout contentInsets];
-[CEKWheelScrubberCollectionViewLayout prepareLayout];
-[CEKWheelScrubberCollectionViewLayout layoutAttributesForItemAtIndexPath:];
-[CEKWheelScrubberCollectionViewLayout layoutAttributesForElementsInRect:];
-[CEKWheelScrubberCollectionViewLayout setCellEffect:];
-[CEKWheelScrubberCollectionViewLayout _cachedContentSize];
-[CEKWheelScrubberCollectionViewLayout _cachedLayoutAttributesCells];
-[CEKWheelScrubberCollectionViewLayout _circularlyWrapped:forCenter:radius:scale:];
-[CEKWheelScrubberCollectionViewLayout _setCachedContentSize:];
-[CEKWheelScrubberCollectionViewLayout _setCachedLayoutAttributesCells:];
-[CEKWheelScrubberCollectionViewLayout cellEffect];
-[CEKWheelScrubberCollectionViewLayout setWheelScrubberDelegate:];
-[CEKWheelScrubberCollectionViewLayout wheelScrubberDelegate];
```
