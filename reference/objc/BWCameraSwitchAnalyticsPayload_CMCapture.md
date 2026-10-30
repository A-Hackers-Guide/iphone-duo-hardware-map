# `BWCameraSwitchAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 20 instance variables, 24 properties, 45 instance methods, 0 class methods

## Instance variables

```
i _switchReason;
f _uiZoom;
@"NSString" _switchFromPortType;
@"NSString" _switchToPortType;
@"NSString" _afRecommendedPortType;
@"NSString" _clientApplicationID;
i _deviceType;
f _gravityZ;
{?="width"i"height"i} _videoDimensions;
I _timeSinceLastAutoSwitch;
I _switchDelay;
Q _switchDelayReasons;
f _tofMeasuredDepth;
I _tofROIType;
I _fallbackCameras;
@"NSDictionary" _apsSubjectDistance;
@"NSDictionary" _logicalFocusLensPosition;
@"NSDictionary" _focusingMethod;
@"NSDictionary" _luxLevel;
@"NSDictionary" _frameRate;
```

## Properties

```
@property (Ti,N,V_switchReason) switchReason;
@property (Tf,N,V_uiZoom) uiZoom;
@property (T@"NSString",&,N,V_switchFromPortType) switchFromPortType;
@property (T@"NSString",&,N,V_switchToPortType) switchToPortType;
@property (T@"NSString",&,N,V_afRecommendedPortType) afRecommendedPortType;
@property (T@"NSString",C,N,V_clientApplicationID) clientApplicationID;
@property (Ti,N,V_deviceType) deviceType;
@property (Tf,N,V_gravityZ) gravityZ;
@property (T{?=ii},N,V_videoDimensions) videoDimensions;
@property (TI,N,V_timeSinceLastAutoSwitch) timeSinceLastAutoSwitch;
@property (TI,N,V_switchDelay) switchDelay;
@property (TQ,N,V_switchDelayReasons) switchDelayReasons;
@property (Tf,N,V_tofMeasuredDepth) tofMeasuredDepth;
@property (TI,N,V_tofROIType) tofROIType;
@property (TI,N,V_fallbackCameras) fallbackCameras;
@property (T@"NSDictionary",&,N,V_apsSubjectDistance) apsSubjectDistance;
@property (T@"NSDictionary",&,N,V_logicalFocusLensPosition) logicalFocusLensPosition;
@property (T@"NSDictionary",&,N,V_focusingMethod) focusingMethod;
@property (T@"NSDictionary",&,N,V_luxLevel) luxLevel;
@property (T@"NSDictionary",&,N,V_frameRate) frameRate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWCameraSwitchAnalyticsPayload setDeviceType:];
-[BWCameraSwitchAnalyticsPayload setVideoDimensions:];
-[BWCameraSwitchAnalyticsPayload eventDictionary];
-[BWCameraSwitchAnalyticsPayload tofROIType];
-[BWCameraSwitchAnalyticsPayload videoDimensions];
-[BWCameraSwitchAnalyticsPayload setUiZoom:];
-[BWCameraSwitchAnalyticsPayload init];
-[BWCameraSwitchAnalyticsPayload deviceType];
-[BWCameraSwitchAnalyticsPayload dealloc];
-[BWCameraSwitchAnalyticsPayload gravityZ];
-[BWCameraSwitchAnalyticsPayload reset];
-[BWCameraSwitchAnalyticsPayload setClientApplicationID:];
-[BWCameraSwitchAnalyticsPayload tofMeasuredDepth];
-[BWCameraSwitchAnalyticsPayload eventName];
-[BWCameraSwitchAnalyticsPayload setGravityZ:];
-[BWCameraSwitchAnalyticsPayload luxLevel];
-[BWCameraSwitchAnalyticsPayload focusingMethod];
-[BWCameraSwitchAnalyticsPayload setSwitchDelayReasons:];
-[BWCameraSwitchAnalyticsPayload logicalFocusLensPosition];
-[BWCameraSwitchAnalyticsPayload setLuxLevel:];
-[BWCameraSwitchAnalyticsPayload uiZoom];
-[BWCameraSwitchAnalyticsPayload setFrameRate:];
-[BWCameraSwitchAnalyticsPayload switchDelayReasons];
-[BWCameraSwitchAnalyticsPayload clientApplicationID];
-[BWCameraSwitchAnalyticsPayload frameRate];
-[BWCameraSwitchAnalyticsPayload fallbackCameras];
-[BWCameraSwitchAnalyticsPayload setSwitchDelay:];
-[BWCameraSwitchAnalyticsPayload afRecommendedPortType];
-[BWCameraSwitchAnalyticsPayload apsSubjectDistance];
-[BWCameraSwitchAnalyticsPayload setAfRecommendedPortType:];
-[BWCameraSwitchAnalyticsPayload setApsSubjectDistance:];
-[BWCameraSwitchAnalyticsPayload setFallbackCameras:];
-[BWCameraSwitchAnalyticsPayload setFocusingMethod:];
-[BWCameraSwitchAnalyticsPayload setLogicalFocusLensPosition:];
-[BWCameraSwitchAnalyticsPayload setSwitchFromPortType:];
-[BWCameraSwitchAnalyticsPayload setSwitchReason:];
-[BWCameraSwitchAnalyticsPayload setSwitchToPortType:];
-[BWCameraSwitchAnalyticsPayload setTimeSinceLastAutoSwitch:];
-[BWCameraSwitchAnalyticsPayload setTofMeasuredDepth:];
-[BWCameraSwitchAnalyticsPayload setTofROIType:];
-[BWCameraSwitchAnalyticsPayload switchDelay];
-[BWCameraSwitchAnalyticsPayload switchFromPortType];
-[BWCameraSwitchAnalyticsPayload switchReason];
-[BWCameraSwitchAnalyticsPayload switchToPortType];
-[BWCameraSwitchAnalyticsPayload timeSinceLastAutoSwitch];
```
