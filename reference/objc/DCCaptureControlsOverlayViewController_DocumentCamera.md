# `DCCaptureControlsOverlayViewController`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 37 instance variables, 5 properties, 20 instance methods, 0 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 updateButtonTitlesOnModeChange;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_deviceHasFlash;
? delegate;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_captureNavigationBar;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_captureControlsNavigationItem;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_captureButton;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_controlsStackView;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_flashButton;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_filterButton;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_autoButton;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 titleControlsStackView;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 flashControls;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 filterControls;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 autoControls;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 modeSelectionStackView;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_autoModeButton;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_manualModeButton;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_flashBarButtonItem;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_filterBarButtonItem;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_autoBarButtonItem;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_closeBarButtonItem;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_doneBarButtonItem;
B doneButtonShowing;
{CGSize=dd} thumbnailContentSize;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 staticConstraints;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 userInterfaceLayoutContext;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 currentInterfaceOrientationAdjustedForLayout;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 showsCaptureControlsAsToolbarItems;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 hostsControlsInTitleArea;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 needsInitialChromeUpdate;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 captureButtonLayoutGuideUpdater;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 bottomPlacardLayoutGuideUpdater;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 thumbnailLayoutGuideUpdater;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_phoneLayoutStrategy;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_padLayoutStrategy;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_doneAction;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 $__lazy_storage_$_closeAction;
```

## Properties

```
@property (T@"<_TtP14DocumentCamera46DCCaptureControlsOverlayViewControllerDelegate_>",N,W,Vdelegate) delegate;
@property (T@"UILayoutGuide",N,R) bottomPlacardLayoutGuide;
@property (T@"UILayoutGuide",N,R) thumbnailLayoutGuide;
@property (TB,N,VdoneButtonShowing) doneButtonShowing;
@property (T{CGSize=dd},N,VthumbnailContentSize) thumbnailContentSize;
```

## Instance methods

```
-[DCCaptureControlsOverlayViewController viewDidLoad];
-[DCCaptureControlsOverlayViewController initWithNibName:bundle:];
-[DCCaptureControlsOverlayViewController viewWillAppear:];
-[DCCaptureControlsOverlayViewController _canShowWhileLocked];
-[DCCaptureControlsOverlayViewController setDelegate:];
-[DCCaptureControlsOverlayViewController delegate];
-[DCCaptureControlsOverlayViewController viewWillLayoutSubviews];
-[DCCaptureControlsOverlayViewController initWithCoder:];
-[DCCaptureControlsOverlayViewController closeButtonTapped];
-[DCCaptureControlsOverlayViewController autoButtonTapped];
-[DCCaptureControlsOverlayViewController autoModeButtonTapped];
-[DCCaptureControlsOverlayViewController bottomPlacardLayoutGuide];
-[DCCaptureControlsOverlayViewController captureButtonTapped];
-[DCCaptureControlsOverlayViewController doneButtonShowing];
-[DCCaptureControlsOverlayViewController manualModeButtonTapped];
-[DCCaptureControlsOverlayViewController setCaptureButtonEnabled:];
-[DCCaptureControlsOverlayViewController setDoneButtonShowing:];
-[DCCaptureControlsOverlayViewController setThumbnailContentSize:];
-[DCCaptureControlsOverlayViewController thumbnailContentSize];
-[DCCaptureControlsOverlayViewController thumbnailLayoutGuide];
```
