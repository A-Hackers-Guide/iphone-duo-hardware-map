# `AVVCRecordDeviceInfo`

- Image: [`/System/Library/Frameworks/AVFAudio.framework/AVFAudio`](../userland/System__Library__Frameworks__AVFAudio.framework__AVFAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _isRemoteDevice;
B _isUpsamplingSourceAudio;
I _remoteDeviceCategory;
@"NSString" _recordRoute;
@"NSString" _remoteProductIdentifier;
@"NSUUID" _remoteDeviceUID;
@"NSString" _remoteDeviceUIDString;
```

## Properties

```
@property (T@"NSString",R,N,V_recordRoute) recordRoute;
@property (TB,R,V_isRemoteDevice) isRemoteDevice;
@property (T@"NSString",R,N,V_remoteProductIdentifier) remoteProductIdentifier;
@property (T@"NSUUID",R,N,V_remoteDeviceUID) remoteDeviceUID;
@property (TI,R,N,V_remoteDeviceCategory) remoteDeviceCategory;
@property (TB,R,N,V_isUpsamplingSourceAudio) isUpsamplingSourceAudio;
@property (T@"NSString",R,N,V_remoteDeviceUIDString) remoteDeviceUIDString;
```

## Instance methods

```
-[AVVCRecordDeviceInfo dealloc];
-[AVVCRecordDeviceInfo recordRoute];
-[AVVCRecordDeviceInfo isRemoteDevice];
-[AVVCRecordDeviceInfo remoteDeviceUID];
-[AVVCRecordDeviceInfo initWithRecordingEngine:];
-[AVVCRecordDeviceInfo isUpsamplingSourceAudio];
-[AVVCRecordDeviceInfo remoteDeviceCategory];
-[AVVCRecordDeviceInfo remoteDeviceUIDString];
-[AVVCRecordDeviceInfo remoteProductIdentifier];
```
