# `AVPlannedVideoSegmentWritingRequest`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVPlannedSegmentWritingRequest`
- 5 instance variables, 1 properties, 9 instance methods, 1 class methods

## Instance variables

```
q _frameCount;
@"NSDictionary" _resumableOutputSettings;
@"AVAssetWriterInput" _writerInput;
^{OpaqueVTCompressionSession=} _compressionSession;
@"NSString" _expectedVideoCodecType;
```

## Properties

```
@property (Tq,R,V_frameCount) frameCount;
```

## Class methods

```
+[AVPlannedVideoSegmentWritingRequest requestWithSegmentFileOutputURL:assemblyTrackID:timeRange:frameCount:clientState:outputSettings:expectedVideoCodecType:progress:finishBlock:];
```

## Instance methods

```
-[AVPlannedVideoSegmentWritingRequest frameCount];
-[AVPlannedVideoSegmentWritingRequest dealloc];
-[AVPlannedVideoSegmentWritingRequest description];
-[AVPlannedVideoSegmentWritingRequest compressionSession];
-[AVPlannedVideoSegmentWritingRequest createResumableCompressionSessionWithAllocator:width:height:codecType:encoderSpecification:sourceImageBufferAttributes:compressedDataAllocator:outputCallback:outputCallbackRefCon:returningError:];
-[AVPlannedVideoSegmentWritingRequest initWithSegmentFileOutputURL:assemblyTrackID:timeRange:frameCount:clientState:resumableOutputSettings:expectedVideoCodecType:progress:finishBlock:];
-[AVPlannedVideoSegmentWritingRequest resumableAssetWriterInputWithMediaType:outputSettings:sourceFormatHint:returningError:];
-[AVPlannedVideoSegmentWritingRequest resumableOutputSettings];
-[AVPlannedVideoSegmentWritingRequest writerInput];
```
