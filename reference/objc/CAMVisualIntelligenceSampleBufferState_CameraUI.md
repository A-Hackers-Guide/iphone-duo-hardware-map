# `CAMVisualIntelligenceSampleBufferState`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMLocationControllerListener`
- 8 instance variables, 12 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _configuringCaptureSession;
@"CAMSystemPressureState" _systemPressureState;
d _zoomFactor;
d _uprightRotationDegrees;
@"CLLocation" _location;
@"CLHeading" _heading;
@"NSObject<OS_dispatch_queue>" _listeningQueue;
@"CAMLocationController" _locationController;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_listeningQueue) listeningQueue;
@property (T@"CAMLocationController",R,N,V_locationController) locationController;
@property (T@"CLLocation",&,N,V_location) location;
@property (T@"CLHeading",&,N,V_heading) heading;
@property (T@"CAMSystemPressureState",&,N,V_systemPressureState) systemPressureState;
@property (Td,N,V_zoomFactor) zoomFactor;
@property (TB,N,V_configuringCaptureSession) configuringCaptureSession;
@property (Td,N,V_uprightRotationDegrees) uprightRotationDegrees;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMVisualIntelligenceSampleBufferState setHeading:];
-[CAMVisualIntelligenceSampleBufferState zoomFactor];
-[CAMVisualIntelligenceSampleBufferState setZoomFactor:];
-[CAMVisualIntelligenceSampleBufferState location];
-[CAMVisualIntelligenceSampleBufferState locationController];
-[CAMVisualIntelligenceSampleBufferState dealloc];
-[CAMVisualIntelligenceSampleBufferState heading];
-[CAMVisualIntelligenceSampleBufferState setLocation:];
-[CAMVisualIntelligenceSampleBufferState systemPressureState];
-[CAMVisualIntelligenceSampleBufferState authorizationStatusUpdated:];
-[CAMVisualIntelligenceSampleBufferState configuringCaptureSession];
-[CAMVisualIntelligenceSampleBufferState currentHeadingUpdated:];
-[CAMVisualIntelligenceSampleBufferState currentLocationUpdated:];
-[CAMVisualIntelligenceSampleBufferState initWithListeningQueue:locationController:];
-[CAMVisualIntelligenceSampleBufferState listeningQueue];
-[CAMVisualIntelligenceSampleBufferState setConfiguringCaptureSession:];
-[CAMVisualIntelligenceSampleBufferState setSystemPressureState:];
-[CAMVisualIntelligenceSampleBufferState setUprightRotationDegrees:];
-[CAMVisualIntelligenceSampleBufferState uprightRotationDegrees];
```
