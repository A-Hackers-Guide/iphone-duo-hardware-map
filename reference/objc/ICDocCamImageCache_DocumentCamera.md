# `ICDocCamImageCache`

- Image: [`/System/Library/PrivateFrameworks/DocumentCamera.framework/DocumentCamera`](../userland/System__Library__PrivateFrameworks__DocumentCamera.framework__DocumentCamera.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 30 instance methods, 0 class methods

## Instance variables

```
@"<DCDataCryptorDelegate>" _dataCryptorDelegate;
@"NSURL" _cachesDirectoryURL;
@"NSURL" _docCamImageDirectoryURL;
@"NSObject<OS_dispatch_queue>" _imageCacheQueue;
@"DCLRUCache" _inMemoryImageCache;
@"NSMutableDictionary" _imageSizeCache;
```

## Properties

```
@property (T@"NSURL",R,N,V_cachesDirectoryURL) cachesDirectoryURL;
@property (T@"NSURL",R,N,V_docCamImageDirectoryURL) docCamImageDirectoryURL;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_imageCacheQueue) imageCacheQueue;
@property (T@"DCLRUCache",&,N,V_inMemoryImageCache) inMemoryImageCache;
@property (T@"NSMutableDictionary",&,N,V_imageSizeCache) imageSizeCache;
@property (T@"<DCDataCryptorDelegate>",&,N,V_dataCryptorDelegate) dataCryptorDelegate;
```

## Instance methods

```
-[ICDocCamImageCache init];
-[ICDocCamImageCache dealloc];
-[ICDocCamImageCache applicationWillTerminate:];
-[ICDocCamImageCache didReceiveMemoryWarning:];
-[ICDocCamImageCache initWithDataCryptorDelegate:];
-[ICDocCamImageCache inMemoryImageCache];
-[ICDocCamImageCache getImageURL:];
-[ICDocCamImageCache dataCryptorDelegate];
-[ICDocCamImageCache getImageURL:async:];
-[ICDocCamImageCache cachesDirectoryURL];
-[ICDocCamImageCache imageCacheQueue];
-[ICDocCamImageCache deleteAllImages];
-[ICDocCamImageCache clearInMemoryCache];
-[ICDocCamImageCache createNSDataFrom:metaData:];
-[ICDocCamImageCache deleteImage:];
-[ICDocCamImageCache docCamImageDirectoryURL];
-[ICDocCamImageCache getImage:];
-[ICDocCamImageCache getImageSize:];
-[ICDocCamImageCache imagePropertiesFromMetadata:orientation:];
-[ICDocCamImageCache imageSizeCache];
-[ICDocCamImageCache initWithDataCryptorDelegate:cachesDirectoryURL:];
-[ICDocCamImageCache makeSureScanDirectoryExists:];
-[ICDocCamImageCache replaceImage:metaData:uuid:];
-[ICDocCamImageCache setDataCryptorDelegate:];
-[ICDocCamImageCache setImage:metaData:];
-[ICDocCamImageCache setImage:metaData:addToMemoryCache:completion:];
-[ICDocCamImageCache setImageCacheQueue:];
-[ICDocCamImageCache setImageSizeCache:];
-[ICDocCamImageCache setInMemoryImageCache:];
-[ICDocCamImageCache writeImage:metaData:toURL:error:];
```
