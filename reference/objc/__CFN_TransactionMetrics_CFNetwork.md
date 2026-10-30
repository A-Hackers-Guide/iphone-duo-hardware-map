# `__CFN_TransactionMetrics`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 39 instance variables, 5 properties, 7 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} lock;
B _scheduledOriginLoad;
B _firstOnConnection;
C _schedulingTier;
B _APSRelayAttempted;
B _APSRelaySucceeded;
i _pidForHAR;
@"NSObject<OS_dispatch_group>" _tcpInfoGroup;
q _lastResponseHeaderSize;
q _lastResponseBodySize;
q _lastResponseBodyTransferSize;
@"NSUUID" _UUID;
@"NSURLRequest" _request;
@"NSURLRequest" _transferredRequest;
@"NSURLResponse" _cachedResponse;
@"NSURLResponse" _lastResponse;
@"__CFN_ConnectionMetrics" _connectionMetrics;
q _requestHeaderSize;
q _requestBodySize;
q _requestBodyTransferSize;
q _responseHeaderSize;
q _responseBodySize;
q _responseBodyTransferSize;
d _beginTime;
d _endTime;
d _cacheLookupBeginTime;
d _cacheLookupEndTime;
d _requestBeginTime;
d _requestEndTime;
d _responseBeginTime;
d _responseEndTime;
Q _endReason;
q _options;
d _reusedAfterTime;
@"NSObject<OS_nw_data_transfer_report>" _dataTransferReport;
@"NSDictionary" _tcpInfoBegin;
@"NSDictionary" _tcpInfoEnd;
@"NSDictionary" _subflowCountsBegin;
@"NSDictionary" _subflowCountsEnd;
```

## Properties

```
@property (T@"__CFN_ConnectionMetrics",R) _daemon_connectionMetrics;
@property (Tq,R,N) _daemon_requestHeaderSize;
@property (Tq,R,N) _daemon_requestBodyTransferSize;
@property (Tq,R,N) _daemon_responseHeaderSize;
@property (Tq,R,N) _daemon_responseBodyTransferSize;
```

## Class methods

```
+[__CFN_TransactionMetrics supportsSecureCoding];
```

## Instance methods

```
-[__CFN_TransactionMetrics _daemon_connectionMetrics];
-[__CFN_TransactionMetrics _daemon_requestHeaderSize];
-[__CFN_TransactionMetrics _daemon_responseBodyTransferSize];
-[__CFN_TransactionMetrics _daemon_responseHeaderSize];
-[__CFN_TransactionMetrics _daemon_requestBodyTransferSize];
-[__CFN_TransactionMetrics encodeWithCoder:];
-[__CFN_TransactionMetrics initWithCoder:];
```
