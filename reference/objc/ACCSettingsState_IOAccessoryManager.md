# `ACCSettingsState`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`](../userland/System__Library__CoreAccessories__PlugIns__Transports__IOAccessoryManager.transport__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _boolValue;
B _exists;
q _defaultValue;
q _invalidValue;
q _intValue;
@"NSString" _key;
@"NSString" _applicationID;
@"NSString" _notificationName;
```

## Properties

```
@property (Tq,R,N,V_defaultValue) defaultValue;
@property (Tq,R,N,V_invalidValue) invalidValue;
@property (Tq,R,N,V_intValue) intValue;
@property (TB,R,N,V_boolValue) boolValue;
@property (TB,R,N,V_exists) exists;
@property (T@"NSString",R,N,V_key) key;
@property (T@"NSString",R,N,V_applicationID) applicationID;
@property (T@"NSString",R,N,V_notificationName) notificationName;
```

## Instance methods

```
-[ACCSettingsState applicationID];
-[ACCSettingsState intValue];
-[ACCSettingsState exists];
-[ACCSettingsState boolValue];
-[ACCSettingsState update];
-[ACCSettingsState defaultValue];
-[ACCSettingsState dealloc];
-[ACCSettingsState notificationName];
-[ACCSettingsState description];
-[ACCSettingsState key];
-[ACCSettingsState _readLoggingPrefs];
-[ACCSettingsState _registerForLoggingPrefsNotification];
-[ACCSettingsState initWithKey:applicationID:notification:defaultValue:invalidValue:];
-[ACCSettingsState invalidValue];
```
