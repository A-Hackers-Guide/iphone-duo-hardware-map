# `FigCPEFPAirPlaySession`

- Image: [`/System/Library/Frameworks/MediaToolbox.framework/MediaToolbox`](../userland/System__Library__Frameworks__MediaToolbox.framework__MediaToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _invalid;
I _fairPlayContext;
@"NSDictionary" _protectionInfo;
@"NSDictionary" _contentInfo;
^{__CFAllocator=} _fairPlayDeallocator;
^{OpaqueFigEndpointPlaybackSession=} _playbackSession;
@"NSString" _mediaControlUUID;
I _vodkaVersion;
^{FPStreamOpaque_=} _fairPlaySession;
@"NSObject<OS_dispatch_queue>" _serializationQueue;
```

## Instance methods

```
-[FigCPEFPAirPlaySession dealloc];
-[FigCPEFPAirPlaySession endSession];
-[FigCPEFPAirPlaySession authorizeItemCompletionHandler_objc:picData:playerGUID:error:];
-[FigCPEFPAirPlaySession beginSessionWithCompletionQueue:completionHandler:];
-[FigCPEFPAirPlaySession createPicRequestWithError:];
-[FigCPEFPAirPlaySession initWithFairPlayContext:contentInfo:routeInfo:playbackSession:mediaControlUUID:];
-[FigCPEFPAirPlaySession initWithFairPlayContext:protectionInfo:routeInfo:playbackSession:mediaControlUUID:];
-[FigCPEFPAirPlaySession initWithFairPlayContext:routeInfo:playbackSession:mediaControlUUID:];
-[FigCPEFPAirPlaySession legacySinfs];
-[FigCPEFPAirPlaySession mediaControlParamsWithStoreResponse:];
-[FigCPEFPAirPlaySession sicWithPic:];
```
