# `SRFetchResult`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 6 instance variables, 8 properties, 19 instance methods, 2 class methods

## Instance variables

```
d _timestamp;
@"NSData" _sampleData;
@"NSDictionary" _metadata;
@"NSDictionary" _configuration;
# _sampleClass;
@"SRCursor" __cursor;
```

## Properties

```
@property (T@"NSData",&,V_sampleData) sampleData;
@property (T@"NSDictionary",&,V_metadata) metadata;
@property (T@"NSDictionary",&,V_configuration) configuration;
@property (T#,&,V_sampleClass) sampleClass;
@property (T@"SRCursor",&,N,V__cursor) _cursor;
@property (T@,R,C) sample;
@property (Td,R,V_timestamp) timestamp;
@property (T@"SRSourceDevice",R,N) sourceDevice;
```

## Class methods

```
+[SRFetchResult initialize];
+[SRFetchResult new];
```

## Instance methods

```
-[SRFetchResult init];
-[SRFetchResult dealloc];
-[SRFetchResult timestamp];
-[SRFetchResult setConfiguration:];
-[SRFetchResult metadata];
-[SRFetchResult configuration];
-[SRFetchResult setMetadata:];
-[SRFetchResult copyWithZone:];
-[SRFetchResult sourceDevice];
-[SRFetchResult sample];
-[SRFetchResult setSampleClass:];
-[SRFetchResult _cursor];
-[SRFetchResult _sensorConfiguration];
-[SRFetchResult initWithBytes:length:timestamp:metadata:configuration:cursor:sampleClass:];
-[SRFetchResult initWithData:timestamp:metadata:configuration:cursor:sampleClass:];
-[SRFetchResult sampleClass];
-[SRFetchResult sampleData];
-[SRFetchResult setSampleData:];
-[SRFetchResult set_cursor:];
```
