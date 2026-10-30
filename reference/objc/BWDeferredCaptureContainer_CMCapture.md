# `BWDeferredCaptureContainer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWDeferredContainer`
- 11 instance variables, 5 properties, 25 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _flushQueue;
@"NSObject<OS_dispatch_group>" _flushGroup;
B _flushBuffersUponCommit;
B _foldersCreated;
B _committed;
B _preflushed;
B _cached;
Q _cacheExpiryTime;
@"NSDate" _commitTime;
q _commitDurationNS;
q _flushDurationNS;
```

## Properties

```
@property (TB,R,N,V_committed) committed;
@property (TB,N,V_cached) cached;
@property (TQ,N,V_cacheExpiryTime) cacheExpiryTime;
@property (Tq,R,N,V_commitDurationNS) commitDurationNS;
@property (Tq,R,N,V_flushDurationNS) flushDurationNS;
```

## Class methods

```
+[BWDeferredCaptureContainer captureRequestIdentifierForManifest:];
+[BWDeferredCaptureContainer timeForManifest:index:];
```

## Instance methods

```
-[BWDeferredCaptureContainer commit];
-[BWDeferredCaptureContainer abort];
-[BWDeferredCaptureContainer flush];
-[BWDeferredCaptureContainer dealloc];
-[BWDeferredCaptureContainer cached];
-[BWDeferredCaptureContainer setCached:];
-[BWDeferredCaptureContainer committed];
-[BWDeferredCaptureContainer cacheExpiryTime];
-[BWDeferredCaptureContainer flushDurationNS];
-[BWDeferredCaptureContainer commitArray:tag:];
-[BWDeferredCaptureContainer commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:compressionCropRect:metadataTag:portType:];
-[BWDeferredCaptureContainer commitBuffer:tag:bufferType:captureFrameFlags:compressionProfile:compressionCropRect:metadataTag:rawThumbnailsBufferTag:rawThumbnailsMetadataTag:mainRawThumbnailBufferTag:mainRawThumbnailMetadataTag:sifrRawThumbnailBufferTag:sifrRawThumbnailMetadataTag:hueMapBufferTag:hueMapMetadataTag:portType:];
-[BWDeferredCaptureContainer commitDictionary:tag:];
-[BWDeferredCaptureContainer commitDurationNS];
-[BWDeferredCaptureContainer commitInference:tag:inferenceAttachmentKey:portType:];
-[BWDeferredCaptureContainer commitInferenceBuffer:tag:metadataTag:inferenceAttachedMediaKey:compressionProfile:portType:];
-[BWDeferredCaptureContainer commitMetadata:tag:bufferTag:];
-[BWDeferredCaptureContainer commitPhotoDescriptor:];
-[BWDeferredCaptureContainer commitStillImageSettings:];
-[BWDeferredCaptureContainer copyXPCEncoding:];
-[BWDeferredCaptureContainer initWithApplicationID:captureRequestIdentifier:baseFolderURL:flushBuffersUponCommit:err:];
-[BWDeferredCaptureContainer preflush];
-[BWDeferredCaptureContainer setCacheExpiryTime:];
-[BWDeferredCaptureContainer waitForFlush];
-[BWDeferredCaptureContainer waitForFlushWithTimeoutInSeconds:];
```
