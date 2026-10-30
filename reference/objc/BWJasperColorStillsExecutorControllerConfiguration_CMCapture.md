# `BWJasperColorStillsExecutorControllerConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerConfiguration`
- 5 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"BWVideoFormat" _inputColorFormat;
@"BWVideoFormat" _outputDepthFormat;
{?="width"i"height"i} _standardFormatDimensions;
i _horizontalSensorBinningFactor;
i _verticalSensorBinningFactor;
```

## Properties

```
@property (T@"BWVideoFormat",&,N,V_inputColorFormat) inputColorFormat;
@property (T@"BWVideoFormat",&,N,V_outputDepthFormat) outputDepthFormat;
@property (T{?=ii},N,V_standardFormatDimensions) standardFormatDimensions;
@property (Ti,N,V_horizontalSensorBinningFactor) horizontalSensorBinningFactor;
@property (Ti,N,V_verticalSensorBinningFactor) verticalSensorBinningFactor;
```

## Instance methods

```
-[BWJasperColorStillsExecutorControllerConfiguration verticalSensorBinningFactor];
-[BWJasperColorStillsExecutorControllerConfiguration setHorizontalSensorBinningFactor:];
-[BWJasperColorStillsExecutorControllerConfiguration horizontalSensorBinningFactor];
-[BWJasperColorStillsExecutorControllerConfiguration setVerticalSensorBinningFactor:];
-[BWJasperColorStillsExecutorControllerConfiguration dealloc];
-[BWJasperColorStillsExecutorControllerConfiguration description];
-[BWJasperColorStillsExecutorControllerConfiguration inputColorFormat];
-[BWJasperColorStillsExecutorControllerConfiguration outputDepthFormat];
-[BWJasperColorStillsExecutorControllerConfiguration postponedProcessorSetupSupported];
-[BWJasperColorStillsExecutorControllerConfiguration setInputColorFormat:];
-[BWJasperColorStillsExecutorControllerConfiguration setOutputDepthFormat:];
-[BWJasperColorStillsExecutorControllerConfiguration setStandardFormatDimensions:];
-[BWJasperColorStillsExecutorControllerConfiguration standardFormatDimensions];
```
