# `SBProcessSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSSettingDescriptionProvider`, `SBProcessSettings`, `NSCopying`, `BSDescriptionProviding`
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
-[SBProcessSettings succinctDescriptionBuilder];
-[SBProcessSettings init];
-[SBProcessSettings dealloc];
-[SBProcessSettings valueDescriptionForFlag:object:ofSetting:];
-[SBProcessSettings keyDescriptionForSetting:];
-[SBProcessSettings descriptionWithMultilinePrefix:];
-[SBProcessSettings succinctDescription];
-[SBProcessSettings isEmpty];
-[SBProcessSettings description];
-[SBProcessSettings copyWithZone:];
-[SBProcessSettings descriptionBuilderWithMultilinePrefix:];
-[SBProcessSettings applyProcessSettings:];
-[SBProcessSettings boolForProcessSetting:];
-[SBProcessSettings clearProcessSettings];
-[SBProcessSettings copyProcessSettings];
-[SBProcessSettings flagForProcessSetting:];
-[SBProcessSettings objectForProcessSetting:];
-[SBProcessSettings setFlag:forProcessSetting:];
-[SBProcessSettings setObject:forProcessSetting:];
```
