# `BTShareAudioBringCloseViewController`

- Image: [`/System/Library/PrivateFrameworks/BluetoothServicesUI.framework/BluetoothServicesUI`](../userland/System__Library__PrivateFrameworks__BluetoothServicesUI.framework__BluetoothServicesUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BTShareAudioBaseViewController`
- 8 instance variables, 5 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _cycleImageArray;
@"NSObject<OS_dispatch_source>" _cycleImageTimer;
I _cycleNextIndex;
@"UILabel" _infoLabel;
@"UIImageView" _bannerImageView;
@"UIView" _productImageContainerView;
@"UIImageView" _shareImageView;
@"UIButton" _cancelButton;
```

## Properties

```
@property (T@"UILabel",&,N,V_infoLabel) infoLabel;
@property (T@"UIImageView",&,N,V_bannerImageView) bannerImageView;
@property (T@"UIView",&,N,V_productImageContainerView) productImageContainerView;
@property (T@"UIImageView",&,N,V_shareImageView) shareImageView;
@property (T@"UIButton",&,N,V_cancelButton) cancelButton;
```

## Instance methods

```
-[BTShareAudioBringCloseViewController setCancelButton:];
-[BTShareAudioBringCloseViewController cancelButton];
-[BTShareAudioBringCloseViewController viewWillDisappear:];
-[BTShareAudioBringCloseViewController viewDidLayoutSubviews];
-[BTShareAudioBringCloseViewController viewWillAppear:];
-[BTShareAudioBringCloseViewController bannerImageView];
-[BTShareAudioBringCloseViewController setBannerImageView:];
-[BTShareAudioBringCloseViewController _cycleProductImage];
-[BTShareAudioBringCloseViewController eventCancel:];
-[BTShareAudioBringCloseViewController infoLabel];
-[BTShareAudioBringCloseViewController setInfoLabel:];
-[BTShareAudioBringCloseViewController setShareImageView:];
-[BTShareAudioBringCloseViewController shareImageView];
-[BTShareAudioBringCloseViewController productImageContainerView];
-[BTShareAudioBringCloseViewController setProductImageContainerView:];
```
