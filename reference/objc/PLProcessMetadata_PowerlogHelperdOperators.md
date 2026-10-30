# `PLProcessMetadata`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
i _pid;
@"NSString" _bundleId;
@"NSString" _name;
Q _coalitionID;
@"NSDate" _lastActiveStart;
@"NSDate" _lastSuspendStart;
@"PLCoalitionSample" _coalitionSample;
@"NSNumber" _applicationState;
```

## Properties

```
@property (Ti,V_pid) pid;
@property (T@"NSString",&,V_bundleId) bundleId;
@property (T@"NSString",&,V_name) name;
@property (TQ,V_coalitionID) coalitionID;
@property (T@"NSDate",&,V_lastActiveStart) lastActiveStart;
@property (T@"NSDate",&,V_lastSuspendStart) lastSuspendStart;
@property (T@"PLCoalitionSample",&,V_coalitionSample) coalitionSample;
@property (T@"NSNumber",&,V_applicationState) applicationState;
```

## Instance methods

```
-[PLProcessMetadata setPid:];
-[PLProcessMetadata applicationState];
-[PLProcessMetadata setBundleId:];
-[PLProcessMetadata setApplicationState:];
-[PLProcessMetadata pid];
-[PLProcessMetadata bundleId];
-[PLProcessMetadata description];
-[PLProcessMetadata setName:];
-[PLProcessMetadata name];
-[PLProcessMetadata initWithPid:];
-[PLProcessMetadata setCoalitionID:];
-[PLProcessMetadata coalitionID];
-[PLProcessMetadata coalitionSample];
-[PLProcessMetadata lastActiveStart];
-[PLProcessMetadata lastSuspendStart];
-[PLProcessMetadata setCoalitionSample:];
-[PLProcessMetadata setLastActiveStart:];
-[PLProcessMetadata setLastSuspendStart:];
```
