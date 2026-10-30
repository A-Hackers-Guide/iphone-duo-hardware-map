# `SBSensorActivityAttribution`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBActivityAttribution`
- Protocols: `SBFSensorActivityAttribution`
- 2 instance variables, 16 properties, 12 instance methods, 0 class methods

## Instance variables

```
q _sensor;
@"STDataAccessAttribution" _dataAccessAttribution;
```

## Properties

```
@property (Tq,R,N,V_sensor) sensor;
@property (T@"NSString",R,C,N) cameraIdentifier;
@property (TB,R,N) usedRecently;
@property (TB,R,N) hasSatisfiedMinimumOnTime;
@property (T@"STDataAccessAttribution",R,C,N,V_dataAccessAttribution) dataAccessAttribution;
@property (T@"NSString",R,C,N) displayName;
@property (T@"NSString",R,C,N) bundleIdentifier;
@property (T@"NSString",R,C,N) attributionGroup;
@property (T@"NSString",R,C,N) website;
@property (TB,R,N) isSystemService;
@property (T@"NSString",R,C,N) activeEntityBundleIdentifier;
@property (T@"NSString",R,C,N) executableDisplayName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSensorActivityAttribution succinctDescriptionBuilder];
-[SBSensorActivityAttribution usedRecently];
-[SBSensorActivityAttribution descriptionWithMultilinePrefix:];
-[SBSensorActivityAttribution succinctDescription];
-[SBSensorActivityAttribution hasSatisfiedMinimumOnTime];
-[SBSensorActivityAttribution sensor];
-[SBSensorActivityAttribution cameraIdentifier];
-[SBSensorActivityAttribution hash];
-[SBSensorActivityAttribution dataAccessAttribution];
-[SBSensorActivityAttribution isEqual:];
-[SBSensorActivityAttribution initWithDataAccessAttribution:];
-[SBSensorActivityAttribution descriptionBuilderWithMultilinePrefix:];
```
