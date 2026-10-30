# `FigCaptureSoftISPCalibrationSinkPipelineConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 27 instance methods, 0 class methods

## Instance variables

```
I _pipelineStagePriority;
i _noiseReductionAndFusionScheme;
I _sensorRawPixelFormat;
{?="width"i"height"i} _rawSensorDimensions;
{CGPoint="x"d"y"d} _sensorCenterOffset;
B _quadraProcessingSupportEnabled;
i _horizontalSensorBinningFactor;
i _verticalSensorBinningFactor;
@"NSDictionary" _sensorIDStringsByPortType;
@"NSArray" _portTypesWithCalibrationEnabled;
@? _cameraInfoByPortTypeProvider;
@"NSDictionary" _moduleCalibrationByPortType;
@"NSDictionary" _dimensionsByResolutionFlavorByPortType;
```

## Properties

```
@property (TI,N,V_pipelineStagePriority) pipelineStagePriority;
@property (Ti,N,V_noiseReductionAndFusionScheme) noiseReductionAndFusionScheme;
@property (TI,N,V_sensorRawPixelFormat) sensorRawPixelFormat;
@property (T{?=ii},N,V_rawSensorDimensions) rawSensorDimensions;
@property (T{CGPoint=dd},N,V_sensorCenterOffset) sensorCenterOffset;
@property (TB,N,V_quadraProcessingSupportEnabled) quadraProcessingSupportEnabled;
@property (Ti,N,V_horizontalSensorBinningFactor) horizontalSensorBinningFactor;
@property (Ti,N,V_verticalSensorBinningFactor) verticalSensorBinningFactor;
@property (T@"NSDictionary",&,N,V_sensorIDStringsByPortType) sensorIDStringsByPortType;
@property (T@"NSArray",&,N,V_portTypesWithCalibrationEnabled) portTypesWithCalibrationEnabled;
@property (T@?,C,N,V_cameraInfoByPortTypeProvider) cameraInfoByPortTypeProvider;
@property (T@"NSDictionary",&,N,V_moduleCalibrationByPortType) moduleCalibrationByPortType;
@property (T@"NSDictionary",&,N,V_dimensionsByResolutionFlavorByPortType) dimensionsByResolutionFlavorByPortType;
```

## Instance methods

```
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration verticalSensorBinningFactor];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration sensorRawPixelFormat];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration setHorizontalSensorBinningFactor:];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration setDimensionsByResolutionFlavorByPortType:];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration rawSensorDimensions];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration moduleCalibrationByPortType];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration setQuadraProcessingSupportEnabled:];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration horizontalSensorBinningFactor];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration setSensorCenterOffset:];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration setRawSensorDimensions:];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration sensorCenterOffset];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration setVerticalSensorBinningFactor:];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration setModuleCalibrationByPortType:];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration quadraProcessingSupportEnabled];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration pipelineStagePriority];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration setSensorIDStringsByPortType:];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration noiseReductionAndFusionScheme];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration dimensionsByResolutionFlavorByPortType];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration setPipelineStagePriority:];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration sensorIDStringsByPortType];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration setPortTypesWithCalibrationEnabled:];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration dealloc];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration setNoiseReductionAndFusionScheme:];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration setSensorRawPixelFormat:];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration portTypesWithCalibrationEnabled];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration cameraInfoByPortTypeProvider];
-[FigCaptureSoftISPCalibrationSinkPipelineConfiguration setCameraInfoByPortTypeProvider:];
```
