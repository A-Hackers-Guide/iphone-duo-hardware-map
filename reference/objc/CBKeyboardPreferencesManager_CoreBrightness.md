# `CBKeyboardPreferencesManager`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 5 instance methods, 11 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableDictionary" _preferences;
```

## Class methods

```
+[CBKeyboardPreferencesManager sharedInstance];
+[CBKeyboardPreferencesManager copyAllPreferences];
+[CBKeyboardPreferencesManager copyPreferenceForKey:];
+[CBKeyboardPreferencesManager copyPreferenceForKey:keyboardID:];
+[CBKeyboardPreferencesManager getBoolPreference:forKey:];
+[CBKeyboardPreferencesManager getFloatPreference:forKey:];
+[CBKeyboardPreferencesManager getIntPreference:forKey:];
+[CBKeyboardPreferencesManager setBoolPreference:forKey:];
+[CBKeyboardPreferencesManager setFloatPreference:forKey:];
+[CBKeyboardPreferencesManager setIntPreference:forKey:];
+[CBKeyboardPreferencesManager setPreference:forKey:];
```

## Instance methods

```
-[CBKeyboardPreferencesManager init];
-[CBKeyboardPreferencesManager dealloc];
-[CBKeyboardPreferencesManager copyAllPrefereneces];
-[CBKeyboardPreferencesManager copyPreferenceForKey:];
-[CBKeyboardPreferencesManager setPreference:forKey:];
```
