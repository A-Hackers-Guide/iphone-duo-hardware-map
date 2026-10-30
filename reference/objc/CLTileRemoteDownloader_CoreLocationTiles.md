# `CLTileRemoteDownloader`

- Image: [`/System/Library/PrivateFrameworks/CoreLocationTiles.framework/CoreLocationTiles`](../userland/System__Library__PrivateFrameworks__CoreLocationTiles.framework__CoreLocationTiles.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
{unique_ptr<CLConnection, CLConnectionDeleter>=""{?="__ptr_"^{CLConnection}}} _connection;
B _canDownloadOverCellular;
@"NSObject<OS_dispatch_queue>" _queue;
@? _onDownloadAndDecompression;
@? _onFileDownload;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@?,C,N,V_onDownloadAndDecompression) onDownloadAndDecompression;
@property (T@?,C,N,V_onFileDownload) onFileDownload;
@property (TB,N,V_canDownloadOverCellular) canDownloadOverCellular;
```

## Instance methods

```
-[CLTileRemoteDownloader handleMessage:];
-[CLTileRemoteDownloader setup];
-[CLTileRemoteDownloader setOnDownloadAndDecompression:];
-[CLTileRemoteDownloader setCanDownloadOverCellular:];
-[CLTileRemoteDownloader dealloc];
-[CLTileRemoteDownloader queue];
-[CLTileRemoteDownloader initWithQueue:canDownloadOverCellular:];
-[CLTileRemoteDownloader onDownloadAndDecompression];
-[CLTileRemoteDownloader initWithConnection:onQueue:];
-[CLTileRemoteDownloader downloadAndDecompressFrom:toDecompressedDestination:withTimeout:withCompletionHandler:];
-[CLTileRemoteDownloader setOnFileDownload:];
-[CLTileRemoteDownloader onFileDownload];
-[CLTileRemoteDownloader handleDisconnection];
-[CLTileRemoteDownloader cancel];
-[CLTileRemoteDownloader canDownloadOverCellular];
-[CLTileRemoteDownloader downloadFile:toDestination:withTimeout:withCompletionHandler:];
-[CLTileRemoteDownloader setQueue:];
```
