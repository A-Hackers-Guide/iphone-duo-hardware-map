# `CFXLiveCaptureViewController`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `CFXRendererDelegate`, `JFXVideoCameraVideoDelegate`, `JFXVideoCameraAudioDelegate`, `UIGestureRecognizerDelegate`
- 21 instance variables, 33 properties, 90 instance methods, 1 class methods

## Instance variables

```
B _useLocalCameraViewfinder;
B _isCapturingVideo_recordingQ;
B _isCapturingPhoto_recordingQ;
@"<JFXAnimojiTrackingLossDelegate>" _trackingLossDelegate;
@"<CFXLiveCaptureViewControllerDelegate>" _delegate;
@"CFXEffectComposition" _composition;
@"UIView" _containerView;
q _captureMode;
@"CFXThermalPolicyManager" _thermalPolicyManager;
@"JFXImageView" _renderImageView;
@"UIView" _debugControlsView;
@"UIView" _uncroppedRenderImagePlaceHolderView;
@"NSObject<OS_dispatch_queue>" _renderQ;
@"CFXRenderer" _renderer_renderQ;
@"NSObject<OS_dispatch_queue>" _recordingQ;
@"NSObject<OS_dispatch_queue>" _renderImageQ;
@"JTImage" _renderedImage_renderImageQ;
@"JFXVideoWriter" _videoWriter;
@"NSMutableArray" _renderFrameCompletionBlocks;
@"JFXOrientationMonitor" _orientationMonitor;
{?="value"q"timescale"i"flags"I"epoch"q} _currentRenderPresentationTime_renderImageQ;
```

## Properties

```
@property (T@"UIView",&,N,V_containerView) containerView;
@property (T@"JFXImageView",W,N,V_renderImageView) renderImageView;
@property (T@"UIView",W,N,V_debugControlsView) debugControlsView;
@property (T@"UIView",&,N,V_uncroppedRenderImagePlaceHolderView) uncroppedRenderImagePlaceHolderView;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_renderQ) renderQ;
@property (T@"CFXRenderer",&,N,V_renderer_renderQ) renderer_renderQ;
@property (T@"CFXEffectComposition",&,N,V_composition) composition;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_recordingQ) recordingQ;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_renderImageQ) renderImageQ;
@property (T@"JTImage",&,N,V_renderedImage_renderImageQ) renderedImage_renderImageQ;
@property (T{?=qiIq},N,V_currentRenderPresentationTime_renderImageQ) currentRenderPresentationTime_renderImageQ;
@property (T@"JTImage",R,N) renderedImage;
@property (T{?=qiIq},R,N) currentRenderPresentationTime;
@property (TB,N,V_isCapturingVideo_recordingQ) isCapturingVideo_recordingQ;
@property (TB,N,V_isCapturingPhoto_recordingQ) isCapturingPhoto_recordingQ;
@property (T@"JFXVideoWriter",&,N,V_videoWriter) videoWriter;
@property (T@"NSMutableArray",&,N,V_renderFrameCompletionBlocks) renderFrameCompletionBlocks;
@property (T@"JFXOrientationMonitor",&,N,V_orientationMonitor) orientationMonitor;
@property (T@"<JFXAnimojiTrackingLossDelegate>",W,N,V_trackingLossDelegate) trackingLossDelegate;
@property (T@"<CFXLiveCaptureViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T{?=dd},R,N) normalizedMinimumHitTestArea;
@property (TB,N,V_useLocalCameraViewfinder) useLocalCameraViewfinder;
@property (T@"UIView",R,N) localCameraViewfinderView;
@property (T@"UIView",R,N) uncroppedCameraViewfinderPlaceholderView;
@property (Tq,N,V_captureMode) captureMode;
@property (TB,R,N) isCapturing;
@property (TB,R,N) livePlayerIsSaturated;
@property (T@"CFXThermalPolicyManager",&,N,V_thermalPolicyManager) thermalPolicyManager;
@property (T@"UIColor",N) animojiBackgroundColor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CFXLiveCaptureViewController instantiate];
```

## Instance methods

```
-[CFXLiveCaptureViewController setComposition:];
-[CFXLiveCaptureViewController isCapturing];
-[CFXLiveCaptureViewController setContainerView:];
-[CFXLiveCaptureViewController viewWillDisappear:];
-[CFXLiveCaptureViewController viewDidLoad];
-[CFXLiveCaptureViewController composition];
-[CFXLiveCaptureViewController renderedImage];
-[CFXLiveCaptureViewController containerView];
-[CFXLiveCaptureViewController viewWillAppear:];
-[CFXLiveCaptureViewController setCaptureMode:];
-[CFXLiveCaptureViewController setDelegate:];
-[CFXLiveCaptureViewController captureMode];
-[CFXLiveCaptureViewController didReceiveMemoryWarning];
-[CFXLiveCaptureViewController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[CFXLiveCaptureViewController delegate];
-[CFXLiveCaptureViewController initWithCoder:];
-[CFXLiveCaptureViewController animojiBackgroundColor];
-[CFXLiveCaptureViewController setAnimojiBackgroundColor:];
-[CFXLiveCaptureViewController CFX_createUncroppedCameraPlaceholderViewIfNecessary];
-[CFXLiveCaptureViewController CFX_executeRenderCallbacksQueuedBeforeTime:];
-[CFXLiveCaptureViewController CFX_livePreviewDoubleTapped:];
-[CFXLiveCaptureViewController CFX_livePreviewPinched:];
-[CFXLiveCaptureViewController CFX_livePreviewTapped:];
-[CFXLiveCaptureViewController CFX_setAnimationEnabledForOverlays:];
-[CFXLiveCaptureViewController CFX_setupVideoWriterWithAudio:completion:];
-[CFXLiveCaptureViewController renderImageView];
-[CFXLiveCaptureViewController setIsCapturingVideo_recordingQ:];
-[CFXLiveCaptureViewController CFX_installGestures];
-[CFXLiveCaptureViewController CFX_livePreviewPanned:];
-[CFXLiveCaptureViewController CFX_livePreviewRotated:];
-[CFXLiveCaptureViewController CFX_tearDownVideoWriter:];
-[CFXLiveCaptureViewController renderQ];
-[CFXLiveCaptureViewController setIsCapturingPhoto_recordingQ:];
-[CFXLiveCaptureViewController setRenderFrameCompletionBlocks:];
-[CFXLiveCaptureViewController setVideoWriter:];
-[CFXLiveCaptureViewController cancelVideoRecording];
-[CFXLiveCaptureViewController capturePhotoWithFlashMode:completion:];
-[CFXLiveCaptureViewController currentRenderPresentationTime];
-[CFXLiveCaptureViewController currentRenderPresentationTime_renderImageQ];
-[CFXLiveCaptureViewController debugControlsView];
-[CFXLiveCaptureViewController executeAfterNextFrameIsRendered:];
-[CFXLiveCaptureViewController flushRenderer];
-[CFXLiveCaptureViewController isCapturingPhoto_recordingQ];
-[CFXLiveCaptureViewController isCapturingVideo_recordingQ];
-[CFXLiveCaptureViewController livePlayerIsSaturated];
-[CFXLiveCaptureViewController localCameraViewfinderView];
-[CFXLiveCaptureViewController locationInCaptureViewForGestureRecognizer:];
-[CFXLiveCaptureViewController normalizedMinimumHitTestArea];
-[CFXLiveCaptureViewController orientationMonitor];
-[CFXLiveCaptureViewController pauseRenderingCameraFrames];
-[CFXLiveCaptureViewController processAudioSample:];
-[CFXLiveCaptureViewController recordingQ];
-[CFXLiveCaptureViewController removeAllEffects:];
-[CFXLiveCaptureViewController removeAllEffectsOfType:completion:];
-[CFXLiveCaptureViewController renderFrameCompletionBlocks];
-[CFXLiveCaptureViewController renderImageQ];
-[CFXLiveCaptureViewController renderVideoFrame:];
-[CFXLiveCaptureViewController renderedImage_renderImageQ];
-[CFXLiveCaptureViewController renderer:didPrepareToRenderFrameAtPresentationTime:];
-[CFXLiveCaptureViewController renderer:didRenderFrame:];
-[CFXLiveCaptureViewController renderer_renderQ];
-[CFXLiveCaptureViewController resumeRenderingCameraFrames];
-[CFXLiveCaptureViewController setCurrentRenderPresentationTime_renderImageQ:];
-[CFXLiveCaptureViewController setDebugControlsView:];
-[CFXLiveCaptureViewController setOrientationMonitor:];
-[CFXLiveCaptureViewController setRecordingQ:];
-[CFXLiveCaptureViewController setRenderImageQ:];
-[CFXLiveCaptureViewController setRenderImageView:];
-[CFXLiveCaptureViewController setRenderQ:];
-[CFXLiveCaptureViewController setRenderedImage_renderImageQ:];
-[CFXLiveCaptureViewController setRenderer_renderQ:];
-[CFXLiveCaptureViewController setThermalPolicyManager:];
-[CFXLiveCaptureViewController setTrackingLossDelegate:];
-[CFXLiveCaptureViewController setUncroppedRenderImagePlaceHolderView:];
-[CFXLiveCaptureViewController setUseLocalCameraViewfinder:];
-[CFXLiveCaptureViewController startButtonTouchUpInside:];
-[CFXLiveCaptureViewController startRenderingCameraFrames];
-[CFXLiveCaptureViewController startVideoRecordingWithFlashMode:];
-[CFXLiveCaptureViewController stopButtonTouchUpInside:];
-[CFXLiveCaptureViewController stopRenderingCameraFrames];
-[CFXLiveCaptureViewController stopRenderingCameraFrames:];
-[CFXLiveCaptureViewController stopVideoRecording:];
-[CFXLiveCaptureViewController thermalPolicyManager];
-[CFXLiveCaptureViewController toggleDebugControlsView:];
-[CFXLiveCaptureViewController trackingLossDelegate];
-[CFXLiveCaptureViewController uncroppedCameraViewfinderPlaceholderView];
-[CFXLiveCaptureViewController uncroppedRenderImagePlaceHolderView];
-[CFXLiveCaptureViewController useLocalCameraViewfinder];
-[CFXLiveCaptureViewController videoWriter];
-[CFXLiveCaptureViewController willDropCameraFrame];
```
