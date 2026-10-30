# `JFXARKitCameraSessionController`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ARSessionDelegate`
- 11 instance variables, 15 properties, 30 instance methods, 0 class methods

## Instance variables

```
B _running;
@"<JFXARKitFrameDelegate>" _frameDelegate;
@"ARSession" _arSession;
@"ARFaceTrackingConfiguration" _faceTrackingConfiguration;
@"JFXCustomImageSensor" _customImageSensor;
@"CMMotionManager" _motionManager;
@"ARMotionSensor" _motionSensor;
@"ARDeviceOrientationSensor" _orientationSensor;
@"AVCaptureSession" _underlyingAVCaptureSession;
@"AVCaptureDevice" _underlyingAVCaptureDevice;
@"NSObject<OS_dispatch_queue>" _arSessionDelegateQueue;
```

## Properties

```
@property (T@"ARSession",&,N,V_arSession) arSession;
@property (T@"ARFaceTrackingConfiguration",&,N,V_faceTrackingConfiguration) faceTrackingConfiguration;
@property (T@"JFXCustomImageSensor",&,N,V_customImageSensor) customImageSensor;
@property (T@"CMMotionManager",&,N,V_motionManager) motionManager;
@property (T@"ARMotionSensor",&,N,V_motionSensor) motionSensor;
@property (T@"ARDeviceOrientationSensor",&,N,V_orientationSensor) orientationSensor;
@property (T@"AVCaptureSession",&,N,V_underlyingAVCaptureSession) underlyingAVCaptureSession;
@property (T@"AVCaptureDevice",&,N,V_underlyingAVCaptureDevice) underlyingAVCaptureDevice;
@property (TB,N,V_running) running;
@property (T@"NSObject<OS_dispatch_queue>",N,V_arSessionDelegateQueue) arSessionDelegateQueue;
@property (T@"<JFXARKitFrameDelegate>",W,N,V_frameDelegate) frameDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[JFXARKitCameraSessionController dealloc];
-[JFXARKitCameraSessionController setRunning:];
-[JFXARKitCameraSessionController running];
-[JFXARKitCameraSessionController motionManager];
-[JFXARKitCameraSessionController setMotionManager:];
-[JFXARKitCameraSessionController setFrameDelegate:];
-[JFXARKitCameraSessionController session:didUpdateFrame:];
-[JFXARKitCameraSessionController arSession];
-[JFXARKitCameraSessionController frameDelegate];
-[JFXARKitCameraSessionController setArSession:];
-[JFXARKitCameraSessionController JT_setupARSession:];
-[JFXARKitCameraSessionController provideSensorFrameSet:trackedFacesMetadata:faceObjectsMetadata:];
-[JFXARKitCameraSessionController arSessionDelegateQueue];
-[JFXARKitCameraSessionController customImageSensor];
-[JFXARKitCameraSessionController faceTrackingConfiguration];
-[JFXARKitCameraSessionController initWithAVCaptureSession:captureDevice:arSessionDelegateQueue:];
-[JFXARKitCameraSessionController motionSensor];
-[JFXARKitCameraSessionController orientationSensor];
-[JFXARKitCameraSessionController processExternalSensorData:];
-[JFXARKitCameraSessionController setArSessionDelegateQueue:];
-[JFXARKitCameraSessionController setCustomImageSensor:];
-[JFXARKitCameraSessionController setFaceTrackingConfiguration:];
-[JFXARKitCameraSessionController setMotionSensor:];
-[JFXARKitCameraSessionController setOrientationSensor:];
-[JFXARKitCameraSessionController setUnderlyingAVCaptureDevice:];
-[JFXARKitCameraSessionController setUnderlyingAVCaptureSession:];
-[JFXARKitCameraSessionController startARSession];
-[JFXARKitCameraSessionController stopARSession];
-[JFXARKitCameraSessionController underlyingAVCaptureDevice];
-[JFXARKitCameraSessionController underlyingAVCaptureSession];
```
