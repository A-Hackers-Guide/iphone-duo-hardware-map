# `NPHVMSyncSessionManager`

- Image: [`/System/Library/PrivateFrameworks/TelephonyRPC.framework/TelephonyRPC`](../userland/System__Library__PrivateFrameworks__TelephonyRPC.framework__TelephonyRPC.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SYSessionDelegate`, `SYChangeSerializer`
- 5 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _deltaSyncChanges;
@"NSMutableArray" _deltaSyncChangeTypes;
Q _deltaSyncCurrentIdx;
B _cancelled;
@"NSObject<NPHVMSyncSessionManagerDelegate>" _delegate;
```

## Properties

```
@property (T@"NSObject<NPHVMSyncSessionManagerDelegate>",N,V_delegate) delegate;
@property (TB,GisCancelled,V_cancelled) cancelled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[NPHVMSyncSessionManager setCancelled:];
-[NPHVMSyncSessionManager init];
-[NPHVMSyncSessionManager isCancelled];
-[NPHVMSyncSessionManager setDelegate:];
-[NPHVMSyncSessionManager delegate];
-[NPHVMSyncSessionManager dataFromChange:];
-[NPHVMSyncSessionManager changeFromData:ofType:];
-[NPHVMSyncSessionManager decodeChangeData:fromProtocolVersion:ofType:];
-[NPHVMSyncSessionManager encodeSYChangeForBackwardCompatibility:protocolVersion:];
-[NPHVMSyncSessionManager syncSession:applyChanges:completion:];
-[NPHVMSyncSessionManager syncSession:didEndWithError:];
-[NPHVMSyncSessionManager syncSession:enqueueChanges:error:];
-[NPHVMSyncSessionManager syncSession:resetDataStoreWithError:];
-[NPHVMSyncSessionManager enqueueVoicemailChanges:changeType:];
```
