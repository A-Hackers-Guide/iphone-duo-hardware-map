# `CAMTopBar`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 16 instance variables, 16 properties, 47 instance methods, 1 class methods

## Instance variables

```
B _floating;
@"<CAMControlVisibilityUpdateDelegate>" _visibilityUpdateDelegate;
q _style;
q _backgroundStyle;
@"CAMFlashButton" _flashButton;
@"CAMElapsedTimeView" _elapsedTimeView;
@"CAMHDRButton" _HDRButton;
@"CAMFlipButton" _flipButton;
@"CEKApertureButton" _apertureButton;
@"CAMIntensityButton" _intensityButton;
@"CAMTimerButton" _timerButton;
@"CAMLivePhotoButton" _livePhotoButton;
@"CAMSharedLibraryButton" _sharedLibraryButton;
@"PUReviewScreenDoneButton" _doneButton;
@"CAMVideoConfigurationStatusIndicator" _videoConfigurationStatusIndicator;
q _orientation;
```

## Properties

```
@property (T@"<CAMControlVisibilityUpdateDelegate>",W,N,V_visibilityUpdateDelegate) visibilityUpdateDelegate;
@property (Tq,N,V_style) style;
@property (Tq,N,V_backgroundStyle) backgroundStyle;
@property (T@"CAMFlashButton",&,N,V_flashButton) flashButton;
@property (T@"CAMElapsedTimeView",&,N,V_elapsedTimeView) elapsedTimeView;
@property (T@"CAMHDRButton",&,N,V_HDRButton) HDRButton;
@property (T@"CAMFlipButton",&,N,V_flipButton) flipButton;
@property (T@"CEKApertureButton",&,N,V_apertureButton) apertureButton;
@property (T@"CAMIntensityButton",&,N,V_intensityButton) intensityButton;
@property (T@"CAMTimerButton",&,N,V_timerButton) timerButton;
@property (T@"CAMLivePhotoButton",&,N,V_livePhotoButton) livePhotoButton;
@property (T@"CAMSharedLibraryButton",&,N,V_sharedLibraryButton) sharedLibraryButton;
@property (T@"PUReviewScreenDoneButton",&,N,V_doneButton) doneButton;
@property (T@"CAMVideoConfigurationStatusIndicator",&,N,V_videoConfigurationStatusIndicator) videoConfigurationStatusIndicator;
@property (Tq,N,V_orientation) orientation;
@property (TB,R,N,GisFloating,V_floating) floating;
```

## Class methods

```
+[CAMTopBar isFloatingStyle:];
```

## Instance methods

```
-[CAMTopBar setOrientation:];
-[CAMTopBar isFloating];
-[CAMTopBar setDoneButton:];
-[CAMTopBar doneButton];
-[CAMTopBar setStyle:animated:];
-[CAMTopBar orientation];
-[CAMTopBar elapsedTimeView];
-[CAMTopBar style];
-[CAMTopBar setStyle:];
-[CAMTopBar backgroundStyle];
-[CAMTopBar initWithCoder:];
-[CAMTopBar initWithFrame:];
-[CAMTopBar setBackgroundStyle:animated:];
-[CAMTopBar setBackgroundStyle:];
-[CAMTopBar livePhotoButton];
-[CAMTopBar apertureButton];
-[CAMTopBar flipButton];
-[CAMTopBar setApertureButton:];
-[CAMTopBar setFlipButton:];
-[CAMTopBar HDRButton];
-[CAMTopBar setFlashButton:];
-[CAMTopBar intensityButton];
-[CAMTopBar setTimerButton:];
-[CAMTopBar configureForMode:];
-[CAMTopBar configureForMode:animated:];
-[CAMTopBar flashButton];
-[CAMTopBar setElapsedTimeView:];
-[CAMTopBar setHDRButton:];
-[CAMTopBar setIntensityButton:];
-[CAMTopBar setLivePhotoButton:];
-[CAMTopBar setSharedLibraryButton:];
-[CAMTopBar setVideoConfigurationStatusIndicator:];
-[CAMTopBar setVisibilityUpdateDelegate:];
-[CAMTopBar sharedLibraryButton];
-[CAMTopBar shouldHideApertureButtonForGraphConfiguration:];
-[CAMTopBar shouldHideDoneButtonForGraphConfiguration:];
-[CAMTopBar shouldHideElapsedTimeViewForGraphConfiguration:];
-[CAMTopBar shouldHideFlashButtonForGraphConfiguration:];
-[CAMTopBar shouldHideFlipButtonForGraphConfiguration:];
-[CAMTopBar shouldHideHDRButtonForGraphConfiguration:];
-[CAMTopBar shouldHideIntensityButtonForGraphConfiguration:];
-[CAMTopBar shouldHideLivePhotoButtonForGraphConfiguration:];
-[CAMTopBar shouldHideSharedLibraryButtonForGraphConfiguration:];
-[CAMTopBar shouldHideTimerButtonForGraphConfiguration:];
-[CAMTopBar timerButton];
-[CAMTopBar videoConfigurationStatusIndicator];
-[CAMTopBar visibilityUpdateDelegate];
```
