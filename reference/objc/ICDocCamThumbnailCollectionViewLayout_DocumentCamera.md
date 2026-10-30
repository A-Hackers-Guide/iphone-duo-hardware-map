# `ICDocCamThumbnailCollectionViewLayout`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewLayout`
- 8 instance variables, 8 properties, 41 instance methods, 0 class methods

## Instance variables

```
B _transitioning;
B _compactLayout;
@"ICDocCamUserInterfaceLayoutContext" _userInterfaceLayoutContext;
@"<ICDocCamThumbnailViewLayoutDelegate>" _delegate;
@"NSDictionary" _layoutInfo;
@"NSMutableArray" _deleteIndexPaths;
@"NSMutableArray" _insertIndexPaths;
{CGSize="width"d"height"d} _itemSize;
```

## Properties

```
@property (T@"ICDocCamUserInterfaceLayoutContext",&,N,V_userInterfaceLayoutContext) userInterfaceLayoutContext;
@property (T@"NSDictionary",&,N,V_layoutInfo) layoutInfo;
@property (T@"NSMutableArray",&,N,V_deleteIndexPaths) deleteIndexPaths;
@property (T@"NSMutableArray",&,N,V_insertIndexPaths) insertIndexPaths;
@property (TB,N,V_compactLayout) compactLayout;
@property (T{CGSize=dd},N,V_itemSize) itemSize;
@property (T@"<ICDocCamThumbnailViewLayoutDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_transitioning) transitioning;
```

## Instance methods

```
-[ICDocCamThumbnailCollectionViewLayout setup];
-[ICDocCamThumbnailCollectionViewLayout layoutAttributesForDecorationViewOfKind:atIndexPath:];
-[ICDocCamThumbnailCollectionViewLayout shouldInvalidateLayoutForBoundsChange:];
-[ICDocCamThumbnailCollectionViewLayout collectionViewContentSize];
-[ICDocCamThumbnailCollectionViewLayout setDelegate:];
-[ICDocCamThumbnailCollectionViewLayout finalLayoutAttributesForDisappearingItemAtIndexPath:];
-[ICDocCamThumbnailCollectionViewLayout delegate];
-[ICDocCamThumbnailCollectionViewLayout prepareForCollectionViewUpdates:];
-[ICDocCamThumbnailCollectionViewLayout setTransitioning:];
-[ICDocCamThumbnailCollectionViewLayout initWithCoder:];
-[ICDocCamThumbnailCollectionViewLayout initialLayoutAttributesForAppearingItemAtIndexPath:];
-[ICDocCamThumbnailCollectionViewLayout preferredContentSize];
-[ICDocCamThumbnailCollectionViewLayout finalizeCollectionViewUpdates];
-[ICDocCamThumbnailCollectionViewLayout transitioning];
-[ICDocCamThumbnailCollectionViewLayout prepareLayout];
-[ICDocCamThumbnailCollectionViewLayout layoutAttributesForItemAtIndexPath:];
-[ICDocCamThumbnailCollectionViewLayout layoutAttributesForElementsInRect:];
-[ICDocCamThumbnailCollectionViewLayout prepareForAnimatedBoundsChange:];
-[ICDocCamThumbnailCollectionViewLayout prepareForTransitionFromLayout:];
-[ICDocCamThumbnailCollectionViewLayout deleteIndexPaths];
-[ICDocCamThumbnailCollectionViewLayout finalLayoutAttributesForDisappearingDecorationElementOfKind:atIndexPath:];
-[ICDocCamThumbnailCollectionViewLayout finalizeAnimatedBoundsChange];
-[ICDocCamThumbnailCollectionViewLayout finalizeLayoutTransition];
-[ICDocCamThumbnailCollectionViewLayout initialLayoutAttributesForAppearingDecorationElementOfKind:atIndexPath:];
-[ICDocCamThumbnailCollectionViewLayout insertIndexPaths];
-[ICDocCamThumbnailCollectionViewLayout itemSize];
-[ICDocCamThumbnailCollectionViewLayout prepareForTransitionToLayout:];
-[ICDocCamThumbnailCollectionViewLayout setDeleteIndexPaths:];
-[ICDocCamThumbnailCollectionViewLayout setInsertIndexPaths:];
-[ICDocCamThumbnailCollectionViewLayout setItemSize:];
-[ICDocCamThumbnailCollectionViewLayout layoutInfo];
-[ICDocCamThumbnailCollectionViewLayout setLayoutInfo:];
-[ICDocCamThumbnailCollectionViewLayout prepareLayout:];
-[ICDocCamThumbnailCollectionViewLayout compactFrameForThumbnailAtIndexPath:withSize:];
-[ICDocCamThumbnailCollectionViewLayout compactLayout];
-[ICDocCamThumbnailCollectionViewLayout frameForThumbnailAtIndexPath:];
-[ICDocCamThumbnailCollectionViewLayout frameSizeForImageSize:];
-[ICDocCamThumbnailCollectionViewLayout initWithUserInterfaceLayoutContext:];
-[ICDocCamThumbnailCollectionViewLayout setCompactLayout:];
-[ICDocCamThumbnailCollectionViewLayout setUserInterfaceLayoutContext:];
-[ICDocCamThumbnailCollectionViewLayout userInterfaceLayoutContext];
```
