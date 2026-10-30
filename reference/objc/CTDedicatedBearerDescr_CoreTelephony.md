# `CTDedicatedBearerDescr`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 7 instance variables, 7 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"NSString" _src_ip;
@"NSArray" _src_ports;
@"NSString" _remote_ip;
@"NSArray" _remote_ports;
Q _ip_protocol;
@"NSString" _traffic_class;
q _direction;
```

## Properties

```
@property (T@"NSString",&,N,V_src_ip) src_ip;
@property (T@"NSArray",&,N,V_src_ports) src_ports;
@property (T@"NSString",&,N,V_remote_ip) remote_ip;
@property (T@"NSArray",&,N,V_remote_ports) remote_ports;
@property (TQ,N,V_ip_protocol) ip_protocol;
@property (T@"NSString",&,N,V_traffic_class) traffic_class;
@property (Tq,N,V_direction) direction;
```

## Class methods

```
+[CTDedicatedBearerDescr supportsSecureCoding];
```

## Instance methods

```
-[CTDedicatedBearerDescr init];
-[CTDedicatedBearerDescr setDirection:];
-[CTDedicatedBearerDescr direction];
-[CTDedicatedBearerDescr encodeWithCoder:];
-[CTDedicatedBearerDescr description];
-[CTDedicatedBearerDescr initWithCoder:];
-[CTDedicatedBearerDescr copyWithZone:];
-[CTDedicatedBearerDescr setIp_protocol:];
-[CTDedicatedBearerDescr ip_protocol];
-[CTDedicatedBearerDescr remote_ip];
-[CTDedicatedBearerDescr remote_ports];
-[CTDedicatedBearerDescr setRemote_ip:];
-[CTDedicatedBearerDescr setRemote_ports:];
-[CTDedicatedBearerDescr setSrc_ip:];
-[CTDedicatedBearerDescr setSrc_ports:];
-[CTDedicatedBearerDescr setTraffic_class:];
-[CTDedicatedBearerDescr src_ip];
-[CTDedicatedBearerDescr src_ports];
-[CTDedicatedBearerDescr traffic_class];
```
