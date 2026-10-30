# `FBSSettingsDiffInspector`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"BSMutableKeyedSettings" _observerInfo;
@"BSMutableSettings" _otherSettingsObserverInfo;
B _iteratingObservers;
```

## Instance methods

```
-[FBSSettingsDiffInspector removeAllObservers];
-[FBSSettingsDiffInspector succinctDescriptionBuilder];
-[FBSSettingsDiffInspector init];
-[FBSSettingsDiffInspector dealloc];
-[FBSSettingsDiffInspector descriptionWithMultilinePrefix:];
-[FBSSettingsDiffInspector succinctDescription];
-[FBSSettingsDiffInspector description];
-[FBSSettingsDiffInspector inspectDiff:withContext:];
-[FBSSettingsDiffInspector descriptionBuilderWithMultilinePrefix:];
-[FBSSettingsDiffInspector observeOtherSetting:withBlock:];
-[FBSSettingsDiffInspector observeProperty:withBlock:];
-[FBSSettingsDiffInspector observeSetting:withBlock:];
```
