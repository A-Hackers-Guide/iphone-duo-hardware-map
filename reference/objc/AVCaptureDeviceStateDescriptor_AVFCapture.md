# `AVCaptureDeviceStateDescriptor`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"NSString" _deviceType;
@"NSSet" _mediaTypes;
q _position;
@"NSString" _uniqueID;
@"NSString" _localizedName;
```

## Properties

```
@property (T@"NSString",R,N,V_deviceType) deviceType;
@property (T@"NSSet",R,N,V_mediaTypes) mediaTypes;
@property (Tq,R,N,V_position) position;
@property (T@"NSString",R,N,V_uniqueID) uniqueID;
@property (T@"NSString",R,N,V_localizedName) localizedName;
```

## Class methods

```
+[AVCaptureDeviceStateDescriptor descriptorForDevice:];
+[AVCaptureDeviceStateDescriptor mediaTypesForDevice:];
```

## Instance methods

```
-[AVCaptureDeviceStateDescriptor position];
-[AVCaptureDeviceStateDescriptor mediaTypes];
-[AVCaptureDeviceStateDescriptor debugDescription];
-[AVCaptureDeviceStateDescriptor deviceType];
-[AVCaptureDeviceStateDescriptor dealloc];
-[AVCaptureDeviceStateDescriptor localizedName];
-[AVCaptureDeviceStateDescriptor uniqueID];
-[AVCaptureDeviceStateDescriptor hash];
-[AVCaptureDeviceStateDescriptor description];
-[AVCaptureDeviceStateDescriptor isEqual:];
-[AVCaptureDeviceStateDescriptor _initWithDeviceType:mediaTypes:position:uniqueID:localizedName:];
```
