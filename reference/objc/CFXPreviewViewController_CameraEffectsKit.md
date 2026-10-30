# `CFXPreviewViewController`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `CFXEffectEditorViewDelegate`, `CFXFullScreenTextEditViewControllerDelegate`, `JFXCompositionPlayerViewControllerDelegate`, `JFXExportDelegate`, `CFXPlayButtonViewDelegate`, `UIViewWindowListener`
- 28 instance variables, 39 properties, 161 instance methods, 2 class methods

## Instance variables

```
B _presentingFilterPicker;
B _capturedWithBackCamera;
B _userInterfaceHidden;
B _saveMediaItemToFunCamPhotosAlbumUponExport;
B _dockIsMagnified;
@"<CFXPreviewViewControllerDelegate>" _delegate;
@"CFXControlsViewController" _previewControls;
@"CFXEffectBrowserContentPresenterViewController" _effectBrowserContentPresenterViewController;
@"UIView" _playerContainerView;
@"UIView" _appStripAndPreviewControlsContainer;
@"UIButton" _exportButton;
@"NSLayoutConstraint" _previewControlsContainerHeightConstraint;
@"NSLayoutConstraint" _previewControlsContainerWidthConstraint;
@"NSLayoutConstraint" _previewControlsContainerTrailingConstraint;
@"NSLayoutConstraint" _previewControlsContainerLeadingConstraint;
@"NSLayoutConstraint" _previewControlsContainerTopConstraint;
Q _appliedDirectOverlayEditingGestures;
@"UIView" _bottomControlsDrawer;
d _dockMagnifiedHeightDelta;
@"UISlider" _playbackSlider;
@"UIView" _previewControlsContainerView;
@"CFXPlayButtonView" _playButton;
@"CFXMediaItem" _mediaItem;
@"CFXClipPlayerViewController" _previewPlayer;
@"JFXCompositionExporter" _exporter;
@"JFXEffectsPreviewGenerator" _stillImagePreviewGenerator;
@"JFXOrientationMonitor" _orientationMonitor;
@"CFXEffectEditorView" _effectEditor;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",W,N,V_playerContainerView) playerContainerView;
@property (T@"UIView",W,N,V_appStripAndPreviewControlsContainer) appStripAndPreviewControlsContainer;
@property (T@"UIButton",W,N,V_exportButton) exportButton;
@property (T@"NSLayoutConstraint",&,N,V_previewControlsContainerHeightConstraint) previewControlsContainerHeightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_previewControlsContainerWidthConstraint) previewControlsContainerWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_previewControlsContainerTrailingConstraint) previewControlsContainerTrailingConstraint;
@property (T@"NSLayoutConstraint",&,N,V_previewControlsContainerLeadingConstraint) previewControlsContainerLeadingConstraint;
@property (T@"NSLayoutConstraint",&,N,V_previewControlsContainerTopConstraint) previewControlsContainerTopConstraint;
@property (TB,N,GuserInterfaceIsHidden,V_userInterfaceHidden) userInterfaceHidden;
@property (TB,N,V_saveMediaItemToFunCamPhotosAlbumUponExport) saveMediaItemToFunCamPhotosAlbumUponExport;
@property (TQ,N,V_appliedDirectOverlayEditingGestures) appliedDirectOverlayEditingGestures;
@property (T@"UIView",&,N,V_bottomControlsDrawer) bottomControlsDrawer;
@property (TB,N,V_dockIsMagnified) dockIsMagnified;
@property (Td,N,V_dockMagnifiedHeightDelta) dockMagnifiedHeightDelta;
@property (T@"CFXEffectBrowserContentPresenterViewController",&,N,V_effectBrowserContentPresenterViewController) effectBrowserContentPresenterViewController;
@property (T@"UISlider",&,N,V_playbackSlider) playbackSlider;
@property (T@"UIView",W,N,V_previewControlsContainerView) previewControlsContainerView;
@property (T@"CFXPlayButtonView",W,N,V_playButton) playButton;
@property (T@"CFXMediaItem",&,N,V_mediaItem) mediaItem;
@property (T@"CFXClip",R,N) previewClip;
@property (T@"CFXClipPlayerViewController",&,N,V_previewPlayer) previewPlayer;
@property (T@"JFXCompositionExporter",&,N,V_exporter) exporter;
@property (T@"JFXEffectsPreviewGenerator",&,N,V_stillImagePreviewGenerator) stillImagePreviewGenerator;
@property (T@"JFXOrientationMonitor",&,N,V_orientationMonitor) orientationMonitor;
@property (T@"CFXEffectEditorView",&,N,V_effectEditor) effectEditor;
@property (T{?=dd},R,N) normalizedMinimumHitTestArea;
@property (T@"<CFXPreviewViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView",&,N) effectsPickerDrawer;
@property (TB,N,GisPresentingFilterPicker,V_presentingFilterPicker) presentingFilterPicker;
@property (TB,N,V_capturedWithBackCamera) capturedWithBackCamera;
@property (T@"CFXControlsViewController",W,N,V_previewControls) previewControls;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CFXPreviewViewController liveCaptureSnapshotView];
+[CFXPreviewViewController setLiveCaptureSnapshotView:];
```

## Instance methods

```
-[CFXPreviewViewController mediaItem];
-[CFXPreviewViewController viewDidLoad];
-[CFXPreviewViewController viewDidLayoutSubviews];
-[CFXPreviewViewController viewWillAppear:];
-[CFXPreviewViewController setDelegate:];
-[CFXPreviewViewController viewDidAppear:];
-[CFXPreviewViewController setPlayButton:];
-[CFXPreviewViewController delegate];
-[CFXPreviewViewController viewDidDisappear:];
-[CFXPreviewViewController playButton];
-[CFXPreviewViewController prepareForSegue:sender:];
-[CFXPreviewViewController setMediaItem:];
-[CFXPreviewViewController setEffectsPickerDrawer:];
-[CFXPreviewViewController CFX_addEffect:];
-[CFXPreviewViewController displayEffectEditorForEffect:forMode:];
-[CFXPreviewViewController effectEditorView:didRemoveEffect:];
-[CFXPreviewViewController fullScreenTextEditViewController:didFinishEditingByRemovingEffect:];
-[CFXPreviewViewController presentFullScreenTextEditorForEffect:insertingEffect:];
-[CFXPreviewViewController removeEffectEditor];
-[CFXPreviewViewController CFX_AVAssetExportPresetWithColorSpace:];
-[CFXPreviewViewController CFX_addAssetAtURL:resourceType:completionHandler:];
-[CFXPreviewViewController CFX_canApplyFaceTracking];
-[CFXPreviewViewController CFX_createAlbumWithCompletionHandler:];
-[CFXPreviewViewController CFX_hidePreviewUI];
-[CFXPreviewViewController CFX_prepareFaceTrackingDataForOverlayInsertionWithCompletion:];
-[CFXPreviewViewController CFX_previewPlayerCurrentTime];
-[CFXPreviewViewController CFX_saveImageToURL:image:compressionQuality:asHEIF:metadata:];
-[CFXPreviewViewController CFX_setFrameAndRenderSizes];
-[CFXPreviewViewController CFX_showPreviewUI];
-[CFXPreviewViewController CFX_togglePreviewUI];
-[CFXPreviewViewController effectEditorView:effectAtPoint:];
-[CFXPreviewViewController previewControls];
-[CFXPreviewViewController CFX_addAssetWithIdentifier:intoAlbum:completionHandler:];
-[CFXPreviewViewController CFX_addURLToCameraRoll:isStill:completionHandler:];
-[CFXPreviewViewController CFX_exportPhotoWithEffects];
-[CFXPreviewViewController CFX_fetchAssetWithLocalIdentifier:];
-[CFXPreviewViewController CFX_layoutPlayerContainerView];
-[CFXPreviewViewController CFX_notifyDelegateExportMediaItemFinishedWithError:];
-[CFXPreviewViewController CFX_setEffectAnimationsEnabledIfPossible:updatePlayer:];
-[CFXPreviewViewController CFX_setIsExporting:];
-[CFXPreviewViewController dockIsMagnified];
-[CFXPreviewViewController effectEditorView:didTransformEffect:transform:relativeToBounds:];
-[CFXPreviewViewController effectEditorView:textForEffect:];
-[CFXPreviewViewController JFX_orientationMonitorInterfaceOrientationNotification:];
-[CFXPreviewViewController isEditingEffect];
-[CFXPreviewViewController addEffect:completion:];
-[CFXPreviewViewController addOverlayEffect:atScreenLocation:atScreenSize:rotationAngle:completion:];
-[CFXPreviewViewController animationDurationForCompositionTransition:shouldScale:];
-[CFXPreviewViewController appStripAndPreviewControlsContainer];
-[CFXPreviewViewController appliedDirectOverlayEditingGestures];
-[CFXPreviewViewController bottomControlsBounds];
-[CFXPreviewViewController bottomControlsCenter];
-[CFXPreviewViewController bottomControlsDrawer];
-[CFXPreviewViewController bottomControlsSnapshot];
-[CFXPreviewViewController capturedWithBackCamera];
-[CFXPreviewViewController configureBottomControlsForOrientation];
-[CFXPreviewViewController configureUIForOrientation];
-[CFXPreviewViewController didFinishExport:];
-[CFXPreviewViewController dispatchWhenPlayerReadyForDisplayEffectUpdate:];
-[CFXPreviewViewController dockMagnifiedHeightDelta];
-[CFXPreviewViewController effectBrowserContentPresenterViewController];
-[CFXPreviewViewController effectEditor];
-[CFXPreviewViewController effectEditorView:didBeginEditingTextForEffect:];
-[CFXPreviewViewController effectEditorView:didEditTextForEffect:newText:];
-[CFXPreviewViewController effectEditorView:didEndEditingByTappingOutSideEffectAtScreenPoint:];
-[CFXPreviewViewController effectEditorView:didEndEditingTextForEffect:wasCancelled:];
-[CFXPreviewViewController effectEditorView:didMoveEffect:withTouchPoint:];
-[CFXPreviewViewController effectEditorView:frameForEffect:relativeToBounds:];
-[CFXPreviewViewController effectEditorView:hitAreaBoundingFrameForEffect:adjustForMinimumSize:relativeToBounds:];
-[CFXPreviewViewController effectEditorView:isEffectAtPoint:effect:];
-[CFXPreviewViewController effectEditorView:isFaceTrackingDataAvailableForEffect:];
-[CFXPreviewViewController effectEditorView:isFaceTrackingEffect:];
-[CFXPreviewViewController effectEditorView:maximumTextLengthForEffect:];
-[CFXPreviewViewController effectEditorView:overlayEffectFrameForEffect:relativeToBounds:];
-[CFXPreviewViewController effectEditorView:presentCustomTextEditingUI:];
-[CFXPreviewViewController effectEditorView:removeButtonPositionForEffect:relativeToBounds:];
-[CFXPreviewViewController effectEditorView:shouldEditTextForEffect:];
-[CFXPreviewViewController effectEditorView:spacingBetweenCenterPointOfEffect:point:relativeToBounds:];
-[CFXPreviewViewController effectEditorView:textEditingPropertiesForEffect:relativeToBounds:];
-[CFXPreviewViewController effectEditorViewDidBeginEditing:];
-[CFXPreviewViewController effectEditorViewDidEndEditing:];
-[CFXPreviewViewController effectEditorViewShouldShowFaceReticle:];
-[CFXPreviewViewController effectsPickerDrawer];
-[CFXPreviewViewController exportButton];
-[CFXPreviewViewController exportButtonTapped:];
-[CFXPreviewViewController exportMediaItemToFileURL:];
-[CFXPreviewViewController exportProgressedTo:];
-[CFXPreviewViewController exporter];
-[CFXPreviewViewController faceTrackingInterfaceOrientationForfullScreenTextEditViewController:];
-[CFXPreviewViewController filterPickerPreviewBackgroundImageAtSizeInPixels:completion:];
-[CFXPreviewViewController fullScreenTextEditViewController:didBeginAnimationBeforeEditingEffect:completion:];
-[CFXPreviewViewController fullScreenTextEditViewController:didBeginEditingEffect:];
-[CFXPreviewViewController fullScreenTextEditViewController:didFinishAnimationAfterEditingEffect:completion:];
-[CFXPreviewViewController fullScreenTextEditViewController:didFinishEditingEffect:withUpdatedText:];
-[CFXPreviewViewController fullScreenTextEditViewController:willBeginAnimationAfterEditingEffect:updatedText:];
-[CFXPreviewViewController fullScreenTextEditViewController:willBeginAnimationBeforeEditingEffect:];
-[CFXPreviewViewController hideBottomControls];
-[CFXPreviewViewController isPresentingFilterPicker];
-[CFXPreviewViewController normalizedMinimumHitTestArea];
-[CFXPreviewViewController orientationMonitor];
-[CFXPreviewViewController playButtonViewDidTapPause:];
-[CFXPreviewViewController playButtonViewDidTapPlay:];
-[CFXPreviewViewController playbackAreaDoubleTapped:];
-[CFXPreviewViewController playbackAreaPanned:gesture:normalizedClipPoint:normalizedMinimumSize:translationDelta:atTime:timeScale:];
-[CFXPreviewViewController playbackAreaPinched:gesture:normalizedClipPoints:normalizedCenterPoint:normalizedMinimumSize:scaleDelta:atTime:timeScale:];
-[CFXPreviewViewController playbackAreaRotated:gesture:normalizedClipPoints:normalizedCenterPoint:normalizedMinimumSize:rotateDelta:atTime:];
-[CFXPreviewViewController playbackAreaTapped:normalizedClipPoint:normalizedMinimumSize:atTime:];
-[CFXPreviewViewController playbackDidStart:];
-[CFXPreviewViewController playbackDidStop:currentTime:];
-[CFXPreviewViewController playbackSlider];
-[CFXPreviewViewController playbackSliderValueChanged:];
-[CFXPreviewViewController playbackTimeDidChange:currentTime:];
-[CFXPreviewViewController playerContainerView];
-[CFXPreviewViewController playerContentFrame];
-[CFXPreviewViewController previewClip];
-[CFXPreviewViewController previewControlsContainerHeightConstraint];
-[CFXPreviewViewController previewControlsContainerLeadingConstraint];
-[CFXPreviewViewController previewControlsContainerTopConstraint];
-[CFXPreviewViewController previewControlsContainerTrailingConstraint];
-[CFXPreviewViewController previewControlsContainerView];
-[CFXPreviewViewController previewControlsContainerWidthConstraint];
-[CFXPreviewViewController previewPlayer];
-[CFXPreviewViewController saveMediaItemToFunCamPhotosAlbumUponExport];
-[CFXPreviewViewController scaleClip:scale:atNormalizedLocation:];
-[CFXPreviewViewController setAppStripAndPreviewControlsContainer:];
-[CFXPreviewViewController setAppliedDirectOverlayEditingGestures:];
-[CFXPreviewViewController setBottomControlsDrawer:];
-[CFXPreviewViewController setCapturedWithBackCamera:];
-[CFXPreviewViewController setDockIsMagnified:];
-[CFXPreviewViewController setDockMagnifiedHeightDelta:];
-[CFXPreviewViewController setEffectAnimationsEnabledIfPossible:];
-[CFXPreviewViewController setEffectBrowserContentPresenterViewController:];
-[CFXPreviewViewController setEffectEditor:];
-[CFXPreviewViewController setExportButton:];
-[CFXPreviewViewController setExporter:];
-[CFXPreviewViewController setOrientationMonitor:];
-[CFXPreviewViewController setPlayButtonHiddenIfPossible:];
-[CFXPreviewViewController setPlaybackSlider:];
-[CFXPreviewViewController setPlayerContainerView:];
-[CFXPreviewViewController setPresentingFilterPicker:];
-[CFXPreviewViewController setPreviewControls:];
-[CFXPreviewViewController setPreviewControlsContainerHeightConstraint:];
-[CFXPreviewViewController setPreviewControlsContainerLeadingConstraint:];
-[CFXPreviewViewController setPreviewControlsContainerTopConstraint:];
-[CFXPreviewViewController setPreviewControlsContainerTrailingConstraint:];
-[CFXPreviewViewController setPreviewControlsContainerView:];
-[CFXPreviewViewController setPreviewControlsContainerWidthConstraint:];
-[CFXPreviewViewController setPreviewPlayer:];
-[CFXPreviewViewController setSaveMediaItemToFunCamPhotosAlbumUponExport:];
-[CFXPreviewViewController setStillImagePreviewGenerator:];
-[CFXPreviewViewController setUserInterfaceHidden:];
-[CFXPreviewViewController shouldExportOnly];
-[CFXPreviewViewController shouldKeepPlayButtonHidden];
-[CFXPreviewViewController shouldUseFaceTracking];
-[CFXPreviewViewController showBottomControls];
-[CFXPreviewViewController stillImagePreviewGenerator];
-[CFXPreviewViewController updateEffectEditorLayout];
-[CFXPreviewViewController updateFullScreenTextEditorLayout];
-[CFXPreviewViewController updateUIForDockMagnify:dockHeightDelta:];
-[CFXPreviewViewController userInterfaceIsHidden];
-[CFXPreviewViewController view:willMoveToWindow:];
```
