# `CAMSmartStyleSettingsResourceLoader`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PEResourceLoaderDelegate`
- 8 instance variables, 15 properties, 26 instance methods, 4 class methods

## Instance variables

```
@"<CAMSmartStyleSettingsResourceLoaderDelegate>" _delegate;
@"NSString" _assetIdentifier;
@"NSString" _logIdentifier;
q _status;
@"CAMSmartStyleSettingsResourceLoadResult" _resourceLoadResult;
@"NSObject<OS_dispatch_queue>" __resourceLoadingQueue;
@"PEResourceLoader" __resourceLoader;
d __startTime;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__resourceLoadingQueue) _resourceLoadingQueue;
@property (T@"PEResourceLoader",R,N,V__resourceLoader) _resourceLoader;
@property (Td,R,N,V__startTime) _startTime;
@property (TB,R,N) _isFileURL;
@property (T@"NSString",R,N) _filename;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) _cropRect;
@property (Tq,N,S_setStatus:,V_status) status;
@property (T@"<CAMSmartStyleSettingsResourceLoaderDelegate>",W,N,V_delegate) delegate;
@property (T@"NSString",R,C,N,V_assetIdentifier) assetIdentifier;
@property (T@"NSString",R,C,N,V_logIdentifier) logIdentifier;
@property (T@"CAMSmartStyleSettingsResourceLoadResult",R,N,V_resourceLoadResult) resourceLoadResult;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CAMSmartStyleSettingsResourceLoader _filenameCropRectDelimiter];
+[CAMSmartStyleSettingsResourceLoader assetIdentifierForFilename:cropRect:];
+[CAMSmartStyleSettingsResourceLoader cropRectFromAssetIdentifier:];
+[CAMSmartStyleSettingsResourceLoader filenameFromAssetIdentifier:];
```

## Instance methods

```
-[CAMSmartStyleSettingsResourceLoader _startTime];
-[CAMSmartStyleSettingsResourceLoader assetIdentifier];
-[CAMSmartStyleSettingsResourceLoader _resourceLoader];
-[CAMSmartStyleSettingsResourceLoader initWithDelegate:loadingQueue:assetIdentifier:logIdentifier:];
-[CAMSmartStyleSettingsResourceLoader _loadWithFileURL:];
-[CAMSmartStyleSettingsResourceLoader resourceLoader:request:downloadProgress:];
-[CAMSmartStyleSettingsResourceLoader resourceLoader:request:didCompleteWithResult:];
-[CAMSmartStyleSettingsResourceLoader status];
-[CAMSmartStyleSettingsResourceLoader _cropRect];
-[CAMSmartStyleSettingsResourceLoader _loadingQueue_createCompositionControllerForFileURL:];
-[CAMSmartStyleSettingsResourceLoader resourceLoader:request:mediaLoadDidFailWithError:];
-[CAMSmartStyleSettingsResourceLoader logIdentifier];
-[CAMSmartStyleSettingsResourceLoader _filename];
-[CAMSmartStyleSettingsResourceLoader setDelegate:];
-[CAMSmartStyleSettingsResourceLoader _isFileURL];
-[CAMSmartStyleSettingsResourceLoader photoEditResourceLoadRequestResourcesAvailabilityChanged:previousAvailability:currentAvailability:];
-[CAMSmartStyleSettingsResourceLoader resourceLoadResult];
-[CAMSmartStyleSettingsResourceLoader delegate];
-[CAMSmartStyleSettingsResourceLoader _compositionControllerFromStillAssetAtUrl:imageProperties:];
-[CAMSmartStyleSettingsResourceLoader _loadingQueue_fetchAsset];
-[CAMSmartStyleSettingsResourceLoader _didCreateCompositionController:forFileURL:imageProperties:];
-[CAMSmartStyleSettingsResourceLoader _resourceLoadingQueue];
-[CAMSmartStyleSettingsResourceLoader _loadWithAsset:];
-[CAMSmartStyleSettingsResourceLoader startLoading];
-[CAMSmartStyleSettingsResourceLoader _loadingQueue_fetchFileURL];
-[CAMSmartStyleSettingsResourceLoader _setStatus:];
```
