# `OTMetricsSessionData`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSString" _flowID;
@"NSString" _deviceSessionID;
@"NSString" _idMSTDLNotificationFlowID;
```

## Properties

```
@property (T@"NSString",R,V_flowID) flowID;
@property (T@"NSString",R,V_deviceSessionID) deviceSessionID;
@property (T@"NSString",R,V_idMSTDLNotificationFlowID) idMSTDLNotificationFlowID;
```

## Class methods

```
+[OTMetricsSessionData supportsSecureCoding];
```

## Instance methods

```
-[OTMetricsSessionData flowID];
-[OTMetricsSessionData encodeWithCoder:];
-[OTMetricsSessionData hash];
-[OTMetricsSessionData initWithCoder:];
-[OTMetricsSessionData isEqual:];
-[OTMetricsSessionData deviceSessionID];
-[OTMetricsSessionData idMSTDLNotificationFlowID];
-[OTMetricsSessionData initWithFlowID:deviceSessionID:idMSTDLNotificationFlowID:];
```
