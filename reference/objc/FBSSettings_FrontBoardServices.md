# `FBSSettings`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSSettingsSubclass`, `BSXPCSecureCoding`, `BSXPCCoding`, `BSDescriptionProviding`, `FBSSettings`, `NSCopying`, `NSMutableCopying`
- 9 instance variables, 5 properties, 45 instance methods, 20 class methods

## Instance variables

```
# _baseClass;
@"BSKeyedSettings" _settings;
@"BSKeyedSettings" _localSettings;
@"BSSettings" _legacyLocalSettings;
@"BSSettings" _legacyOtherSettings;
@"FBSSettings" _progenitor;
@"NSOrderedSet" _orderedExtensions;
B _mutable;
B _needsCoW;
```

## Properties

```
@property (T@"BSSettings",R,C,N) otherSettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSSettings supportsBSXPCSecureCoding];
+[FBSSettings _baseClass];
+[FBSSettings initialize];
+[FBSSettings allSettings];
+[FBSSettings subclassExtension];
+[FBSSettings mutableSubclass];
+[FBSSettings _settingsExtensionsForSceneExtension:];
+[FBSSettings immutableSubclass];
+[FBSSettings _mutableClass];
+[FBSSettings settingForProperty:];
+[FBSSettings _counterpartClass];
+[FBSSettings _descriptionProvider];
+[FBSSettings _diffClass];
+[FBSSettings _extensionsAreLocal];
+[FBSSettings _legacyDescriptionProvider];
+[FBSSettings _setCounterpartClass:];
+[FBSSettings allSettingsFromExtension:];
+[FBSSettings allSettingsFromProtocol:];
+[FBSSettings settingForSubclassProperty:];
+[FBSSettings subclassExtensions];
```

## Instance methods

```
-[FBSSettings mutableCopyWithZone:];
-[FBSSettings debugDescription];
-[FBSSettings succinctDescriptionBuilder];
-[FBSSettings init];
-[FBSSettings initWithXPCDictionary:];
-[FBSSettings settings:valueDescriptionForFlag:object:ofSetting:];
-[FBSSettings valueDescriptionForFlag:object:ofSetting:];
-[FBSSettings keyDescriptionForSetting:];
-[FBSSettings descriptionWithMultilinePrefix:];
-[FBSSettings succinctDescription];
-[FBSSettings copy:];
-[FBSSettings encodeWithXPCDictionary:];
-[FBSSettings conformsToExtension:];
-[FBSSettings hash];
-[FBSSettings description];
-[FBSSettings encodeWithBSXPCCoder:];
-[FBSSettings initWithBSXPCCoder:];
-[FBSSettings copyWithZone:];
-[FBSSettings isEqual:];
-[FBSSettings initWithSettings:];
-[FBSSettings descriptionBuilderWithMultilinePrefix:];
-[FBSSettings valueForProperty:expectedClass:];
-[FBSSettings containsSetting:];
-[FBSSettings otherSettings];
-[FBSSettings setValue:forProperty:];
-[FBSSettings settings:appendDescriptionToBuilder:forFlag:object:ofSetting:];
-[FBSSettings appendDescriptionToBuilder:forFlag:object:ofSetting:];
-[FBSSettings settings:keyDescriptionForSetting:];
-[FBSSettings _addSceneExtension:];
-[FBSSettings _addSceneExtension:applyingSettings:];
-[FBSSettings _allSceneExtensions];
-[FBSSettings _appendToDescriptionBuilder:];
-[FBSSettings _copyClearingProgenitor:];
-[FBSSettings _hasAdditionalDescription];
-[FBSSettings _hasAnySceneExtension];
-[FBSSettings _indirect_isEmpty];
-[FBSSettings _isEmptyForCoding:];
-[FBSSettings _isEqualToSettings:];
-[FBSSettings _progenitor];
-[FBSSettings _removeAllSceneExtensions];
-[FBSSettings _removeSceneExtension:];
-[FBSSettings _removeVolatileSettings];
-[FBSSettings _sceneExtensionNames];
-[FBSSettings mutableCopy:];
-[FBSSettings valueForSetting:];
```
