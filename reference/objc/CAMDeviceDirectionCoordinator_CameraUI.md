# `CAMDeviceDirectionCoordinator`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 9 instance methods, 0 class methods

## Instance variables

```
B __hasValidDirections;
@"AVCaptureDeviceDirectionCoordinator" __coordinator;
@? __changeHandler;
```

## Properties

```
@property (T@"AVCaptureDeviceDirectionCoordinator",&,N,V__coordinator) _coordinator;
@property (T@?,C,N,V__changeHandler) _changeHandler;
@property (TB,N,V__hasValidDirections) _hasValidDirections;
```

## Instance methods

```
-[CAMDeviceDirectionCoordinator _changeHandler];
-[CAMDeviceDirectionCoordinator _coordinator];
-[CAMDeviceDirectionCoordinator _descriptorForCAMDevicePosition:fromArray:];
-[CAMDeviceDirectionCoordinator _hasValidDirections];
-[CAMDeviceDirectionCoordinator directionForDevicePosition:];
-[CAMDeviceDirectionCoordinator initWithView:devices:changeHandler:];
-[CAMDeviceDirectionCoordinator set_changeHandler:];
-[CAMDeviceDirectionCoordinator set_coordinator:];
-[CAMDeviceDirectionCoordinator set_hasValidDirections:];
```
