# `CBAgregateSettingsProvider`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBAdaptiveAutoBrightnessSettingsProvider`
- 3 instance variables, 4 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"CBPreferencesSettingsProvider" _preferencesSettingsProvider;
@"CBTrialSettingsProvider" _trialSettingsProvider;
@"NSObject<OS_os_log>" _logHandle;
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
+[CBAgregateSettingsProvider sharedInstance];
```

## Instance methods

```
-[CBAgregateSettingsProvider dealloc];
-[CBAgregateSettingsProvider aabUpdateStrategyType];
-[CBAgregateSettingsProvider getMLABModelPath];
-[CBAgregateSettingsProvider initWithPreferences:andTrial:];
-[CBAgregateSettingsProvider registerAutoBrightnessSettingsUpdateHandler:];
-[CBAgregateSettingsProvider unregisterAutoBrightnessSettingsUpdateHandler];
```
