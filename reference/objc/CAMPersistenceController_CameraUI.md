# `CAMPersistenceController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMStillImagePersistenceCoordinatorDelegate`, `CAMVideoPersistenceCoordinationDelegate`, `CAMCaptureService`
- 19 instance variables, 22 properties, 86 instance methods, 7 class methods

## Instance variables

```
{?="respondsToDidCompleteAllLocalPersistenceForRequest"B} _resultDelegateFlags;
@"NSMutableDictionary" _pendingLivePhotoTextOrientations;
@"NSMutableArray" _pendingLocalPersistenceWrappers;
@"NSMutableArray" _pendingRemotePersistenceWrappers;
@"<CAMPersistenceResultDelegate>" _resultDelegate;
@"<CAMPersistenceControllerPersonalPhotographerDelegate>" _personalPhotographerDelegate;
@"CAMThumbnailGenerator" __localPersistenceThumbnailGenerator;
@"CAMThumbnailGenerator" __remotePersistenceThumbnailGenerator;
@"NSObject<OS_dispatch_queue>" __localPersistenceQueue;
@"NSObject<OS_dispatch_queue>" __remotePersistenceQueue;
@"CAMLocationController" __locationController;
@"CAMProtectionController" __protectionController;
@"CAMPowerController" __powerController;
@"CAMBurstController" __burstController;
@"NSObject<OS_dispatch_queue>" __resultDelegateIsolationQueue;
@"NSObject<OS_dispatch_queue>" __coordinationQueue;
@"NSMapTable" __coordinationQueueGroupsByIdentifier;
@"NSMutableDictionary" __coordinationQueue_stillImagePersistenceCoordinators;
@"NSMutableDictionary" __coordinationQueue_videoPersistenceCoordinators;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__localPersistenceQueue) _localPersistenceQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__remotePersistenceQueue) _remotePersistenceQueue;
@property (T@"CAMThumbnailGenerator",R,N,V__localPersistenceThumbnailGenerator) _localPersistenceThumbnailGenerator;
@property (T@"CAMThumbnailGenerator",R,N,V__remotePersistenceThumbnailGenerator) _remotePersistenceThumbnailGenerator;
@property (T@"NSMutableArray",R,N,V_pendingLocalPersistenceWrappers) _pendingLocalPersistenceWrappers;
@property (T@"NSMutableArray",R,N,V_pendingRemotePersistenceWrappers) _pendingRemotePersistenceWrappers;
@property (T@"CAMLocationController",R,N,V__locationController) _locationController;
@property (T@"CAMProtectionController",R,N,V__protectionController) _protectionController;
@property (T@"CAMPowerController",R,N,V__powerController) _powerController;
@property (T@"CAMBurstController",R,N,V__burstController) _burstController;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__resultDelegateIsolationQueue) _resultDelegateIsolationQueue;
@property (TB,R,N) resultDelegateRespondsToDidCompleteAllLocalPersistenceForRequest;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__coordinationQueue) _coordinationQueue;
@property (T@"NSMapTable",R,N,V__coordinationQueueGroupsByIdentifier) _coordinationQueueGroupsByIdentifier;
@property (T@"NSMutableDictionary",R,N,V__coordinationQueue_stillImagePersistenceCoordinators) _coordinationQueue_stillImagePersistenceCoordinators;
@property (T@"NSMutableDictionary",R,N,V__coordinationQueue_videoPersistenceCoordinators) _coordinationQueue_videoPersistenceCoordinators;
@property (T@"<CAMPersistenceResultDelegate>",W,N,V_resultDelegate) resultDelegate;
@property (T@"<CAMPersistenceControllerPersonalPhotographerDelegate>",W,N,V_personalPhotographerDelegate) personalPhotographerDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMPersistenceController clientVideoMetadataForLocation:withCreationDate:];
+[CAMPersistenceController clientVideoMetadataForRequest:withCreationDate:isEV0ForHDR:livePhotoIdentifierOverride:slomoPlayback:];
+[CAMPersistenceController delimiterForIncomingAssetFilenames];
+[CAMPersistenceController pathForIncomingDirectory];
+[CAMPersistenceController uniqueIncomingPathForAssetWithUUID:captureTime:extension:];
+[CAMPersistenceController uniquePathForAssetWithUUID:captureTime:extension:usingIncomingDirectory:];
+[CAMPersistenceController videoMetadataDateFormatter];
```

## Instance methods

```
-[CAMPersistenceController _powerController];
-[CAMPersistenceController _locationController];
-[CAMPersistenceController stillImageRequestDidCompleteCapture:error:];
-[CAMPersistenceController stillImageRequest:didCompleteVideoCaptureWithResult:];
-[CAMPersistenceController _coordinateRemotePersistenceForVideoLocalResult:coordinationInfo:request:];
-[CAMPersistenceController writePrivateMetadataFileToURL:withPrivateClientMetadata:sharedLibraryMode:contactIDsInProximity:sharedLibraryDiagnostics:];
-[CAMPersistenceController _writeDataToURL:withData:error:];
-[CAMPersistenceController _adjustmentsDataForVideoRequest:];
-[CAMPersistenceController _videoPersistenceUUIDForRequest:withResult:];
-[CAMPersistenceController _videoRemotePowerAssertionReasonForCoordinationInfo:];
-[CAMPersistenceController videoPersistenceCoordinator:requestsTimeoutScheduledForDeferredRemotePersistenceForCoordinationInfo:request:];
-[CAMPersistenceController _handleVideoPersistenceForRequest:withResult:];
-[CAMPersistenceController stillImagePersistenceCoordinator:requestsTimeoutScheduledForDeferredRemotePersistenceForCoordinationInfo:request:];
-[CAMPersistenceController videoRequest:didCompleteCaptureWithResult:];
-[CAMPersistenceController _saveAssetsIndividually:pendingRemoteWrappers:];
-[CAMPersistenceController _jobDictionaryForTimelapsePlaceholderResult:];
-[CAMPersistenceController _xmpEncodedDiagnosticDataFromDictionary:];
-[CAMPersistenceController init];
-[CAMPersistenceController _physicallyRotatedJPEGDataFromCapturePhoto:];
-[CAMPersistenceController resultDelegateRespondsToDidCompleteAllLocalPersistenceForRequest];
-[CAMPersistenceController initWithLocationController:burstController:protectionController:powerController:];
-[CAMPersistenceController emptyLocalPersistenceStorageWithTimeout:completionHandler:];
-[CAMPersistenceController _batchSaveAssets:pendingRemoteWrappers:];
-[CAMPersistenceController _notifyDelegateOfCompletedStillImageLocalPersistenceForRequest:withResult:];
-[CAMPersistenceController _jobDictionaryForVideoLocalResult:fromRequest:loggingIdentifier:];
-[CAMPersistenceController dealloc];
-[CAMPersistenceController _createMetadataForPhysicallyOrientedImage:];
-[CAMPersistenceController _coordinateRemotePersistenceForStillImageLocalResult:coordinationInfo:request:];
-[CAMPersistenceController setResultDelegate:];
-[CAMPersistenceController _locallyPersistVideoCaptureResult:forRequest:withCompletionHandler:];
-[CAMPersistenceController _coordinationQueue_videoPersistenceCoordinators];
-[CAMPersistenceController _extensionForUniformType:];
-[CAMPersistenceController _persistVideoCaptureResult:withRequest:];
-[CAMPersistenceController _notifyDelegateOfCompletedStillImageRemotePersistenceForRequest:withReply:fromBatchOfSize:error:];
-[CAMPersistenceController setPersonalPhotographerDelegate:];
-[CAMPersistenceController didFinishPersonalPhotographerSessionWithResults:request:error:];
-[CAMPersistenceController _notifyDelegateOfCompletedVideoRemotePersistenceForRequest:withReply:error:];
-[CAMPersistenceController _removeCoordinationGroupForIdentifier:];
-[CAMPersistenceController _locallyPersistStillImageResult:forRequest:withCompletionHandler:];
-[CAMPersistenceController videoPersistenceCoordinator:requestsRemotePersistenceForLocalPersistenceResult:captureRequest:powerAssertionReason:];
-[CAMPersistenceController _jobDictionaryForStillImageLocalResult:filteredLocalResult:fromRequest:loggingIdentifier:];
-[CAMPersistenceController _mainThread_handleApplicationDidEnterBackground:];
-[CAMPersistenceController _writeJPEGToURL:withData:thumbnail:properties:error:];
-[CAMPersistenceController _localPersistenceThumbnailGenerator];
-[CAMPersistenceController _coordinationGroupForIdentifier:];
-[CAMPersistenceController persistBurstWithIdentifier:result:completionHandler:];
-[CAMPersistenceController _batchGroupIdentifierForRequest:];
-[CAMPersistenceController _notifyDelegateOfCompletedVideoLocalPersistenceForRequest:withResult:];
-[CAMPersistenceController persistPlaceholderTimelapseVideoWithResult:completionHandler:];
-[CAMPersistenceController _handleCompletedStillImageJobForRequest:withReply:fromBatchOfSize:completionHandler:error:];
-[CAMPersistenceController _stillPersistenceUUIDForRequest:withVideoResult:];
-[CAMPersistenceController _burstController];
-[CAMPersistenceController _stillImageLocalPowerAssertionReasonForCoordinationInfo:];
-[CAMPersistenceController _remotePersistenceThumbnailGenerator];
-[CAMPersistenceController _pendingLocalPersistenceWrappers];
-[CAMPersistenceController _adjustmentsDataForCinematicVideoRequest:result:];
-[CAMPersistenceController _createOpenWriteStreamWithURL:error:];
-[CAMPersistenceController _uniformTypeForStillImageRequest:result:];
-[CAMPersistenceController _dispatchRemotePersistenceForLocalVideoPersistenceResult:request:powerAssertionReason:loggingIdentifier:];
-[CAMPersistenceController _persistStillImageCaptureSurfaceResult:withRequest:];
-[CAMPersistenceController _affineTransformForRotationDegrees:mirrored:];
-[CAMPersistenceController _videoLocalPowerAssertionReasonForCoordinationInfo:];
-[CAMPersistenceController _resultDelegateIsolationQueue];
-[CAMPersistenceController _handleStillImagePersistenceForRequest:withResult:];
-[CAMPersistenceController _protectionController];
-[CAMPersistenceController _coordinationQueue];
-[CAMPersistenceController _handleCompletedVideoJobForRequest:withReply:completionHandler:error:];
-[CAMPersistenceController _ensureCoordinationGroupForIdentifier:];
-[CAMPersistenceController _applyTextExifOrientation:toVideoAtURL:];
-[CAMPersistenceController _adjustmentsDataForRequest:captureDimensions:portraitMetadata:];
-[CAMPersistenceController performDeferredRemotePersistenceWithCompletionHandler:];
-[CAMPersistenceController _pendingRemotePersistenceWrappers];
-[CAMPersistenceController stillImageRequest:didCompleteStillImageCaptureWithResult:];
-[CAMPersistenceController _remotePersistenceQueue];
-[CAMPersistenceController _dispatchRemotePersistenceForLocalPersistenceResult:filteredLocalResult:request:powerAssertionReason:loggingIdentifier:];
-[CAMPersistenceController stillImagePersistenceCoordinator:requestsRemotePersistenceForLocalPersistenceResult:filteredLocalResult:request:powerAssertionReason:];
-[CAMPersistenceController panoramaRequest:didCompleteCaptureWithResult:];
-[CAMPersistenceController resultDelegate];
-[CAMPersistenceController _localPersistenceQueue];
-[CAMPersistenceController personalPhotographerDelegate];
-[CAMPersistenceController _adjustmentsDataForSloMoVideoRequest:];
-[CAMPersistenceController _coordinationQueue_stillImagePersistenceCoordinators];
-[CAMPersistenceController _persistenceErrorForWriteStream:url:code:];
-[CAMPersistenceController _remotelyPersistStillImageJob:forRequest:loggingIdentifier:completionHandler:];
-[CAMPersistenceController _coordinationQueueGroupsByIdentifier];
-[CAMPersistenceController _remotelyPersistVideoJob:forRequest:loggingIdentifier:withSendHandler:completionHandler:];
```
