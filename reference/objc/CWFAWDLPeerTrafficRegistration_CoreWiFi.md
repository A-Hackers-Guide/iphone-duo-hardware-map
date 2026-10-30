# `CWFAWDLPeerTrafficRegistration`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 8 instance variables, 8 properties, 24 instance methods, 1 class methods

## Instance variables

```
B _active;
i _sessionFlags;
@"NSString" _serviceName;
Q _desiredBandwidth;
Q _desiredLatency;
Q _preferredChannel;
Q _secondaryPreferredChannel;
@"NSArray" _peerContextList;
```

## Properties

```
@property (T@"NSString",C,N,V_serviceName) serviceName;
@property (TB,N,GisActive,V_active) active;
@property (Ti,N,V_sessionFlags) sessionFlags;
@property (TQ,N,V_desiredBandwidth) desiredBandwidth;
@property (TQ,N,V_desiredLatency) desiredLatency;
@property (TQ,N,V_preferredChannel) preferredChannel;
@property (TQ,N,V_secondaryPreferredChannel) secondaryPreferredChannel;
@property (T@"NSArray",C,N,V_peerContextList) peerContextList;
```

## Class methods

```
+[CWFAWDLPeerTrafficRegistration supportsSecureCoding];
```

## Instance methods

```
-[CWFAWDLPeerTrafficRegistration sessionFlags];
-[CWFAWDLPeerTrafficRegistration setActive:];
-[CWFAWDLPeerTrafficRegistration serviceName];
-[CWFAWDLPeerTrafficRegistration setServiceName:];
-[CWFAWDLPeerTrafficRegistration encodeWithCoder:];
-[CWFAWDLPeerTrafficRegistration hash];
-[CWFAWDLPeerTrafficRegistration description];
-[CWFAWDLPeerTrafficRegistration setSessionFlags:];
-[CWFAWDLPeerTrafficRegistration initWithCoder:];
-[CWFAWDLPeerTrafficRegistration isActive];
-[CWFAWDLPeerTrafficRegistration copyWithZone:];
-[CWFAWDLPeerTrafficRegistration isEqual:];
-[CWFAWDLPeerTrafficRegistration preferredChannel];
-[CWFAWDLPeerTrafficRegistration setPreferredChannel:];
-[CWFAWDLPeerTrafficRegistration desiredLatency];
-[CWFAWDLPeerTrafficRegistration peerContextList];
-[CWFAWDLPeerTrafficRegistration desiredBandwidth];
-[CWFAWDLPeerTrafficRegistration isEqualToAWDLPeerTrafficRegistration:];
-[CWFAWDLPeerTrafficRegistration secondaryPreferredChannel];
-[CWFAWDLPeerTrafficRegistration serializedRegistrationInfo];
-[CWFAWDLPeerTrafficRegistration setDesiredBandwidth:];
-[CWFAWDLPeerTrafficRegistration setDesiredLatency:];
-[CWFAWDLPeerTrafficRegistration setPeerContextList:];
-[CWFAWDLPeerTrafficRegistration setSecondaryPreferredChannel:];
```
