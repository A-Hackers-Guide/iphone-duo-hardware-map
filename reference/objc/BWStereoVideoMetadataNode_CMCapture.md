# `BWStereoVideoMetadataNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 9 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
^{__CFData=} _serializedRectificationQuaternion;
i _consecutiveSpatiallyAggressiveFramesThreshold;
i _numberOfFramesEvaluatedForAggressiveStatus;
i _numberOfConsecutiveLuxLevelAggressiveFrames;
i _numberOfLuxLevelAggressiveFrames;
i _numberOfConsecutiveFocusDistanceAggressiveFrames;
i _numberOfFocusDistanceAggressiveFrames;
{?="value"q"timescale"i"flags"I"epoch"q} _startingPTS;
i _aggregateStereoVideoCaptureStatus;
```

## Class methods

```
+[BWStereoVideoMetadataNode initialize];
```

## Instance methods

```
-[BWStereoVideoMetadataNode renderSampleBuffer:forInput:];
-[BWStereoVideoMetadataNode dealloc];
-[BWStereoVideoMetadataNode nodeSubType];
-[BWStereoVideoMetadataNode didSelectFormat:forInput:];
-[BWStereoVideoMetadataNode nodeType];
-[BWStereoVideoMetadataNode didReachEndOfDataForInput:];
-[BWStereoVideoMetadataNode initWithPorts:secondaryPort:cameraInfoByPortType:errStatus:];
```
