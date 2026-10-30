# `BLSHEnvironmentUpdateData`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSString" _environmentIdentifier;
q _newBacklightState;
Q _pendingTransitionStateCount;
Q _timeStamp;
```

## Properties

```
@property (T@"NSString",R,C,N,V_environmentIdentifier) environmentIdentifier;
@property (Tq,R,N,V_newBacklightState) newBacklightState;
@property (TQ,R,N,V_pendingTransitionStateCount) pendingTransitionStateCount;
@property (TQ,R,N,V_timeStamp) timeStamp;
```

## Instance methods

```
-[BLSHEnvironmentUpdateData environmentIdentifier];
-[BLSHEnvironmentUpdateData description];
-[BLSHEnvironmentUpdateData isEqual:];
-[BLSHEnvironmentUpdateData timeStamp];
-[BLSHEnvironmentUpdateData initWithEnvironmentIdentifier:newBacklightState:pendingTransitionStateCount:];
-[BLSHEnvironmentUpdateData newBacklightState];
-[BLSHEnvironmentUpdateData pendingTransitionStateCount];
```
