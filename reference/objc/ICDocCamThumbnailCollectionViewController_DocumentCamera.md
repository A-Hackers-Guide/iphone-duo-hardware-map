# `ICDocCamThumbnailCollectionViewController`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UICollectionViewController`
- Protocols: `UICollectionViewDataSource`, `UICollectionViewDelegate`, `ICDocCamThumbnailViewLayoutDelegate`
- 7 instance variables, 11 properties, 37 instance methods, 0 class methods

## Instance variables

```
B _isPerformingBatchUpdates;
B _needReloadAfterBatchUpdates;
@"NSMutableArray" _documentInfoArray;
@"ICDocCamImageCache" _imageCache;
@"ICDocCamUserInterfaceLayoutContext" _userInterfaceLayoutContext;
@"<ICDocCamThumbnailViewDelegate>" _delegate;
@"ICDocCamThumbnailCollectionViewLayout" _layout;
```

## Properties

```
@property (T@"ICDocCamUserInterfaceLayoutContext",N,V_userInterfaceLayoutContext) userInterfaceLayoutContext;
@property (T@"<ICDocCamThumbnailViewDelegate>",W,N,V_delegate) delegate;
@property (T@"ICDocCamThumbnailCollectionViewLayout",&,N,V_layout) layout;
@property (TB,N,V_isPerformingBatchUpdates) isPerformingBatchUpdates;
@property (TB,N,V_needReloadAfterBatchUpdates) needReloadAfterBatchUpdates;
@property (T@"NSMutableArray",&,N,V_documentInfoArray) documentInfoArray;
@property (T@"ICDocCamImageCache",&,N,V_imageCache) imageCache;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ICDocCamThumbnailCollectionViewController setImageCache:];
-[ICDocCamThumbnailCollectionViewController collectionView:didEndDisplayingCell:forItemAtIndexPath:];
-[ICDocCamThumbnailCollectionViewController rootView];
-[ICDocCamThumbnailCollectionViewController collectionView:numberOfItemsInSection:];
-[ICDocCamThumbnailCollectionViewController collectionView:willDisplayCell:forItemAtIndexPath:];
-[ICDocCamThumbnailCollectionViewController update];
-[ICDocCamThumbnailCollectionViewController collectionView:didSelectItemAtIndexPath:];
-[ICDocCamThumbnailCollectionViewController supportedInterfaceOrientations];
-[ICDocCamThumbnailCollectionViewController collectionView:cellForItemAtIndexPath:];
-[ICDocCamThumbnailCollectionViewController numberOfSectionsInCollectionView:];
-[ICDocCamThumbnailCollectionViewController viewDidLoad];
-[ICDocCamThumbnailCollectionViewController shouldAutorotate];
-[ICDocCamThumbnailCollectionViewController _canShowWhileLocked];
-[ICDocCamThumbnailCollectionViewController setDelegate:];
-[ICDocCamThumbnailCollectionViewController imageCache];
-[ICDocCamThumbnailCollectionViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[ICDocCamThumbnailCollectionViewController didReceiveMemoryWarning];
-[ICDocCamThumbnailCollectionViewController delegate];
-[ICDocCamThumbnailCollectionViewController viewWillLayoutSubviews];
-[ICDocCamThumbnailCollectionViewController layout];
-[ICDocCamThumbnailCollectionViewController isPerformingBatchUpdates];
-[ICDocCamThumbnailCollectionViewController setLayout:];
-[ICDocCamThumbnailCollectionViewController _updatePreferredContentSizeIfNeeded];
-[ICDocCamThumbnailCollectionViewController setNeedReloadAfterBatchUpdates:];
-[ICDocCamThumbnailCollectionViewController addNewDocument:completionBlock:];
-[ICDocCamThumbnailCollectionViewController animateLayoutChange];
-[ICDocCamThumbnailCollectionViewController collectionView:imageSizeAtIndex:];
-[ICDocCamThumbnailCollectionViewController documentInfoArray];
-[ICDocCamThumbnailCollectionViewController initWithUserInterfaceLayoutContext:delegate:];
-[ICDocCamThumbnailCollectionViewController needReloadAfterBatchUpdates];
-[ICDocCamThumbnailCollectionViewController reloadDataForCollectionView];
-[ICDocCamThumbnailCollectionViewController setDocumentInfoArray:];
-[ICDocCamThumbnailCollectionViewController setImageWithUUID:forCell:useResizedImage:];
-[ICDocCamThumbnailCollectionViewController setIsPerformingBatchUpdates:];
-[ICDocCamThumbnailCollectionViewController setUserInterfaceLayoutContext:];
-[ICDocCamThumbnailCollectionViewController targetViewRect];
-[ICDocCamThumbnailCollectionViewController userInterfaceLayoutContext];
```
