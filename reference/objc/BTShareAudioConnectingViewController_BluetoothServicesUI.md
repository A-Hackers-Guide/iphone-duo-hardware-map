# `BTShareAudioConnectingViewController`

- Image: [`/System/Library/PrivateFrameworks/BluetoothServicesUI.framework/BluetoothServicesUI`](../userland/System__Library__PrivateFrameworks__BluetoothServicesUI.framework__BluetoothServicesUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BTShareAudioBaseViewController`
- 11 instance variables, 10 properties, 26 instance methods, 0 class methods

## Instance variables

```
I _productIDActive;
I _colorCode;
I _productID;
@"UIImageView" _productImageView;
@"BTMediaPlayerView" _productMovieView;
@"UIImageView" _shareImageView;
@"UIView" _progressView;
@"UIActivityIndicatorView" _progressActivity;
@"UILabel" _progressLabel;
@"UIButton" _cancelButton;
@"NSString" _deviceName;
```

## Properties

```
@property (T@"UIImageView",&,N,V_productImageView) productImageView;
@property (T@"BTMediaPlayerView",&,N,V_productMovieView) productMovieView;
@property (T@"UIImageView",&,N,V_shareImageView) shareImageView;
@property (T@"UIView",&,N,V_progressView) progressView;
@property (T@"UIActivityIndicatorView",&,N,V_progressActivity) progressActivity;
@property (T@"UILabel",&,N,V_progressLabel) progressLabel;
@property (T@"UIButton",&,N,V_cancelButton) cancelButton;
@property (TI,N,V_colorCode) colorCode;
@property (T@"NSString",C,N,V_deviceName) deviceName;
@property (TI,N,V_productID) productID;
```

## Instance methods

```
-[BTShareAudioConnectingViewController setProductID:];
-[BTShareAudioConnectingViewController productID];
-[BTShareAudioConnectingViewController setCancelButton:];
-[BTShareAudioConnectingViewController cancelButton];
-[BTShareAudioConnectingViewController setColorCode:];
-[BTShareAudioConnectingViewController viewWillDisappear:];
-[BTShareAudioConnectingViewController progressView];
-[BTShareAudioConnectingViewController viewWillAppear:];
-[BTShareAudioConnectingViewController setDeviceName:];
-[BTShareAudioConnectingViewController setProgressView:];
-[BTShareAudioConnectingViewController colorCode];
-[BTShareAudioConnectingViewController deviceName];
-[BTShareAudioConnectingViewController progressLabel];
-[BTShareAudioConnectingViewController setProgressLabel:];
-[BTShareAudioConnectingViewController _updateDeviceVisual:];
-[BTShareAudioConnectingViewController _updateForDeviceInfo];
-[BTShareAudioConnectingViewController eventCancel:];
-[BTShareAudioConnectingViewController productImageView];
-[BTShareAudioConnectingViewController productMovieView];
-[BTShareAudioConnectingViewController progressActivity];
-[BTShareAudioConnectingViewController sessionProgressEvent:info:];
-[BTShareAudioConnectingViewController setProductImageView:];
-[BTShareAudioConnectingViewController setProductMovieView:];
-[BTShareAudioConnectingViewController setProgressActivity:];
-[BTShareAudioConnectingViewController setShareImageView:];
-[BTShareAudioConnectingViewController shareImageView];
```
