# `_UICollectionViewListCellReorderControl`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIControl`
- Protocols: `UIGestureRecognizerDelegate`
- 7 instance variables, 7 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"UIImageView" _imageView;
@"UILongPressGestureRecognizer" _reorderRecognizer;
B _tracking;
B _needsImageViewUpdate;
@"<_UICollectionViewListCellReorderControlDelegate>" _delegate;
@"<UITableConstants>" _constants;
@"UIColor" _accessoryTintColor;
```

## Properties

```
@property (T@"<_UICollectionViewListCellReorderControlDelegate>",W,N,V_delegate) delegate;
@property (T@"<UITableConstants>",&,N,V_constants) constants;
@property (T@"UIColor",&,N,V_accessoryTintColor) accessoryTintColor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UICollectionViewListCellReorderControl setConstants:];
-[_UICollectionViewListCellReorderControl gestureRecognizer:shouldReceiveTouch:];
-[_UICollectionViewListCellReorderControl _minimumSizeForHitTesting];
-[_UICollectionViewListCellReorderControl layoutSubviews];
-[_UICollectionViewListCellReorderControl touchesBegan:withEvent:];
-[_UICollectionViewListCellReorderControl sizeThatFits:];
-[_UICollectionViewListCellReorderControl setDelegate:];
-[_UICollectionViewListCellReorderControl gestureRecognizerShouldBegin:];
-[_UICollectionViewListCellReorderControl _updateImageViewIfNeeded];
-[_UICollectionViewListCellReorderControl delegate];
-[_UICollectionViewListCellReorderControl _setNeedsImageViewUpdate];
-[_UICollectionViewListCellReorderControl accessoryTintColor];
-[_UICollectionViewListCellReorderControl setAccessoryTintColor:];
-[_UICollectionViewListCellReorderControl constants];
-[_UICollectionViewListCellReorderControl beginReordering];
-[_UICollectionViewListCellReorderControl _setTracking:];
-[_UICollectionViewListCellReorderControl cancelReorderingGesture];
-[_UICollectionViewListCellReorderControl endReordering:];
-[_UICollectionViewListCellReorderControl gestureMovedToPoint:];
-[_UICollectionViewListCellReorderControl initWithDelegate:constants:];
-[_UICollectionViewListCellReorderControl pan:];
```
