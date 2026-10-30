# `UICollectionViewLayoutAttributes`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `UIDynamicItem`
- 19 instance variables, 18 properties, 32 instance methods, 3 class methods

## Instance variables

```
@"NSString" _elementKind;
@"NSIndexPath" _indexPath;
@"NSString" _reuseIdentifier;
{CGPoint="x"d"y"d} _center;
{CGSize="width"d"height"d} _size;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
d _alpha;
q _zPosition;
{CATransform3D="m11"d"m12"d"m13"d"m14"d"m21"d"m22"d"m23"d"m24"d"m31"d"m32"d"m33"d"m34"d"m41"d"m42"d"m43"d"m44"d} _transform;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _maskViewFrame;
@ _preferredSizingData;
@"_UICollectionLayoutListAttributes" _listAttributes;
{?="isCellKind"b1"isDecorationView"b1"isHidden"b1"isClone"b1"masksToBounds"b1"maskedCorners"b4"hasDefaultLayoutMargins"b1"removeMaskViewAfterAnimation"b1"pinningAlignment"b4"pinnedToVisibleBounds"b1"hasCustomAttributes"b1} _layoutFlags;
B _hasMaskViewFrame;
q _zIndex;
Q _selectionGrouping;
d _visibleRectDisplacement;
d _cornerRadius;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _defaultLayoutMargins;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) frame;
@property (T{CGPoint=dd},N,V_center) center;
@property (T{CGSize=dd},N,V_size) size;
@property (T{CATransform3D=dddddddddddddddd},N,V_transform) transform3D;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N) bounds;
@property (T{CGAffineTransform=dddddd},N) transform;
@property (Td,N,V_alpha) alpha;
@property (Tq,N,V_zIndex) zIndex;
@property (TB,N,GisHidden) hidden;
@property (T@"NSIndexPath",&,N,V_indexPath) indexPath;
@property (TQ,R,N) representedElementCategory;
@property (T@"NSString",R,N) representedElementKind;
@property (TQ,?,R,N) collisionBoundsType;
@property (T@"UIBezierPath",?,R,N) collisionBoundingPath;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UICollectionViewLayoutAttributes layoutAttributesForCellWithIndexPath:];
+[UICollectionViewLayoutAttributes layoutAttributesForDecorationViewOfKind:withIndexPath:];
+[UICollectionViewLayoutAttributes layoutAttributesForSupplementaryViewOfKind:withIndexPath:];
```

## Instance methods

```
-[UICollectionViewLayoutAttributes indexPath];
-[UICollectionViewLayoutAttributes setHidden:];
-[UICollectionViewLayoutAttributes init];
-[UICollectionViewLayoutAttributes zIndex];
-[UICollectionViewLayoutAttributes setZIndex:];
-[UICollectionViewLayoutAttributes setCenter:];
-[UICollectionViewLayoutAttributes setTransform:];
-[UICollectionViewLayoutAttributes transform];
-[UICollectionViewLayoutAttributes setBounds:];
-[UICollectionViewLayoutAttributes size];
-[UICollectionViewLayoutAttributes isHidden];
-[UICollectionViewLayoutAttributes setAlpha:];
-[UICollectionViewLayoutAttributes setIndexPath:];
-[UICollectionViewLayoutAttributes center];
-[UICollectionViewLayoutAttributes setFrame:];
-[UICollectionViewLayoutAttributes hash];
-[UICollectionViewLayoutAttributes bounds];
-[UICollectionViewLayoutAttributes description];
-[UICollectionViewLayoutAttributes alpha];
-[UICollectionViewLayoutAttributes copyWithZone:];
-[UICollectionViewLayoutAttributes isEqual:];
-[UICollectionViewLayoutAttributes setSize:];
-[UICollectionViewLayoutAttributes frame];
-[UICollectionViewLayoutAttributes setTransform3D:];
-[UICollectionViewLayoutAttributes _listLayoutItemMaxWidth];
-[UICollectionViewLayoutAttributes _setZPosition:];
-[UICollectionViewLayoutAttributes _zPosition];
-[UICollectionViewLayoutAttributes initialLayoutAttributesForInsertedDecorationElementOfKind:atIndexPath:];
-[UICollectionViewLayoutAttributes isSizeEqualForPreferredFittingAttributes:];
-[UICollectionViewLayoutAttributes representedElementCategory];
-[UICollectionViewLayoutAttributes representedElementKind];
-[UICollectionViewLayoutAttributes transform3D];
```
