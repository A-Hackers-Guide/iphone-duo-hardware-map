# `AVSampleCursor`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 0 properties, 33 instance methods, 2 class methods

## Instance variables

```
@"AVSampleCursorInternal" _sampleCursor;
```

## Class methods

```
+[AVSampleCursor initialize];
+[AVSampleCursor sampleCursorWithFigSampleCursor:];
```

## Instance methods

```
-[AVSampleCursor init];
-[AVSampleCursor dealloc];
-[AVSampleCursor presentationTimeStamp];
-[AVSampleCursor description];
-[AVSampleCursor copyWithZone:];
-[AVSampleCursor stepInPresentationOrderByCount:];
-[AVSampleCursor decodeTimeStamp];
-[AVSampleCursor _figSampleCursor];
-[AVSampleCursor canProvideSampleBuffers];
-[AVSampleCursor comparePositionInDecodeOrderWithPositionOfCursor:];
-[AVSampleCursor copyCurrentSampleFormatDescription];
-[AVSampleCursor createSampleBufferForCurrentSampleReturningError:];
-[AVSampleCursor createSampleBufferFromCurrentSampleToEndCursor:error:];
-[AVSampleCursor currentChunkInfo];
-[AVSampleCursor currentChunkStorageRange];
-[AVSampleCursor currentChunkStorageURL];
-[AVSampleCursor currentSampleAudioDependencyInfo];
-[AVSampleCursor currentSampleDependencyAttachments];
-[AVSampleCursor currentSampleDependencyInfo];
-[AVSampleCursor currentSampleDuration];
-[AVSampleCursor currentSampleIndexInChunk];
-[AVSampleCursor currentSampleStorageRange];
-[AVSampleCursor currentSampleSyncInfo];
-[AVSampleCursor initWithFigSampleCursor:];
-[AVSampleCursor samplesRequiredForDecoderRefresh];
-[AVSampleCursor samplesWithEarlierDecodeTimeStampsMayHaveLaterPresentationTimeStampsThanCursor:];
-[AVSampleCursor samplesWithLaterDecodeTimeStampsMayHaveEarlierPresentationTimeStampsThanCursor:];
-[AVSampleCursor seamIdentifier];
-[AVSampleCursor stepByDecodeTime:];
-[AVSampleCursor stepByDecodeTime:wasPinned:];
-[AVSampleCursor stepByPresentationTime:];
-[AVSampleCursor stepByPresentationTime:wasPinned:];
-[AVSampleCursor stepInDecodeOrderByCount:];
```
