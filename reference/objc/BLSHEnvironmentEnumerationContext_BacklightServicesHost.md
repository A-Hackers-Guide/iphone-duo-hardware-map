# `BLSHEnvironmentEnumerationContext`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`
- 8 instance variables, 7 properties, 7 instance methods, 2 class methods

## Instance variables

```
C _source;
@"NSString" _reason;
@"BLSBacklightChangeEvent" _event;
B _isFlipbook;
@"NSString" _enumeratingEnvironmentIdentifier;
q _backlightState;
Q _environmentCount;
Q _enumeratedCount;
```

## Properties

```
@property (Tq,R,N,V_backlightState) backlightState;
@property (TQ,R,N,V_environmentCount) environmentCount;
@property (TQ,R,N,V_enumeratedCount) enumeratedCount;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHEnvironmentEnumerationContext contextForUpdateFlipbookVisualState:backlightState:environmentCount:];
+[BLSHEnvironmentEnumerationContext contextForUpdateTransitionStatesToBacklightState:reason:event:environmentCount:];
```

## Instance methods

```
-[BLSHEnvironmentEnumerationContext backlightState];
-[BLSHEnvironmentEnumerationContext description];
-[BLSHEnvironmentEnumerationContext appendDescriptionToStream:];
-[BLSHEnvironmentEnumerationContext enumeratedCount];
-[BLSHEnvironmentEnumerationContext didEnumerateEnvironment:];
-[BLSHEnvironmentEnumerationContext environmentCount];
-[BLSHEnvironmentEnumerationContext initWithSource:backlightState:reason:event:isFlipbook:environmentCount:];
```
