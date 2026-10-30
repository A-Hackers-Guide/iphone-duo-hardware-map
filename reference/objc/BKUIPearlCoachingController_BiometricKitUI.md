# `BKUIPearlCoachingController`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 11 instance variables, 12 properties, 34 instance methods, 0 class methods

## Instance variables

```
B _inBuddy;
B _inSheet;
B _isDisplayZoomEnabled;
q _orientation;
@"<BKUIPearlCoachingControllerDelegate>" _delegate;
@"BKUIPearlCoachingDeviceView" _deviceView;
@"BKUIPearlInstructionView" _instructionView;
@"UIButton" _escapeHatchButton;
@"BKUIButtonTray" _buttonTray;
@"UIScrollView" _scrollview;
@"UIView" _scrollContentView;
```

## Properties

```
@property (T@"BKUIPearlCoachingDeviceView",&,N,V_deviceView) deviceView;
@property (T@"BKUIPearlInstructionView",&,N,V_instructionView) instructionView;
@property (T@"UIButton",&,N,V_escapeHatchButton) escapeHatchButton;
@property (TB,R,N,GisDeviceFlat) deviceFlat;
@property (T@"BKUIButtonTray",&,N,V_buttonTray) buttonTray;
@property (T@"UIScrollView",&,N,V_scrollview) scrollview;
@property (T@"UIView",&,N,V_scrollContentView) scrollContentView;
@property (Tq,V_orientation) orientation;
@property (TB,N,V_inBuddy) inBuddy;
@property (TB,N,V_inSheet) inSheet;
@property (TB,N,V_isDisplayZoomEnabled) isDisplayZoomEnabled;
@property (T@"<BKUIPearlCoachingControllerDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[BKUIPearlCoachingController setOrientation:];
-[BKUIPearlCoachingController orientation];
-[BKUIPearlCoachingController viewDidLoad];
-[BKUIPearlCoachingController scrollview];
-[BKUIPearlCoachingController viewWillAppear:];
-[BKUIPearlCoachingController setDelegate:];
-[BKUIPearlCoachingController viewWillTransitionToSize:withTransitionCoordinator:];
-[BKUIPearlCoachingController delegate];
-[BKUIPearlCoachingController deviceOrientationChanged];
-[BKUIPearlCoachingController buttonTray];
-[BKUIPearlCoachingController setButtonTray:];
-[BKUIPearlCoachingController needsToShow];
-[BKUIPearlCoachingController inBuddy];
-[BKUIPearlCoachingController setInBuddy:];
-[BKUIPearlCoachingController instructionView];
-[BKUIPearlCoachingController setInstructionView:];
-[BKUIPearlCoachingController scrollContentView];
-[BKUIPearlCoachingController setScrollContentView:];
-[BKUIPearlCoachingController updateInstructionText];
-[BKUIPearlCoachingController inSheet];
-[BKUIPearlCoachingController resetDeviceView];
-[BKUIPearlCoachingController deviceView];
-[BKUIPearlCoachingController didOrientationChange];
-[BKUIPearlCoachingController escapeHatchButton];
-[BKUIPearlCoachingController escapeHatchButtonPressed:];
-[BKUIPearlCoachingController handleRotation];
-[BKUIPearlCoachingController isDeviceFlat];
-[BKUIPearlCoachingController isDisplayZoomEnabled];
-[BKUIPearlCoachingController setDeviceView:];
-[BKUIPearlCoachingController setEscapeHatchButton:];
-[BKUIPearlCoachingController setInSheet:];
-[BKUIPearlCoachingController setIsDisplayZoomEnabled:];
-[BKUIPearlCoachingController setScrollview:];
-[BKUIPearlCoachingController stopCoachingAnimation];
```
