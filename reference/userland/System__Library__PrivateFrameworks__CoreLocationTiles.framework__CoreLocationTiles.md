# `/System/Library/PrivateFrameworks/CoreLocationTiles.framework/CoreLocationTiles`

iOS 27.2 dyld shared cache image. Version `3187.0.1.0.0`. **[DSC]**

## Linked libraries (9)

- `/usr/lib/libz.1.dylib`
- `/System/Library/PrivateFrameworks/LocationSupport.framework/LocationSupport`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CFNetwork.framework/CFNetwork`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/Security.framework/Security`
- `/usr/lib/libobjc.A.dylib`

## Objective-C: 2 classes, 0 protocols, 20 methods, 4 properties

### Class pages

Every class and protocol, with its methods: [`CLCertificatePinningHelper`](../objc/CLCertificatePinningHelper_CoreLocationTiles.md), [`CLTileRemoteDownloader`](../objc/CLTileRemoteDownloader_CoreLocationTiles.md)

### Classes

`CLCertificatePinningHelper`, `CLTileRemoteDownloader`

### Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@?,C,N,V_onDownloadAndDecompression) onDownloadAndDecompression;
@property (T@?,C,N,V_onFileDownload) onFileDownload;
@property (TB,N,V_canDownloadOverCellular) canDownloadOverCellular;
```

## Strings (62)

```
cl3.apple.com
cl2.apple.com
kCLConnectionDownloadAndDecompress
kCLConnectionDownloadFileRequestKey
activity
TilesFramework
v8@?0
gsp10-ssl.apple.com
1.2.840.113635.100.6.27.35
Utility
kCLConnectionDownloadAndDecompressSuccess
kCLConnectionDownloadFileSuccess
gs-loc.apple.com
cl5.apple.com
com.apple.locationd.Utility
kCLConnectionDownloadAndDecompressCancel
kCLConnectionDownloadAndDecompressURLResponseKey
ingest.apple-studies.com
ingest.stg.apple-studies.com
com.apple.location.tilesservice
kCLConnectionDownloadFileCancel
kCLConnectionDownloadAndDecompressError
kCLConnectionDownloadAndDecompressErrorKey
kCLConnectionDownloadFileURLResponseKey
iphone-ld.apple.com
kCLConnectionDownloadFileDestinationURLKey
kCLConnectionDownloadAndDecompressFileKey
configuration.apple.com
cl4.apple.com
kCLConnectionDownloadFile
kCLConnectionDownloadFileKey
kCLConnectionDownloadAndDecompressDestinationURLKey
kCLConnectionDownloadFileError
kCLConnectionDownloadFileErrorKey
basic_string
v24@?0{shared_ptr<CLConnectionMessage>=^{CLConnectionMessage}^{__shared_weak_count}}8
kCLConnectionDownloadAndDecompressRequestKey
com.apple.CoreLocationTiles
kCLTileErrorDomain
#TileRemoteDownloader Ignoring new download request with invalid source url
{\"msg%{public}.0s\":\"TileRemoteDownloader Ignoring new download request with invalid destination url\", \"destination\":%{private, location:escape_only}@}
{\"msg%{public}.0s\":\"#TileRemoteDownloader - starting request\", \"self\":\"%{public}p\", \"connection\":\"%{public}p\", \"canDownloadOverCellular\":%{public}hhd, \"srcURL\":%{public, location:escape_only}@, \"destination\":%{private, loc
{\"msg%{public}.0s\":\"Unable to create a security policy\", \"host\":%{public, location:escape_only}s, \"leafOID\":%{public, location:escape_only}s}
{\"msg%{public}.0s\":\"Can't SecTrustEvaluate returned the error\", \"errorCode\":%{private}ld, \"error\":%{private, location:escape_only}@}
Can't SecTrustEvaluate returned the error
{\"msg%{public}.0s\":\"#TileRemoteDownloader - starting request\", \"self\":\"%{public}p\", \"connection\":\"%{public}p\", \"canDownloadOverCellular\":%{public}hhd, \"srcURL\":%{public, location:escape_only}@, \"decompressedDestination\":%{
TileRemoteDownloader Ignoring new download request with invalid destination url
{\"msg%{public}.0s\":\"#TileRemoteDownloader Handling message from service\", \"event\":%{public, location:escape_only}s, \"messageName\":%{public, location:escape_only}s, \"self\":\"%{public}p\"}
CL: #TileRemoteDownloader Service is unavailable, sending error to clients
{\"msg%{public}.0s\":\"#Warning No pinning rule for host\", \"host\":%{private, location:escape_only}s}
{\"msg%{public}.0s\":\"#Warning Empty pinning rule for host\", \"host\":%{private, location:escape_only}s}
{\"msg%{public}.0s\":\"#TileRemoteDownloader Ignoring new download request with invalid source string\", \"URLString\":%{public, location:escape_only}s}
{\"msg%{public}.0s\":\"TileRemoteDownloader Ignoring new download request with invalid decompressed destination url\", \"decompressedDestination\":%{private, location:escape_only}@}
TileRemoteDownloader Ignoring new download request with invalid decompressed destination url
CL: #TileRemoteDownloader Handling message from service
{\"msg%{public}.0s\":\"#TileRemoteDownloader Service is unavailable, sending error to clients\", \"event\":%{public, location:escape_only}s}
Unable to create a security policy
Ignoring #TileRemoteDownloader request with invalid timeout
#TileRemoteDownloader Ignoring new download request with invalid source string
{\"msg%{public}.0s\":\"#TileRemoteDownloader Ignoring new download request with invalid source url\", \"URL\":%{public, location:escape_only}@}
{\"msg%{public}.0s\":\"#VerifyHost result\", \"result\":%{private}lu}
{\"msg%{public}.0s\":\"Ignoring #TileRemoteDownloader request with invalid timeout\", \"Timeout_s\":\"%{public}.09f\"}
```
