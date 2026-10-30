# `CAMBottomBar`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 19 instance variables, 19 properties, 41 instance methods, 3 class methods

## Instance variables

```
q _layoutStyle;
q _backgroundStyle;
@"UIView" _backgroundView;
@"<CAMControlVisibilityUpdateDelegate>" _visibilityUpdateDelegate;
@"CUShutterButton" _shutterButton;
@"CUShutterButton" _stillDuringVideoButton;
@"CAMImageWell" _imageWell;
@"UIButton" _reviewButton;
@"UIButton" _creativeCameraButton;
@"PUReviewScreenDoneButton" _doneButton;
@"CAMFlipButton" _flipButton;
@"CAMFlashButton" _flashButton;
@"CAMHDRButton" _HDRButton;
@"CAMTimerButton" _timerButton;
@"CAMLivePhotoButton" _livePhotoButton;
@"CAMSharedLibraryButton" _sharedLibraryButton;
@"CEKApertureButton" _apertureButton;
@"CAMImageAnalysisButton" _imageAnalysisButton;
@"UIView" _imageAnalysisButtonBackgroundOverlay;
```

## Properties

```
@property (Tq,N,V_layoutStyle) layoutStyle;
@property (Tq,N,V_backgroundStyle) backgroundStyle;
@property (T@"UIView",R,N,V_backgroundView) backgroundView;
@property (T@"<CAMControlVisibilityUpdateDelegate>",W,N,V_visibilityUpdateDelegate) visibilityUpdateDelegate;
@property (T@"CUShutterButton",&,N,V_shutterButton) shutterButton;
@property (T@"CUShutterButton",&,N,V_stillDuringVideoButton) stillDuringVideoButton;
@property (T@"CAMImageWell",&,N,V_imageWell) imageWell;
@property (T@"UIButton",&,N,V_reviewButton) reviewButton;
@property (T@"UIButton",&,N,V_creativeCameraButton) creativeCameraButton;
@property (T@"PUReviewScreenDoneButton",&,N,V_doneButton) doneButton;
@property (T@"CAMFlipButton",&,N,V_flipButton) flipButton;
@property (T@"CAMFlashButton",&,N,V_flashButton) flashButton;
@property (T@"CAMHDRButton",&,N,V_HDRButton) HDRButton;
@property (T@"CAMTimerButton",&,N,V_timerButton) timerButton;
@property (T@"CAMLivePhotoButton",&,N,V_livePhotoButton) livePhotoButton;
@property (T@"CAMSharedLibraryButton",&,N,V_sharedLibraryButton) sharedLibraryButton;
@property (T@"CEKApertureButton",&,N,V_apertureButton) apertureButton;
@property (T@"CAMImageAnalysisButton",&,N,V_imageAnalysisButton) imageAnalysisButton;
@property (T@"UIView",&,N,V_imageAnalysisButtonBackgroundOverlay) imageAnalysisButtonBackgroundOverlay;
```

## Class methods

```
+[CAMBottomBar wantsVerticalBarForLayoutStyle:];
+[CAMBottomBar shouldUseSafeAreaInsetForLayoutStyle:traitCollection:];
+[CAMBottomBar shutterButtonAlignmentRectInBounds:forLayoutStyle:traitCollection:safeAreaInsets:];
```

## Instance methods

```
-[CAMBottomBar setLayoutStyle:];
-[CAMBottomBar layoutStyle];
-[CAMBottomBar setDoneButton:];
-[CAMBottomBar doneButton];
-[CAMBottomBar imageAnalysisButton];
-[CAMBottomBar initWithLayoutStyle:];
-[CAMBottomBar backgroundStyle];
-[CAMBottomBar backgroundView];
-[CAMBottomBar setImageAnalysisButton:];
-[CAMBottomBar initWithCoder:];
-[CAMBottomBar initWithFrame:];
-[CAMBottomBar setBackgroundStyle:animated:];
-[CAMBottomBar setBackgroundStyle:];
-[CAMBottomBar shutterButton];
-[CAMBottomBar livePhotoButton];
-[CAMBottomBar apertureButton];
-[CAMBottomBar flipButton];
-[CAMBottomBar setApertureButton:];
-[CAMBottomBar setFlipButton:];
-[CAMBottomBar HDRButton];
-[CAMBottomBar setFlashButton:];
-[CAMBottomBar setTimerButton:];
-[CAMBottomBar creativeCameraButton];
-[CAMBottomBar flashButton];
-[CAMBottomBar imageAnalysisButtonBackgroundOverlay];
-[CAMBottomBar imageWell];
-[CAMBottomBar reviewButton];
-[CAMBottomBar setCreativeCameraButton:];
-[CAMBottomBar setHDRButton:];
-[CAMBottomBar setImageAnalysisButtonBackgroundOverlay:];
-[CAMBottomBar setImageWell:];
-[CAMBottomBar setLivePhotoButton:];
-[CAMBottomBar setReviewButton:];
-[CAMBottomBar setSharedLibraryButton:];
-[CAMBottomBar setShutterButton:];
-[CAMBottomBar setStillDuringVideoButton:];
-[CAMBottomBar setVisibilityUpdateDelegate:];
-[CAMBottomBar sharedLibraryButton];
-[CAMBottomBar stillDuringVideoButton];
-[CAMBottomBar timerButton];
-[CAMBottomBar visibilityUpdateDelegate];
```
