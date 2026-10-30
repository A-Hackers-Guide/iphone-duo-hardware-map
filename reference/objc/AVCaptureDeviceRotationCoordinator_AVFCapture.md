# `AVCaptureDeviceRotationCoordinator`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVCaptureVisibilityHelperLayerDelegate`
- 17 instance variables, 4 properties, 27 instance methods, 1 class methods

## Instance variables

```
@"AVWeakReference" _coordinatorWeakReference;
@"AVWeakReference" _deviceWeakReference;
q _devicePosition;
@"NSString" _deviceType;
@"AVWeakReference" _previewLayerWeakReference;
@"AVCaptureVisibilityHelperLayer" _rotationHelperLayer;
d _videoRotationAngleForHorizonLevelPreview;
d _videoRotationAngleForHorizonLevelCapture;
B _isInitialVideoRotationAngleForHorizonLevelPreviewSet;
B _isInitialVideoRotationAngleForHorizonLevelCaptureSet;
[4d] _videoRotationAnglesRelativeToDeviceOrientation;
B _monitorSystemReferenceAngle;
B _suppliesVideoRotationAngleForHorizonLevelPreviewWithoutPreviewLayer;
Q _previewLayerSystemReferenceAngleMode;
@"FBSOrientationObserver" _activeInterfaceOrientationObserver;
B _monitorDeviceOrientation;
i _deviceOrientationNotificationToken;
```

## Properties

```
@property (T@"AVCaptureDevice",R,W,N) device;
@property (T@"CALayer",R,W,N) previewLayer;
@property (Td,R,N) videoRotationAngleForHorizonLevelPreview;
@property (Td,R,N) videoRotationAngleForHorizonLevelCapture;
```

## Class methods

```
+[AVCaptureDeviceRotationCoordinator initialize];
```

## Instance methods

```
-[AVCaptureDeviceRotationCoordinator debugDescription];
-[AVCaptureDeviceRotationCoordinator device];
-[AVCaptureDeviceRotationCoordinator dealloc];
-[AVCaptureDeviceRotationCoordinator description];
-[AVCaptureDeviceRotationCoordinator initWithDevice:previewLayer:];
-[AVCaptureDeviceRotationCoordinator videoRotationAngleForHorizonLevelCapture];
-[AVCaptureDeviceRotationCoordinator videoRotationAngleForHorizonLevelPreview];
-[AVCaptureDeviceRotationCoordinator _bsDeviceOrientationToVideoRotationAngle:unsupportedDeviceOrientation:];
-[AVCaptureDeviceRotationCoordinator _calculateVideoRotationAngleForHorizonLevelCaptureWithDeviceOrientation:];
-[AVCaptureDeviceRotationCoordinator _calculateVideoRotationAngleForHorizonLevelPreviewWithSystemReferenceAngle:];
-[AVCaptureDeviceRotationCoordinator _currentDeviceOrientation];
-[AVCaptureDeviceRotationCoordinator _handleActiveInterfaceOrientationUpdate:];
-[AVCaptureDeviceRotationCoordinator _handleDeviceAngleDidChangeNotification:];
-[AVCaptureDeviceRotationCoordinator _handleDevicePrimaryDisplayRegionDidChangeNotification:];
-[AVCaptureDeviceRotationCoordinator _handleSystemReferenceAngleDidChangeNotification:];
-[AVCaptureDeviceRotationCoordinator _initWithDevice:previewLayer:suppliesVideoRotationAngleForHorizonLevelPreviewWithoutPreviewLayer:];
-[AVCaptureDeviceRotationCoordinator _initWithDeviceWithoutPreviewLayer:];
-[AVCaptureDeviceRotationCoordinator _isExternalDeviceType:];
-[AVCaptureDeviceRotationCoordinator _shouldInvertBackCameraRotationForDeviceAngle];
-[AVCaptureDeviceRotationCoordinator _systemReferenceAngleForDeviceOrientation:onDisplayRegion:];
-[AVCaptureDeviceRotationCoordinator _updateVideoRotationAngleForHorizonLevelCapture];
-[AVCaptureDeviceRotationCoordinator _updateVideoRotationAngleForHorizonLevelPreview];
-[AVCaptureDeviceRotationCoordinator _videoRotationAngleForDeviceOrientation:];
-[AVCaptureDeviceRotationCoordinator handleVideoPreviewLayerDidBecomeVisibleNotification:];
-[AVCaptureDeviceRotationCoordinator previewLayer];
-[AVCaptureDeviceRotationCoordinator videoRotationAngleRelativeToDeviceOrientation:];
-[AVCaptureDeviceRotationCoordinator visibilityHelperLayer:visibilityChanged:];
```
