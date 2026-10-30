# `BWPhotoDecompressorNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 11 instance variables, 0 properties, 14 instance methods, 1 class methods

## Instance variables

```
B _downstreamIsSharingOutputPool;
B _synchronizedSlaveAttachedMediaDecompressionEnabled;
@"BWPhotoDecompressor" _photoDecompressor;
@"BWPhotoDecompressor" _synchronizedSlavePhotoDecompressor;
@"NSMutableArray" _emitSampleBufferSemaphores;
@"NSMutableArray" _emitSynchronizedSlaveSampleBufferSemaphores;
@"NSMutableSet" _disabledSynchronizedSlaveSemaphores;
i _numberOfTimesWaited;
i _numberOfBuffersEmitted;
i _numberOfTimesSynchronizedSlaveWaited;
i _numberOfSynchronizedSlaveBuffersEmitted;
```

## Class methods

```
+[BWPhotoDecompressorNode initialize];
```

## Instance methods

```
-[BWPhotoDecompressorNode prepareForCurrentConfigurationToBecomeLive];
-[BWPhotoDecompressorNode suspendResources];
-[BWPhotoDecompressorNode renderSampleBuffer:forInput:];
-[BWPhotoDecompressorNode addEmitSynchronizedSlaveSampleBufferSemaphore:];
-[BWPhotoDecompressorNode dealloc];
-[BWPhotoDecompressorNode initWithSynchronizedSlaveAttachedMediaDecompressionEnabled:];
-[BWPhotoDecompressorNode handleDroppedSample:forInput:];
-[BWPhotoDecompressorNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWPhotoDecompressorNode didReachEndOfDataForConfigurationID:input:];
-[BWPhotoDecompressorNode downstreamIsSharingOutputPool];
-[BWPhotoDecompressorNode nodeSubType];
-[BWPhotoDecompressorNode addEmitSampleBufferSemaphore:];
-[BWPhotoDecompressorNode nodeType];
-[BWPhotoDecompressorNode setDownstreamIsSharingOutputPool:];
```
