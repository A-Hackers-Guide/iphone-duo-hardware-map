# `CAMPanoramaView`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 29 instance variables, 30 properties, 72 instance methods, 1 class methods

## Instance variables

```
B _painting;
B __currentlyShowingMoveInstructions;
B __currentlyMovingTooFast;
q _direction;
q _devicePosition;
@"<CAMPanoramaViewDelegate>" _delegate;
@"CAMPanoramaPreviewView" _previewView;
q _layoutStyle;
@"_TtC8CameraUI20CAMDockKitController" _dockKitController;
@"UIView" __stripBackgroundView;
@"UIView" __stripContainerView;
@"UIView" __maskingView;
@"CAMPanoramaArrowView" __arrowView;
@"CAMPanoramaLevelView" __levelView;
@"CAMPanoramaLabel" __instructionLabel;
@"NSString" __speedString;
@"NSString" __moveUpString;
@"NSString" __moveDownString;
@"NSString" __arrowString;
@"NSString" __instructionString;
@"CAMPanoramaPaintingStatus" __currentPaintingStatus;
d __filteredNormalizedBaselineOffset;
^d __previousSpeeds;
d __currentAverageSpeed;
Q __arrowUpdateFrame;
q __lastDevicePosition;
{CGSize="width"d"height"d} _panoramaCaptureSize;
{CGPoint="x"d"y"d} __initialArrowCenter;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} __lastLayoutBounds;
```

## Properties

```
@property (T@"UIView",R,N,V__stripBackgroundView) _stripBackgroundView;
@property (T@"UIView",R,N,V__stripContainerView) _stripContainerView;
@property (T@"UIView",R,N,V__maskingView) _maskingView;
@property (T@"CAMPanoramaArrowView",R,N,V__arrowView) _arrowView;
@property (T@"CAMPanoramaLevelView",R,N,V__levelView) _levelView;
@property (T@"CAMPanoramaLabel",R,N,V__instructionLabel) _instructionLabel;
@property (T@"NSString",R,C,N,V__speedString) _speedString;
@property (T@"NSString",R,C,N,V__moveUpString) _moveUpString;
@property (T@"NSString",R,C,N,V__moveDownString) _moveDownString;
@property (T@"NSString",R,C,N,V__arrowString) _arrowString;
@property (T@"NSString",R,C,N,V__instructionString) _instructionString;
@property (T{CGPoint=dd},N,S_setInitialArrowCenter:,V__initialArrowCenter) _initialArrowCenter;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,S_setLastLayoutBounds:,V__lastLayoutBounds) _lastLayoutBounds;
@property (TB,N,GisPainting,S_setPainting:,V_painting) painting;
@property (T@"CAMPanoramaPaintingStatus",&,N,S_setCurrentPaintingStatus:,V__currentPaintingStatus) _currentPaintingStatus;
@property (Td,N,S_setFilteredNormalizedBaselineOffset:,V__filteredNormalizedBaselineOffset) _filteredNormalizedBaselineOffset;
@property (TB,N,G_isCurrentlyShowingMoveInstructions,S_setCurrentlyShowingMoveInstructions:,V__currentlyShowingMoveInstructions) _currentlyShowingMoveInstructions;
@property (T^d,R,N,V__previousSpeeds) _previousSpeeds;
@property (TB,N,G_isCurrentlyMovingTooFast,S_setCurrentlyMovingTooFast:,V__currentlyMovingTooFast) _currentlyMovingTooFast;
@property (Td,N,S_setCurrentAverageSpeed:,V__currentAverageSpeed) _currentAverageSpeed;
@property (TQ,N,S_setArrowUpdateFrame:,V__arrowUpdateFrame) _arrowUpdateFrame;
@property (Tq,N,V__lastDevicePosition) _lastDevicePosition;
@property (Tq,N,V_direction) direction;
@property (Tq,N,V_devicePosition) devicePosition;
@property (T@"<CAMPanoramaViewDelegate>",W,N,V_delegate) delegate;
@property (T@"CAMPanoramaPreviewView",R,N,V_previewView) previewView;
@property (T@"UIView",R,N) instructionView;
@property (Tq,N,V_layoutStyle) layoutStyle;
@property (T{CGSize=dd},N,V_panoramaCaptureSize) panoramaCaptureSize;
@property (T@"_TtC8CameraUI20CAMDockKitController",W,N,SsetDockKitController:,V_dockKitController) dockKitController;
```

## Class methods

```
+[CAMPanoramaView layerClass];
```

## Instance methods

```
-[CAMPanoramaView setLayoutStyle:];
-[CAMPanoramaView _levelView];
-[CAMPanoramaView layoutStyle];
-[CAMPanoramaView previewView];
-[CAMPanoramaView setDockKitController:];
-[CAMPanoramaView startProcessingPanorama];
-[CAMPanoramaView dealloc];
-[CAMPanoramaView stopPainting];
-[CAMPanoramaView setDirection:];
-[CAMPanoramaView panoramaCaptureSize];
-[CAMPanoramaView layoutSubviews];
-[CAMPanoramaView setTransform:];
-[CAMPanoramaView direction];
-[CAMPanoramaView setDelegate:];
-[CAMPanoramaView _setPainting:];
-[CAMPanoramaView devicePosition];
-[CAMPanoramaView delegate];
-[CAMPanoramaView initWithCoder:];
-[CAMPanoramaView finishedProcessingPanorama];
-[CAMPanoramaView startPainting];
-[CAMPanoramaView setPanoramaCaptureSize:];
-[CAMPanoramaView initWithFrame:];
-[CAMPanoramaView isPainting];
-[CAMPanoramaView setDevicePosition:];
-[CAMPanoramaView instructionView];
-[CAMPanoramaView _previousSpeeds];
-[CAMPanoramaView _moveDownString];
-[CAMPanoramaView _arrowString];
-[CAMPanoramaView _arrowUpdateFrame];
-[CAMPanoramaView _arrowView];
-[CAMPanoramaView _cancelDelayedMoveInstructions];
-[CAMPanoramaView _currentAverageSpeed];
-[CAMPanoramaView _currentPaintingStatus];
-[CAMPanoramaView _filteredNormalizedBaselineOffset];
-[CAMPanoramaView _frameForArrowViewWithDirection:offset:];
-[CAMPanoramaView _hideArrowInstructionsAfterDelay];
-[CAMPanoramaView _hideInstructionLabel];
-[CAMPanoramaView _hideSpeedInstructionsAfterDelay];
-[CAMPanoramaView _initialArrowCenter];
-[CAMPanoramaView _instructionLabel];
-[CAMPanoramaView _instructionString];
-[CAMPanoramaView _isCurrentlyMovingTooFast];
-[CAMPanoramaView _isCurrentlyShowingMoveInstructions];
-[CAMPanoramaView _lastDevicePosition];
-[CAMPanoramaView _lastLayoutBounds];
-[CAMPanoramaView _maskingView];
-[CAMPanoramaView _moveUpString];
-[CAMPanoramaView _previewSizeForBounds:];
-[CAMPanoramaView _resetPaintingUIAnimated:];
-[CAMPanoramaView _setArrowUpdateFrame:];
-[CAMPanoramaView _setCurrentAverageSpeed:];
-[CAMPanoramaView _setCurrentPaintingStatus:];
-[CAMPanoramaView _setCurrentlyMovingTooFast:];
-[CAMPanoramaView _setCurrentlyShowingMoveInstructions:];
-[CAMPanoramaView _setFilteredNormalizedBaselineOffset:];
-[CAMPanoramaView _setInitialArrowCenter:];
-[CAMPanoramaView _setLastLayoutBounds:];
-[CAMPanoramaView _showArrowInstructions];
-[CAMPanoramaView _showMoveDownInstructions];
-[CAMPanoramaView _showMoveDownInstructionsAfterDelay];
-[CAMPanoramaView _showMoveUpInstructions];
-[CAMPanoramaView _showMoveUpInstructionsAfterDelay];
-[CAMPanoramaView _showSpeedInstructions];
-[CAMPanoramaView _speedString];
-[CAMPanoramaView _stripBackgroundView];
-[CAMPanoramaView _stripContainerView];
-[CAMPanoramaView _updateInstructionLabelForInstruction:];
-[CAMPanoramaView dockKitController];
-[CAMPanoramaView initWithPanoramaPreviewView:layoutStyle:];
-[CAMPanoramaView setDirection:animated:];
-[CAMPanoramaView set_lastDevicePosition:];
-[CAMPanoramaView updatePaintingWithStatus:];
```
