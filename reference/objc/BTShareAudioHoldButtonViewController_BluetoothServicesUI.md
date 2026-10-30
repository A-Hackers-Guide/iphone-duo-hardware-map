# `BTShareAudioHoldButtonViewController`

- Image: [`/System/Library/PrivateFrameworks/BluetoothServicesUI.framework/BluetoothServicesUI`](../userland/System__Library__PrivateFrameworks__BluetoothServicesUI.framework__BluetoothServicesUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BTShareAudioBaseViewController`
- 8 instance variables, 8 properties, 22 instance methods, 0 class methods

## Instance variables

```
I _colorCode;
I _productID;
@"UIImageView" _productImageView;
@"BTMediaPlayerView" _productMovieView;
@"UIView" _productMovieContainerView;
@"UIImageView" _shareImageView;
@"UILabel" _infoLabel;
@"UIButton" _cancelButton;
```

## Properties

```
@property (T@"UIImageView",&,N,V_productImageView) productImageView;
@property (T@"BTMediaPlayerView",&,N,V_productMovieView) productMovieView;
@property (T@"UIView",&,N,V_productMovieContainerView) productMovieContainerView;
@property (T@"UIImageView",&,N,V_shareImageView) shareImageView;
@property (T@"UILabel",&,N,V_infoLabel) infoLabel;
@property (T@"UIButton",&,N,V_cancelButton) cancelButton;
@property (TI,N,V_colorCode) colorCode;
@property (TI,N,V_productID) productID;
```

## Instance methods

```
-[BTShareAudioHoldButtonViewController setProductID:];
-[BTShareAudioHoldButtonViewController productID];
-[BTShareAudioHoldButtonViewController setCancelButton:];
-[BTShareAudioHoldButtonViewController cancelButton];
-[BTShareAudioHoldButtonViewController setColorCode:];
-[BTShareAudioHoldButtonViewController viewWillDisappear:];
-[BTShareAudioHoldButtonViewController viewDidLayoutSubviews];
-[BTShareAudioHoldButtonViewController viewWillAppear:];
-[BTShareAudioHoldButtonViewController colorCode];
-[BTShareAudioHoldButtonViewController _updateDeviceVisual:];
-[BTShareAudioHoldButtonViewController eventCancel:];
-[BTShareAudioHoldButtonViewController infoLabel];
-[BTShareAudioHoldButtonViewController productImageView];
-[BTShareAudioHoldButtonViewController productMovieView];
-[BTShareAudioHoldButtonViewController setInfoLabel:];
-[BTShareAudioHoldButtonViewController setProductImageView:];
-[BTShareAudioHoldButtonViewController setProductMovieView:];
-[BTShareAudioHoldButtonViewController setShareImageView:];
-[BTShareAudioHoldButtonViewController shareImageView];
-[BTShareAudioHoldButtonViewController _holdImageForPID:colorCode:];
-[BTShareAudioHoldButtonViewController productMovieContainerView];
-[BTShareAudioHoldButtonViewController setProductMovieContainerView:];
```
