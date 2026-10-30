# `BWFigCaptureSession`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWPipelineNotificationDelegate`, `BWRemoteQueueSinkNodeDelegate`, `BWNodeRenderDelegate`, `BWNodeFileCoordinatorStatusDelegate`, `BWNodeFileWriterStatusDelegate`, `BWStillImageCaptureStatusDelegate`, `BWImageQueueSinkNodePreviewTapDelegate`, `BWIrisStagingNodeIrisRequestDelegate`, `BWPreviewStitcherDelegate`, `BWVideoPIPOverlayDelegate`, `FigCaptureDisplayLayoutObserver`, `BWPreviewStabilizationNodeDelegate`, `BWFigVideoCaptureDeviceShutterSoundRelaxationDelegate`, `BWPersonalPhotographerCaptureRegistrationDelegate`, `BWBroadcastVideoDelegate`, `BWGraphStatusDelegate`, `FigCaptureInterruptionDelegate`
- 3 instance variables, 4 properties, 56 instance methods, 0 class methods

## Instance variables

```
^{OpaqueFigCaptureSession=} _captureSession;
@"FigCaptureSessionPipelines" _pipelines;
q _graphID;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWFigCaptureSession graph:didStartSourceNode:error:];
-[BWFigCaptureSession isTrueVideoActiveForShutterSoundRelaxation];
-[BWFigCaptureSession stagingNode:willEmitIrisRequest:];
-[BWFigCaptureSession trueVideoCaptureAdditionalZoomFactorForPreviewStitcher:];
-[BWFigCaptureSession postNotification:notificationPayload:];
-[BWFigCaptureSession stillImageCoordinator:willBeginCaptureBeforeResolvingSettingsForID:];
-[BWFigCaptureSession layoutMonitor:didUpdateLayout:];
-[BWFigCaptureSession imageQueueSinkNode:didAttemptToEnqueuePreviewSampleBuffer:withSuccess:];
-[BWFigCaptureSession fileWriter:writerPipelineIndex:stoppedRecordingSampleDataForSettingsID:];
-[BWFigCaptureSession fileCoordinator:stoppedBeforeStartedRecordingForSettings:pendingIrisMovieInfos:errorCode:];
-[BWFigCaptureSession stagingNode:waitingToEmitFrameWithPTS:];
-[BWFigCaptureSession stillImageCoordinator:updateSettingsAfterLiveReconfiguration:];
-[BWFigCaptureSession stillImageCoordinator:willPrepareStillImageCaptureWithSettings:clientInitiated:];
-[BWFigCaptureSession dealloc];
-[BWFigCaptureSession videoPIPOverlayNode:overlayRectDidChange:];
-[BWFigCaptureSession didChangeSubjectGazing:];
-[BWFigCaptureSession remoteQueueSinkNode:queueBecameReady:];
-[BWFigCaptureSession stillImageCoordinator:didCapturePhotoForSettings:];
-[BWFigCaptureSession stagingNode:valveClosedWithPendingIrisRequests:];
-[BWFigCaptureSession interruptionTriggered:];
-[BWFigCaptureSession stagingNode:readyToReceiveRequestsWithEarliestAllowedStillImageCaptureHostPTS:];
-[BWFigCaptureSession graphDidResolveRetainedBufferCounts:];
-[BWFigCaptureSession remoteQueueSinkNodeDidDeliverFirstVideoFrame:];
-[BWFigCaptureSession remoteQueueSinkNode:dumpStateForReason:];
-[BWFigCaptureSession previewStitcherTrueVideoExitTransitionDidComplete:];
-[BWFigCaptureSession remoteQueueSinkNode:localQueueBecameReady:];
-[BWFigCaptureSession imageQueueSinkNodeDidDisplayFirstFrame:timedOut:];
-[BWFigCaptureSession stillImageCoordinator:didSelectNewReferenceFrameWithPTS:transform:forSettings:];
-[BWFigCaptureSession interruptionResolved:];
-[BWFigCaptureSession stillImageCoordinator:willBeginCaptureForSettings:];
-[BWFigCaptureSession previewStitcherReadyForPrimaryCaptureRectUpdates:];
-[BWFigCaptureSession previewStitcherSmartFramingFieldOfViewTransitionAppliedZoomFactor:zoomFactor:];
-[BWFigCaptureSession imageQueueSinkNodeDidDisplayFirstFrame:atHostTime:];
-[BWFigCaptureSession fileWriter:frameDroppedForSettingsID:withError:];
-[BWFigCaptureSession fileWriter:startedRecordingForSettings:writerPipelineIndex:startPTS:];
-[BWFigCaptureSession fileWriter:pausedRecordingForSettingsID:];
-[BWFigCaptureSession graphDidPrepareNodes:];
-[BWFigCaptureSession node:format:didBecomeLiveForOutput:];
-[BWFigCaptureSession node:format:didBecomeLiveForInput:configurationID:];
-[BWFigCaptureSession fileWriter:resumedRecordingForSettingsID:];
-[BWFigCaptureSession stillImageCoordinator:didCancelMomentCaptureForSettingsID:streamingDisruptionEndPTS:];
-[BWFigCaptureSession fileCoordinator:sentMarkerBufferForFileWriterAction:withPTS:settings:errorCode:];
-[BWFigCaptureSession node:willRenderSampleBuffer:forInput:];
-[BWFigCaptureSession broadcastVideoSinkNode:videoSettingsDidChange:];
-[BWFigCaptureSession hvsScoringNode:didFinishPersonalPhotographerSessionWithCapturesToKeep:capturesToDelete:stillImageCoordinatorNode:settings:];
-[BWFigCaptureSession imageQueueSinkNodeDidDisplayFirstFrameForCurrentConfiguration:atHostTime:withPreviewStartedTime:];
-[BWFigCaptureSession previewStabilizationNode:didApplyPreviewStabilizationShift:forPortType:];
-[BWFigCaptureSession previewStitcher:overCaptureStatusDidChange:];
-[BWFigCaptureSession stillImageCoordinator:didResolveStillImagePTS:forSettings:isPreBracketedEV0:];
-[BWFigCaptureSession previewStitcher:didApplyWiderCameraShift:widerCameraScaleFactor:forWiderCameraPortType:narrowerCameraShift:narrowerCameraScaleFactor:forNarrowerCameraPortType:inSuperWideMacroMode:widerCameraShiftAtBaseZoom:];
-[BWFigCaptureSession stillImageCoordinator:didSelectVitalityMode:forSettings:];
-[BWFigCaptureSession stillImageCoordinator:willCapturePhotoForSettings:error:];
-[BWFigCaptureSession fileWriter:writerPipelineIndex:stoppedRecordingForSettings:withError:thumbnailSurface:irisMovieInfo:debugMetadataSidecarFileURL:videoDBGFileURL:recordingSucceeded:];
-[BWFigCaptureSession graph:didFinishStartingWithError:];
-[BWFigCaptureSession broadcastVideoSinkNode:didDropSampleBufferWithPresentationTimeStamp:dropReason:];
-[BWFigCaptureSession stillImageCoordinator:readyToRespondToRequestAfterRequestWithSettings:];
```
