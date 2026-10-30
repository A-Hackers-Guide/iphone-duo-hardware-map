# `BWVideoDefringingNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 8 instance variables, 0 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _isSlomo;
B _propagateSynchronizedSlaveFrame;
@"NSString" _sensorIDString;
@"NSString" _portType;
^{opaqueCMFormatDescription=} _outputFormatDescription;
@"NSString" _cameraToDefringe;
@"FigVideoDefringingProcessor" _videoDefringingProcessor;
@"BWLimitedGMErrorLogger" _limitedGMErrorLogger;
```

## Class methods

```
+[BWVideoDefringingNode initialize];
```

## Instance methods

```
-[BWVideoDefringingNode prepareForCurrentConfigurationToBecomeLive];
-[BWVideoDefringingNode renderSampleBuffer:forInput:];
-[BWVideoDefringingNode dealloc];
-[BWVideoDefringingNode didSelectFormat:forInput:forAttachedMediaKey:];
-[BWVideoDefringingNode nodeSubType];
-[BWVideoDefringingNode nodeType];
-[BWVideoDefringingNode didReachEndOfDataForInput:];
-[BWVideoDefringingNode initWithSensorIDString:portType:propagateSynchronizedSlaveFrame:isSlomo:];
```
