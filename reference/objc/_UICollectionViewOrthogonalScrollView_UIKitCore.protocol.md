# `_UICollectionViewOrthogonalScrollView` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T{CGPoint=dd},R,N) contentOffset;
@property (T{CGSize=dd},R,N) contentSize;
@property (TB,R,N,GisTracking) tracking;
@property (TB,R,N,GisDragging) dragging;
@property (TB,R,N,GisDecelerating) decelerating;
```

## Instance methods

```
-[_UICollectionViewOrthogonalScrollView contentOffset];
-[_UICollectionViewOrthogonalScrollView contentSize];
-[_UICollectionViewOrthogonalScrollView isDragging];
-[_UICollectionViewOrthogonalScrollView isTracking];
-[_UICollectionViewOrthogonalScrollView _panGestureLocationInView:];
-[_UICollectionViewOrthogonalScrollView _panGestureVelocityInView:];
-[_UICollectionViewOrthogonalScrollView isDecelerating];
```
