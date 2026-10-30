# `BWStreamingCameraCalibrationDataNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 6 instance variables, 4 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _cameraInfoByPortType;
i _horizontalSensorBinningFactor;
i _verticalSensorBinningFactor;
i _preparedRotationDegrees;
B _mirroringEnabled;
i _liveRotationDegrees;
```

## Properties

```
@property (Ti,N,V_preparedRotationDegrees) rotationDegrees;
@property (TB,N,V_mirroringEnabled) mirroringEnabled;
@property (Ti,N,V_horizontalSensorBinningFactor) horizontalSensorBinningFactor;
@property (Ti,N,V_verticalSensorBinningFactor) verticalSensorBinningFactor;
```

## Class methods

```
+[BWStreamingCameraCalibrationDataNode initialize];
```

## Instance methods

```
-[BWStreamingCameraCalibrationDataNode verticalSensorBinningFactor];
-[BWStreamingCameraCalibrationDataNode setHorizontalSensorBinningFactor:];
-[BWStreamingCameraCalibrationDataNode horizontalSensorBinningFactor];
-[BWStreamingCameraCalibrationDataNode setVerticalSensorBinningFactor:];
-[BWStreamingCameraCalibrationDataNode renderSampleBuffer:forInput:];
-[BWStreamingCameraCalibrationDataNode makeCurrentConfigurationLive];
-[BWStreamingCameraCalibrationDataNode rotationDegrees];
-[BWStreamingCameraCalibrationDataNode dealloc];
-[BWStreamingCameraCalibrationDataNode setMirroringEnabled:];
-[BWStreamingCameraCalibrationDataNode hasNonLiveConfigurationChanges];
-[BWStreamingCameraCalibrationDataNode mirroringEnabled];
-[BWStreamingCameraCalibrationDataNode setRotationDegrees:];
-[BWStreamingCameraCalibrationDataNode nodeSubType];
-[BWStreamingCameraCalibrationDataNode configurationWithID:updatedFormat:didBecomeLiveForInput:];
-[BWStreamingCameraCalibrationDataNode nodeType];
-[BWStreamingCameraCalibrationDataNode initWithCameraInfoByPortType:];
```
