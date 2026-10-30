# `CBDisplayPreferences`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 2 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSUserDefaults" _cbDefaults;
@"NSString" _key;
@"<CBPrimitiveConfigurationProvider>" _bbdPrefs;
@"NSMutableDictionary" _prefsValue;
@"NSObject<OS_os_log>" _logHandle;
```

## Properties

```
@property (T@"NSDictionary",C,N,GgetAABUserPreference) AABUserPreference;
@property (TB,N,GgetAutobrightnessEnabled) autoBrightnessEnabled;
```

## Instance methods

```
-[CBDisplayPreferences dealloc];
-[CBDisplayPreferences setAutoBrightnessEnabled:];
-[CBDisplayPreferences flushPrefs];
-[CBDisplayPreferences getAABUserPreference];
-[CBDisplayPreferences getAutobrightnessEnabled];
-[CBDisplayPreferences initWithDisplayKey:];
-[CBDisplayPreferences initWithDisplayKey:andBackend:andBackboard:];
-[CBDisplayPreferences loadPrefs];
-[CBDisplayPreferences migrateAABUserPreferences];
-[CBDisplayPreferences migrationTimestamp];
-[CBDisplayPreferences populatePrefs:];
-[CBDisplayPreferences setAABUserPreference:];
```
