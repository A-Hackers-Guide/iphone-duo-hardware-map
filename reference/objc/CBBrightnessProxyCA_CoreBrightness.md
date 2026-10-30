# `CBBrightnessProxyCA`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBBrightnessProxy`
- 17 instance variables, 33 properties, 68 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"CAWindowServerDisplay" _brightnessControl;
B _allowUpdates;
@ _brightnessNotificationRequestEDR;
@"NSString" _brightnessRequestEDRHeadroom;
@"NSString" _brightnessRequestRampDuration;
@"NSString" _brightnessSecureIndicatorType;
@"NSString" _brightnessSecureIndicatorActiveCount;
@ _brightnessNotificationSecureIndicatorOn;
@ _brightnessNotificationSecureIndicatorOff;
@ _brightnessNotificationPowerOn;
@ _brightnessNotificationPowerOff;
Q _CBDispTypeIntegrated;
Q _CBDispTypeExternal;
Q _CBDispTypeWireless;
Q _CBDispTypeVirtual;
Q _CBDispTypeDFR;
```

## Properties

```
@property (TB,V_allowUpdates) allowUpdates;
@property (T@,R,V_brightnessNotificationRequestEDR) brightnessNotificationRequestEDR;
@property (T@,R,D) brightnessNotificationAttached;
@property (T@,R,D) brightnessNotificationDetached;
@property (T@,R,V_brightnessNotificationPowerOn) brightnessNotificationPowerOn;
@property (T@,R,V_brightnessNotificationPowerOff) brightnessNotificationPowerOff;
@property (T@,R,V_brightnessNotificationSecureIndicatorOn) brightnessNotificationSecureIndicatorOn;
@property (T@,R,V_brightnessNotificationSecureIndicatorOff) brightnessNotificationSecureIndicatorOff;
@property (T@"NSString",R,V_brightnessSecureIndicatorType) brightnessSecureIndicatorType;
@property (T@"NSString",R,V_brightnessSecureIndicatorActiveCount) brightnessSecureIndicatorActiveCount;
@property (T@"NSString",R,V_brightnessRequestEDRHeadroom) brightnessRequestEDRHeadroom;
@property (T@"NSString",R,V_brightnessRequestRampDuration) brightnessRequestRampDuration;
@property (TQ,R,V_CBDispTypeIntegrated) CBDispTypeIntegrated;
@property (TQ,R,V_CBDispTypeExternal) CBDispTypeExternal;
@property (TQ,R,V_CBDispTypeWireless) CBDispTypeWireless;
@property (TQ,R,V_CBDispTypeVirtual) CBDispTypeVirtual;
@property (TQ,R,V_CBDispTypeDFR) CBDispTypeDFR;
@property (TQ,R) displayType;
@property (Ti,R) displayId;
@property (TQ,R,D) vendorId;
@property (TQ,R,D) productId;
@property (TQ,R,D) serialNumber;
@property (T@"NSDictionary",R,D) brightnessCapabilities;
@property (T@"NSUUID",R) uuid;
@property (TB,R) whitePointAvailable;
@property (TB,R,D) brightnessAvailable;
@property (Tf,R) maximumLuminance;
@property (T@"NSUUID",R,D) containerId;
@property (T{?=ff},R,D) nativeWhitePoint;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CBBrightnessProxyCA setContrastPreservation:];
-[CBBrightnessProxyCA setPotentialHeadroom:];
-[CBBrightnessProxyCA setIndicatorBrightness:];
-[CBBrightnessProxyCA setIndicatorBrightnessLimit:];
-[CBBrightnessProxyCA registerForNotifications:withBlock:];
-[CBBrightnessProxyCA maximumLuminance];
-[CBBrightnessProxyCA forceCommitBrightness:withBlock:];
-[CBBrightnessProxyCA setNotificationQueue:];
-[CBBrightnessProxyCA brightnessAvailable];
-[CBBrightnessProxyCA getProductId];
-[CBBrightnessProxyCA setBrightnessLimit:];
-[CBBrightnessProxyCA unregisterNotificationBlocks];
-[CBBrightnessProxyCA setHeadroom:];
-[CBBrightnessProxyCA setBrightnessControlDisabled:];
-[CBBrightnessProxyCA productId];
-[CBBrightnessProxyCA setSDRBrightness:];
-[CBBrightnessProxyCA commitBrightness:withBlock:];
-[CBBrightnessProxyCA brightnessCapabilities];
-[CBBrightnessProxyCA setWhitePoint:rampDuration:error:];
-[CBBrightnessProxyCA whitePointAvailable];
-[CBBrightnessProxyCA CBDispTypeVirtual];
-[CBBrightnessProxyCA vendorId];
-[CBBrightnessProxyCA setAmbient:];
-[CBBrightnessProxyCA setContrastEnhancer:];
-[CBBrightnessProxyCA setLowAmbientAdaptation:];
-[CBBrightnessProxyCA commitBrightness:];
-[CBBrightnessProxyCA setFilteredAmbient:];
-[CBBrightnessProxyCA setHighAmbientAdaptation:];
-[CBBrightnessProxyCA brightnessSecureIndicatorActiveCount];
-[CBBrightnessProxyCA isBrightnessAvailable];
-[CBBrightnessProxyCA displayType];
-[CBBrightnessProxyCA brightnessSecureIndicatorType];
-[CBBrightnessProxyCA uuid];
-[CBBrightnessProxyCA CBDispTypeWireless];
-[CBBrightnessProxyCA brightnessRequestRampDuration];
-[CBBrightnessProxyCA displayId];
-[CBBrightnessProxyCA brightnessNotificationRequestEDR];
-[CBBrightnessProxyCA isWhitePointAvailable];
-[CBBrightnessProxyCA setAdaptationScale:];
-[CBBrightnessProxyCA dealloc];
-[CBBrightnessProxyCA getDisplayId];
-[CBBrightnessProxyCA initWithCAWindowServerDisplay:];
-[CBBrightnessProxyCA nativeWhitePoint];
-[CBBrightnessProxyCA setApplyPolicy];
-[CBBrightnessProxyCA containerId];
-[CBBrightnessProxyCA brightnessNotificationSecureIndicatorOff];
-[CBBrightnessProxyCA setReferenceHeadroom:];
-[CBBrightnessProxyCA getSerialNumber];
-[CBBrightnessProxyCA brightnessNotificationSecureIndicatorOn];
-[CBBrightnessProxyCA getVendorId];
-[CBBrightnessProxyCA serialNumber];
-[CBBrightnessProxyCA brightnessNotificationPowerOn];
-[CBBrightnessProxyCA brightnessRequestEDRHeadroom];
-[CBBrightnessProxyCA setAllowUpdates:];
-[CBBrightnessProxyCA brightnessNotificationPowerOff];
-[CBBrightnessProxyCA getBrightnessCapabilities];
-[CBBrightnessProxyCA isWhitePointD50XYZ];
-[CBBrightnessProxyCA CBDispTypeIntegrated];
-[CBBrightnessProxyCA getUUID];
-[CBBrightnessProxyCA CBDispTypeDFR];
-[CBBrightnessProxyCA brightnessNotificationDetached];
-[CBBrightnessProxyCA CBDispTypeExternal];
-[CBBrightnessProxyCA allowUpdates];
-[CBBrightnessProxyCA getDisplayType];
-[CBBrightnessProxyCA brightnessNotificationAttached];
-[CBBrightnessProxyCA registerForFrameInfoUpdates:error:];
-[CBBrightnessProxyCA unregisterFromFrameInfoUpdates];
-[CBBrightnessProxyCA setContrastEnhancer:rampDuration:error:];
```
