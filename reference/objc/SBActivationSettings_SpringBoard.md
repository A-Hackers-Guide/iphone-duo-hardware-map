# `SBActivationSettings`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSSettingDescriptionProvider`, `SBActivationSettings`, `NSCopying`, `BSDescriptionProviding`
- 1 instance variables, 5 properties, 23 instance methods, 0 class methods

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
-[SBActivationSettings clearActivationSettings];
-[SBActivationSettings applyActivationSettings:];
-[SBActivationSettings succinctDescriptionBuilder];
-[SBActivationSettings init];
-[SBActivationSettings dealloc];
-[SBActivationSettings valueDescriptionForFlag:object:ofSetting:];
-[SBActivationSettings keyDescriptionForSetting:];
-[SBActivationSettings descriptionWithMultilinePrefix:];
-[SBActivationSettings flagForActivationSetting:];
-[SBActivationSettings copyActivationSettingsPassingFilter:];
-[SBActivationSettings succinctDescription];
-[SBActivationSettings boolForActivationSetting:];
-[SBActivationSettings isEmpty];
-[SBActivationSettings copyActivationSettings];
-[SBActivationSettings hash];
-[SBActivationSettings setObject:forActivationSetting:];
-[SBActivationSettings description];
-[SBActivationSettings objectForActivationSetting:];
-[SBActivationSettings setFlag:forActivationSetting:];
-[SBActivationSettings copyWithZone:];
-[SBActivationSettings isEqual:];
-[SBActivationSettings _settingsAreValidToMoveContentToNewScene];
-[SBActivationSettings descriptionBuilderWithMultilinePrefix:];
```
