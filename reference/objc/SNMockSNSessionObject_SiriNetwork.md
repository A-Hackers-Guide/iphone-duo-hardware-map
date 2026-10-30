# `SNMockSNSessionObject`

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SNSessionObject`, `SNThunking`
- 3 instance variables, 6 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_data>" _data;
@"NSError" serializedAceDataError;
@"NSString" aceId;
```

## Properties

```
@property (T@"NSString",C,N,VaceId) aceId;
@property (T@"NSString",C,N) refId;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SNMockSNSessionObject isProvisional];
-[SNMockSNSessionObject aceId];
-[SNMockSNSessionObject refId];
-[SNMockSNSessionObject setAceId:];
-[SNMockSNSessionObject setRefId:];
-[SNMockSNSessionObject logDiagnostics];
-[SNMockSNSessionObject siriCore_supportedByLocalSession];
-[SNMockSNSessionObject isRestartable];
-[SNMockSNSessionObject supportedByRemoteLimitedSession];
-[SNMockSNSessionObject bufferingAllowedDuringActiveSession];
-[SNMockSNSessionObject isRetryable];
-[SNMockSNSessionObject serializedAceDataError:];
-[SNMockSNSessionObject sessionRequestId];
-[SNMockSNSessionObject setDispatchData:];
-[SNMockSNSessionObject setSerializedAceDataError:];
-[SNMockSNSessionObject setSessionRequestId:];
-[SNMockSNSessionObject siriNetwork_invokeThunk];
-[SNMockSNSessionObject supportedByLocalSession];
```
