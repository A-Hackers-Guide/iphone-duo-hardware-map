# `SNSessionObject` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SiriNetwork.framework/SiriNetwork`](../userland/System__Library__PrivateFrameworks__SiriNetwork.framework__SiriNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 14 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C,N) aceId;
@property (T@"NSString",C,N) refId;
```

## Instance methods

```
-[SNSessionObject isProvisional];
-[SNSessionObject aceId];
-[SNSessionObject refId];
-[SNSessionObject setAceId:];
-[SNSessionObject setRefId:];
-[SNSessionObject logDiagnostics];
-[SNSessionObject isRestartable];
-[SNSessionObject supportedByRemoteLimitedSession];
-[SNSessionObject bufferingAllowedDuringActiveSession];
-[SNSessionObject isRetryable];
-[SNSessionObject serializedAceDataError:];
-[SNSessionObject sessionRequestId];
-[SNSessionObject setSessionRequestId:];
-[SNSessionObject supportedByLocalSession];
```
