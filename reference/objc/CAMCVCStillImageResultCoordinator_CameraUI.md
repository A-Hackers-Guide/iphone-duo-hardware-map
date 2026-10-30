# `CAMCVCStillImageResultCoordinator`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 17 properties, 30 instance methods, 0 class methods

## Instance variables

```
B _expectingPairedVideo;
B _allowMultipleCaptures;
B _shouldReturnFilteredPhotosAsSingleAsset;
B __didReceiveForceRemainingDispatchesIfPossible;
@"<CAMCVCStillImageResultCoordinatorDelegate>" _delegate;
@"NSString" _identifier;
@"NSSet" _allExpectedResultSpecifiers;
@"NSMutableSet" __receivedPhotos;
@"NSMutableSet" __receivedVideos;
@"NSMutableSet" __photoResultSpecifiersDelayingForcedDispatch;
@"NSMutableSet" __videoResultSpecifiersDelayingForcedDispatch;
@"NSMutableSet" __handledResultSpecifiers;
@"NSMutableSet" __dispatchedResultSpecifiers;
@"NSMutableDictionary" __pendingPhotoProperties;
@"NSMutableDictionary" __pendingVideoProperties;
@"NSMutableDictionary" __pendingAssetAdjustments;
```

## Properties

```
@property (T@"NSMutableSet",R,N,V__receivedPhotos) _receivedPhotos;
@property (T@"NSMutableSet",R,N,V__receivedVideos) _receivedVideos;
@property (T@"NSMutableSet",R,N,V__photoResultSpecifiersDelayingForcedDispatch) _photoResultSpecifiersDelayingForcedDispatch;
@property (T@"NSMutableSet",R,N,V__videoResultSpecifiersDelayingForcedDispatch) _videoResultSpecifiersDelayingForcedDispatch;
@property (TB,R,N,G_isDelayingForcedDispatch) _delayingForcedDispatch;
@property (TB,N,S_setDidReceiveForceRemainingDispatchesIfPossible:,V__didReceiveForceRemainingDispatchesIfPossible) _didReceiveForceRemainingDispatchesIfPossible;
@property (T@"NSMutableSet",R,N,V__handledResultSpecifiers) _handledResultSpecifiers;
@property (T@"NSMutableSet",R,N,V__dispatchedResultSpecifiers) _dispatchedResultSpecifiers;
@property (T@"NSMutableDictionary",R,N,V__pendingPhotoProperties) _pendingPhotoProperties;
@property (T@"NSMutableDictionary",R,N,V__pendingVideoProperties) _pendingVideoProperties;
@property (T@"NSMutableDictionary",R,N,V__pendingAssetAdjustments) _pendingAssetAdjustments;
@property (T@"<CAMCVCStillImageResultCoordinatorDelegate>",R,W,N,V_delegate) delegate;
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"NSSet",R,N,V_allExpectedResultSpecifiers) allExpectedResultSpecifiers;
@property (TB,R,N,GisExpectingPairedVideo,V_expectingPairedVideo) expectingPairedVideo;
@property (TB,R,N,V_allowMultipleCaptures) allowMultipleCaptures;
@property (TB,R,N,V_shouldReturnFilteredPhotosAsSingleAsset) shouldReturnFilteredPhotosAsSingleAsset;
```

## Instance methods

```
-[CAMCVCStillImageResultCoordinator isExpectingPairedVideo];
-[CAMCVCStillImageResultCoordinator identifier];
-[CAMCVCStillImageResultCoordinator delegate];
-[CAMCVCStillImageResultCoordinator allExpectedResultSpecifiers];
-[CAMCVCStillImageResultCoordinator _receivedPhotos];
-[CAMCVCStillImageResultCoordinator _receivedVideos];
-[CAMCVCStillImageResultCoordinator _attemptDispatchForPairWithFilteredResultSpecifiers:unfilteredResultSpecifiers:forceRemainingDispatches:];
-[CAMCVCStillImageResultCoordinator _attemptDispatchForResultSpecifiers:forceRemainingDispatches:];
-[CAMCVCStillImageResultCoordinator _didReceiveForceRemainingDispatchesIfPossible];
-[CAMCVCStillImageResultCoordinator _dispatchPendingPropertiesForced:];
-[CAMCVCStillImageResultCoordinator _dispatchedResultSpecifiers];
-[CAMCVCStillImageResultCoordinator _errorForResultSpecifiers:allowMissingVideo:];
-[CAMCVCStillImageResultCoordinator _errorWithDescription:code:];
-[CAMCVCStillImageResultCoordinator _handledResultSpecifiers];
-[CAMCVCStillImageResultCoordinator _isDelayingForcedDispatch];
-[CAMCVCStillImageResultCoordinator _isWaitingOnResultSpecifiers:];
-[CAMCVCStillImageResultCoordinator _pendingAssetAdjustments];
-[CAMCVCStillImageResultCoordinator _pendingPhotoProperties];
-[CAMCVCStillImageResultCoordinator _pendingVideoProperties];
-[CAMCVCStillImageResultCoordinator _photoResultSpecifiersDelayingForcedDispatch];
-[CAMCVCStillImageResultCoordinator _setDidReceiveForceRemainingDispatchesIfPossible:];
-[CAMCVCStillImageResultCoordinator _videoResultSpecifiersDelayingForcedDispatch];
-[CAMCVCStillImageResultCoordinator allowMultipleCaptures];
-[CAMCVCStillImageResultCoordinator delayForcedDispatchForPhotoResultSpecifiers:];
-[CAMCVCStillImageResultCoordinator delayForcedDispatchForVideoResultSpecifiers:];
-[CAMCVCStillImageResultCoordinator forceRemainingDispatchesIfPossible];
-[CAMCVCStillImageResultCoordinator initWithDelegate:identifier:allExpectedResultSpecifiers:isExpectingPairedVideo:allowMultipleCaptures:shouldReturnFilteredPhotosAsSingleAsset:];
-[CAMCVCStillImageResultCoordinator shouldReturnFilteredPhotosAsSingleAsset];
-[CAMCVCStillImageResultCoordinator updatePhotoProperties:assetAdjustments:forResultSpecifiers:];
-[CAMCVCStillImageResultCoordinator updateVideoProperties:forResultSpecifiers:wantsDepthRenderedForStill:];
```
