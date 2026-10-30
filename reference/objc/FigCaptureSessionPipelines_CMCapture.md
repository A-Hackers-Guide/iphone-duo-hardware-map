# `FigCaptureSessionPipelines`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 20 properties, 83 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _cameraSourcePipelines;
@"FigCaptureMicSourcePipeline" _micSourcePipeline;
@"NSMutableArray" _metadataSourcePipelines;
@"NSMutableArray" _videoDataSinkPipelines;
@"NSMutableArray" _previewSinkPipelines;
@"NSMutableArray" _movieFileSinkPipelines;
@"NSMutableArray" _depthDataSinkPipelines;
@"NSMutableArray" _videoThumbnailSinkPipelines;
@"NSMutableArray" _metadataSinkPipelines;
@"NSMutableArray" _visionDataSinkPipelines;
@"NSMutableArray" _audioDataSinkPipelines;
@"NSMutableArray" _audioFileSinkPipelines;
@"NSMutableArray" _stillImageSinkPipelineStorages;
@"NSMutableArray" _softISPCalibrationSinkPipelines;
@"NSMutableArray" _pointCloudDataSinkPipelines;
@"NSMutableArray" _cameraCalibrationDataSinkPipelines;
@"NSMutableArray" _cinematographyPipelines;
@"NSMutableArray" _lidarDepthPipelines;
@"NSMutableArray" _secureVideoDataSinkPipelines;
@"NSMutableArray" _broadcastVideoSinkPipelines;
@"NSMutableDictionary" _cameraSourcePipelinesBySessionID;
@"NSMutableDictionary" _metadataSinkPipelinesBySessionID;
```

## Properties

```
@property (T@"FigCaptureMicSourcePipeline",&,N,V_micSourcePipeline) micSourcePipeline;
@property (T@"NSArray",R,N,V_cameraSourcePipelines) cameraSourcePipelines;
@property (T@"FigCaptureCameraSourcePipeline",R,N) firstColorCameraSourcePipeline;
@property (T@"NSArray",R,N,V_metadataSourcePipelines) metadataSourcePipelines;
@property (T@"NSArray",R,N,V_previewSinkPipelines) previewSinkPipelines;
@property (T@"NSArray",R,N,V_videoDataSinkPipelines) videoDataSinkPipelines;
@property (T@"NSArray",R,N,V_movieFileSinkPipelines) movieFileSinkPipelines;
@property (T@"NSArray",R,N,V_stillImageSinkPipelineStorages) stillImageSinkPipelineSessionStorages;
@property (T@"NSArray",R,N,V_softISPCalibrationSinkPipelines) softISPCalibrationSinkPipelines;
@property (T@"NSArray",R,N,V_depthDataSinkPipelines) depthDataSinkPipelines;
@property (T@"NSArray",R,N,V_videoThumbnailSinkPipelines) videoThumbnailSinkPipelines;
@property (T@"NSArray",R,N,V_metadataSinkPipelines) metadataSinkPipelines;
@property (T@"NSArray",R,N,V_visionDataSinkPipelines) visionDataSinkPipelines;
@property (T@"NSArray",R,N,V_audioDataSinkPipelines) audioDataSinkPipelines;
@property (T@"NSArray",R,N,V_audioFileSinkPipelines) audioFileSinkPipelines;
@property (T@"NSArray",R,N,V_pointCloudDataSinkPipelines) pointCloudDataSinkPipelines;
@property (T@"NSArray",R,N,V_cameraCalibrationDataSinkPipelines) cameraCalibrationDataSinkPipelines;
@property (T@"NSArray",R,N,V_cinematographyPipelines) cinematographyPipelines;
@property (T@"NSArray",R,N,V_secureVideoDataSinkPipelines) secureVideoDataSinkPipelines;
@property (T@"NSArray",R,N,V_broadcastVideoSinkPipelines) broadcastVideoSinkPipelines;
```

## Instance methods

```
-[FigCaptureSessionPipelines updateClientAuditToken:];
-[FigCaptureSessionPipelines previewSinkPipelines];
-[FigCaptureSessionPipelines addVideoThumbnailSinkPipeline:];
-[FigCaptureSessionPipelines addLiDARDepthPipeline:];
-[FigCaptureSessionPipelines audioDataSinkPipelineWithSinkID:];
-[FigCaptureSessionPipelines broadcastVideoSinkPipelines];
-[FigCaptureSessionPipelines softISPCalibrationSinkPipelines];
-[FigCaptureSessionPipelines addMetadataSourcePipeline:];
-[FigCaptureSessionPipelines addMetadataSinkPipeline:sessionID:];
-[FigCaptureSessionPipelines visionDataSinkPipelines];
-[FigCaptureSessionPipelines addVisionDataSinkPipeline:];
-[FigCaptureSessionPipelines addPreviewSinkPipeline:];
-[FigCaptureSessionPipelines cameraSourcePipelineWithSourceID:];
-[FigCaptureSessionPipelines metadataSinkPipelineWithSessionID:sinkID:];
-[FigCaptureSessionPipelines stillImageSinkPipelineSessionStorages];
-[FigCaptureSessionPipelines cameraCalibrationDataSinkPipelines];
-[FigCaptureSessionPipelines addCameraSourcePipeline:sessionID:];
-[FigCaptureSessionPipelines addVideoDataSinkPipeline:];
-[FigCaptureSessionPipelines videoThumbnailSinkPipelines];
-[FigCaptureSessionPipelines setMicSourcePipeline:];
-[FigCaptureSessionPipelines videoDataSinkPipelines];
-[FigCaptureSessionPipelines videoDataSinkPipelinesWithSourceID:sourceDeviceType:];
-[FigCaptureSessionPipelines dealloc];
-[FigCaptureSessionPipelines addPointCloudDataSinkPipeline:];
-[FigCaptureSessionPipelines cameraSourcePipelineWithSessionID:sourceDeviceType:];
-[FigCaptureSessionPipelines metadataSinkPipelineWithSinkID:];
-[FigCaptureSessionPipelines metadataSinkPipelines];
-[FigCaptureSessionPipelines metadataSinkPipelinesWithSessionID:];
-[FigCaptureSessionPipelines pointCloudDataSinkPipelines];
-[FigCaptureSessionPipelines addCameraCalibrationDataSinkPipeline:];
-[FigCaptureSessionPipelines broadcastVideoSinkPipelineWithVideoConnectionID:];
-[FigCaptureSessionPipelines cameraSourcePipelines];
-[FigCaptureSessionPipelines stillImageSinkPipelineSessionStorageWithSinkID:];
-[FigCaptureSessionPipelines videoDataSinkPipelineWithSinkID:];
-[FigCaptureSessionPipelines cinematographyPipelines];
-[FigCaptureSessionPipelines videoThumbnailSinkPipelineWithSinkID:];
-[FigCaptureSessionPipelines addAudioFileSinkPipeline:];
-[FigCaptureSessionPipelines metadataSourcePipelines];
-[FigCaptureSessionPipelines cameraSourcePipelinesWithSessionID:];
-[FigCaptureSessionPipelines firstColorCameraSourcePipeline];
-[FigCaptureSessionPipelines cameraCalibrationDataSinkPipelineWithSinkID:];
-[FigCaptureSessionPipelines movieFileSinkPipelineWithIrisStagingNode:];
-[FigCaptureSessionPipelines movieFileSinkPipelineWithSinkID:];
-[FigCaptureSessionPipelines visionDataSinkPipelineWithSinkID:];
-[FigCaptureSessionPipelines videoDataSinkPipelineForMetadataWithSourceID:sourceDeviceType:];
-[FigCaptureSessionPipelines pointCloudDataSinkPipelineWithSinkID:];
-[FigCaptureSessionPipelines addSecureVideoDataSinkPipeline:];
-[FigCaptureSessionPipelines depthDataSinkPipelineWithSinkID:];
-[FigCaptureSessionPipelines cameraSourcePipelineCompatibleWithCameraConfiguration:];
-[FigCaptureSessionPipelines addDepthDataSinkPipeline:];
-[FigCaptureSessionPipelines movieFileSinkPipelineWithVideoConnectionID:];
-[FigCaptureSessionPipelines secureVideoDataSinkPipelines];
-[FigCaptureSessionPipelines addMetadataSinkPipeline:];
-[FigCaptureSessionPipelines addCinematographyPipeline:];
-[FigCaptureSessionPipelines addAudioDataSinkPipeline:];
-[FigCaptureSessionPipelines audioFileSinkPipelineWithFileSinkNode:];
-[FigCaptureSessionPipelines depthDataSinkPipelines];
-[FigCaptureSessionPipelines micSourcePipeline];
-[FigCaptureSessionPipelines movieFileSinkPipelineWithSourceID:sourceDeviceType:];
-[FigCaptureSessionPipelines secureVideoSinkPipelineWithSinkID:];
-[FigCaptureSessionPipelines audioDataSinkPipelines];
-[FigCaptureSessionPipelines stillImageSinkPipelineSessionStorageWithStillImageCoordinator:];
-[FigCaptureSessionPipelines removeCameraSourcePipelinesWithSessionID:];
-[FigCaptureSessionPipelines previewSinkPipelineForStillImageSinkID:];
-[FigCaptureSessionPipelines addMovieFileSinkPipeline:];
-[FigCaptureSessionPipelines addBroadcastVideoSinkPipeline:];
-[FigCaptureSessionPipelines previewSinkPipelineWithSinkID:];
-[FigCaptureSessionPipelines removeMetadataSinkPipelinesWithSessionID:];
-[FigCaptureSessionPipelines previewSinkPipelineWithSourceID:sourceDeviceType:];
-[FigCaptureSessionPipelines addCameraSourcePipeline:];
-[FigCaptureSessionPipelines secondaryPreviewSinkPipelinesForPreviewSinkPipeline:];
-[FigCaptureSessionPipelines audioFileSinkPipelineWithSinkID:];
-[FigCaptureSessionPipelines addStillImageSinkPipelineSessionStorage:];
-[FigCaptureSessionPipelines broadcastVideoSinkPipelineWithSinkID:];
-[FigCaptureSessionPipelines depthDataSinkPipelineWithSourceID:sourceDeviceType:];
-[FigCaptureSessionPipelines metadataSinkPipelineWithSourceID:sourceDeviceType:];
-[FigCaptureSessionPipelines movieFileSinkPipelineWithFileSinkNode:];
-[FigCaptureSessionPipelines audioFileSinkPipelines];
-[FigCaptureSessionPipelines movieFileSinkPipelineWithFileCoordinatorNode:];
-[FigCaptureSessionPipelines lidarDepthPipelineWithRGBCameraSourceID:];
-[FigCaptureSessionPipelines cinematographyPipelineWithSourceID:];
-[FigCaptureSessionPipelines movieFileSinkPipelines];
-[FigCaptureSessionPipelines addSoftISPCalibrationSinkPipeline:];
```
