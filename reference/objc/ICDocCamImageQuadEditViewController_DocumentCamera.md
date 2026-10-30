# `ICDocCamImageQuadEditViewController`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIScrollViewDelegate`, `ICDocCamImageQuadEditOverlayDelegate`, `DCUnsavedDataDelegate`
- 28 instance variables, 32 properties, 93 instance methods, 0 class methods

## Instance variables

```
B _showImageAsAspectFit;
B _inCaptureMode;
B _didAdjustQuad;
B _shouldAdjustForApectFitIfNecessary;
B _didPressSave;
B _didCallCompletion;
@"UIScrollView" _scrollView;
@"ICDocCamImageQuadEditImageView" _imageView;
@"ICDocCamImageQuadEditImageView" _backgroundImageView;
@"ICDocCamImageQuadEditOverlay" _overlay;
d _knobHeight;
@"UIColor" _knobColor;
@"DCPlacardView" _placard;
@"UINavigationBar" _captureNavigationBar;
@"UINavigationItem" _captureNavigationItem;
@"UIBarButtonItem" _cancelBarButtonItem;
@"UIBarButtonItem" _doneBarButtonItem;
@"UIImage" _image;
@"<DCScanDataDelegate>" _scanDataDelegate;
@"CAShapeLayer" _overlayMask;
@"UIBezierPath" _overlayMaskPath;
@"ICDocCamImageQuad" _quad;
@"ICDocCamImageQuad" _initialQuad;
q _orientation;
@? _completionHandler;
@"NSNumber" _startOrientationIsPortrait;
@"NSLayoutConstraint" _placardTopConstraint;
@"UINavigationBar" _quadEditNavigationBar;
```

## Properties

```
@property (T@"UIScrollView",&,N,V_scrollView) scrollView;
@property (T@"ICDocCamImageQuadEditImageView",&,N,V_imageView) imageView;
@property (T@"ICDocCamImageQuadEditImageView",&,N,V_backgroundImageView) backgroundImageView;
@property (T@"CAShapeLayer",&,N,V_overlayMask) overlayMask;
@property (T@"UIBezierPath",&,N,V_overlayMaskPath) overlayMaskPath;
@property (T@"ICDocCamImageQuad",&,N,V_quad) quad;
@property (T@"ICDocCamImageQuad",&,N,V_initialQuad) initialQuad;
@property (Tq,N,V_orientation) orientation;
@property (T@?,C,N,V_completionHandler) completionHandler;
@property (T@"NSNumber",&,N,V_startOrientationIsPortrait) startOrientationIsPortrait;
@property (TB,N,V_didAdjustQuad) didAdjustQuad;
@property (TB,N,V_shouldAdjustForApectFitIfNecessary) shouldAdjustForApectFitIfNecessary;
@property (TB,N,V_didPressSave) didPressSave;
@property (TB,N,V_didCallCompletion) didCallCompletion;
@property (T@"DCPlacardView",&,N,V_placard) placard;
@property (T@"NSLayoutConstraint",&,N,V_placardTopConstraint) placardTopConstraint;
@property (T@"UINavigationBar",&,N,V_quadEditNavigationBar) quadEditNavigationBar;
@property (T@"ICDocCamImageQuadEditOverlay",&,N,V_overlay) overlay;
@property (Td,R,N,V_knobHeight) knobHeight;
@property (T@"UIColor",R,N,V_knobColor) knobColor;
@property (T@"UINavigationBar",&,N,V_captureNavigationBar) captureNavigationBar;
@property (T@"UINavigationItem",&,N,V_captureNavigationItem) captureNavigationItem;
@property (T@"UIBarButtonItem",&,N,V_cancelBarButtonItem) cancelBarButtonItem;
@property (T@"UIBarButtonItem",&,N,V_doneBarButtonItem) doneBarButtonItem;
@property (T@"UIImage",R,N,V_image) image;
@property (T@"<DCScanDataDelegate>",R,N,V_scanDataDelegate) scanDataDelegate;
@property (TB,N,V_showImageAsAspectFit) showImageAsAspectFit;
@property (TB,N,V_inCaptureMode) inCaptureMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[ICDocCamImageQuadEditViewController setOrientation:];
-[ICDocCamImageQuadEditViewController cancelBarButtonItem];
-[ICDocCamImageQuadEditViewController setCompletionHandler:];
-[ICDocCamImageQuadEditViewController applicationWillResignActive:];
-[ICDocCamImageQuadEditViewController completionHandler];
-[ICDocCamImageQuadEditViewController setOverlay:];
-[ICDocCamImageQuadEditViewController scrollViewDidEndZooming:withView:atScale:];
-[ICDocCamImageQuadEditViewController viewForZoomingInScrollView:];
-[ICDocCamImageQuadEditViewController setImageView:];
-[ICDocCamImageQuadEditViewController scrollView];
-[ICDocCamImageQuadEditViewController orientation];
-[ICDocCamImageQuadEditViewController dealloc];
-[ICDocCamImageQuadEditViewController viewDidLoad];
-[ICDocCamImageQuadEditViewController setScrollView:];
-[ICDocCamImageQuadEditViewController viewDidLayoutSubviews];
-[ICDocCamImageQuadEditViewController viewWillAppear:];
-[ICDocCamImageQuadEditViewController _canShowWhileLocked];
-[ICDocCamImageQuadEditViewController viewDidAppear:];
-[ICDocCamImageQuadEditViewController overlay];
-[ICDocCamImageQuadEditViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[ICDocCamImageQuadEditViewController doneBarButtonItem];
-[ICDocCamImageQuadEditViewController viewWillLayoutSubviews];
-[ICDocCamImageQuadEditViewController updateFonts];
-[ICDocCamImageQuadEditViewController setBackgroundImageView:];
-[ICDocCamImageQuadEditViewController contentSizeCategoryDidChange:];
-[ICDocCamImageQuadEditViewController backgroundImageView];
-[ICDocCamImageQuadEditViewController image];
-[ICDocCamImageQuadEditViewController prefersStatusBarHidden];
-[ICDocCamImageQuadEditViewController imageView];
-[ICDocCamImageQuadEditViewController setCancelBarButtonItem:];
-[ICDocCamImageQuadEditViewController setDoneBarButtonItem:];
-[ICDocCamImageQuadEditViewController cancelButtonPressed:];
-[ICDocCamImageQuadEditViewController knobColor];
-[ICDocCamImageQuadEditViewController quad];
-[ICDocCamImageQuadEditViewController setQuad:];
-[ICDocCamImageQuadEditViewController setupAccessibility];
-[ICDocCamImageQuadEditViewController prepareForDismissal];
-[ICDocCamImageQuadEditViewController initWithImage:quad:scanDataDelegate:orientation:completionHandler:];
-[ICDocCamImageQuadEditViewController setShowImageAsAspectFit:];
-[ICDocCamImageQuadEditViewController scanWasDeleted:];
-[ICDocCamImageQuadEditViewController saveButtonPressed:];
-[ICDocCamImageQuadEditViewController centerAndScaleImageInScrollView];
-[ICDocCamImageQuadEditViewController quadForOverlay:];
-[ICDocCamImageQuadEditViewController setInitialQuad:];
-[ICDocCamImageQuadEditViewController setOverlayMask:];
-[ICDocCamImageQuadEditViewController overlayMaskPath];
-[ICDocCamImageQuadEditViewController placard];
-[ICDocCamImageQuadEditViewController adjustedQuad];
-[ICDocCamImageQuadEditViewController callCompletionHandler:withImage:quad:preparingForDismissal:];
-[ICDocCamImageQuadEditViewController captureNavigationBar];
-[ICDocCamImageQuadEditViewController captureNavigationItem];
-[ICDocCamImageQuadEditViewController currentZoomFactorForOverlay];
-[ICDocCamImageQuadEditViewController didAdjustQuad];
-[ICDocCamImageQuadEditViewController didCallCompletion];
-[ICDocCamImageQuadEditViewController didPressSave];
-[ICDocCamImageQuadEditViewController finalQuad];
-[ICDocCamImageQuadEditViewController finalQuadFromOverlay];
-[ICDocCamImageQuadEditViewController imageFrameInOverlayCoordinates];
-[ICDocCamImageQuadEditViewController inCaptureMode];
-[ICDocCamImageQuadEditViewController initialQuad];
-[ICDocCamImageQuadEditViewController knobHeight];
-[ICDocCamImageQuadEditViewController overlayDidLayout:];
-[ICDocCamImageQuadEditViewController overlayMask];
-[ICDocCamImageQuadEditViewController placardTopConstraint];
-[ICDocCamImageQuadEditViewController quadEditNavigationBar];
-[ICDocCamImageQuadEditViewController quadForOverlay];
-[ICDocCamImageQuadEditViewController refreshNavigationBar];
-[ICDocCamImageQuadEditViewController scanDataDelegate];
-[ICDocCamImageQuadEditViewController selectedKnobDidChange:];
-[ICDocCamImageQuadEditViewController selectedKnobDidPanToRect:];
-[ICDocCamImageQuadEditViewController setCaptureNavigationBar:];
-[ICDocCamImageQuadEditViewController setCaptureNavigationItem:];
-[ICDocCamImageQuadEditViewController setDidAdjustQuad:];
-[ICDocCamImageQuadEditViewController setDidCallCompletion:];
-[ICDocCamImageQuadEditViewController setDidPressSave:];
-[ICDocCamImageQuadEditViewController setInCaptureMode:];
-[ICDocCamImageQuadEditViewController setOverlayMaskPath:];
-[ICDocCamImageQuadEditViewController setPlacard:];
-[ICDocCamImageQuadEditViewController setPlacardTopConstraint:];
-[ICDocCamImageQuadEditViewController setQuadEditNavigationBar:];
-[ICDocCamImageQuadEditViewController setShouldAdjustForApectFitIfNecessary:];
-[ICDocCamImageQuadEditViewController setStartOrientationIsPortrait:];
-[ICDocCamImageQuadEditViewController setUpImageView];
-[ICDocCamImageQuadEditViewController setUpPlacard];
-[ICDocCamImageQuadEditViewController shouldAdjustForApectFitIfNecessary];
-[ICDocCamImageQuadEditViewController showImageAsAspectFit];
-[ICDocCamImageQuadEditViewController startOrientationIsPortrait];
-[ICDocCamImageQuadEditViewController uiInitialQuadForOverlay:];
-[ICDocCamImageQuadEditViewController uiQuadForOverlay:];
-[ICDocCamImageQuadEditViewController unitImageRectForOverlayRect:];
-[ICDocCamImageQuadEditViewController updateOverlayScrimMask];
-[ICDocCamImageQuadEditViewController updateToAspectFitIfNecessary];
-[ICDocCamImageQuadEditViewController updateTopConstraintForPlacard];
```
