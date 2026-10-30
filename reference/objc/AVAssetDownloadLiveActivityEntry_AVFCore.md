# `AVAssetDownloadLiveActivityEntry`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"<AVAssetDownloadLiveActivityDownload>" _download;
@"NSString" _assetTitle;
q _state;
@"NSProgress" _byteProgress;
```

## Properties

```
@property (T@"<AVAssetDownloadLiveActivityDownload>",&,N,V_download) download;
@property (T@"NSString",C,N,V_assetTitle) assetTitle;
@property (Tq,N,V_state) state;
@property (T@"NSProgress",&,N,V_byteProgress) byteProgress;
```

## Instance methods

```
-[AVAssetDownloadLiveActivityEntry setState:];
-[AVAssetDownloadLiveActivityEntry fractionCompleted];
-[AVAssetDownloadLiveActivityEntry dealloc];
-[AVAssetDownloadLiveActivityEntry download];
-[AVAssetDownloadLiveActivityEntry state];
-[AVAssetDownloadLiveActivityEntry assetTitle];
-[AVAssetDownloadLiveActivityEntry setAssetTitle:];
-[AVAssetDownloadLiveActivityEntry byteProgress];
-[AVAssetDownloadLiveActivityEntry initWithDownload:];
-[AVAssetDownloadLiveActivityEntry setByteProgress:];
-[AVAssetDownloadLiveActivityEntry setDownload:];
-[AVAssetDownloadLiveActivityEntry updateToBytesWritten:bytesExpectedToWrite:];
```
