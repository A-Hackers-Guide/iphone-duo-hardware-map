# `BWVideoCompressorNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 58 instance variables, 0 properties, 37 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _compressionSettings;
@"NSDictionary" _compressionSettingsPreparedFor;
B _nextFrameEncodeAsKeyFrame;
B _prioritizeEncodingSpeedOverQuality;
i _pipelineTraceID;
^{OpaqueVTCompressionSession=} _compressionSession;
@"NSDictionary" _compressionSessionSupportedProperties;
B _didPrepareToEncode;
B _sourceIsHDResolution;
I _sourcePixelFormatType;
@"NSObject<OS_dispatch_queue>" _emitterQueue;
@"NSObject<OS_dispatch_queue>" _compressionSessionStateQueue;
@"NSObject<OS_dispatch_source>" _reapCompressionSessionTimer;
d _reapCompressionSessionTimerDurationInSeconds;
B _compressionSessionReuseEnabled;
B _compressionSessionCanBeReused;
B _resetCodec;
B _signalHDRSceneChange;
i _numberOfFramesDroppedBecauseTooManyCompressedBytesInFlight;
q _inFlightCompressedBytesWarningThreshold;
B _inFlightCompressedBytesOverWarningThreshold;
B _encodedFirstVideoBuffer;
B _emittedFirstVideoBuffer;
@"NSObject<OS_dispatch_queue>" _thermalAndPowerNotificationQueue;
d _bFrameEncodingAllowedAtHigherPressureTimeLimit;
d _bFrameEncodingAllowedAtHigherPressureStopTime;
i _nonBFrameAverageBitRate;
i _thermalPressureNotificationToken;
i _thermalPressureLevel;
i _powerPressureNotificationToken;
i _powerPressureLevel;
B _bFrameEncodingRequested;
B _bFrameEncodingAllowed;
B _propagateStabilizedFacesToAVE;
B _overCaptureEnabled;
B _shouldAttachDebugSEI;
B _shouldPassSerializedDepthImageBuffers;
B _flushRequestReceived;
f _maxVideoFrameRate;
B _attachThumbnailSourcePixelBuffer;
^{__CVBuffer=} _thumbnailSourcePixelBuffer;
@"BWLimitedGMErrorLogger" _limitedGMErrorLogger;
B _compressionDimensionsFromInputEnabled;
B _compressionColorSpacePropertiesFromInputEnabled;
B _stereoVideoCompressionEnabled;
@"NSArray" _stereoTaggedCollections;
@"NSString" _codecNameString;
^{__CFString=} _alternateCompressionSettingsKey;
q _maximumAllowedInFlightCompressedBytes;
B _delayedCompressorCleanupEnabled;
@"NSArray" _smuggledSampleBufferAttachments;
{?="value"q"timescale"i"flags"I"epoch"q} _previousFrameOriginalPTS;
@"NSDictionary" _compressionPropertiesOverrides;
i _timewarpMode;
f _stereoVideoBaseline;
@"NSDictionary" _cameraInfoForPortType;
i _movieRecordingEndOfDataBehavior;
B _encoderPriorityInversionFixEnabled;
```

## Class methods

```
+[BWVideoCompressorNode initialize];
```

## Instance methods

```
-[BWVideoCompressorNode prepareForCurrentConfigurationToBecomeLive];
-[BWVideoCompressorNode suspendResources];
-[BWVideoCompressorNode setPipelineTraceID:];
-[BWVideoCompressorNode pipelineTraceID];
-[BWVideoCompressorNode setMaximumAllowedInFlightCompressedBytes:];
-[BWVideoCompressorNode alternateCompressionSettingsKey];
-[BWVideoCompressorNode renderSampleBuffer:forInput:];
-[BWVideoCompressorNode setCompressionDimensionsFromInputEnabled:];
-[BWVideoCompressorNode makeCurrentConfigurationLive];
-[BWVideoCompressorNode stereoVideoBaseline];
-[BWVideoCompressorNode encoderPriorityInversionFixEnabled];
-[BWVideoCompressorNode insertKeyFrame];
-[BWVideoCompressorNode dealloc];
-[BWVideoCompressorNode setStereoVideoBaseline:];
-[BWVideoCompressorNode maximumAllowedInFlightCompressedBytes];
-[BWVideoCompressorNode _compresessionSession];
-[BWVideoCompressorNode compressionDimensionsFromInputEnabled];
-[BWVideoCompressorNode hasNonLiveConfigurationChanges];
-[BWVideoCompressorNode setReapCompressionSessionTimerDurationInSeconds:];
-[BWVideoCompressorNode _releaseCompressionSession];
-[BWVideoCompressorNode movieRecordingEndOfDataBehavior];
-[BWVideoCompressorNode compressionColorSpacePropertiesFromInputEnabled];
-[BWVideoCompressorNode prioritizeEncodingSpeedOverQuality];
-[BWVideoCompressorNode setMovieRecordingEndOfDataBehavior:];
-[BWVideoCompressorNode handleDroppedSample:forInput:];
-[BWVideoCompressorNode didReachEndOfDataForConfigurationID:input:];
-[BWVideoCompressorNode setEncoderPriorityInversionFixEnabled:];
-[BWVideoCompressorNode setCompressionColorSpacePropertiesFromInputEnabled:];
-[BWVideoCompressorNode nodeSubType];
-[BWVideoCompressorNode compressionPropertiesOverrides];
-[BWVideoCompressorNode initWithCompressionSettings:overCaptureEnabled:stereoVideoCompressionEnabled:maxVideoFrameRate:delayedCompressorCleanupEnabled:maxLossyCompressionLevel:cameraInfoByPortType:];
-[BWVideoCompressorNode setCompressionPropertiesOverrides:];
-[BWVideoCompressorNode setPrioritizeEncodingSpeedOverQuality:];
-[BWVideoCompressorNode didSelectFormat:forInput:];
-[BWVideoCompressorNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWVideoCompressorNode nodeType];
-[BWVideoCompressorNode setAlternateCompressionSettingsKey:];
```
