# `TMBLControl`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLControl`
- 4 instance variables, 0 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"NSObject<OS_dispatch_queue>" _queue;
@? _callback;
@"NSMutableDictionary" _displays;
```

## Instance methods

```
-[TMBLControl useSyncBrightnessTransactionForDisplay:];
-[TMBLControl findDisplays];
-[TMBLControl copyStatusInfo];
-[TMBLControl addDisplayModuleForBrightnessControlProxy:];
-[TMBLControl setPropertyWithKey:property:client:];
-[TMBLControl copyIdentifiers];
-[TMBLControl handleCAWindowServerDisplay:];
-[TMBLControl init];
-[TMBLControl stop];
-[TMBLControl dealloc];
-[TMBLControl copyPropertyForKey:client:handle:error:];
-[TMBLControl start];
-[TMBLControl setProperty:forKey:andHandle:error:];
-[TMBLControl scheduleDisplayModeCompletionTimerIn:forDisplay:andMode:];
-[TMBLControl handleDisplayModeUpdatePropertyHandler:displayHandle:];
-[TMBLControl clearDisplaySet];
-[TMBLControl removeDisplayModuleWithID:];
-[TMBLControl _copyPropertyInternalForKey:];
-[TMBLControl _copyPropertyForKey:client:handle:error:];
-[TMBLControl _setPropertyWithKey:property:client:];
-[TMBLControl _setInternalProperty:forKey:andHandle:];
-[TMBLControl copyPropertyWithKey:client:];
-[TMBLControl _setProperty:forKey:andHandle:error:];
```
