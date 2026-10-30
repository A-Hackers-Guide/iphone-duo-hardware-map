# `SRReaderFetchRequest`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRRequestFetching`
- 5 instance variables, 11 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"<SRRequestReading>" _readerRequest;
B _bypassHoldingPeriod;
d _from;
d _to;
@"SRCursor" _cursor;
```

## Properties

```
@property (T@"NSString",&,N) sensor;
@property (T@"NSString",&,N) bundleIdentifier;
@property (T@"NSString",&,N) deviceIdentifier;
@property (Td,V_from) from;
@property (Td,V_to) to;
@property (TB,V_bypassHoldingPeriod) bypassHoldingPeriod;
@property (T@"SRCursor",&,N,V_cursor) cursor;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRReaderFetchRequest supportsSecureCoding];
```

## Instance methods

```
-[SRReaderFetchRequest setTo:];
-[SRReaderFetchRequest to];
-[SRReaderFetchRequest cursor];
-[SRReaderFetchRequest setFrom:];
-[SRReaderFetchRequest from];
-[SRReaderFetchRequest setDeviceIdentifier:];
-[SRReaderFetchRequest init];
-[SRReaderFetchRequest dealloc];
-[SRReaderFetchRequest bundleIdentifier];
-[SRReaderFetchRequest deviceIdentifier];
-[SRReaderFetchRequest sensor];
-[SRReaderFetchRequest encodeWithCoder:];
-[SRReaderFetchRequest description];
-[SRReaderFetchRequest initWithCoder:];
-[SRReaderFetchRequest setBundleIdentifier:];
-[SRReaderFetchRequest setCursor:];
-[SRReaderFetchRequest setSensor:];
-[SRReaderFetchRequest bypassHoldingPeriod];
-[SRReaderFetchRequest setBypassHoldingPeriod:];
```
