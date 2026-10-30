# `CFXCameraViewController`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `CFXCaptureViewControllerDelegate`, `JFXRemoteCommandServerDelegate`, `CFXEffectBrowserContentPresenterViewControllerDelegate`, `CFXStageManagerWarningViewControllerDelegate`, `CFXEffectBrowserViewControllerDelegate`
- 32 instance variables, 44 properties, 134 instance methods, 2 class methods

## Instance variables

```
B _showsViewfinder;
B _usesInternalCaptureSession;
B _cameraControlsShown;
B _capturingFunCamMedia;
B _externalCaptureSessionCameraPositionSet;
B _isEffectsAnalyticsRunning;
q _aspectRatioCrop;
q _captureMode;
@"<CFXCameraViewControllerDelegate>" _delegate;
@"NSString" _animojiOnlyEffectID;
@"CFXCaptureViewController" _captureViewController;
@"CFXEffectBrowserViewController" _effectBrowserViewController;
@"CFXCameraControlsViewController" _cameraControlsViewController;
q _cameraPosition;
q _initialFlashMode;
@"NSString" _effectBrowserPresentedAppIdentifier;
@"JFXRemoteCommandServer" _remoteCommandServer;
@"UIView" _effectsPickerSnapshotContainerView;
@"NSObject<OS_dispatch_queue>" _externalCaptureSessionInputDeserializationQueue;
@"NSObject<OS_dispatch_queue>" _externalCaptureSessionInputProcessingQueue;
@"NSObject<OS_dispatch_queue>" _externalCaptureSessionOutputProcessingQueue;
@"JFXPixelRotationSession" _externalCaptureSessionRotationSession;
q _lastDeviceOrientation;
q _externalCaptureSessionCameraPosition;
@"JFXThreadSafeDictionary" _externalCaptureSessionInputFrameTimestamps;
@"NSTimer" _effectsInStreamTimer;
@"CFXThermalPolicyManager" _thermalPolicyManager;
@"JFXMetadataValidator" _metadataValidator;
@"CFXCameraStreamBufferQueue" _outputBufferQueue;
@"CFXStageManagerWarningViewController" _stageManagerWarning;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _externalPresentationRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _externalContentRect;
```

## Properties

```
@property (T@"CFXCaptureViewController",&,N,V_captureViewController) captureViewController;
@property (T@"CFXEffectBrowserViewController",&,N,V_effectBrowserViewController) effectBrowserViewController;
@property (T@"CFXCameraControlsViewController",&,N,V_cameraControlsViewController) cameraControlsViewController;
@property (Tq,N,V_cameraPosition) cameraPosition;
@property (Tq,N,V_initialFlashMode) initialFlashMode;
@property (TB,N,V_cameraControlsShown) cameraControlsShown;
@property (TB,N,V_capturingFunCamMedia) capturingFunCamMedia;
@property (T@"NSString",&,N,V_effectBrowserPresentedAppIdentifier) effectBrowserPresentedAppIdentifier;
@property (T@"JFXRemoteCommandServer",&,N,V_remoteCommandServer) remoteCommandServer;
@property (T@"UIView",&,N,V_effectsPickerSnapshotContainerView) effectsPickerSnapshotContainerView;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_externalCaptureSessionInputDeserializationQueue) externalCaptureSessionInputDeserializationQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_externalCaptureSessionInputProcessingQueue) externalCaptureSessionInputProcessingQueue;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_externalCaptureSessionOutputProcessingQueue) externalCaptureSessionOutputProcessingQueue;
@property (T@"JFXPixelRotationSession",&,N,V_externalCaptureSessionRotationSession) externalCaptureSessionRotationSession;
@property (Tq,N,V_lastDeviceOrientation) lastDeviceOrientation;
@property (Tq,N,V_externalCaptureSessionCameraPosition) externalCaptureSessionCameraPosition;
@property (TB,N,V_externalCaptureSessionCameraPositionSet) externalCaptureSessionCameraPositionSet;
@property (T@"JFXThreadSafeDictionary",&,N,V_externalCaptureSessionInputFrameTimestamps) externalCaptureSessionInputFrameTimestamps;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_externalPresentationRect) externalPresentationRect;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_externalContentRect) externalContentRect;
@property (T@"NSTimer",&,N,V_effectsInStreamTimer) effectsInStreamTimer;
@property (T@"CFXThermalPolicyManager",&,N,V_thermalPolicyManager) thermalPolicyManager;
@property (T@"JFXMetadataValidator",&,N,V_metadataValidator) metadataValidator;
@property (T@"CFXCameraStreamBufferQueue",&,N,V_outputBufferQueue) outputBufferQueue;
@property (T@"CFXStageManagerWarningViewController",&,N,V_stageManagerWarning) stageManagerWarning;
@property (TB,N,V_isEffectsAnalyticsRunning) isEffectsAnalyticsRunning;
@property (Tq,R,N,V_aspectRatioCrop) aspectRatioCrop;
@property (Tq,R,N,V_captureMode) captureMode;
@property (T@"<CFXCameraViewControllerDelegate>",W,N,V_delegate) delegate;
@property (Tq,R,N) devicePosition;
@property (T@"UIView",&,N) effectsPickerDrawer;
@property (TB,R,N,GisEffectsPickerHidden) effectsPickerHidden;
@property (Tq,R,N) effectsState;
@property (Tq,R,N) flashMode;
@property (Tq,R,N) mode;
@property (TB,N,V_showsViewfinder) showsViewfinder;
@property (Td,N) userInterfaceAlpha;
@property (TB,N,V_usesInternalCaptureSession) usesInternalCaptureSession;
@property (T@"UIColor",&,N) animojiOnlyBackgroundColor;
@property (T@"NSString",&,N,V_animojiOnlyEffectID) animojiOnlyEffectID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CFXCameraViewController initialize];
+[CFXCameraViewController preheatWithWindow:captureMode:devicePosition:aspectRatioCrop:];
```

## Instance methods

```
-[CFXCameraViewController aspectRatioCrop];
-[CFXCameraViewController initWithMode:];
-[CFXCameraViewController dealloc];
-[CFXCameraViewController removeAllEffects];
-[CFXCameraViewController willMoveToParentViewController:];
-[CFXCameraViewController viewDidLoad];
-[CFXCameraViewController viewDidLayoutSubviews];
-[CFXCameraViewController setDelegate:];
-[CFXCameraViewController viewDidAppear:];
-[CFXCameraViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[CFXCameraViewController captureMode];
-[CFXCameraViewController loadView];
-[CFXCameraViewController mode];
-[CFXCameraViewController stopCaptureSession];
-[CFXCameraViewController devicePosition];
-[CFXCameraViewController delegate];
-[CFXCameraViewController startCaptureSession];
-[CFXCameraViewController flashMode];
-[CFXCameraViewController cameraPosition];
-[CFXCameraViewController effectBrowserViewController:didSelectAppWithIdentifier:];
-[CFXCameraViewController effectBrowserViewController:didSelectEffect:];
-[CFXCameraViewController effectBrowserViewController:willChangeDockHeight:];
-[CFXCameraViewController effectsState];
-[CFXCameraViewController initWithCaptureMode:devicePosition:flashMode:aspectRatioCrop:captureSettings:];
-[CFXCameraViewController renderFrameWithImageDataArchive:imagePixelBuffer:depthPixelBuffer:orientation:presentationRect:contentsRect:];
-[CFXCameraViewController resign];
-[CFXCameraViewController setEffectsPickerDrawer:];
-[CFXCameraViewController setEffectsPickerHidden:animated:];
-[CFXCameraViewController setShowsViewfinder:];
-[CFXCameraViewController setUsesInternalCaptureSession:];
-[CFXCameraViewController shouldAlwaysPresentExpandedAppsForEffectBrowserViewController:];
-[CFXCameraViewController showMemojiPicker:];
-[CFXCameraViewController setCameraPosition:];
-[CFXCameraViewController setEffectBrowserViewController:];
-[CFXCameraViewController CFX_automationAddEffectWithEffectTypeIdentifier:identifier:string:];
-[CFXCameraViewController animojiEffectID];
-[CFXCameraViewController JFX_exitAnalytics];
-[CFXCameraViewController showsViewfinder];
-[CFXCameraViewController allowLandscapeForEffectBrowserViewController:];
-[CFXCameraViewController animojiOnlyBackgroundColor];
-[CFXCameraViewController animojiOnlyEffectID];
-[CFXCameraViewController cameraControlsShown];
-[CFXCameraViewController cameraControlsViewController];
-[CFXCameraViewController cameraControlsViewControllerForCaptureViewController:];
-[CFXCameraViewController captureViewController];
-[CFXCameraViewController captureViewController:didCaptureMediaItem:];
-[CFXCameraViewController captureViewController:didChangeEffectComposition:];
-[CFXCameraViewController captureViewController:didRenderFrame:];
-[CFXCameraViewController captureViewController:presentationRectWasPinchedWithState:scale:velocity:];
-[CFXCameraViewController captureViewController:switchedToCameraPosition:];
-[CFXCameraViewController captureViewControllerCameraFlipButtonWasTapped:];
-[CFXCameraViewController captureViewControllerDidStartVideoRecording:];
-[CFXCameraViewController captureViewControllerDidStopVideoRecording:];
-[CFXCameraViewController captureViewControllerDoneButtonWasTapped:];
-[CFXCameraViewController captureViewControllerEffectsButtonWasTapped:];
-[CFXCameraViewController captureViewControllerPresentationRectWasDoubleTapped:];
-[CFXCameraViewController captureViewControllerStartCaptureSession:];
-[CFXCameraViewController captureViewControllerStopCaptureSession:];
-[CFXCameraViewController capturingFunCamMedia];
-[CFXCameraViewController effectBrowserPresentedAppIdentifier];
-[CFXCameraViewController effectBrowserViewController];
-[CFXCameraViewController effectBrowserViewController:didDropOverlayEffect:atScreenLocation:atScreenSize:rotationAngle:];
-[CFXCameraViewController effectBrowserViewController:didRemoveAllEffectsOfType:];
-[CFXCameraViewController effectBrowserViewController:filterPickerPreviewBackgroundImageAtSizeInPixels:completion:];
-[CFXCameraViewController effectBrowserViewController:screenTopBarHeightForWindowBounds:orientation:];
-[CFXCameraViewController effectBrowserViewControllerDidStartCaptureSession:];
-[CFXCameraViewController effectBrowserViewControllerDidStopCaptureSession:];
-[CFXCameraViewController effectsInStreamTimer];
-[CFXCameraViewController effectsPickerDrawer];
-[CFXCameraViewController effectsPickerSnapshotContainerView];
-[CFXCameraViewController externalCaptureSessionCameraPosition];
-[CFXCameraViewController externalCaptureSessionCameraPositionSet];
-[CFXCameraViewController externalCaptureSessionInputDeserializationQueue];
-[CFXCameraViewController externalCaptureSessionInputFrameTimestamps];
-[CFXCameraViewController externalCaptureSessionInputProcessingQueue];
-[CFXCameraViewController externalCaptureSessionOutputProcessingQueue];
-[CFXCameraViewController externalCaptureSessionRotationSession];
-[CFXCameraViewController externalContentRect];
-[CFXCameraViewController externalPresentationRect];
-[CFXCameraViewController initWithCaptureMode:];
-[CFXCameraViewController initWithCaptureMode:devicePosition:flashMode:aspectRatioCrop:];
-[CFXCameraViewController initialFlashMode];
-[CFXCameraViewController isEffectsAnalyticsRunning];
-[CFXCameraViewController isEffectsPickerHidden];
-[CFXCameraViewController lastDeviceOrientation];
-[CFXCameraViewController localizedPromptForHidingAnimojiForEffectBrowserViewController:];
-[CFXCameraViewController metadataValidator];
-[CFXCameraViewController noteInputFrameWithTimestamp:];
-[CFXCameraViewController noteOutputFrameWithTimestamp:];
-[CFXCameraViewController outputBufferQueue];
-[CFXCameraViewController remoteCommandServer];
-[CFXCameraViewController remoteCommandServer:didReceiveAddShapeCommandWithIdentifier:];
-[CFXCameraViewController remoteCommandServer:didReceiveAddStickerCommandWithData:offset:scale:rotation:];
-[CFXCameraViewController remoteCommandServer:didReceiveAddStickerCommandWithIdentifier:offset:scale:rotation:];
-[CFXCameraViewController remoteCommandServer:didReceiveAddTextCommandWithIdentifier:string:];
-[CFXCameraViewController remoteCommandServer:didReceiveRemoveEffectsCommandWithTypeIdentifiers:];
-[CFXCameraViewController remoteCommandServer:didReceiveSetAnimojiCommandWithIdentifier:];
-[CFXCameraViewController remoteCommandServer:didReceiveSetFilterCommandWithIdentifier:];
-[CFXCameraViewController remoteCommandServer:didReceiveSetMemojiCommandWithContentsOfFile:];
-[CFXCameraViewController renderFrameWithImageData:orientation:presentationRect:contentsRect:];
-[CFXCameraViewController selectedAnimojiIdentifierForEffectBrowserViewController:];
-[CFXCameraViewController selectedFilterIdentifierForEffectBrowserViewController:];
-[CFXCameraViewController setAnimojiOnlyBackgroundColor:];
-[CFXCameraViewController setAnimojiOnlyEffectID:];
-[CFXCameraViewController setCameraControlsShown:];
-[CFXCameraViewController setCameraControlsViewController:];
-[CFXCameraViewController setCaptureViewController:];
-[CFXCameraViewController setCapturingFunCamMedia:];
-[CFXCameraViewController setEffectBrowserPresentedAppIdentifier:];
-[CFXCameraViewController setEffectsInStreamTimer:];
-[CFXCameraViewController setEffectsPickerSnapshotContainerView:];
-[CFXCameraViewController setExternalCaptureSessionCameraPosition:];
-[CFXCameraViewController setExternalCaptureSessionCameraPositionSet:];
-[CFXCameraViewController setExternalCaptureSessionInputFrameTimestamps:];
-[CFXCameraViewController setExternalCaptureSessionRotationSession:];
-[CFXCameraViewController setExternalContentRect:];
-[CFXCameraViewController setExternalPresentationRect:];
-[CFXCameraViewController setInitialFlashMode:];
-[CFXCameraViewController setIsEffectsAnalyticsRunning:];
-[CFXCameraViewController setLastDeviceOrientation:];
-[CFXCameraViewController setMetadataValidator:];
-[CFXCameraViewController setOutputBufferQueue:];
-[CFXCameraViewController setRemoteCommandServer:];
-[CFXCameraViewController setStageManagerWarning:];
-[CFXCameraViewController setThermalPolicyManager:];
-[CFXCameraViewController setTransitionState:animated:];
-[CFXCameraViewController setUserInterfaceAlpha:];
-[CFXCameraViewController shouldRotateCellsForDeviceOrientation];
-[CFXCameraViewController stageManagerWarning];
-[CFXCameraViewController stageManagerWarningDoneButtonWasTapped:];
-[CFXCameraViewController thermalPolicyManager];
-[CFXCameraViewController updateUIForVideoRecording:];
-[CFXCameraViewController userInterfaceAlpha];
-[CFXCameraViewController usesInternalCaptureSession];
```
