# `BWPointCloudDensificationNodeConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"BWSensorConfiguration" _rgbSensorConfiguration;
@"BWSensorConfiguration" _timeOfFlightSensorConfiguration;
i _rgbCameraHorizontalSensorBinningFactor;
i _rgbCameraVerticalSensorBinningFactor;
B _filteringEnabled;
I _depthPixelFormat;
{?="width"i"height"i} _depthOutputDimensions;
i _timeOfFlightCameraType;
```

## Properties

```
@property (T@"BWSensorConfiguration",R,N,V_rgbSensorConfiguration) rgbSensorConfiguration;
@property (T@"BWSensorConfiguration",R,N,V_timeOfFlightSensorConfiguration) timeOfFlightSensorConfiguration;
@property (Ti,R,N,V_rgbCameraHorizontalSensorBinningFactor) rgbCameraHorizontalSensorBinningFactor;
@property (Ti,R,N,V_rgbCameraVerticalSensorBinningFactor) rgbCameraVerticalSensorBinningFactor;
@property (TB,R,N,V_filteringEnabled) filteringEnabled;
@property (TI,R,N,V_depthPixelFormat) depthPixelFormat;
@property (T{?=ii},R,N,V_depthOutputDimensions) depthOutputDimensions;
@property (Ti,R,N,V_timeOfFlightCameraType) timeOfFlightCameraType;
```

## Instance methods

```
-[BWPointCloudDensificationNodeConfiguration depthPixelFormat];
-[BWPointCloudDensificationNodeConfiguration dealloc];
-[BWPointCloudDensificationNodeConfiguration timeOfFlightCameraType];
-[BWPointCloudDensificationNodeConfiguration timeOfFlightSensorConfiguration];
-[BWPointCloudDensificationNodeConfiguration depthOutputDimensions];
-[BWPointCloudDensificationNodeConfiguration filteringEnabled];
-[BWPointCloudDensificationNodeConfiguration initWithRGBSensorConfiguration:timeOfFlightSensorConfiguration:rgbCameraHorizontalSensorBinningFactor:rgbCameraVerticalSensorBinningFactor:filteringEnabled:depthPixelFormat:depthOutputDimensions:timeOfFlightCameraType:];
-[BWPointCloudDensificationNodeConfiguration rgbCameraHorizontalSensorBinningFactor];
-[BWPointCloudDensificationNodeConfiguration rgbCameraVerticalSensorBinningFactor];
-[BWPointCloudDensificationNodeConfiguration rgbSensorConfiguration];
```
