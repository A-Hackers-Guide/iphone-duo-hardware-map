# `PNPPencilView`

- Image: [`/System/Library/PrivateFrameworks/PencilPairingUI.framework/PencilPairingUI`](../userland/System__Library__PrivateFrameworks__PencilPairingUI.framework__PencilPairingUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `PNPPencilInteractionEventDestination`, `PNPDeviceStateConfigurable`
- 9 instance variables, 7 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"UIImageView" _pencilImageView;
@"_PNPPencilMovieView" _pencilMovieView;
@"UIView" _touchIndicatorView;
B _touchIndicatorShown;
d _touchIndicatorPosition;
@"PNPDeviceState" _deviceState;
Q _variant;
B _spinning;
@"<PNPPencilViewDelegate>" _delegate;
```

## Properties

```
@property (T@"<PNPPencilViewDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_spinning) spinning;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"PNPDeviceState",C,N,V_deviceState) deviceState;
```

## Class methods

```
+[PNPPencilView _hardwareImageForVariant:];
```

## Instance methods

```
-[PNPPencilView setSpinning:];
-[PNPPencilView intrinsicContentSize];
-[PNPPencilView initWithVariant:];
-[PNPPencilView deviceState];
-[PNPPencilView layoutSubviews];
-[PNPPencilView setDeviceState:];
-[PNPPencilView sizeThatFits:];
-[PNPPencilView setDelegate:];
-[PNPPencilView delegate];
-[PNPPencilView initWithCoder:];
-[PNPPencilView spinning];
-[PNPPencilView _animateIndicatorToShown:withCompletionBlock:];
-[PNPPencilView _edgeAccurateSizeForLength:depth:deviceState:];
-[PNPPencilView _prepareMovieView];
-[PNPPencilView _resetTouchIndicatorPosition];
-[PNPPencilView cleanupSpinningResources];
-[PNPPencilView comfortableContainingSizeForDeviceState:];
-[PNPPencilView completeRevolutionWithCompletionBlock:];
-[PNPPencilView eventSource:hadPencilDoubleTapped:];
-[PNPPencilView intrinsicSizeForDeviceState:];
-[PNPPencilView prepareMovieForSpinningPencil:];
-[PNPPencilView transformForDeviceState:];
```
