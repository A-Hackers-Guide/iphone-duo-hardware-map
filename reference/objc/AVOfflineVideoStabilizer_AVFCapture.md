# `AVOfflineVideoStabilizer`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `VISProcessorDelegate`
- 18 instance variables, 7 properties, 14 instance methods, 2 class methods

## Instance variables

```
{?="value"q"timescale"i"flags"I"epoch"q} _targetFrameDuration;
i _metadataPrimingCount;
f _lookAheadTime;
@"AVWeakReference" _dataProviderWeakReference;
^{__CVPixelBufferPool=} _pixelBufferPool;
B _clientMarkedEndOfVideoData;
q _videoOutputFrameNumber;
^{opaqueCMFormatDescription=} _cachedVideoFormatDescription;
@"NSMutableDictionary" _cachedInputBufferAttributes;
@"NSMutableArray" _outputSampleBuffers;
B _clientMarkedEndOfMetadata;
q _metadataOutputFrameNumber;
@"NSMutableArray" _futureFrameMetadataDicts;
@"NSSet" _requiredMetadataKeys;
@"NSSet" _optionalMetadataKeys;
B _stabilizationEnabled;
B _isFirstFrame;
@"<VISProcessor>" _visProcessor;
```

## Properties

```
@property (T@"NSMutableArray",R,N,V_outputSampleBuffers) outputSampleBuffers;
@property (Ti,R,N) preferredSourcePixelBufferPrimingFrameCount;
@property (Ti,R,N) preferredSourceStabilizationMetadataPrimingCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVOfflineVideoStabilizer initialize];
+[AVOfflineVideoStabilizer offlineVideoStabilizerWithTargetFrameDuration:dataProvider:destinationBufferPool:stabilizationEnabled:];
```

## Instance methods

```
-[AVOfflineVideoStabilizer dealloc];
-[AVOfflineVideoStabilizer didCompleteProcessingOfBuffer:withStatus:];
-[AVOfflineVideoStabilizer _validateSourcePixelBuffer:withSampleTime:metadata:isEndOfData:];
-[AVOfflineVideoStabilizer _copyStabilizedSampleBuffer:];
-[AVOfflineVideoStabilizer _createSampleBufferWithPixelBuffer:sampleTime:futureMetadata:status:];
-[AVOfflineVideoStabilizer _extendedRowsOfOutputBuffer];
-[AVOfflineVideoStabilizer _setupVISProcessor];
-[AVOfflineVideoStabilizer _teardownVISProcessor];
-[AVOfflineVideoStabilizer _validateStabilizationMetadata:withSampleTime:isEndOfData:];
-[AVOfflineVideoStabilizer copyStabilizedSampleBuffer:];
-[AVOfflineVideoStabilizer initWithTargetFrameDuration:dataProvider:destinationBufferPool:stabilizationEnabled:];
-[AVOfflineVideoStabilizer outputSampleBuffers];
-[AVOfflineVideoStabilizer preferredSourcePixelBufferPrimingFrameCount];
-[AVOfflineVideoStabilizer preferredSourceStabilizationMetadataPrimingCount];
```
