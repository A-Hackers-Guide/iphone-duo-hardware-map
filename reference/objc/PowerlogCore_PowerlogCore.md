# `PowerlogCore`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 9 properties, 19 instance methods, 6 class methods

## Instance variables

```
@"NSObject<OS_dispatch_source>" _fVMPressureSource;
@"NSDate" _launchDate;
@"PLCoreStorage" _storage;
@"PLAccountingOperator" _accounting;
@"PLCoreAgent" _agents;
@"PLCoreService" _services;
@"PPSCoreStorage" _coreStorage;
@"PPSCollectionOperator" _collection;
@"NSObject<OS_os_transaction>" _userRequestTransaction;
@"PLCFNotificationOperatorComposition" _fireSBCListener;
```

## Properties

```
@property (T@"NSObject<OS_os_transaction>",&,V_userRequestTransaction) userRequestTransaction;
@property (T@"PLCFNotificationOperatorComposition",&,V_fireSBCListener) fireSBCListener;
@property (T@"NSDate",R,V_launchDate) launchDate;
@property (T@"PLCoreStorage",R,V_storage) storage;
@property (T@"PLAccountingOperator",R,V_accounting) accounting;
@property (T@"PLCoreAgent",R,V_agents) agents;
@property (T@"PLCoreService",R,V_services) services;
@property (T@"PPSCoreStorage",R,V_coreStorage) coreStorage;
@property (T@"PPSCollectionOperator",R,V_collection) collection;
```

## Class methods

```
+[PowerlogCore sharedCore];
+[PowerlogCore isDebugEnabled];
+[PowerlogCore allowRun];
+[PowerlogCore deprecateOldFullMode];
+[PowerlogCore setupCore];
+[PowerlogCore sharedCoreStarted];
```

## Instance methods

```
-[PowerlogCore services];
-[PowerlogCore init];
-[PowerlogCore dealloc];
-[PowerlogCore collection];
-[PowerlogCore storage];
-[PowerlogCore agents];
-[PowerlogCore launchDate];
-[PowerlogCore accounting];
-[PowerlogCore didRecieveMemoryPressureWarning];
-[PowerlogCore fireSBCListener];
-[PowerlogCore coreStorage];
-[PowerlogCore fireSignificantBatteryChangeNotification];
-[PowerlogCore setFireSBCListener:];
-[PowerlogCore setUserRequestTransaction:];
-[PowerlogCore setupForPreUnlockTelemetry];
-[PowerlogCore startCore];
-[PowerlogCore startCoreForTest];
-[PowerlogCore stopCore];
-[PowerlogCore userRequestTransaction];
```
