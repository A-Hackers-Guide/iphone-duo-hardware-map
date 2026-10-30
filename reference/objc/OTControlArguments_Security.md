# `OTControlArguments`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 7 instance variables, 7 properties, 26 instance methods, 1 class methods

## Instance variables

```
B _canSendMetrics;
@"NSString" _contextID;
@"NSString" _containerName;
@"NSString" _altDSID;
@"NSString" _flowID;
@"NSString" _deviceSessionID;
q _stableTrustedDeviceIDStatus;
```

## Properties

```
@property (T@"NSString",&,V_contextID) contextID;
@property (T@"NSString",&,V_containerName) containerName;
@property (T@"NSString",&,V_altDSID) altDSID;
@property (T@"NSString",&,V_flowID) flowID;
@property (T@"NSString",&,V_deviceSessionID) deviceSessionID;
@property (TB,V_canSendMetrics) canSendMetrics;
@property (Tq,V_stableTrustedDeviceIDStatus) stableTrustedDeviceIDStatus;
```

## Class methods

```
+[OTControlArguments supportsSecureCoding];
```

## Instance methods

```
-[OTControlArguments initWithAltDSID:];
-[OTControlArguments initWithAltDSID:flowID:deviceSessionID:canSendMetrics:];
-[OTControlArguments stableTrustedDeviceIDStatus];
-[OTControlArguments setAltDSID:];
-[OTControlArguments altDSID];
-[OTControlArguments setContextID:];
-[OTControlArguments flowID];
-[OTControlArguments init];
-[OTControlArguments initWithAltDSID:flowID:deviceSessionID:];
-[OTControlArguments initWithConfiguration:];
-[OTControlArguments canSendMetrics];
-[OTControlArguments setCanSendMetrics:];
-[OTControlArguments containerName];
-[OTControlArguments setStableTrustedDeviceIDStatus:];
-[OTControlArguments encodeWithCoder:];
-[OTControlArguments makeConfigurationContext];
-[OTControlArguments description];
-[OTControlArguments initWithContainerName:contextID:altDSID:flowID:deviceSessionID:];
-[OTControlArguments initWithCoder:];
-[OTControlArguments setDeviceSessionID:];
-[OTControlArguments contextID];
-[OTControlArguments initWithContainerName:contextID:altDSID:];
-[OTControlArguments initWithContainerName:contextID:altDSID:flowID:deviceSessionID:canSendMetrics:stableTrustedDeviceIDStatus:];
-[OTControlArguments deviceSessionID];
-[OTControlArguments setFlowID:];
-[OTControlArguments setContainerName:];
```
