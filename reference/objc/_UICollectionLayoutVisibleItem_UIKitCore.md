# `_UICollectionLayoutVisibleItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCollectionLayoutVisibleItem`
- 3 instance variables, 18 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _dirty;
@"UICollectionViewLayoutAttributes" _layoutAttributes;
@"NSCollectionLayoutItem" _layoutItem;
```

## Properties

```
@property (Td,N) alpha;
@property (Tq,N) zIndex;
@property (TB,N,GisHidden) hidden;
@property (T{CGPoint=dd},N) center;
@property (T{CGAffineTransform=dddddd},N) transform;
@property (T{CATransform3D=dddddddddddddddd},N) transform3D;
@property (T@"NSString",R,N) name;
@property (T@"NSIndexPath",R,N) indexPath;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) frame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
@property (TQ,R,N) representedElementCategory;
@property (T@"NSString",R,N) representedElementKind;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,?,R,N) collisionBoundsType;
@property (T@"UIBezierPath",?,R,N) collisionBoundingPath;
```

## Instance methods

```
-[_UICollectionLayoutVisibleItem indexPath];
-[_UICollectionLayoutVisibleItem setHidden:];
-[_UICollectionLayoutVisibleItem zIndex];
-[_UICollectionLayoutVisibleItem setZIndex:];
-[_UICollectionLayoutVisibleItem setCenter:];
-[_UICollectionLayoutVisibleItem setTransform:];
-[_UICollectionLayoutVisibleItem transform];
-[_UICollectionLayoutVisibleItem isHidden];
-[_UICollectionLayoutVisibleItem setAlpha:];
-[_UICollectionLayoutVisibleItem center];
-[_UICollectionLayoutVisibleItem bounds];
-[_UICollectionLayoutVisibleItem description];
-[_UICollectionLayoutVisibleItem alpha];
-[_UICollectionLayoutVisibleItem name];
-[_UICollectionLayoutVisibleItem frame];
-[_UICollectionLayoutVisibleItem setTransform3D:];
-[_UICollectionLayoutVisibleItem representedElementCategory];
-[_UICollectionLayoutVisibleItem representedElementKind];
-[_UICollectionLayoutVisibleItem transform3D];
```
