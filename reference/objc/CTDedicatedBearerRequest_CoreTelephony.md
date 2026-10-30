# `CTDedicatedBearerRequest`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 8 instance variables, 8 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _details;
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
@property (T@"NSArray",&,N,V_details) details;
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
+[CTDedicatedBearerRequest supportsSecureCoding];
```

## Instance methods

```
-[CTDedicatedBearerRequest details];
-[CTDedicatedBearerRequest setDetails:];
-[CTDedicatedBearerRequest init];
-[CTDedicatedBearerRequest setDirection:];
-[CTDedicatedBearerRequest direction];
-[CTDedicatedBearerRequest encodeWithCoder:];
-[CTDedicatedBearerRequest description];
-[CTDedicatedBearerRequest initWithCoder:];
-[CTDedicatedBearerRequest copyWithZone:];
-[CTDedicatedBearerRequest setIp_protocol:];
-[CTDedicatedBearerRequest ip_protocol];
-[CTDedicatedBearerRequest remote_ip];
-[CTDedicatedBearerRequest remote_ports];
-[CTDedicatedBearerRequest setRemote_ip:];
-[CTDedicatedBearerRequest setRemote_ports:];
-[CTDedicatedBearerRequest setSrc_ip:];
-[CTDedicatedBearerRequest setSrc_ports:];
-[CTDedicatedBearerRequest setTraffic_class:];
-[CTDedicatedBearerRequest src_ip];
-[CTDedicatedBearerRequest src_ports];
-[CTDedicatedBearerRequest traffic_class];
```
