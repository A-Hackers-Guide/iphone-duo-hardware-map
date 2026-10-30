# `CMHistoricalFetchToken`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 19 instance methods, 3 class methods

## Instance variables

```
@"NSMutableArray" _tables;
Q _version;
Q _fetchType;
d _startTime;
d _endTime;
```

## Properties

```
@property (T@"NSMutableArray",C,N,V_tables) tables;
@property (TQ,N,V_version) version;
@property (TQ,N,V_fetchType) fetchType;
@property (Td,N,V_startTime) startTime;
@property (Td,N,V_endTime) endTime;
```

## Class methods

```
+[CMHistoricalFetchToken supportsSecureCoding];
+[CMHistoricalFetchToken cardioToken];
+[CMHistoricalFetchToken mobilityToken];
```

## Instance methods

```
-[CMHistoricalFetchToken endTime];
-[CMHistoricalFetchToken setEndTime:];
-[CMHistoricalFetchToken startTime];
-[CMHistoricalFetchToken fetchType];
-[CMHistoricalFetchToken dealloc];
-[CMHistoricalFetchToken version];
-[CMHistoricalFetchToken setStartTime:];
-[CMHistoricalFetchToken encodeWithCoder:];
-[CMHistoricalFetchToken hash];
-[CMHistoricalFetchToken description];
-[CMHistoricalFetchToken initWithCoder:];
-[CMHistoricalFetchToken setVersion:];
-[CMHistoricalFetchToken copyWithZone:];
-[CMHistoricalFetchToken isEqual:];
-[CMHistoricalFetchToken getProgressState];
-[CMHistoricalFetchToken initWithType:cursorList:];
-[CMHistoricalFetchToken setFetchType:];
-[CMHistoricalFetchToken setTables:];
-[CMHistoricalFetchToken tables];
```
