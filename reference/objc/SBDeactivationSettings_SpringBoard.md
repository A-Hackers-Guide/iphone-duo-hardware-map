# `SBDeactivationSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSSettingDescriptionProvider`, `SBDeactivationSettings`, `NSCopying`, `BSDescriptionProviding`
- 1 instance variables, 5 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"BSMutableSettings" _settings;
```

## Properties

```
@property (TB,R,N,GisEmpty) empty;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDeactivationSettings succinctDescriptionBuilder];
-[SBDeactivationSettings init];
-[SBDeactivationSettings dealloc];
-[SBDeactivationSettings valueDescriptionForFlag:object:ofSetting:];
-[SBDeactivationSettings keyDescriptionForSetting:];
-[SBDeactivationSettings descriptionWithMultilinePrefix:];
-[SBDeactivationSettings succinctDescription];
-[SBDeactivationSettings isEmpty];
-[SBDeactivationSettings description];
-[SBDeactivationSettings copyWithZone:];
-[SBDeactivationSettings descriptionBuilderWithMultilinePrefix:];
-[SBDeactivationSettings setFlag:forDeactivationSetting:];
-[SBDeactivationSettings applyDeactivationSettings:];
-[SBDeactivationSettings boolForDeactivationSetting:];
-[SBDeactivationSettings clearDeactivationSettings];
-[SBDeactivationSettings copyDeactivationSettings];
-[SBDeactivationSettings flagForDeactivationSetting:];
-[SBDeactivationSettings objectForDeactivationSetting:];
-[SBDeactivationSettings setObject:forDeactivationSetting:];
```
