# `CAMWhiteBalanceCommand`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCaptureCommand`
- 3 instance variables, 3 properties, 10 instance methods, 0 class methods

## Instance variables

```
q __whiteBalanceMode;
{?="temperature"f"tint"f} __temperatureAndTintValues;
@? __temperatureAndTintCompletionHandler;
```

## Properties

```
@property (Tq,R,N,V__whiteBalanceMode) _whiteBalanceMode;
@property (T{?=ff},R,N,V__temperatureAndTintValues) _temperatureAndTintValues;
@property (T@?,R,C,N,V__temperatureAndTintCompletionHandler) _temperatureAndTintCompletionHandler;
```

## Instance methods

```
-[CAMWhiteBalanceCommand initWithLockedTemperature:tint:completionHandler:];
-[CAMWhiteBalanceCommand _temperatureAndTintCompletionHandler];
-[CAMWhiteBalanceCommand _whiteBalanceMode];
-[CAMWhiteBalanceCommand _setWhiteBalanceModeOnDevice:];
-[CAMWhiteBalanceCommand _temperatureAndTintValues];
-[CAMWhiteBalanceCommand _setTemperatureAndTintOnDevice:completionHandler:];
-[CAMWhiteBalanceCommand executeWithContext:];
-[CAMWhiteBalanceCommand _descriptionForWhiteBalanceMode:];
-[CAMWhiteBalanceCommand copyWithZone:];
-[CAMWhiteBalanceCommand initWithWhiteBalanceMode:];
```
