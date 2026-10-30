# `W5Event`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 17 instance methods, 1 class methods

## Instance variables

```
q _eventID;
d _timestamp;
@"NSDictionary" _info;
@"W5Peer" _peer;
```

## Properties

```
@property (Tq,N,V_eventID) eventID;
@property (Td,N,V_timestamp) timestamp;
@property (T@"NSDictionary",C,N,V_info) info;
@property (T@"W5Peer",C,N,V_peer) peer;
```

## Class methods

```
+[W5Event supportsSecureCoding];
```

## Instance methods

```
-[W5Event setTimestamp:];
-[W5Event eventID];
-[W5Event info];
-[W5Event setInfo:];
-[W5Event isEqualToEvent:];
-[W5Event dealloc];
-[W5Event timestamp];
-[W5Event encodeWithCoder:];
-[W5Event peer];
-[W5Event conformsToProtocol:];
-[W5Event hash];
-[W5Event description];
-[W5Event initWithCoder:];
-[W5Event setEventID:];
-[W5Event copyWithZone:];
-[W5Event isEqual:];
-[W5Event setPeer:];
```
