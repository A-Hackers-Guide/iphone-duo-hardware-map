# `JFXPickerCameraSource`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 5 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"NSMutableSet" _registeredPickers;
@"NSObject<OS_dispatch_queue>" _registeredPickersQueue;
@"PVLivePlayerCameraSource" _registeredPickersSource;
```

## Properties

```
@property (T@"NSMutableSet",&,N,V_registeredPickers) registeredPickers;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_registeredPickersQueue) registeredPickersQueue;
@property (T@"PVLivePlayerCameraSource",&,N,V_registeredPickersSource) registeredPickersSource;
@property (T@"PVLivePlayerCameraSource",R,N) pickerSource;
@property (TB,R,N) isPickerPreviewing;
```

## Class methods

```
+[JFXPickerCameraSource sharedInstance];
```

## Instance methods

```
-[JFXPickerCameraSource init];
-[JFXPickerCameraSource isPickerPreviewing];
-[JFXPickerCameraSource pickerSource];
-[JFXPickerCameraSource registerPickerAsPreviewingWithObject:];
-[JFXPickerCameraSource registeredPickers];
-[JFXPickerCameraSource registeredPickersQueue];
-[JFXPickerCameraSource registeredPickersSource];
-[JFXPickerCameraSource setRegisteredPickers:];
-[JFXPickerCameraSource setRegisteredPickersQueue:];
-[JFXPickerCameraSource setRegisteredPickersSource:];
-[JFXPickerCameraSource unregisterPickerAsPreviewingWithObject:];
```
