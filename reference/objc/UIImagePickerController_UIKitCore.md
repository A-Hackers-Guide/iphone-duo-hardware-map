# `UIImagePickerController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UINavigationController`
- Protocols: `_UIRemoteViewControllerContaining`, `NSCoding`
- 19 instance variables, 22 properties, 115 instance methods, 7 class methods

## Instance variables

```
q _sourceType;
@ _image;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _cropRect;
@"NSArray" _mediaTypes;
@"NSMutableDictionary" _properties;
i _previousStatusBarStyle;
B _previousStatusBarHidden;
# _photoPickerRequestOptionsClass;
@? _photoPickerDisplayCompletion;
@? _photoPickerPreviewDisplayCompletion;
B _photoPickerDidStartDelayingPresentation;
B _photoPickerDidEndDelayingPresentation;
B _photoPickerIsPreheating;
B _photoPickerIsReadyForDisplay;
B _photoPickerViewControllerIsConnected;
@"UIViewController" _photoPickerPreheatedViewController;
{?="visible"b1"isCleaningUp"b1"didRevertStatusBar"b1} _imagePickerFlags;
Q _savingOptions;
@"NSExtension" _photosExtension;
```

## Properties

```
@property (T@"NSExtension",&,N,V_photosExtension) photosExtension;
@property (T#,R,N) photoPickerRequestOptionsClass;
@property (T@"<UINavigationControllerDelegate><UIImagePickerControllerDelegate>",W,D,N) delegate;
@property (Tq,N) sourceType;
@property (T@"NSArray",C,N) mediaTypes;
@property (TB,N) allowsEditing;
@property (TB,N) allowsImageEditing;
@property (Tq,N) imageExportPreset;
@property (Td,N) videoMaximumDuration;
@property (Tq,N) videoQuality;
@property (T@"NSString",C,N) videoExportPreset;
@property (TB,N) showsCameraControls;
@property (T@"UIView",&,N) cameraOverlayView;
@property (T{CGAffineTransform=dddddd},N) cameraViewTransform;
@property (Tq,N) cameraCaptureMode;
@property (Tq,N) cameraDevice;
@property (Tq,N) cameraFlashMode;
@property (T@"_UIRemoteViewController",R,N) _containedRemoteViewController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIImagePickerController _isMediaTypeAvailable:forSource:];
+[UIImagePickerController _reviewCapturedItems];
+[UIImagePickerController availableCaptureModesForCameraDevice:];
+[UIImagePickerController availableMediaTypesForSourceType:];
+[UIImagePickerController isCameraDeviceAvailable:];
+[UIImagePickerController isFlashAvailableForCameraDevice:];
+[UIImagePickerController isSourceTypeAvailable:];
```

## Instance methods

```
-[UIImagePickerController videoQuality];
-[UIImagePickerController setVideoQuality:];
-[UIImagePickerController mediaTypes];
-[UIImagePickerController shouldAutorotateToInterfaceOrientation:];
-[UIImagePickerController init];
-[UIImagePickerController viewWillDisappear:];
-[UIImagePickerController supportedInterfaceOrientations];
-[UIImagePickerController _containedRemoteViewController];
-[UIImagePickerController _setValue:forProperty:];
-[UIImagePickerController sourceType];
-[UIImagePickerController _properties];
-[UIImagePickerController setVideoExportPreset:];
-[UIImagePickerController setAllowsEditing:];
-[UIImagePickerController setSourceType:];
-[UIImagePickerController videoExportPreset];
-[UIImagePickerController viewWillAppear:];
-[UIImagePickerController allowsEditing];
-[UIImagePickerController encodeWithCoder:];
-[UIImagePickerController viewDidDisappear:];
-[UIImagePickerController initWithCoder:];
-[UIImagePickerController _preferredModalPresentationStyle];
-[UIImagePickerController photosExtension];
-[UIImagePickerController _adjustedContentSizeForPopover:];
-[UIImagePickerController _setAllowsIris:];
-[UIImagePickerController _setProperties:];
-[UIImagePickerController _testPerformPreviewOfFirstPhoto];
-[UIImagePickerController cameraFlashMode];
-[UIImagePickerController _allowsImageEditing];
-[UIImagePickerController _allowsIris];
-[UIImagePickerController _allowsMultipleSelection];
-[UIImagePickerController _autoDismiss];
-[UIImagePickerController _cameraViewController];
-[UIImagePickerController _convertAutoloopsToGIF];
-[UIImagePickerController _createInitialControllerWithCompletion:];
-[UIImagePickerController _didRevertStatusBar];
-[UIImagePickerController _handleEndingPhotoPickerPresentationDelay];
-[UIImagePickerController _handleInstantiatedRemoteViewController:request:error:completion:];
-[UIImagePickerController _handleMatchingExtension:viewControllerClassName:completion:];
-[UIImagePickerController _handlePushViewController:];
-[UIImagePickerController _handleTopViewControllerReadyForDisplay:];
-[UIImagePickerController _imagePickerDidCancel];
-[UIImagePickerController _imagePickerDidCompleteWithInfo:];
-[UIImagePickerController _imagePickerDidCompleteWithInfoArray:];
-[UIImagePickerController _imagePickerSavingOptions];
-[UIImagePickerController _initWithSourceImageData:cropRect:];
-[UIImagePickerController _initializeProperties];
-[UIImagePickerController _invalidatePhotoPickerServices];
-[UIImagePickerController _isCameraCaptureModeValid:];
-[UIImagePickerController _isSupportedInterfaceOrientation:];
-[UIImagePickerController _multipleSelectionLimit];
-[UIImagePickerController _onlyShowAutoloops];
-[UIImagePickerController _photoPickerDisplayCompletion];
-[UIImagePickerController _photoPickerPreviewDisplayCompletion];
-[UIImagePickerController _populateArchivedChildViewControllers:];
-[UIImagePickerController _propertiesForPhotoPickerExtension];
-[UIImagePickerController _removeAllChildren];
-[UIImagePickerController _requiresPickingConfirmation];
-[UIImagePickerController _setAllowsImageEditing:];
-[UIImagePickerController _setAllowsMultipleSelection:];
-[UIImagePickerController _setConvertAutoloopsToGIF:];
-[UIImagePickerController _setImagePickerSavingOptions:];
-[UIImagePickerController _setMultipleSelectionLimit:];
-[UIImagePickerController _setOnlyShowAutoloops:];
-[UIImagePickerController _setPhotoPickerDisplayCompletion:];
-[UIImagePickerController _setPhotoPickerPreviewDisplayCompletion:];
-[UIImagePickerController _setRequiresPickingConfirmation:];
-[UIImagePickerController _setShowsFileSizePicker:];
-[UIImagePickerController _setShowsPrompt:];
-[UIImagePickerController _setStaticPrompt:];
-[UIImagePickerController _setTargetForPrompt:];
-[UIImagePickerController _setupControllersForCurrentMediaTypes];
-[UIImagePickerController _setupControllersForCurrentSourceTypeWithCompletion:];
-[UIImagePickerController _shouldDelayPresentation];
-[UIImagePickerController _showsFileSizePicker];
-[UIImagePickerController _showsPrompt];
-[UIImagePickerController _sourceTypeIsCamera];
-[UIImagePickerController _stagedPhotoPickerIsReadyForDisplay];
-[UIImagePickerController _staticPrompt];
-[UIImagePickerController _targetForPrompt];
-[UIImagePickerController _updateCameraCaptureMode];
-[UIImagePickerController _valueForProperty:];
-[UIImagePickerController _viewControllerPresentationDidInitiate];
-[UIImagePickerController allowsImageEditing];
-[UIImagePickerController cameraCaptureMode];
-[UIImagePickerController cameraDevice];
-[UIImagePickerController cameraOverlayView];
-[UIImagePickerController cameraViewTransform];
-[UIImagePickerController cancelPhotoPicker];
-[UIImagePickerController didDisplayPhotoPickerPreview];
-[UIImagePickerController didDisplayPhotoPickerSourceType:];
-[UIImagePickerController didSelectMediaWithInfoDictionary:];
-[UIImagePickerController didSelectMultipleMediaItemsWithInfoDictionaries:];
-[UIImagePickerController dismissCurrentViewControllerFromPhotoPickerAnimated:];
-[UIImagePickerController imageExportPreset];
-[UIImagePickerController photoPickerIsReadyForDisplay];
-[UIImagePickerController photoPickerRequestOptionsClass];
-[UIImagePickerController setAllowsImageEditing:];
-[UIImagePickerController setCameraCaptureMode:];
-[UIImagePickerController setCameraDevice:];
-[UIImagePickerController setCameraFlashMode:];
-[UIImagePickerController setCameraOverlayView:];
-[UIImagePickerController setCameraViewTransform:];
-[UIImagePickerController setImageExportPreset:];
-[UIImagePickerController setMediaTypes:];
-[UIImagePickerController setPhotoPickerViewControllerTitle:];
-[UIImagePickerController setPhotosExtension:];
-[UIImagePickerController setShowsCameraControls:];
-[UIImagePickerController setVideoMaximumDuration:];
-[UIImagePickerController showsCameraControls];
-[UIImagePickerController startVideoCapture];
-[UIImagePickerController stopVideoCapture];
-[UIImagePickerController takePicture];
-[UIImagePickerController updateContentUnavailableConfigurationUsingState:];
-[UIImagePickerController videoMaximumDuration];
-[UIImagePickerController viewWillUnload];
```
