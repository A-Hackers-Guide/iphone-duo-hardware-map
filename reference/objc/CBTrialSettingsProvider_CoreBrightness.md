# `CBTrialSettingsProvider`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBAdaptiveAutoBrightnessSettingsProvider`
- 3 instance variables, 4 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"TRIClient" _client;
@"<TRINotificationToken>" _notificationToken;
@"TRIExperimentIdentifiers" _experimentIdentifiers;
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
+[CBTrialSettingsProvider sharedInstance];
```

## Instance methods

```
-[CBTrialSettingsProvider init];
-[CBTrialSettingsProvider dealloc];
-[CBTrialSettingsProvider aabUpdateStrategyType];
-[CBTrialSettingsProvider copyExperimentIdentifiers];
-[CBTrialSettingsProvider getMLABModelPath];
-[CBTrialSettingsProvider registerAutoBrightnessSettingsUpdateHandler:];
-[CBTrialSettingsProvider unregisterAutoBrightnessSettingsUpdateHandler];
```
