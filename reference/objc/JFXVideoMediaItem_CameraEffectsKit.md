# `JFXVideoMediaItem`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `JTAssetMediaItem`
- 6 instance variables, 14 properties, 37 instance methods, 1 class methods

## Instance variables

```
B _isHighFrameRate;
B _capturedByInAppCamera;
B _originalIsHEVC4k;
i _mediaStartOffset;
@"AVAsset" _avAsset;
@"JTVideoMediaUtils" _videoMediaItemUtils;
```

## Properties

```
@property (T@"AVAsset",&,N,V_avAsset) avAsset;
@property (T@"JTVideoMediaUtils",&,N,V_videoMediaItemUtils) videoMediaItemUtils;
@property (TB,N,V_originalIsHEVC4k) originalIsHEVC4k;
@property (T{CGSize=dd},R,N) naturalSize;
@property (T{CGAffineTransform=dddddd},R,N) transform;
@property (T{CGSize=dd},R,N) naturalSizeWithTransform;
@property (Ti,N,V_mediaStartOffset) mediaStartOffset;
@property (Tf,R,N) frameRate;
@property (TB,R,N,V_isHighFrameRate) isHighFrameRate;
@property (TB,R,N) hasVideoTracks;
@property (TB,R,N) hasAudioTracks;
@property (TB,N,V_capturedByInAppCamera) capturedByInAppCamera;
@property (TB,R,N) needsDerivativeMedia;
@property (TB,R,N) isUnsupportedAudio;
```

## Class methods

```
+[JFXVideoMediaItem videoMediaItemWithLocalURL:delegate:completionHandler:];
```

## Instance methods

```
-[JFXVideoMediaItem commonInit];
-[JFXVideoMediaItem assetURL];
-[JFXVideoMediaItem avAsset];
-[JFXVideoMediaItem info];
-[JFXVideoMediaItem naturalSize];
-[JFXVideoMediaItem dealloc];
-[JFXVideoMediaItem setAvAsset:];
-[JFXVideoMediaItem transform];
-[JFXVideoMediaItem colorSpace];
-[JFXVideoMediaItem hash];
-[JFXVideoMediaItem copyWithZone:];
-[JFXVideoMediaItem isEqual:];
-[JFXVideoMediaItem frameRate];
-[JFXVideoMediaItem durationAt30fps];
-[JFXVideoMediaItem isHighFrameRate];
-[JFXVideoMediaItem cacheAssetInformation];
-[JFXVideoMediaItem canBeAddedToSequence];
-[JFXVideoMediaItem capturedByInAppCamera];
-[JFXVideoMediaItem hasAudibleCharacteristic];
-[JFXVideoMediaItem hasAudioTracks];
-[JFXVideoMediaItem hasVideoTracks];
-[JFXVideoMediaItem hasVisualCharacteristic];
-[JFXVideoMediaItem isUnsupportedAudio];
-[JFXVideoMediaItem loadAVAssetWithCompletionHandler:];
-[JFXVideoMediaItem mediaStartOffset];
-[JFXVideoMediaItem mediaserverdCrashed];
-[JFXVideoMediaItem naturalSizeWithTransform];
-[JFXVideoMediaItem needsDerivativeMedia];
-[JFXVideoMediaItem originalIsHEVC4k];
-[JFXVideoMediaItem reloadAVAsset];
-[JFXVideoMediaItem setAssetIs4kHEVC:];
-[JFXVideoMediaItem setCapturedByInAppCamera:];
-[JFXVideoMediaItem setMediaStartOffset:];
-[JFXVideoMediaItem setOriginalIsHEVC4k:];
-[JFXVideoMediaItem setVideoMediaItemUtils:];
-[JFXVideoMediaItem transform:fillDest:];
-[JFXVideoMediaItem videoMediaItemUtils];
```
