# `CAMReviewViewController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `PUAssetExplorerReviewScreenViewControllerDelegate`, `CAMCameraReviewViewController`
- 6 instance variables, 10 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"<CAMCameraReviewDelegate>" _reviewDelegate;
@"NSArray" __initialAssets;
@"PUReviewDataSource" __reviewDataSource;
@"PUReviewAssetsDataSourceManager" __internalReviewDataSourceManager;
@"PUReviewAssetsMediaProvider" __internalReviewMediaProvider;
@"PUAssetExplorerReviewScreenViewController" __internalReviewViewController;
```

## Properties

```
@property (T@"NSArray",R,N,V__initialAssets) _initialAssets;
@property (T@"PUReviewDataSource",R,N,V__reviewDataSource) _reviewDataSource;
@property (T@"PUReviewAssetsDataSourceManager",R,N,V__internalReviewDataSourceManager) _internalReviewDataSourceManager;
@property (T@"PUReviewAssetsMediaProvider",R,N,V__internalReviewMediaProvider) _internalReviewMediaProvider;
@property (T@"PUAssetExplorerReviewScreenViewController",R,N,V__internalReviewViewController) _internalReviewViewController;
@property (T@"<CAMCameraReviewDelegate>",W,N,V_reviewDelegate) reviewDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMReviewViewController initWithAssets:];
-[CAMReviewViewController initWithNibName:bundle:];
-[CAMReviewViewController loadView];
-[CAMReviewViewController initWithCoder:];
-[CAMReviewViewController _reviewDataSource];
-[CAMReviewViewController assetExplorerReviewScreenViewController:canPerformActionType:onAsset:inAssetCollection:];
-[CAMReviewViewController assetExplorerReviewScreenViewController:didPerformCompletionAction:withSelectedAssetUUIDs:livePhotoDisabledAssetUUIDs:substituteAssetsByUUID:];
-[CAMReviewViewController assetExplorerReviewScreenViewController:shouldEnableActionType:onAsset:inAssetCollection:];
-[CAMReviewViewController assetExplorerReviewScreenViewControllerDidPressCancel:];
-[CAMReviewViewController assetExplorerReviewScreenViewControllerDidPressRetake:];
-[CAMReviewViewController reviewDelegate];
-[CAMReviewViewController setReviewDelegate:];
-[CAMReviewViewController _initialAssets];
-[CAMReviewViewController _internalReviewDataSourceManager];
-[CAMReviewViewController _internalReviewMediaProvider];
-[CAMReviewViewController _internalReviewViewController];
```
