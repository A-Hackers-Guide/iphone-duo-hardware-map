# `CBBrightnessProxy` (protocol)

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `FrameInfoProvider`
- 0 instance variables, 28 properties, 62 instance methods, 0 class methods

## Properties

```
@property (T@,R) brightnessNotificationRequestEDR;
@property (T@,R) brightnessNotificationAttached;
@property (T@,R) brightnessNotificationDetached;
@property (T@,R) brightnessNotificationPowerOn;
@property (T@,R) brightnessNotificationPowerOff;
@property (T@,R) brightnessNotificationSecureIndicatorOn;
@property (T@,R) brightnessNotificationSecureIndicatorOff;
@property (T@"NSString",R) brightnessSecureIndicatorType;
@property (T@"NSString",R) brightnessSecureIndicatorActiveCount;
@property (T@"NSString",R) brightnessRequestEDRHeadroom;
@property (T@"NSString",R) brightnessRequestRampDuration;
@property (TQ,R) CBDispTypeIntegrated;
@property (TQ,R) CBDispTypeExternal;
@property (TQ,R) CBDispTypeWireless;
@property (TQ,R) CBDispTypeVirtual;
@property (TQ,R) CBDispTypeDFR;
@property (TQ,R) displayType;
@property (Ti,R) displayId;
@property (TQ,R) vendorId;
@property (TQ,R) productId;
@property (TQ,R) serialNumber;
@property (T@"NSDictionary",R) brightnessCapabilities;
@property (T@"NSUUID",R) uuid;
@property (TB,R) whitePointAvailable;
@property (TB,R) brightnessAvailable;
@property (Tf,R) maximumLuminance;
@property (T@"NSUUID",R) containerId;
@property (T{?=ff},R) nativeWhitePoint;
```

## Instance methods

```
-[CBBrightnessProxy setContrastPreservation:];
-[CBBrightnessProxy setPotentialHeadroom:];
-[CBBrightnessProxy setIndicatorBrightness:];
-[CBBrightnessProxy setIndicatorBrightnessLimit:];
-[CBBrightnessProxy registerForNotifications:withBlock:];
-[CBBrightnessProxy maximumLuminance];
-[CBBrightnessProxy forceCommitBrightness:withBlock:];
-[CBBrightnessProxy setNotificationQueue:];
-[CBBrightnessProxy brightnessAvailable];
-[CBBrightnessProxy getProductId];
-[CBBrightnessProxy setBrightnessLimit:];
-[CBBrightnessProxy unregisterNotificationBlocks];
-[CBBrightnessProxy setHeadroom:];
-[CBBrightnessProxy setBrightnessControlDisabled:];
-[CBBrightnessProxy productId];
-[CBBrightnessProxy setSDRBrightness:];
-[CBBrightnessProxy commitBrightness:withBlock:];
-[CBBrightnessProxy brightnessCapabilities];
-[CBBrightnessProxy setWhitePoint:rampDuration:error:];
-[CBBrightnessProxy whitePointAvailable];
-[CBBrightnessProxy CBDispTypeVirtual];
-[CBBrightnessProxy vendorId];
-[CBBrightnessProxy setAmbient:];
-[CBBrightnessProxy setContrastEnhancer:];
-[CBBrightnessProxy setLowAmbientAdaptation:];
-[CBBrightnessProxy commitBrightness:];
-[CBBrightnessProxy setFilteredAmbient:];
-[CBBrightnessProxy setHighAmbientAdaptation:];
-[CBBrightnessProxy brightnessSecureIndicatorActiveCount];
-[CBBrightnessProxy isBrightnessAvailable];
-[CBBrightnessProxy displayType];
-[CBBrightnessProxy brightnessSecureIndicatorType];
-[CBBrightnessProxy uuid];
-[CBBrightnessProxy CBDispTypeWireless];
-[CBBrightnessProxy brightnessRequestRampDuration];
-[CBBrightnessProxy displayId];
-[CBBrightnessProxy brightnessNotificationRequestEDR];
-[CBBrightnessProxy isWhitePointAvailable];
-[CBBrightnessProxy setAdaptationScale:];
-[CBBrightnessProxy getDisplayId];
-[CBBrightnessProxy nativeWhitePoint];
-[CBBrightnessProxy setApplyPolicy];
-[CBBrightnessProxy containerId];
-[CBBrightnessProxy brightnessNotificationSecureIndicatorOff];
-[CBBrightnessProxy setReferenceHeadroom:];
-[CBBrightnessProxy getSerialNumber];
-[CBBrightnessProxy brightnessNotificationSecureIndicatorOn];
-[CBBrightnessProxy getVendorId];
-[CBBrightnessProxy serialNumber];
-[CBBrightnessProxy brightnessNotificationPowerOn];
-[CBBrightnessProxy brightnessRequestEDRHeadroom];
-[CBBrightnessProxy brightnessNotificationPowerOff];
-[CBBrightnessProxy getBrightnessCapabilities];
-[CBBrightnessProxy isWhitePointD50XYZ];
-[CBBrightnessProxy CBDispTypeIntegrated];
-[CBBrightnessProxy getUUID];
-[CBBrightnessProxy CBDispTypeDFR];
-[CBBrightnessProxy brightnessNotificationDetached];
-[CBBrightnessProxy CBDispTypeExternal];
-[CBBrightnessProxy getDisplayType];
-[CBBrightnessProxy brightnessNotificationAttached];
-[CBBrightnessProxy setContrastEnhancer:rampDuration:error:];
```
