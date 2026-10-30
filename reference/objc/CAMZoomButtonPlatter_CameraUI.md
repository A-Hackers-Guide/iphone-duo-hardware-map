# `CAMZoomButtonPlatter`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 15 instance variables, 18 properties, 61 instance methods, 0 class methods

## Instance variables

```
B _collapsed;
B _centerSelectedZoomEnabled;
B _hasLayoutConflictLeft;
B _hasLayoutConflictRight;
d _zoomFactor;
@"NSArray" _zoomPoints;
@"NSArray" _zoomFactors;
q _contentType;
@"NSArray" _zoomSymbols;
q _buttonAccessoryState;
q _buttonAccessoryPosition;
q _preferredCustomLens;
q _orientation;
@"NSMutableArray" __allButtons;
Q __focalLengthFlashID;
```

## Properties

```
@property (T@"NSMutableArray",R,N,V__allButtons) _allButtons;
@property (TQ,N,S_setFocalLengthFlashID:,V__focalLengthFlashID) _focalLengthFlashID;
@property (TQ,R,N) buttonCount;
@property (Td,N,V_zoomFactor) zoomFactor;
@property (T@"CAMZoomButton",R,N) zoomFactorButton;
@property (T@"NSArray",C,N,V_zoomPoints) zoomPoints;
@property (T@"NSArray",R,N,V_zoomFactors) zoomFactors;
@property (T@"NSArray",R,N) buttons;
@property (Tq,N,V_contentType) contentType;
@property (T@"NSArray",N,V_zoomSymbols) zoomSymbols;
@property (TB,N,GisCollapsed,V_collapsed) collapsed;
@property (Tq,N,V_buttonAccessoryState) buttonAccessoryState;
@property (Tq,N,V_buttonAccessoryPosition) buttonAccessoryPosition;
@property (Tq,N,V_preferredCustomLens) preferredCustomLens;
@property (TB,N,GisCenterSelectedZoomEnabled,V_centerSelectedZoomEnabled) centerSelectedZoomEnabled;
@property (TB,N,V_hasLayoutConflictLeft) hasLayoutConflictLeft;
@property (TB,N,V_hasLayoutConflictRight) hasLayoutConflictRight;
@property (Tq,N,V_orientation) orientation;
```

## Instance methods

```
-[CAMZoomButtonPlatter setContentType:];
-[CAMZoomButtonPlatter setOrientation:animated:];
-[CAMZoomButtonPlatter buttons];
-[CAMZoomButtonPlatter setCollapsed:];
-[CAMZoomButtonPlatter setOrientation:];
-[CAMZoomButtonPlatter setButtonAccessoryPosition:animated:];
-[CAMZoomButtonPlatter setHasLayoutConflictRight:];
-[CAMZoomButtonPlatter setCenterSelectedZoomEnabled:animated:];
-[CAMZoomButtonPlatter _updateButtonAlphas];
-[CAMZoomButtonPlatter zoomFactor];
-[CAMZoomButtonPlatter setZoomFactor:];
-[CAMZoomButtonPlatter intrinsicContentSize];
-[CAMZoomButtonPlatter _updateButtonAlphasAnimationDuration:];
-[CAMZoomButtonPlatter _createPlatterImageForContentSize:];
-[CAMZoomButtonPlatter setZoomPoints:];
-[CAMZoomButtonPlatter zoomPoints];
-[CAMZoomButtonPlatter setPreferredCustomLens:];
-[CAMZoomButtonPlatter _setFocalLengthFlashID:];
-[CAMZoomButtonPlatter setZoomFactor:allowFlashingSubstate:animated:];
-[CAMZoomButtonPlatter _updateButtonsAnimated:];
-[CAMZoomButtonPlatter orientation];
-[CAMZoomButtonPlatter buttonAccessoryState];
-[CAMZoomButtonPlatter hasLayoutConflictRight];
-[CAMZoomButtonPlatter nearestZoomButtonForPoint:];
-[CAMZoomButtonPlatter contentType];
-[CAMZoomButtonPlatter setZoomSymbols:animated:];
-[CAMZoomButtonPlatter setButtonAccessoryState:animated:];
-[CAMZoomButtonPlatter _cancelFocalLengthFlash];
-[CAMZoomButtonPlatter zoomSymbols];
-[CAMZoomButtonPlatter _flashFocalLengthIfNeeded];
-[CAMZoomButtonPlatter layoutSubviews];
-[CAMZoomButtonPlatter _focalLengthFlashID];
-[CAMZoomButtonPlatter defaultZoomFactorForButton:];
-[CAMZoomButtonPlatter zoomFactors];
-[CAMZoomButtonPlatter zoomFactorButton];
-[CAMZoomButtonPlatter nearestZoomButtonForTouch:];
-[CAMZoomButtonPlatter hasLayoutConflictLeft];
-[CAMZoomButtonPlatter setHasLayoutConflictRight:animated:];
-[CAMZoomButtonPlatter setHasLayoutConflictLeft:animated:];
-[CAMZoomButtonPlatter preferredCustomLens];
-[CAMZoomButtonPlatter setZoomSymbols:];
-[CAMZoomButtonPlatter setButtonAccessoryPosition:];
-[CAMZoomButtonPlatter setCenterSelectedZoomEnabled:];
-[CAMZoomButtonPlatter isCollapsed];
-[CAMZoomButtonPlatter baseZoomPointForButton:];
-[CAMZoomButtonPlatter isCenterSelectedZoomEnabled];
-[CAMZoomButtonPlatter setContentType:animated:];
-[CAMZoomButtonPlatter setCollapsed:animated:];
-[CAMZoomButtonPlatter setZoomPoints:animated:];
-[CAMZoomButtonPlatter _preferredContentSizeCategoryChanged];
-[CAMZoomButtonPlatter buttonCount];
-[CAMZoomButtonPlatter _intrinsicContentSizeForButtonCount:];
-[CAMZoomButtonPlatter _allButtons];
-[CAMZoomButtonPlatter _zoomFactorForButton:zoomPoint:isZoomFactorButton:];
-[CAMZoomButtonPlatter initWithFrame:];
-[CAMZoomButtonPlatter _indexesForChanges:];
-[CAMZoomButtonPlatter setButtonAccessoryState:];
-[CAMZoomButtonPlatter setHasLayoutConflictLeft:];
-[CAMZoomButtonPlatter _createZoomButton];
-[CAMZoomButtonPlatter _updateButtonAccessoryAnimated:];
-[CAMZoomButtonPlatter buttonAccessoryPosition];
```
