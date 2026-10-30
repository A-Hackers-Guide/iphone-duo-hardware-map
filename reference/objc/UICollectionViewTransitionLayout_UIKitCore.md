# `UICollectionViewTransitionLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewLayout`
- 13 instance variables, 3 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"UICollectionViewLayout" _fromLayout;
@"UICollectionViewLayout" _toLayout;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _fromVisibleBounds;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _toVisibleBounds;
{CGSize="width"d"height"d} _contentSize;
B _haveValidInfos;
d _transitionProgress;
@"NSMutableDictionary" _transitionInformationsDict;
@"NSMutableDictionary" _currentLayoutInfos;
B _layoutIsValid;
@"NSMutableArray" _disappearingLayoutAttributes;
@"NSMutableArray" _appearingLayoutAttributes;
d _accuracy;
```

## Properties

```
@property (Td,N,V_transitionProgress) transitionProgress;
@property (T@"UICollectionViewLayout",R,N,V_fromLayout) currentLayout;
@property (T@"UICollectionViewLayout",R,N,V_toLayout) nextLayout;
```

## Instance methods

```
-[UICollectionViewTransitionLayout layoutAttributesForSupplementaryViewOfKind:atIndexPath:];
-[UICollectionViewTransitionLayout targetContentOffsetForProposedContentOffset:];
-[UICollectionViewTransitionLayout init];
-[UICollectionViewTransitionLayout layoutAttributesForDecorationViewOfKind:atIndexPath:];
-[UICollectionViewTransitionLayout currentLayout];
-[UICollectionViewTransitionLayout collectionViewContentSize];
-[UICollectionViewTransitionLayout transitionProgress];
-[UICollectionViewTransitionLayout initWithCoder:];
-[UICollectionViewTransitionLayout _supportsAdvancedTransitionAnimations];
-[UICollectionViewTransitionLayout invalidateLayout];
-[UICollectionViewTransitionLayout prepareLayout];
-[UICollectionViewTransitionLayout layoutAttributesForItemAtIndexPath:];
-[UICollectionViewTransitionLayout layoutAttributesForElementsInRect:];
-[UICollectionViewTransitionLayout setTransitionProgress:];
-[UICollectionViewTransitionLayout _finalizeLayoutTransition];
-[UICollectionViewTransitionLayout _newVisibleBounds];
-[UICollectionViewTransitionLayout _oldVisibleBounds];
-[UICollectionViewTransitionLayout _prepareForTransitionFromLayout:];
-[UICollectionViewTransitionLayout _prepareForTransitionToLayout:];
-[UICollectionViewTransitionLayout _setCollectionView:];
-[UICollectionViewTransitionLayout initWithCurrentLayout:nextLayout:];
-[UICollectionViewTransitionLayout interpolatedLayoutAttributesFromLayoutAttributes:toLayoutAttributes:progress:];
-[UICollectionViewTransitionLayout nextLayout];
-[UICollectionViewTransitionLayout updateValue:forAnimatedKey:];
-[UICollectionViewTransitionLayout valueForAnimatedKey:];
```
