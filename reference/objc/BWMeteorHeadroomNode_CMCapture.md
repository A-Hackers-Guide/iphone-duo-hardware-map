# `BWMeteorHeadroomNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 7 instance variables, 0 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSString" _lastCaptureRequestIdentifier;
f _lastMeteorHeadroom;
f _gainMapMainImageDownscalingFactor;
i _headroomProcessingType;
@"FigMetalContext" _metalContext;
@"FigMetalHistogram" _histogram;
@"NSDictionary" _meteorHeadroomParametersByPortType;
```

## Class methods

```
+[BWMeteorHeadroomNode initialize];
```

## Instance methods

```
-[BWMeteorHeadroomNode gainMapMainImageDownscalingFactor];
-[BWMeteorHeadroomNode prepareForCurrentConfigurationToBecomeLive];
-[BWMeteorHeadroomNode setGainMapMainImageDownscalingFactor:];
-[BWMeteorHeadroomNode renderSampleBuffer:forInput:];
-[BWMeteorHeadroomNode dealloc];
-[BWMeteorHeadroomNode didSelectFormat:forInput:];
-[BWMeteorHeadroomNode didReachEndOfDataForInput:];
-[BWMeteorHeadroomNode headroomProcessingType];
-[BWMeteorHeadroomNode initWithNodeConfiguration:sensorConfigurationsByPortType:];
-[BWMeteorHeadroomNode setHeadroomProcessingType:];
```
