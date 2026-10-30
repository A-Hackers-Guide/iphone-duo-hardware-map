# `_UIPrototypingSettingsManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _storedSettings;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_storedSettings) storedSettings;
@property (T@"NSArray",R,N) allSettings;
```

## Class methods

```
+[_UIPrototypingSettingsManager sharedManager];
```

## Instance methods

```
-[_UIPrototypingSettingsManager init];
-[_UIPrototypingSettingsManager allSettings];
-[_UIPrototypingSettingsManager deleteAllStoredSettings];
-[_UIPrototypingSettingsManager setStoredSettings:];
-[_UIPrototypingSettingsManager settingOfType:withName:];
-[_UIPrototypingSettingsManager storedSettings];
-[_UIPrototypingSettingsManager synchronizeStoredSettings];
```
