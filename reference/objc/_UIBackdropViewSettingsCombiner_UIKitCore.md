# `_UIBackdropViewSettingsCombiner`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIBackdropViewSettings`
- 5 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"_UIBackdropViewSettings" _inputSettingsA;
@"_UIBackdropViewSettings" _inputSettingsB;
d _weighting;
@"_UIBackdropViewSettings" _outputSettingsA;
@"_UIBackdropViewSettings" _outputSettingsB;
```

## Properties

```
@property (T@"_UIBackdropViewSettings",&,N,V_outputSettingsA) outputSettingsA;
@property (T@"_UIBackdropViewSettings",&,N,V_outputSettingsB) outputSettingsB;
@property (T@"_UIBackdropViewSettings",&,N,V_inputSettingsA) inputSettingsA;
@property (T@"_UIBackdropViewSettings",&,N,V_inputSettingsB) inputSettingsB;
@property (Td,N,V_weighting) weighting;
```

## Instance methods

```
-[_UIBackdropViewSettingsCombiner computeOutputSettingsUsingModel:];
-[_UIBackdropViewSettingsCombiner setDefaultValues];
-[_UIBackdropViewSettingsCombiner isBackdropVisible];
-[_UIBackdropViewSettingsCombiner weighting];
-[_UIBackdropViewSettingsCombiner setWeighting:];
-[_UIBackdropViewSettingsCombiner outputSettingsA];
-[_UIBackdropViewSettingsCombiner outputSettingsB];
-[_UIBackdropViewSettingsCombiner copyAdditionalSettingsFromSettings:];
-[_UIBackdropViewSettingsCombiner inputSettingsA];
-[_UIBackdropViewSettingsCombiner inputSettingsB];
-[_UIBackdropViewSettingsCombiner requiresBackdropLayer];
-[_UIBackdropViewSettingsCombiner setInputSettingsA:];
-[_UIBackdropViewSettingsCombiner setInputSettingsB:];
-[_UIBackdropViewSettingsCombiner setOutputSettingsA:];
-[_UIBackdropViewSettingsCombiner setOutputSettingsB:];
-[_UIBackdropViewSettingsCombiner setRequiresColorStatistics:];
```
