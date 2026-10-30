# `CADisplayPersistedLatency`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSString" _uuid;
@"NSDictionary" _mode;
d _latency;
```

## Properties

```
@property (T@"NSString",C,N,V_uuid) uuid;
@property (T@"NSDictionary",C,N,V_mode) mode;
@property (Td,N,V_latency) latency;
```

## Class methods

```
+[CADisplayPersistedLatency supportsSecureCoding];
```

## Instance methods

```
-[CADisplayPersistedLatency setLatency:];
-[CADisplayPersistedLatency latency];
-[CADisplayPersistedLatency uuid];
-[CADisplayPersistedLatency dealloc];
-[CADisplayPersistedLatency setUuid:];
-[CADisplayPersistedLatency setMode:];
-[CADisplayPersistedLatency encodeWithCoder:];
-[CADisplayPersistedLatency mode];
-[CADisplayPersistedLatency description];
-[CADisplayPersistedLatency initWithCoder:];
```
