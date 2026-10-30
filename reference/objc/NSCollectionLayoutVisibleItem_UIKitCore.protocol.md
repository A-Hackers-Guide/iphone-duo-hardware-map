# `NSCollectionLayoutVisibleItem` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `UIDynamicItem`
- 0 instance variables, 12 properties, 18 instance methods, 0 class methods

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
```

## Instance methods

```
-[NSCollectionLayoutVisibleItem indexPath];
-[NSCollectionLayoutVisibleItem setHidden:];
-[NSCollectionLayoutVisibleItem zIndex];
-[NSCollectionLayoutVisibleItem setZIndex:];
-[NSCollectionLayoutVisibleItem setCenter:];
-[NSCollectionLayoutVisibleItem setTransform:];
-[NSCollectionLayoutVisibleItem transform];
-[NSCollectionLayoutVisibleItem isHidden];
-[NSCollectionLayoutVisibleItem setAlpha:];
-[NSCollectionLayoutVisibleItem center];
-[NSCollectionLayoutVisibleItem bounds];
-[NSCollectionLayoutVisibleItem alpha];
-[NSCollectionLayoutVisibleItem name];
-[NSCollectionLayoutVisibleItem frame];
-[NSCollectionLayoutVisibleItem setTransform3D:];
-[NSCollectionLayoutVisibleItem representedElementCategory];
-[NSCollectionLayoutVisibleItem representedElementKind];
-[NSCollectionLayoutVisibleItem transform3D];
```
