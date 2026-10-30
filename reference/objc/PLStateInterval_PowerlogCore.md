# `PLStateInterval`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 12 instance variables, 14 properties, 19 instance methods, 1 class methods

## Instance variables

```
B _bundleIDResolved;
i _pid;
@"NSString" _domain;
@"NSString" _label;
@"NSString" _bundleID;
@"NSString" _processName;
d _durationMs;
@"NSDate" _startDate;
@"NSDate" _endDate;
@"NSDictionary" _stableState;
@"NSString" _processImageUUID;
@"NSString" _processImagePath;
```

## Properties

```
@property (T@"NSString",R,C,N,V_domain) domain;
@property (T@"NSString",R,C,N,V_label) label;
@property (T@"NSString",R,C,N,V_bundleID) bundleID;
@property (TB,R,N,V_bundleIDResolved) bundleIDResolved;
@property (T@"NSString",R,C,N,V_processName) processName;
@property (Td,R,N,V_durationMs) durationMs;
@property (T@"NSDate",R,N,V_startDate) startDate;
@property (T@"NSDate",R,N,V_endDate) endDate;
@property (T@"NSDictionary",R,C,N,V_stableState) stableState;
@property (Ti,R,N,V_pid) pid;
@property (T@"NSString",R,C,N,V_processImageUUID) processImageUUID;
@property (T@"NSString",R,C,N,V_processImagePath) processImagePath;
@property (Td,R,N) durationSeconds;
@property (T@"NSString",R,C,N) aggregationKey;
```

## Class methods

```
+[PLStateInterval intervalFromDictionary:];
```

## Instance methods

```
-[PLStateInterval toDictionary];
-[PLStateInterval startDate];
-[PLStateInterval processImagePath];
-[PLStateInterval domain];
-[PLStateInterval label];
-[PLStateInterval endDate];
-[PLStateInterval pid];
-[PLStateInterval processName];
-[PLStateInterval durationSeconds];
-[PLStateInterval description];
-[PLStateInterval bundleID];
-[PLStateInterval copyWithZone:];
-[PLStateInterval processImageUUID];
-[PLStateInterval durationMs];
-[PLStateInterval aggregationKey];
-[PLStateInterval bundleIDResolved];
-[PLStateInterval initWithDomain:label:bundleID:bundleIDResolved:processName:durationMs:startDate:endDate:stableState:pid:processImageUUID:processImagePath:];
-[PLStateInterval intervalWithResolvedBundleID:];
-[PLStateInterval stableState];
```
