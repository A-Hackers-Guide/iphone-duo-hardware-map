# `BTShareAudioConfirmViewController`

- Image: [`/System/Library/PrivateFrameworks/BluetoothServicesUI.framework/BluetoothServicesUI`](../userland/System__Library__PrivateFrameworks__BluetoothServicesUI.framework__BluetoothServicesUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BTShareAudioBaseViewController`
- 8 instance variables, 8 properties, 22 instance methods, 0 class methods

## Instance variables

```
I _colorCode;
I _productID;
@"UIImageView" _productImageView;
@"BTMediaPlayerView" _productMovieView;
@"UIButton" _confirmButton;
@"UIButton" _cancelButton;
@"UIImageView" _shareImageView;
@"NSString" _deviceName;
```

## Properties

```
@property (T@"UIImageView",&,N,V_productImageView) productImageView;
@property (T@"BTMediaPlayerView",&,N,V_productMovieView) productMovieView;
@property (T@"UIButton",&,N,V_confirmButton) confirmButton;
@property (T@"UIButton",&,N,V_cancelButton) cancelButton;
@property (T@"UIImageView",&,N,V_shareImageView) shareImageView;
@property (TI,N,V_colorCode) colorCode;
@property (T@"NSString",C,N,V_deviceName) deviceName;
@property (TI,N,V_productID) productID;
```

## Instance methods

```
-[BTShareAudioConfirmViewController setProductID:];
-[BTShareAudioConfirmViewController productID];
-[BTShareAudioConfirmViewController setCancelButton:];
-[BTShareAudioConfirmViewController cancelButton];
-[BTShareAudioConfirmViewController setColorCode:];
-[BTShareAudioConfirmViewController viewWillDisappear:];
-[BTShareAudioConfirmViewController setConfirmButton:];
-[BTShareAudioConfirmViewController viewWillAppear:];
-[BTShareAudioConfirmViewController setDeviceName:];
-[BTShareAudioConfirmViewController colorCode];
-[BTShareAudioConfirmViewController deviceName];
-[BTShareAudioConfirmViewController confirmButton];
-[BTShareAudioConfirmViewController _updateDeviceVisual:];
-[BTShareAudioConfirmViewController eventCancel:];
-[BTShareAudioConfirmViewController productImageView];
-[BTShareAudioConfirmViewController productMovieView];
-[BTShareAudioConfirmViewController setProductImageView:];
-[BTShareAudioConfirmViewController setProductMovieView:];
-[BTShareAudioConfirmViewController setShareImageView:];
-[BTShareAudioConfirmViewController shareImageView];
-[BTShareAudioConfirmViewController eventPermanentButton:];
-[BTShareAudioConfirmViewController eventTemporarilyShareButton:];
```
