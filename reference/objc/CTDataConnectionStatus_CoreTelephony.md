# `CTDataConnectionStatus`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 12 instance variables, 12 properties, 28 instance methods, 1 class methods

## Instance variables

```
B _suspended;
B _publicNetAllowed;
I _wirelessTechnologyMask;
i _state;
i _ipFamily;
i _contextType;
i _transportType;
@"NSNumber" _pdp;
@"NSString" _interfaceName;
@"NSString" _apnName;
@"NSArray" _qosFlows;
@"NSArray" _trafficDescriptors;
```

## Properties

```
@property (T@"NSNumber",&,N,V_pdp) pdp;
@property (T@"NSString",&,N,V_interfaceName) interfaceName;
@property (T@"NSString",&,N,V_apnName) apnName;
@property (TI,N,V_wirelessTechnologyMask) wirelessTechnologyMask;
@property (Ti,N,V_state) state;
@property (Ti,N,V_ipFamily) ipFamily;
@property (TB,N,V_suspended) suspended;
@property (TB,N,V_publicNetAllowed) publicNetAllowed;
@property (Ti,N,V_contextType) contextType;
@property (Ti,N,V_transportType) transportType;
@property (T@"NSArray",&,N,V_qosFlows) qosFlows;
@property (T@"NSArray",&,N,V_trafficDescriptors) trafficDescriptors;
```

## Class methods

```
+[CTDataConnectionStatus supportsSecureCoding];
```

## Instance methods

```
-[CTDataConnectionStatus suspended];
-[CTDataConnectionStatus setSuspended:];
-[CTDataConnectionStatus ipFamily];
-[CTDataConnectionStatus setState:];
-[CTDataConnectionStatus trafficDescriptors];
-[CTDataConnectionStatus setTransportType:];
-[CTDataConnectionStatus contextType];
-[CTDataConnectionStatus setApnName:];
-[CTDataConnectionStatus setContextType:];
-[CTDataConnectionStatus setInterfaceName:];
-[CTDataConnectionStatus publicNetAllowed];
-[CTDataConnectionStatus setPdp:];
-[CTDataConnectionStatus interfaceName];
-[CTDataConnectionStatus transportType];
-[CTDataConnectionStatus apnName];
-[CTDataConnectionStatus wirelessTechnologyMask];
-[CTDataConnectionStatus setQosFlows:];
-[CTDataConnectionStatus setPublicNetAllowed:];
-[CTDataConnectionStatus setIpFamily:];
-[CTDataConnectionStatus encodeWithCoder:];
-[CTDataConnectionStatus qosFlows];
-[CTDataConnectionStatus description];
-[CTDataConnectionStatus initWithCoder:];
-[CTDataConnectionStatus pdp];
-[CTDataConnectionStatus setTrafficDescriptors:];
-[CTDataConnectionStatus copyWithZone:];
-[CTDataConnectionStatus state];
-[CTDataConnectionStatus setWirelessTechnologyMask:];
```
