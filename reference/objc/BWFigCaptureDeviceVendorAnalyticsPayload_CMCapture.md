# `BWFigCaptureDeviceVendorAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 3 instance variables, 7 properties, 11 instance methods, 0 class methods

## Instance variables

```
i _timerReason;
i _idleOpenDuration;
B _deviceUsed;
```

## Properties

```
@property (Ti,N,V_timerReason) timerReason;
@property (Ti,N,V_idleOpenDuration) idleOpenDuration;
@property (TB,N,V_deviceUsed) deviceUsed;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWFigCaptureDeviceVendorAnalyticsPayload eventDictionary];
-[BWFigCaptureDeviceVendorAnalyticsPayload init];
-[BWFigCaptureDeviceVendorAnalyticsPayload dealloc];
-[BWFigCaptureDeviceVendorAnalyticsPayload reset];
-[BWFigCaptureDeviceVendorAnalyticsPayload eventName];
-[BWFigCaptureDeviceVendorAnalyticsPayload setTimerReason:];
-[BWFigCaptureDeviceVendorAnalyticsPayload deviceUsed];
-[BWFigCaptureDeviceVendorAnalyticsPayload idleOpenDuration];
-[BWFigCaptureDeviceVendorAnalyticsPayload setDeviceUsed:];
-[BWFigCaptureDeviceVendorAnalyticsPayload setIdleOpenDuration:];
-[BWFigCaptureDeviceVendorAnalyticsPayload timerReason];
```
