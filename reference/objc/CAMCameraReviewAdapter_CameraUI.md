# `CAMCameraReviewAdapter`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMCameraCaptureDelegate`
- 2 instance variables, 7 properties, 8 instance methods, 4 class methods

## Instance variables

```
@"NSMutableArray" __pendingAssetsForReview;
@"UIViewController<CAMCameraReviewViewController>" _cachedReviewViewController;
```

## Properties

```
@property (T@"NSMutableArray",R,N,V__pendingAssetsForReview) _pendingAssetsForReview;
@property (T@"UIViewController<CAMCameraReviewViewController>",&,N,G_cachedReviewViewController,S_setCachedReviewViewController:,V_cachedReviewViewController) cachedReviewViewController;
@property (T@"UIViewController<CAMCameraReviewViewController>",R,N) cameraReviewViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMCameraReviewAdapter cameraReviewViewControllerClass];
+[CAMCameraReviewAdapter reviewAssetForAVAsset:audioMix:properties:];
+[CAMCameraReviewAdapter reviewAssetForLivePhoto:withProperties:];
+[CAMCameraReviewAdapter reviewAssetForPhoto:withProperties:];
```

## Instance methods

```
-[CAMCameraReviewAdapter init];
-[CAMCameraReviewAdapter _setCachedReviewViewController:];
-[CAMCameraReviewAdapter _cachedReviewViewController];
-[CAMCameraReviewAdapter _pendingAssetsForReview];
-[CAMCameraReviewAdapter cameraReviewViewController];
-[CAMCameraReviewAdapter cameraViewController:didCaptureAVAsset:andAudioMix:withProperties:error:];
-[CAMCameraReviewAdapter cameraViewController:didCaptureLivePhoto:withProperties:error:];
-[CAMCameraReviewAdapter cameraViewController:didCapturePhoto:withProperties:error:];
```
