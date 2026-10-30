# `FBSSettingsDiff`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `BSSettingDescriptionProvider`, `BSDescriptionProviding`
- 7 instance variables, 4 properties, 26 instance methods, 3 class methods

## Instance variables

```
@"BSSettingsDiff" _diff;
@"BSSettingsDiff" _legacyDiff;
@"BSSettingsDiff" _localDiff;
@"BSSettingsDiff" _legacyLocalDiff;
# _settingsClass;
@"NSSet" _changedSettings;
@"NSSet" _changedLegacySettings;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSSettingsDiff diffFromSettings:toSettings:];
+[FBSSettingsDiff diffByApplyingDiff:toDiff:];
+[FBSSettingsDiff _settingsClass];
```

## Instance methods

```
-[FBSSettingsDiff inspectChangesWithBlock:];
-[FBSSettingsDiff succinctDescriptionBuilder];
-[FBSSettingsDiff init];
-[FBSSettingsDiff initWithXPCDictionary:];
-[FBSSettingsDiff settings:valueDescriptionForFlag:object:ofSetting:];
-[FBSSettingsDiff valueDescriptionForFlag:object:ofSetting:];
-[FBSSettingsDiff keyDescriptionForSetting:];
-[FBSSettingsDiff descriptionWithMultilinePrefix:];
-[FBSSettingsDiff succinctDescription];
-[FBSSettingsDiff encodeWithXPCDictionary:];
-[FBSSettingsDiff description];
-[FBSSettingsDiff descriptionBuilderWithMultilinePrefix:];
-[FBSSettingsDiff applyToMutableSettings:];
-[FBSSettingsDiff containsProperty:];
-[FBSSettingsDiff containsPropertyFromExtension:];
-[FBSSettingsDiff containsSetting:];
-[FBSSettingsDiff settings:keyDescriptionForSetting:];
-[FBSSettingsDiff changedSettings];
-[FBSSettingsDiff _changedSettings];
-[FBSSettingsDiff _isSignifcant];
-[FBSSettingsDiff containsLegacySetting:];
-[FBSSettingsDiff containsSettingNamed:];
-[FBSSettingsDiff evaluateWithInspector:context:];
-[FBSSettingsDiff initWithChangesFromSettings:toSettings:];
-[FBSSettingsDiff inspectOtherChangesWithBlock:];
-[FBSSettingsDiff settingsByApplyingToMutableCopyOfSettings:];
```
