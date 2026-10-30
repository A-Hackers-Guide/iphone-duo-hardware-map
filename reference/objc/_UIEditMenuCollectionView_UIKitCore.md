# `_UIEditMenuCollectionView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionView`
- 2 instance variables, 3 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _pages;
q _targetPage;
```

## Properties

```
@property (T@"NSArray",&,N,V_pages) pages;
@property (Td,R,N) currentPage;
@property (Tq,N,V_targetPage) targetPage;
```

## Instance methods

```
-[_UIEditMenuCollectionView resetTargetPage];
-[_UIEditMenuCollectionView _prepareToPageWithHorizontalVelocity:verticalVelocity:];
-[_UIEditMenuCollectionView clampedPageForPageProgress:];
-[_UIEditMenuCollectionView _contentOffsetIsAtPagingBoundary:];
-[_UIEditMenuCollectionView scrollToTargetPageAnimated:];
-[_UIEditMenuCollectionView setTargetPage:];
-[_UIEditMenuCollectionView contentOffsetForPage:];
-[_UIEditMenuCollectionView currentPage];
-[_UIEditMenuCollectionView pageProgressForContentOffset:clamped:];
-[_UIEditMenuCollectionView decrementTargetPage];
-[_UIEditMenuCollectionView setPages:];
-[_UIEditMenuCollectionView targetPage];
-[_UIEditMenuCollectionView incrementTargetPage];
-[_UIEditMenuCollectionView pages];
-[_UIEditMenuCollectionView viewWidthForPageProgress:];
```
