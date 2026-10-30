# `UIAutonomousSingleAppModeConfiguration`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 8 properties, 19 instance methods, 2 class methods

## Instance variables

```
@"NSMutableDictionary" _propertiesAsDictionary;
Q _style;
@"NSDictionary" _managedConfigurationSettings;
```

## Properties

```
@property (TQ,N,V_style) style;
@property (TB,N) allowsLockButton;
@property (TB,N) allowsAutoLock;
@property (TB,N) allowsAccessibilityShortcut;
@property (TB,N) automaticallyRelaunchesAfterAppCrash;
@property (TB,N) showsUserConfirmationPromptsAndBanners;
@property (T@"NSDictionary",&,N,V_managedConfigurationSettings) managedConfigurationSettings;
@property (T@"NSDictionary",R,N) propertiesAsDictionary;
```

## Class methods

```
+[UIAutonomousSingleAppModeConfiguration defaultConfiguration];
+[UIAutonomousSingleAppModeConfiguration defaultConfigurationForStyle:];
```

## Instance methods

```
-[UIAutonomousSingleAppModeConfiguration style];
-[UIAutonomousSingleAppModeConfiguration setStyle:];
-[UIAutonomousSingleAppModeConfiguration copyWithZone:];
-[UIAutonomousSingleAppModeConfiguration propertiesAsDictionary];
-[UIAutonomousSingleAppModeConfiguration setAllowsAccessibilityShortcut:];
-[UIAutonomousSingleAppModeConfiguration __gaxTrampoline_defaultBoolValueForFeatureKey:];
-[UIAutonomousSingleAppModeConfiguration _boolValueForFeatureKey:];
-[UIAutonomousSingleAppModeConfiguration _setBoolValue:forFeatureKey:];
-[UIAutonomousSingleAppModeConfiguration allowsAccessibilityShortcut];
-[UIAutonomousSingleAppModeConfiguration allowsAutoLock];
-[UIAutonomousSingleAppModeConfiguration allowsLockButton];
-[UIAutonomousSingleAppModeConfiguration automaticallyRelaunchesAfterAppCrash];
-[UIAutonomousSingleAppModeConfiguration managedConfigurationSettings];
-[UIAutonomousSingleAppModeConfiguration setAllowsAutoLock:];
-[UIAutonomousSingleAppModeConfiguration setAllowsLockButton:];
-[UIAutonomousSingleAppModeConfiguration setAutomaticallyRelaunchesAfterAppCrash:];
-[UIAutonomousSingleAppModeConfiguration setManagedConfigurationSettings:];
-[UIAutonomousSingleAppModeConfiguration setShowsUserConfirmationPromptsAndBanners:];
-[UIAutonomousSingleAppModeConfiguration showsUserConfirmationPromptsAndBanners];
```
