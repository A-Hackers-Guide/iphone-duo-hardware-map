# `BWJasperDisparityProcessorInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerInput`
- 6 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<BWJasperDisparityProcessorInputDelegate>" _delegate;
{?="value"q"timescale"i"flags"I"epoch"q} _colorBufferPTS;
d _colorBufferExposureTime;
^{opaqueCMSampleBuffer=} _colorBuffer;
Q _colorBufferType;
B _skipProcessing;
```

## Properties

```
@property (T@"<BWJasperDisparityProcessorInputDelegate>",&,N,V_delegate) delegate;
@property (TB,R,N,GisReadyToExecute) readyToExecute;
@property (T^{opaqueCMSampleBuffer=},R,N,V_colorBuffer) colorBuffer;
@property (TQ,R,N,V_colorBufferType) colorBufferType;
@property (TB,N,V_skipProcessing) skipProcessing;
```

## Instance methods

```
-[BWJasperDisparityProcessorInput skipProcessing];
-[BWJasperDisparityProcessorInput dealloc];
-[BWJasperDisparityProcessorInput setDelegate:];
-[BWJasperDisparityProcessorInput setSkipProcessing:];
-[BWJasperDisparityProcessorInput delegate];
-[BWJasperDisparityProcessorInput description];
-[BWJasperDisparityProcessorInput initWithSettings:portType:];
-[BWJasperDisparityProcessorInput colorBufferType];
-[BWJasperDisparityProcessorInput setColorBufferPTS:exposureTime:];
-[BWJasperDisparityProcessorInput colorBuffer];
-[BWJasperDisparityProcessorInput executeNow];
-[BWJasperDisparityProcessorInput isReadyToExecute];
-[BWJasperDisparityProcessorInput setColorBuffer:type:];
```
