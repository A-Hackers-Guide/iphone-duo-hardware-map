# `W5PingResult`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 17 instance variables, 18 properties, 41 instance methods, 1 class methods

## Instance variables

```
@"NSString" _address;
@"NSString" _interfaceName;
d _timeout;
d _wait;
d _interval;
q _count;
q _trafficClass;
Q _dataLength;
d _packetLoss;
d _min;
d _max;
d _avg;
d _stddev;
@"NSString" _command;
@"NSString" _output;
d _startedAt;
d _endedAt;
```

## Properties

```
@property (T@"NSString",C,N,V_address) address;
@property (T@"NSString",C,N,V_interfaceName) interfaceName;
@property (Td,N,V_timeout) timeout;
@property (Td,N,V_wait) wait;
@property (Td,N,V_interval) interval;
@property (Tq,N,V_count) count;
@property (Tq,N,V_trafficClass) trafficClass;
@property (TQ,N,V_dataLength) dataLength;
@property (Td,N,V_packetLoss) packetLoss;
@property (Td,N,V_min) min;
@property (Td,N,V_max) max;
@property (Td,N,V_avg) avg;
@property (Td,N,V_stddev) stddev;
@property (T@"NSString",C,N,V_command) command;
@property (T@"NSString",C,N,V_output) output;
@property (Td,D,N) timestamp;
@property (Td,N,V_startedAt) startedAt;
@property (Td,N,V_endedAt) endedAt;
```

## Class methods

```
+[W5PingResult supportsSecureCoding];
```

## Instance methods

```
-[W5PingResult min];
-[W5PingResult setDataLength:];
-[W5PingResult trafficClass];
-[W5PingResult address];
-[W5PingResult setCount:];
-[W5PingResult setInterval:];
-[W5PingResult interval];
-[W5PingResult setAddress:];
-[W5PingResult setOutput:];
-[W5PingResult setInterfaceName:];
-[W5PingResult dealloc];
-[W5PingResult timestamp];
-[W5PingResult command];
-[W5PingResult count];
-[W5PingResult interfaceName];
-[W5PingResult wait];
-[W5PingResult timeout];
-[W5PingResult dataLength];
-[W5PingResult endedAt];
-[W5PingResult setEndedAt:];
-[W5PingResult setTrafficClass:];
-[W5PingResult setTimeout:];
-[W5PingResult max];
-[W5PingResult setStartedAt:];
-[W5PingResult encodeWithCoder:];
-[W5PingResult conformsToProtocol:];
-[W5PingResult description];
-[W5PingResult initWithCoder:];
-[W5PingResult output];
-[W5PingResult copyWithZone:];
-[W5PingResult startedAt];
-[W5PingResult setMax:];
-[W5PingResult setCommand:];
-[W5PingResult setMin:];
-[W5PingResult avg];
-[W5PingResult setAvg:];
-[W5PingResult setStddev:];
-[W5PingResult stddev];
-[W5PingResult packetLoss];
-[W5PingResult setPacketLoss:];
-[W5PingResult setWait:];
```
