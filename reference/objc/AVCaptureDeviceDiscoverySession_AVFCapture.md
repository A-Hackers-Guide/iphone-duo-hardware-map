# `AVCaptureDeviceDiscoverySession`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 2 properties, 7 instance methods, 15 class methods

## Instance variables

```
@"NSArray" _deviceTypes;
q _position;
@"NSString" _mediaType;
@"NSArray" _devices;
@"NSArray" _supportedMultiCamDeviceSets;
```

## Properties

```
@property (T@"NSArray",R,N,V_devices) devices;
@property (T@"NSArray",R,N) supportedMultiCamDeviceSets;
```

## Class methods

```
+[AVCaptureDeviceDiscoverySession allDevices];
+[AVCaptureDeviceDiscoverySession initialize];
+[AVCaptureDeviceDiscoverySession discoverySessionWithDeviceTypes:mediaType:position:];
+[AVCaptureDeviceDiscoverySession allAudioDevices];
+[AVCaptureDeviceDiscoverySession allVideoDevices];
+[AVCaptureDeviceDiscoverySession allAudioDeviceTypes];
+[AVCaptureDeviceDiscoverySession allDeviceTypes];
+[AVCaptureDeviceDiscoverySession allMetadataCameraDeviceTypes];
+[AVCaptureDeviceDiscoverySession allMetadataCameraDevices];
+[AVCaptureDeviceDiscoverySession allPointCloudDeviceTypes];
+[AVCaptureDeviceDiscoverySession allPointCloudDevices];
+[AVCaptureDeviceDiscoverySession allSupportedMultiCamDeviceSets];
+[AVCaptureDeviceDiscoverySession allVideoDeviceTypes];
+[AVCaptureDeviceDiscoverySession allVirtualDeviceTypes];
+[AVCaptureDeviceDiscoverySession allVirtualDevices];
```

## Instance methods

```
-[AVCaptureDeviceDiscoverySession init];
-[AVCaptureDeviceDiscoverySession dealloc];
-[AVCaptureDeviceDiscoverySession devices];
-[AVCaptureDeviceDiscoverySession description];
-[AVCaptureDeviceDiscoverySession _handleDeviceConnectedDisconnectedNotification:];
-[AVCaptureDeviceDiscoverySession _initWithDeviceTypes:mediaType:position:allowIOSMacEnvironment:prefersUnsuspendedAndAllowsAnyPosition:];
-[AVCaptureDeviceDiscoverySession supportedMultiCamDeviceSets];
```
