# `ULSettingsRegistry`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 1 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSMutableSet" _settingNames;
```

## Properties

```
@property (T@"NSMutableSet",&,N,V_settingNames) settingNames;
```

## Class methods

```
+[ULSettingsRegistry shared];
```

## Instance methods

```
-[ULSettingsRegistry init];
-[ULSettingsRegistry settingNames];
-[ULSettingsRegistry checkSetting:];
-[ULSettingsRegistry registerSetting:];
-[ULSettingsRegistry setSettingNames:];
```
