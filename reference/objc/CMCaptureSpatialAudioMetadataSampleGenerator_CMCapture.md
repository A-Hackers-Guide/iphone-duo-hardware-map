# `CMCaptureSpatialAudioMetadataSampleGenerator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 1 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"BWAudioRemixAnalysisMetadataNode" _audioRemixAnalysisMetadataNode;
^{opaqueCMSampleBuffer=} _timedMedataSampleBuffer;
^{opaqueCMFormatDescription=} _audioFormatDesc;
B _analyzedFirstBuffer;
{?="value"q"timescale"i"flags"I"epoch"q} _lastAnalyzedPTS;
{?="value"q"timescale"i"flags"I"epoch"q} _lastKnownDuration;
^{OpaqueFigSimpleMutex=} _stateMutex;
```

## Properties

```
@property (T^{opaqueCMFormatDescription=},R,N) timedMetadataSampleBufferFormatDescription;
```

## Class methods

```
+[CMCaptureSpatialAudioMetadataSampleGenerator initialize];
```

## Instance methods

```
-[CMCaptureSpatialAudioMetadataSampleGenerator init];
-[CMCaptureSpatialAudioMetadataSampleGenerator dealloc];
-[CMCaptureSpatialAudioMetadataSampleGenerator consumeMessage:fromOutput:];
-[CMCaptureSpatialAudioMetadataSampleGenerator resetAnalyzer];
-[CMCaptureSpatialAudioMetadataSampleGenerator analyzeAudioSample:];
-[CMCaptureSpatialAudioMetadataSampleGenerator newTimedMetadataSampleBufferAndResetAnalyzer];
-[CMCaptureSpatialAudioMetadataSampleGenerator timedMetadataSampleBufferFormatDescription];
```
