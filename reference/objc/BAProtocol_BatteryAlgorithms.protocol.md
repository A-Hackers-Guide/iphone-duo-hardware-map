# `BAProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BatteryAlgorithms.framework/BatteryAlgorithms`](../userland/System__Library__PrivateFrameworks__BatteryAlgorithms.framework__BatteryAlgorithms.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 7 properties, 14 instance methods, 1 class methods

## Properties

```
@property (T@"NSString",R,N) name;
@property (T@"NSString",R,N) version;
@property (T@"NSString",R,N) algoDescription;
@property (T@"NSNumber",R,N) runPeriod;
@property (T^Q,R,N) runType;
@property (TB,R,N) dataOnDemand;
@property (TB,R,N) freshInitNeeded;
```

## Class methods

```
+[BAProtocol algorithmWithData:];
```

## Instance methods

```
-[BAProtocol init];
-[BAProtocol version];
-[BAProtocol output];
-[BAProtocol name];
-[BAProtocol runWithData:];
-[BAProtocol runType];
-[BAProtocol algoDescription];
-[BAProtocol freshInitNeeded];
-[BAProtocol preRun:];
-[BAProtocol dataOnDemand];
-[BAProtocol freshInitWithData:];
-[BAProtocol getWithSpecifier:];
-[BAProtocol runPeriod];
-[BAProtocol updateWithSpecifier:];
```
