# `BWStillImagePortraitMetadataNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 9 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
i _sdofRenderingVersion;
@"NSDictionary" _sensorConfigurationsByPortType;
@"NSString" _defaultPortType;
f _defaultZoomFactor;
# _sdofRenderingTuningParametersClass;
@"NSString" _currentPortType;
f _currentZoomFactorForSDOFRenderingParameters;
@"NSDictionary" _sdofRenderingParameters;
@"FigSDOFRenderingTuningParameters" _sdofRenderingTuningParameters;
```

## Class methods

```
+[BWStillImagePortraitMetadataNode initialize];
```

## Instance methods

```
-[BWStillImagePortraitMetadataNode prepareForCurrentConfigurationToBecomeLive];
-[BWStillImagePortraitMetadataNode renderSampleBuffer:forInput:];
-[BWStillImagePortraitMetadataNode dealloc];
-[BWStillImagePortraitMetadataNode initWithNodeConfiguration:sdofRenderingVersion:sensorConfigurationsByPortType:defaultPortType:defaultZoomFactor:];
-[BWStillImagePortraitMetadataNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWStillImagePortraitMetadataNode nodeSubType];
-[BWStillImagePortraitMetadataNode nodeType];
```
