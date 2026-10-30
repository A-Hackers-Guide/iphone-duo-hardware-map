# `BWJasperColorStillsExecutorInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerInput`
- 8 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"<BWJasperColorStillsExecutorInputDelegate>" _delegate;
@"NSMutableArray" _pointClouds;
{?="value"q"timescale"i"flags"I"epoch"q} _colorBufferPTS;
d _colorBufferExposureTime;
^{opaqueCMSampleBuffer=} _colorBuffer;
Q _colorBufferType;
i _numberOfPointCloudsRequired;
B _skipProcessing;
```

## Properties

```
@property (T@"<BWJasperColorStillsExecutorInputDelegate>",&,N,V_delegate) delegate;
@property (TB,R,N,GisReadyToExecute) readyToExecute;
@property (T@"NSArray",R,N,V_pointClouds) pointClouds;
@property (T^{opaqueCMSampleBuffer=},R,N,V_colorBuffer) colorBuffer;
@property (TQ,R,N,V_colorBufferType) colorBufferType;
@property (TB,R,N) needMorePointClouds;
@property (TB,N,V_skipProcessing) skipProcessing;
```

## Instance methods

```
-[BWJasperColorStillsExecutorInput skipProcessing];
-[BWJasperColorStillsExecutorInput dealloc];
-[BWJasperColorStillsExecutorInput setDelegate:];
-[BWJasperColorStillsExecutorInput setSkipProcessing:];
-[BWJasperColorStillsExecutorInput delegate];
-[BWJasperColorStillsExecutorInput description];
-[BWJasperColorStillsExecutorInput colorBufferType];
-[BWJasperColorStillsExecutorInput setColorBufferPTS:exposureTime:];
-[BWJasperColorStillsExecutorInput addPointCloud:];
-[BWJasperColorStillsExecutorInput colorBuffer];
-[BWJasperColorStillsExecutorInput initWithSettings:portType:timeOfFlightCameraType:];
-[BWJasperColorStillsExecutorInput isReadyToExecute];
-[BWJasperColorStillsExecutorInput needMorePointClouds];
-[BWJasperColorStillsExecutorInput pointClouds];
-[BWJasperColorStillsExecutorInput setColorBuffer:type:];
```
