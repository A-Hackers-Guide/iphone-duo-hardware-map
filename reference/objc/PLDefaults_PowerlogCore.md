# `PLDefaults`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 19 instance methods, 47 class methods

## Instance variables

```
B _debugEnabled;
B _eplEnabled;
B _enableRestartAtEPL;
@"NSMutableDictionary" _managedPrefsCache;
@"NSMutableDictionary" _instancePrefsCache;
@"NSMutableDictionary" _userPrefsCache;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_managedPrefsCache) managedPrefsCache;
@property (T@"NSMutableDictionary",&,V_instancePrefsCache) instancePrefsCache;
@property (T@"NSMutableDictionary",&,V_userPrefsCache) userPrefsCache;
@property (TB,V_enableRestartAtEPL) enableRestartAtEPL;
@property (TB,V_debugEnabled) debugEnabled;
@property (TB,V_eplEnabled) eplEnabled;
```

## Class methods

```
+[PLDefaults applicationID];
+[PLDefaults doubleForKey:];
+[PLDefaults eplEnabled];
+[PLDefaults enableRestartAtEPL];
+[PLDefaults liveModeQuery];
+[PLDefaults setClassName:debugEnabled:forKey:];
+[PLDefaults boolForKey:];
+[PLDefaults setClass:debugEnabled:];
+[PLDefaults longForKey:];
+[PLDefaults addActiveTaskingRequest:];
+[PLDefaults objectForKey:ifNotSet:];
+[PLDefaults fullPLLog];
+[PLDefaults oldFullMode];
+[PLDefaults isClassDebugEnabled:];
+[PLDefaults setObject:forKey:saveToDisk:];
+[PLDefaults resetUserDefaultCacheForKey:forApplicationID:];
+[PLDefaults isTaskFullEPLMode];
+[PLDefaults setClass:debugEnabled:forKey:];
+[PLDefaults boolForKey:ifNotSet:];
+[PLDefaults removeActiveTaskingRequest:];
+[PLDefaults setClassName:debugEnabled:];
+[PLDefaults objectForKey:];
+[PLDefaults isModelTrigger];
+[PLDefaults isClassDebugEnabled:forKey:];
+[PLDefaults fullMode];
+[PLDefaults setLastUploadDate:ForSubmitReason:];
+[PLDefaults isClassNameDebugEnabled:];
+[PLDefaults mode];
+[PLDefaults objectForKey:synchronize:];
+[PLDefaults taskMode];
+[PLDefaults longForKey:ifNotSet:];
+[PLDefaults registerEPLNotificationWithQueue:];
+[PLDefaults objectExistsForKey:];
+[PLDefaults setObject:forKey:];
+[PLDefaults setObject:forKey:forApplicationID:saveToDisk:];
+[PLDefaults isClassNameDebugEnabled:forKey:];
+[PLDefaults debugEnabled];
+[PLDefaults doubleForKey:ifNotSet:];
+[PLDefaults sharedDefaults];
+[PLDefaults resetUserDefaultCacheForKey:];
+[PLDefaults objectForKey:forApplicationID:synchronize:];
+[PLDefaults fullModeForClass:];
+[PLDefaults allDefaultsEnabled];
+[PLDefaults liteMode];
+[PLDefaults isDevBoard];
+[PLDefaults removeAllActiveTaskingRequests];
+[PLDefaults isModelingDebugEnabled];
```

## Instance methods

```
-[PLDefaults eplEnabled];
-[PLDefaults enableRestartAtEPL];
-[PLDefaults setDebugEnabled:];
-[PLDefaults setEnableRestartAtEPL:];
-[PLDefaults userDefaultsObjectForKey:forApplicationID:synchronize:];
-[PLDefaults init];
-[PLDefaults resetUserDefaultCacheForKey:forApplicationID:];
-[PLDefaults userPrefsCache];
-[PLDefaults setEplEnabled:];
-[PLDefaults setInstancePrefsCache:];
-[PLDefaults managedPrefsCache];
-[PLDefaults instancePrefsCache];
-[PLDefaults setManagedPrefsCache:];
-[PLDefaults setObject:forKey:forApplicationID:saveToDisk:];
-[PLDefaults debugEnabled];
-[PLDefaults managedPrefsObjectForKey:forApplicationID:synchronize:];
-[PLDefaults objectForKey:forApplicationID:synchronize:];
-[PLDefaults setUserPrefsCache:];
-[PLDefaults instancePrefsObjectForKey:];
```
