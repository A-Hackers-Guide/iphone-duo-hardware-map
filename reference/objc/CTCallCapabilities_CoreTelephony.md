# `CTCallCapabilities`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 10 instance variables, 10 properties, 24 instance methods, 1 class methods

## Instance variables

```
B _isWifiCallingAvailable;
B _isVoLTECallingAvailable;
B _isCSCallingAvailable;
B _isEmergencyCallingOnWifiAllowed;
B _isEmergencyCallingOnWifiAvailable;
B _isCarrierSupportsEmergencyCallOnWifiNoLimit;
B _isTTYSupported;
B _isRTTSupported;
B _isEmergencyRTTSupported;
B _isHoldForRTTEnabled;
```

## Properties

```
@property (TB,N,V_isWifiCallingAvailable) isWifiCallingAvailable;
@property (TB,N,V_isVoLTECallingAvailable) isVoLTECallingAvailable;
@property (TB,N,V_isCSCallingAvailable) isCSCallingAvailable;
@property (TB,N,V_isEmergencyCallingOnWifiAllowed) isEmergencyCallingOnWifiAllowed;
@property (TB,N,V_isEmergencyCallingOnWifiAvailable) isEmergencyCallingOnWifiAvailable;
@property (TB,N,V_isCarrierSupportsEmergencyCallOnWifiNoLimit) isCarrierSupportsEmergencyCallOnWifiNoLimit;
@property (TB,N,V_isTTYSupported) isTTYSupported;
@property (TB,N,V_isRTTSupported) isRTTSupported;
@property (TB,N,V_isEmergencyRTTSupported) isEmergencyRTTSupported;
@property (TB,N,V_isHoldForRTTEnabled) isHoldForRTTEnabled;
```

## Class methods

```
+[CTCallCapabilities supportsSecureCoding];
```

## Instance methods

```
-[CTCallCapabilities setIsRTTSupported:];
-[CTCallCapabilities setIsEmergencyCallingOnWifiAvailable:];
-[CTCallCapabilities setIsWifiCallingAvailable:];
-[CTCallCapabilities setIsCarrierSupportsEmergencyCallOnWifiNoLimit:];
-[CTCallCapabilities isRTTSupported];
-[CTCallCapabilities isEmergencyCallingOnWifiAllowed];
-[CTCallCapabilities isCarrierSupportsEmergencyCallOnWifiNoLimit];
-[CTCallCapabilities isEmergencyCallingOnWifiAvailable];
-[CTCallCapabilities isCSCallingAvailable];
-[CTCallCapabilities isVoLTECallingAvailable];
-[CTCallCapabilities isEmergencyRTTSupported];
-[CTCallCapabilities setIsHoldForRTTEnabled:];
-[CTCallCapabilities isTTYSupported];
-[CTCallCapabilities setIsTTYSupported:];
-[CTCallCapabilities isWifiCallingAvailable];
-[CTCallCapabilities setIsEmergencyRTTSupported:];
-[CTCallCapabilities encodeWithCoder:];
-[CTCallCapabilities setIsVoLTECallingAvailable:];
-[CTCallCapabilities description];
-[CTCallCapabilities initWithCoder:];
-[CTCallCapabilities setIsEmergencyCallingOnWifiAllowed:];
-[CTCallCapabilities copyWithZone:];
-[CTCallCapabilities isHoldForRTTEnabled];
-[CTCallCapabilities setIsCSCallingAvailable:];
```
