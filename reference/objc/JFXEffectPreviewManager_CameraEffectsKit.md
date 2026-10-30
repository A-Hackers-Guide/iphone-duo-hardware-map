# `JFXEffectPreviewManager`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PVLivePlayerDelegate`
- 22 instance variables, 27 properties, 71 instance methods, 1 class methods

## Instance variables

```
{?="updateContinousPreviewsForEffectIds"B"willBeginDownloadingPreviewAssetsForEffect"B"downloadingPreviewAssetsForEffect"B"didFinishDownloadingPreviewAssetsForEffect"B} _delegateAvailability;
B _inDealloc;
B _continouslyPreviewing_internal;
@"NSString" _name;
@"NSObject<OS_dispatch_queue>" _callbackQueue;
@"JFXLRUCache" _previewCache;
@"JFXEffectPreviewDiskCache" _previewDiskCache;
@"NSObject<OS_dispatch_queue>" _synchronizationQueue;
@"NSObject<OS_dispatch_queue>" _previewQueue;
@"NSObject<OS_dispatch_semaphore>" _concurrentStaticPreviewSemaphore;
@"NSObject" _pickerPreviewingToken;
@"<JFXEffectPreviewManagerDelegate>" _delegate_internal;
@"JTImage" _defaultPreviewImage_internal;
@"NSValue" __defaultPreviewImageDisplayTransformValue_internal;
@"JFXEffectsPreviewGenerator" _staticPreviewGenerator;
@"PVLivePlayer" _continousPreviewPlayer;
@"JFXEffectContinousPreviewOptions" _continousPreviewOptions;
@"NSMutableSet" _preparedContinousPreviewEffects;
@"NSMutableSet" _effectsPreparingForPreview;
@"NSSet" _currentContinousPreviewEffects;
@"NSMapTable" _assetRequestsForPreviewEffects;
{CGSize="width"d"height"d} _continousPreviewSize;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_callbackQueue) callbackQueue;
@property (T@"JFXLRUCache",R,N,V_previewCache) previewCache;
@property (T@"JFXEffectPreviewDiskCache",R,N,V_previewDiskCache) previewDiskCache;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_synchronizationQueue) synchronizationQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_previewQueue) previewQueue;
@property (T@"NSObject<OS_dispatch_semaphore>",R,N,V_concurrentStaticPreviewSemaphore) concurrentStaticPreviewSemaphore;
@property (T@"NSObject",R,N,V_pickerPreviewingToken) pickerPreviewingToken;
@property (T@"<JFXEffectPreviewManagerDelegate>",W,N,V_delegate_internal) delegate_internal;
@property (TB,N,V_continouslyPreviewing_internal) continouslyPreviewing_internal;
@property (T@"JTImage",&,N,V_defaultPreviewImage_internal) defaultPreviewImage_internal;
@property (T@"NSValue",&,N,V__defaultPreviewImageDisplayTransformValue_internal) _defaultPreviewImageDisplayTransformValue_internal;
@property (T@"JFXEffectsPreviewGenerator",&,N,V_staticPreviewGenerator) staticPreviewGenerator;
@property (T@"PVLivePlayer",&,N,V_continousPreviewPlayer) continousPreviewPlayer;
@property (T{CGSize=dd},N,V_continousPreviewSize) continousPreviewSize;
@property (T@"JFXEffectContinousPreviewOptions",&,N,V_continousPreviewOptions) continousPreviewOptions;
@property (T@"NSMutableSet",&,N,V_preparedContinousPreviewEffects) preparedContinousPreviewEffects;
@property (T@"NSMutableSet",&,N,V_effectsPreparingForPreview) effectsPreparingForPreview;
@property (T@"NSSet",&,N,V_currentContinousPreviewEffects) currentContinousPreviewEffects;
@property (T@"NSMapTable",&,N,V_assetRequestsForPreviewEffects) assetRequestsForPreviewEffects;
@property (T@"NSString",R,N,V_name) name;
@property (T@"<JFXEffectPreviewManagerDelegate>",W,N) delegate;
@property (T@"NSSet",C,N) continousPreviewEffects;
@property (TB,R,N,GisContinouslyPreviewing) continouslyPreviewing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[JFXEffectPreviewManager JFX_createTransparentEmptyImageForPreviewSize:];
```

## Instance methods

```
-[JFXEffectPreviewManager dealloc];
-[JFXEffectPreviewManager setDelegate:];
-[JFXEffectPreviewManager callbackQueue];
-[JFXEffectPreviewManager delegate];
-[JFXEffectPreviewManager previewQueue];
-[JFXEffectPreviewManager name];
-[JFXEffectPreviewManager previewCache];
-[JFXEffectPreviewManager synchronizationQueue];
-[JFXEffectPreviewManager JFX_cancelAssetRequestForAllEffects];
-[JFXEffectPreviewManager JFX_configureCommonRenderingPropertiesForEffect:forPreviewSize:withPreviewOptions:];
-[JFXEffectPreviewManager JFX_delegateDidFinishDownloadingPreviewAssetsForEffect:wasCancelled:error:];
-[JFXEffectPreviewManager JFX_delegateUpdateContinousPreviewsForEffectIDs:];
-[JFXEffectPreviewManager JFX_dispatchBlockOnCallbackQueueImmediatelyWhenPossible:];
-[JFXEffectPreviewManager JFX_loadRenderingResourcesForEffect:completion:];
-[JFXEffectPreviewManager JFX_lowPriorityScheduling];
-[JFXEffectPreviewManager JFX_prepareEffectForContinousPreview:];
-[JFXEffectPreviewManager JFX_renderPreviewForEffect:previewSize:options:completion:];
-[JFXEffectPreviewManager JFX_requestPreviewAssetsForEffect:withPriority:onlyThumbnailAssetWhenAvailable:completion:];
-[JFXEffectPreviewManager JFX_updateAssetRequestsPriorityAssociatedWithEffects:toPriority:];
-[JFXEffectPreviewManager preparedContinousPreviewEffects];
-[JFXEffectPreviewManager JFX_setContinousPreviewEffects:];
-[JFXEffectPreviewManager JFX_delegateDownloadingPreviewAssetsForEffect:progress:];
-[JFXEffectPreviewManager JFX_delegateWillBeginDownloadingPreviewAssetsForEffect:];
-[JFXEffectPreviewManager JFX_rendersDefaultContinousPreviewImage];
-[JFXEffectPreviewManager JFX_startPreparingPreviewsContinuouslyAtSize:options:];
-[JFXEffectPreviewManager JFX_stopCachingPreviewsContinuously];
-[JFXEffectPreviewManager JFX_updateAssetRequestsPriorityNotAssociatedWithEffects:toPriority:];
-[JFXEffectPreviewManager stopCachingPreviewsContinuously];
-[JFXEffectPreviewManager _defaultPreviewImageDisplayTransformValue_internal];
-[JFXEffectPreviewManager assetRequestsForPreviewEffects];
-[JFXEffectPreviewManager buildRenderRequest:time:];
-[JFXEffectPreviewManager cachedPreviewForEffect:completion:];
-[JFXEffectPreviewManager concurrentStaticPreviewSemaphore];
-[JFXEffectPreviewManager continousPreviewEffects];
-[JFXEffectPreviewManager continousPreviewOptions];
-[JFXEffectPreviewManager continousPreviewPlayer];
-[JFXEffectPreviewManager continousPreviewSize];
-[JFXEffectPreviewManager continousPreviewsForEffectIDs:completion:];
-[JFXEffectPreviewManager continouslyPreviewing_internal];
-[JFXEffectPreviewManager currentContinousPreviewEffects];
-[JFXEffectPreviewManager defaultPreviewImage];
-[JFXEffectPreviewManager defaultPreviewImageDisplayTransformValue];
-[JFXEffectPreviewManager defaultPreviewImage_internal];
-[JFXEffectPreviewManager delegate_internal];
-[JFXEffectPreviewManager effectsPreparingForPreview];
-[JFXEffectPreviewManager initWithName:callbackQueue:];
-[JFXEffectPreviewManager isContinouslyPreviewing];
-[JFXEffectPreviewManager pickerPreviewingToken];
-[JFXEffectPreviewManager preparePreviewForEffect:atSize:options:completion:];
-[JFXEffectPreviewManager previewDiskCache];
-[JFXEffectPreviewManager previewForEffect:atSize:options:completion:];
-[JFXEffectPreviewManager purgeCachedPreviewForEffect:];
-[JFXEffectPreviewManager purgeCachedPreviewsForAllEffects];
-[JFXEffectPreviewManager renderRequestComplete:results:completedOutOfOrder:];
-[JFXEffectPreviewManager setAssetRequestsForPreviewEffects:];
-[JFXEffectPreviewManager setContinousPreviewEffects:];
-[JFXEffectPreviewManager setContinousPreviewOptions:];
-[JFXEffectPreviewManager setContinousPreviewPlayer:];
-[JFXEffectPreviewManager setContinousPreviewSize:];
-[JFXEffectPreviewManager setContinouslyPreviewing:];
-[JFXEffectPreviewManager setContinouslyPreviewing_internal:];
-[JFXEffectPreviewManager setCurrentContinousPreviewEffects:];
-[JFXEffectPreviewManager setDefaultPreviewImage:transformValue:];
-[JFXEffectPreviewManager setDefaultPreviewImage_internal:];
-[JFXEffectPreviewManager setDelegate_internal:];
-[JFXEffectPreviewManager setEffectsPreparingForPreview:];
-[JFXEffectPreviewManager setPreparedContinousPreviewEffects:];
-[JFXEffectPreviewManager setStaticPreviewGenerator:];
-[JFXEffectPreviewManager set_defaultPreviewImageDisplayTransformValue_internal:];
-[JFXEffectPreviewManager startPreparingPreviewsContinuouslyAtSize:options:];
-[JFXEffectPreviewManager staticPreviewGenerator];
```
