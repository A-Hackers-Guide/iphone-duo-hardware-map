# `CADisplayPersistedData`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 3 instance variables, 3 properties, 17 instance methods, 3 class methods

## Instance variables

```
@"NSString" _version;
@"NSMutableArray" _latencies;
@"NSMutableArray" _preferredModes;
```

## Properties

```
@property (T@"NSString",C,N,V_version) version;
@property (T@"NSMutableArray",&,N,V_latencies) latencies;
@property (T@"NSMutableArray",&,N,V_preferredModes) preferredModes;
```

## Class methods

```
+[CADisplayPersistedData sharedInstance];
+[CADisplayPersistedData supportsSecureCoding];
+[CADisplayPersistedData supportedClasses];
```

## Instance methods

```
-[CADisplayPersistedData save];
-[CADisplayPersistedData update];
-[CADisplayPersistedData init];
-[CADisplayPersistedData dealloc];
-[CADisplayPersistedData version];
-[CADisplayPersistedData encodeWithCoder:];
-[CADisplayPersistedData description];
-[CADisplayPersistedData initWithCoder:];
-[CADisplayPersistedData setVersion:];
-[CADisplayPersistedData latencies];
-[CADisplayPersistedData latencyForUUID:andMode:];
-[CADisplayPersistedData preferredModeForUUID:];
-[CADisplayPersistedData preferredModes];
-[CADisplayPersistedData setLatencies:];
-[CADisplayPersistedData setLatency:forUUID:andMode:];
-[CADisplayPersistedData setPreferredMode:forUUID:];
-[CADisplayPersistedData setPreferredModes:];
```
