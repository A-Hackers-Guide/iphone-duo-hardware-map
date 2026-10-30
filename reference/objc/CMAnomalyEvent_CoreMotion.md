# `CMAnomalyEvent`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 9 instance variables, 12 properties, 26 instance methods, 1 class methods

## Instance variables

```
B _acknowledgement;
q _state;
q _response;
q _resolution;
d _absoluteTimestamp;
d _updateTimestamp;
Q _identifier;
q _sosState;
q _operatingMode;
```

## Properties

```
@property (Tq,N,V_response) response;
@property (Tq,N,V_resolution) resolution;
@property (TB,N,GisAcknowledgement,V_acknowledgement) acknowledgement;
@property (Td,N,V_absoluteTimestamp) absoluteTimestamp;
@property (Td,N,V_updateTimestamp) updateTimestamp;
@property (Tq,N,V_sosState) sosState;
@property (Tq,N,V_operatingMode) operatingMode;
@property (T@"NSDate",R,N) timestamp;
@property (T@"NSDate",R,N) date;
@property (T@"NSDate",R,N) updateDate;
@property (TQ,R,N,V_identifier) identifier;
@property (Tq,R,N,V_state) state;
```

## Class methods

```
+[CMAnomalyEvent supportsSecureCoding];
```

## Instance methods

```
-[CMAnomalyEvent operatingMode];
-[CMAnomalyEvent setResponse:];
-[CMAnomalyEvent debugDescription];
-[CMAnomalyEvent identifier];
-[CMAnomalyEvent updateDate];
-[CMAnomalyEvent setOperatingMode:];
-[CMAnomalyEvent timestamp];
-[CMAnomalyEvent resolution];
-[CMAnomalyEvent date];
-[CMAnomalyEvent setAbsoluteTimestamp:];
-[CMAnomalyEvent absoluteTimestamp];
-[CMAnomalyEvent encodeWithCoder:];
-[CMAnomalyEvent description];
-[CMAnomalyEvent initWithCoder:];
-[CMAnomalyEvent copyWithZone:];
-[CMAnomalyEvent updateTimestamp];
-[CMAnomalyEvent state];
-[CMAnomalyEvent response];
-[CMAnomalyEvent setResolution:];
-[CMAnomalyEvent initWithIdentifier:absoluteTimestamp:updateTimestamp:state:response:resolution:sosState:operatingMode:];
-[CMAnomalyEvent initWithIdentifier:absoluteTimestamp:updateTimestamp:state:response:resolution:sosState:operatingMode:acknowledgement:];
-[CMAnomalyEvent isAcknowledgement];
-[CMAnomalyEvent setAcknowledgement:];
-[CMAnomalyEvent setSosState:];
-[CMAnomalyEvent setUpdateTimestamp:];
-[CMAnomalyEvent sosState];
```
