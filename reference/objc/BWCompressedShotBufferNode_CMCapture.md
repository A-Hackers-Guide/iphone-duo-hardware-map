# `BWCompressedShotBufferNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- Protocols: `BWCompressedShotBuffer`
- 25 instance variables, 11 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"BWStillImageNodeConfiguration" _nodeConfiguration;
B _optimizedFieldOfViewProcessingCropEnabled;
@"BWNodeInput" _sensorRawInput;
@"BWNodeOutput" _sensorRawOutput;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _bufferTrackingLock;
i _inUseUncompressedBufferCount;
i _inUseCompressedBufferCount;
i _uncompressedEquivalentCapacity;
q _inUseCompressedBytes;
q _compressedByteCapacity;
@"NSMutableArray" _queuedCompressedSampleBuffers;
@? _freeBufferCountIncreasedHandler;
B _passthroughEnabled;
B _compressWhenCompressedBuffersInUseEnabled;
^{CMPhotoCompressionSession=} _compressionSession;
B _compressedSurfacePoolEnabled;
{?="width"i"height"i} _compressionInputDimensions;
{?="width"i"height"i} _compressionInputDimensionsInit;
@"NSObject<OS_dispatch_queue>" _decompressionQueue;
@"BWPhotoDecompressor" _decompressor;
@"BWPixelBufferPool" _decompressionPool;
i _decompressionPoolCapacity;
^{opaqueCMFormatDescription=} _decompressionFormatDescription;
B _rawThumbnailCopyEnabled;
@"BWPixelBufferPool" _rawThumbnailPool;
```

## Properties

```
@property (T@"BWNodeInput",R,N) sensorRawInput;
@property (T@"BWNodeOutput",R,N) sensorRawOutput;
@property (Ti,N) uncompressedEquivalentCapacity;
@property (Ti,R,N) minimumUncompressedEquivalentCapacity;
@property (TB,R,N) compressionResourcesAllocated;
@property (T@?,C,N) freeBufferCountIncreasedHandler;
@property (TB,R,N) passthroughEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWCompressedShotBufferNode initialize];
```

## Instance methods

```
-[BWCompressedShotBufferNode renderSampleBuffer:forInput:];
-[BWCompressedShotBufferNode initWithNodeConfiguration:compressionInputDimensions:];
-[BWCompressedShotBufferNode flushAndWaitForUncompressedEquivalentFreeBufferCount:];
-[BWCompressedShotBufferNode setFreeBufferCountIncreasedHandler:];
-[BWCompressedShotBufferNode dealloc];
-[BWCompressedShotBufferNode freeBufferCountIncreasedHandler];
-[BWCompressedShotBufferNode flushAndWaitUntilThreshold:];
-[BWCompressedShotBufferNode handleStillImagePrewarmWithSettings:resourceConfig:forInput:];
-[BWCompressedShotBufferNode passthroughEnabled];
-[BWCompressedShotBufferNode didReachEndOfDataForConfigurationID:input:];
-[BWCompressedShotBufferNode uncompressedEquivalentCapacity];
-[BWCompressedShotBufferNode hasUncompressedEquivalentFreeBufferCount:];
-[BWCompressedShotBufferNode compressionResourcesAllocated];
-[BWCompressedShotBufferNode nodeSubType];
-[BWCompressedShotBufferNode minimumUncompressedEquivalentCapacity];
-[BWCompressedShotBufferNode sensorRawInput];
-[BWCompressedShotBufferNode getInUseCompressedBufferCount:inUseCompressedBytes:maxInUseCompressedBytes:forUncompressedEquivalentFreeBufferCount:];
-[BWCompressedShotBufferNode sensorRawOutput];
-[BWCompressedShotBufferNode didSelectFormat:forInput:];
-[BWCompressedShotBufferNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWCompressedShotBufferNode handleNodeError:forInput:];
-[BWCompressedShotBufferNode nodeType];
-[BWCompressedShotBufferNode setUncompressedEquivalentCapacity:];
```
