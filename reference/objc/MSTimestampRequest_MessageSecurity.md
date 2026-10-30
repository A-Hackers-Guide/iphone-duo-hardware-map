# `MSTimestampRequest`

- Image: [`/System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity`](../userland/System__Library__PrivateFrameworks__MessageSecurity.framework__MessageSecurity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 13 instance variables, 13 properties, 53 instance methods, 1 class methods

## Instance variables

```
B _certReq;
@"NSData" _timestampRequest;
@"MSMessageImprint" _messageImprint;
@"NSData" _nonce;
@"NSURL" _timestampServer;
q _maxRetryAttempts;
@"MSOID" _reqPolicyID;
q _version;
@"NSObject<OS_dispatch_queue>" _xpcQueue;
@"NSObject<OS_xpc_session>" _xpcSession;
q _retryCount;
q _firstRetryErrorCode;
@"NSDate" _fetchStartTime;
```

## Properties

```
@property (T@"NSData",&,V_nonce) nonce;
@property (TB,V_certReq) certReq;
@property (T@"MSOID",&,V_reqPolicyID) reqPolicyID;
@property (Tq,V_version) version;
@property (T@"MSMessageImprint",&,V_messageImprint) messageImprint;
@property (T@"NSObject<OS_dispatch_queue>",&,V_xpcQueue) xpcQueue;
@property (T@"NSObject<OS_xpc_session>",&,V_xpcSession) xpcSession;
@property (T@"NSData",&,V_timestampRequest) timestampRequest;
@property (Tq,V_retryCount) retryCount;
@property (Tq,V_firstRetryErrorCode) firstRetryErrorCode;
@property (T@"NSDate",&,V_fetchStartTime) fetchStartTime;
@property (T@"NSURL",&,V_timestampServer) timestampServer;
@property (Tq,V_maxRetryAttempts) maxRetryAttempts;
```

## Class methods

```
+[MSTimestampRequest supportsSecureCoding];
```

## Instance methods

```
-[MSTimestampRequest fetchStartTime];
-[MSTimestampRequest nonce];
-[MSTimestampRequest debugDescription];
-[MSTimestampRequest dealloc];
-[MSTimestampRequest version];
-[MSTimestampRequest encodeWithCoder:];
-[MSTimestampRequest setRetryCount:];
-[MSTimestampRequest init:];
-[MSTimestampRequest hash];
-[MSTimestampRequest setXpcQueue:];
-[MSTimestampRequest description];
-[MSTimestampRequest initWithCoder:];
-[MSTimestampRequest setVersion:];
-[MSTimestampRequest xpcQueue];
-[MSTimestampRequest setFetchStartTime:];
-[MSTimestampRequest isEqual:];
-[MSTimestampRequest retryCount];
-[MSTimestampRequest setNonce:];
-[MSTimestampRequest isRetryableError:];
-[MSTimestampRequest fetchTimestampWithError:];
-[MSTimestampRequest init:server:];
-[MSTimestampRequest retryDelayForAttempt:];
-[MSTimestampRequest timestampServer];
-[MSTimestampRequest certReq];
-[MSTimestampRequest setReqPolicyID:];
-[MSTimestampRequest buildMessageImprintForASN1:error:];
-[MSTimestampRequest buildTimestampRequest];
-[MSTimestampRequest cleanupMessageImprint:];
-[MSTimestampRequest createXPCMessageForTimestampFetch];
-[MSTimestampRequest ensureXPCSessionExists:];
-[MSTimestampRequest fetchTimestampWithCompletionBlock:queue:];
-[MSTimestampRequest finishAsyncFetch:error:onQueue:completion:];
-[MSTimestampRequest firstRetryErrorCode];
-[MSTimestampRequest init:server:nonce:];
-[MSTimestampRequest invalidateXPCSession];
-[MSTimestampRequest isEqualToTimestampRequest:error:];
-[MSTimestampRequest maxRetryAttempts];
-[MSTimestampRequest messageImprint];
-[MSTimestampRequest parseMSTimestampResponseFromReply:error:];
-[MSTimestampRequest performAsyncFetchAttempt:maxAttempts:onQueue:completion:];
-[MSTimestampRequest performSingleSyncFetchAttempt:];
-[MSTimestampRequest reqPolicyID];
-[MSTimestampRequest sendTimestampFetchAnalyticsEvent:success:error:samplingRate:];
-[MSTimestampRequest setCertReq:];
-[MSTimestampRequest setFirstRetryErrorCode:];
-[MSTimestampRequest setMaxRetryAttempts:];
-[MSTimestampRequest setMessageImprint:];
-[MSTimestampRequest setTimestampRequest:];
-[MSTimestampRequest setTimestampServer:];
-[MSTimestampRequest setXpcSession:];
-[MSTimestampRequest timestampRequest];
-[MSTimestampRequest validateTimestampRequestData:];
-[MSTimestampRequest xpcSession];
```
