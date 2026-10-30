# `_SBIdleTimerGlobalNumericSettingMonitor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_SBIdleTimerGlobalSettingMonitor`
- 2 instance variables, 1 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSNumber" _settingCache;
@? _fetchSettingFromSource;
```

## Properties

```
@property (T@"NSNumber",R,N) numericValue;
```

## Instance methods

```
-[_SBIdleTimerGlobalNumericSettingMonitor formattedValue];
-[_SBIdleTimerGlobalNumericSettingMonitor dealloc];
-[_SBIdleTimerGlobalNumericSettingMonitor _updateCache];
-[_SBIdleTimerGlobalNumericSettingMonitor numericValue];
-[_SBIdleTimerGlobalNumericSettingMonitor _settingChanged:];
-[_SBIdleTimerGlobalNumericSettingMonitor initWithLabel:delegate:updatingForNotification:fetchingWith:];
```
