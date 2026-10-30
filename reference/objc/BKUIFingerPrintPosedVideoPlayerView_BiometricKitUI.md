# `BKUIFingerPrintPosedVideoPlayerView`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 9 instance variables, 9 properties, 29 instance methods, 1 class methods

## Instance variables

```
@"NSString" _assetName;
@"NSString" _subDirectory;
@"AVQueuePlayer" _videoPlayer;
@"UIImageView" _portraitImageView;
@"UIImage" _horizontalPosedImage;
@"UIImage" _verticalPosedImage;
@"AVPlayerLayer" _playerLayer;
@"NSDictionary" _assetnameForAssetLengthDict;
@"NSObject<OS_os_log>" _log;
```

## Properties

```
@property (T@"AVQueuePlayer",&,N,V_videoPlayer) videoPlayer;
@property (T@"UIImageView",&,N,V_portraitImageView) portraitImageView;
@property (T@"UIImage",&,N,V_horizontalPosedImage) horizontalPosedImage;
@property (T@"UIImage",&,N,V_verticalPosedImage) verticalPosedImage;
@property (T@"AVPlayerLayer",&,N,V_playerLayer) playerLayer;
@property (T@"NSDictionary",&,N,V_assetnameForAssetLengthDict) assetnameForAssetLengthDict;
@property (T@"NSObject<OS_os_log>",&,N,V_log) log;
@property (T@"NSString",C,N,V_assetName) assetName;
@property (T@"NSString",C,N,V_subDirectory) subDirectory;
```

## Class methods

```
+[BKUIFingerPrintPosedVideoPlayerView layerClass];
```

## Instance methods

```
-[BKUIFingerPrintPosedVideoPlayerView setLog:];
-[BKUIFingerPrintPosedVideoPlayerView setAssetName:];
-[BKUIFingerPrintPosedVideoPlayerView assetName];
-[BKUIFingerPrintPosedVideoPlayerView load];
-[BKUIFingerPrintPosedVideoPlayerView playerLayer];
-[BKUIFingerPrintPosedVideoPlayerView setPlayerLayer:];
-[BKUIFingerPrintPosedVideoPlayerView layoutSubviews];
-[BKUIFingerPrintPosedVideoPlayerView videoPlayer];
-[BKUIFingerPrintPosedVideoPlayerView log];
-[BKUIFingerPrintPosedVideoPlayerView setVideoPlayer:];
-[BKUIFingerPrintPosedVideoPlayerView hideVideoPlayer];
-[BKUIFingerPrintPosedVideoPlayerView showVideoPlayer];
-[BKUIFingerPrintPosedVideoPlayerView setAssetnameForAssetLengthDict:];
-[BKUIFingerPrintPosedVideoPlayerView initWithAssetName:subdirectory:];
-[BKUIFingerPrintPosedVideoPlayerView _devicePrefix];
-[BKUIFingerPrintPosedVideoPlayerView _filters];
-[BKUIFingerPrintPosedVideoPlayerView _setFilters:];
-[BKUIFingerPrintPosedVideoPlayerView _updateImageForOrientation:];
-[BKUIFingerPrintPosedVideoPlayerView assetnameForAssetLengthDict];
-[BKUIFingerPrintPosedVideoPlayerView horizontalPosedImage];
-[BKUIFingerPrintPosedVideoPlayerView itemDidFinishPlaying:];
-[BKUIFingerPrintPosedVideoPlayerView portraitImageView];
-[BKUIFingerPrintPosedVideoPlayerView setHorizontalPosedImage:];
-[BKUIFingerPrintPosedVideoPlayerView setPortraitImageView:];
-[BKUIFingerPrintPosedVideoPlayerView setSubDirectory:];
-[BKUIFingerPrintPosedVideoPlayerView setVerticalPosedImage:];
-[BKUIFingerPrintPosedVideoPlayerView subDirectory];
-[BKUIFingerPrintPosedVideoPlayerView transitionToOrientation:];
-[BKUIFingerPrintPosedVideoPlayerView verticalPosedImage];
```
