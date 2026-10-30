# `UICollectionViewAnimation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 11 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"UICollectionReusableView" _view;
@"UICollectionViewLayoutAttributes" _finalLayoutAttributes;
d _startFraction;
d _endFraction;
q _viewType;
@"NSMutableArray" _completionHandlers;
@"NSMutableArray" _startupHandlers;
@? _animationBlock;
{?="animateFromCurrentPosition"b1"deleteAfterAnimation"b1"rasterizeAfterAnimation"b1"resetRasterizationAfterAnimation"b1"updateZIndexAfterAnimation"b1} _collectionViewAnimationFlags;
B _parentInCollectionViewDuringAnimation;
```

## Properties

```
@property (T@"UICollectionReusableView",R,N,V_view) view;
@property (Tq,R,N,V_viewType) viewType;
@property (T@"UICollectionViewLayoutAttributes",R,N,V_finalLayoutAttributes) finalLayoutAttributes;
@property (Td,R,N,V_startFraction) startFraction;
@property (Td,R,N,V_endFraction) endFraction;
@property (TB,R,N) animateFromCurrentPosition;
@property (TB,R,N) deleteAfterAnimation;
@property (TB,R,N) updateZIndexAfterAnimation;
@property (TB,N) rasterizeAfterAnimation;
@property (TB,N) resetRasterizationAfterAnimation;
@property (TB,N,V_parentInCollectionViewDuringAnimation) parentInCollectionViewDuringAnimation;
```

## Instance methods

```
-[UICollectionViewAnimation addCompletionHandler:];
-[UICollectionViewAnimation initWithView:viewType:finalLayoutAttributes:startFraction:endFraction:animateFromCurrentPostion:deleteAfterAnimation:customAnimations:];
-[UICollectionViewAnimation endFraction];
-[UICollectionViewAnimation deleteAfterAnimation];
-[UICollectionViewAnimation start];
-[UICollectionViewAnimation setParentInCollectionViewDuringAnimation:];
-[UICollectionViewAnimation animateFromCurrentPosition];
-[UICollectionViewAnimation setResetRasterizationAfterAnimation:];
-[UICollectionViewAnimation view];
-[UICollectionViewAnimation parentInCollectionViewDuringAnimation];
-[UICollectionViewAnimation setRasterizeAfterAnimation:];
-[UICollectionViewAnimation updateZIndexAfterAnimation];
-[UICollectionViewAnimation description];
-[UICollectionViewAnimation rasterizeAfterAnimation];
-[UICollectionViewAnimation startWithAnimator:];
-[UICollectionViewAnimation finalLayoutAttributes];
-[UICollectionViewAnimation addStartupHandler:];
-[UICollectionViewAnimation startFraction];
-[UICollectionViewAnimation resetRasterizationAfterAnimation];
-[UICollectionViewAnimation viewType];
```
