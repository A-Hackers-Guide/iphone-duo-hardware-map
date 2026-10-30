# `NWURLSessionTaskTransactionMetrics`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSURLSessionTaskTransactionMetrics`
- Protocols: `NSSecureCoding`
- 3 instance variables, 40 properties, 43 instance methods, 1 class methods

## Instance variables

```
{NWURLSessionConnectionTiming="domainLookupStartMS"Q"domainLookupDurationMS"Q"connectStartTimeMS"Q"connectDurationMS"Q"secureConnectionDurationMS"Q"secure"B"valid"B"__pad"[6C]} connectionTiming;
@"NSObject<OS_nw_protocol_metadata>" _transactionMetadata;
@"NSObject<OS_nw_protocol_metadata>" _clientMetadata;
```

## Properties

```
@property (T@"NSURLRequest",R,C,N) request;
@property (T@"NSURLResponse",R,C,N) response;
@property (T@"NSDate",R,C,N) fetchStartDate;
@property (T@"NSDate",R,C,N) domainLookupStartDate;
@property (T@"NSDate",R,C,N) domainLookupEndDate;
@property (T@"NSDate",R,C,N) connectStartDate;
@property (T@"NSDate",R,C,N) secureConnectionStartDate;
@property (T@"NSDate",R,C,N) secureConnectionEndDate;
@property (T@"NSDate",R,C,N) connectEndDate;
@property (T@"NSDate",R,C,N) requestStartDate;
@property (T@"NSDate",R,C,N) requestEndDate;
@property (T@"NSDate",R,C,N) responseStartDate;
@property (T@"NSDate",R,C,N) responseEndDate;
@property (T@"NSString",R,C,N) networkProtocolName;
@property (TB,R,N,GisProxyConnection) proxyConnection;
@property (TB,R,N,GisReusedConnection) reusedConnection;
@property (Tq,R,N) resourceFetchType;
@property (Tq,R,N) countOfRequestHeaderBytesSent;
@property (Tq,R,N) countOfRequestBodyBytesSent;
@property (Tq,R,N) countOfRequestBodyBytesBeforeEncoding;
@property (Tq,R,N) countOfResponseHeaderBytesReceived;
@property (Tq,R,N) countOfResponseBodyBytesReceived;
@property (Tq,R,N) countOfResponseBodyBytesAfterDecoding;
@property (T@"NSString",R,C,N) localAddress;
@property (T@"NSNumber",R,C,N) localPort;
@property (T@"NSString",R,C,N) remoteAddress;
@property (T@"NSNumber",R,C,N) remotePort;
@property (T@"NSNumber",R,C,N) negotiatedTLSProtocolVersion;
@property (T@"NSNumber",R,C,N) negotiatedTLSCipherSuite;
@property (TB,R,N,GisCellular) cellular;
@property (TB,R,N,GisExpensive) expensive;
@property (TB,R,N,GisConstrained) constrained;
@property (TB,R,N,GisMultipath) multipath;
@property (Tq,R,N) domainResolutionProtocol;
@property (T@"NSString",R,C,N) _interfaceName;
@property (T@"NSUUID",R,C,N) _connectionIdentifier;
@property (Ti,R,N) _privacyStance;
@property (TB,R,N) _isUnlistedTracker;
@property (TB,R,N) _usedTFO;
@property (TI,R,N) _effectiveTrafficClass;
```

## Class methods

```
+[NWURLSessionTaskTransactionMetrics supportsSecureCoding];
```

## Instance methods

```
-[NWURLSessionTaskTransactionMetrics isCellular];
-[NWURLSessionTaskTransactionMetrics isConstrained];
-[NWURLSessionTaskTransactionMetrics isExpensive];
-[NWURLSessionTaskTransactionMetrics _privacyStance];
-[NWURLSessionTaskTransactionMetrics responseStartDate];
-[NWURLSessionTaskTransactionMetrics domainLookupStartDate];
-[NWURLSessionTaskTransactionMetrics negotiatedTLSCipherSuite];
-[NWURLSessionTaskTransactionMetrics domainLookupEndDate];
-[NWURLSessionTaskTransactionMetrics connectStartDate];
-[NWURLSessionTaskTransactionMetrics isReusedConnection];
-[NWURLSessionTaskTransactionMetrics _effectiveTrafficClass];
-[NWURLSessionTaskTransactionMetrics countOfRequestBodyBytesBeforeEncoding];
-[NWURLSessionTaskTransactionMetrics secureConnectionEndDate];
-[NWURLSessionTaskTransactionMetrics countOfResponseBodyBytesAfterDecoding];
-[NWURLSessionTaskTransactionMetrics request];
-[NWURLSessionTaskTransactionMetrics countOfRequestBodyBytesSent];
-[NWURLSessionTaskTransactionMetrics requestStartDate];
-[NWURLSessionTaskTransactionMetrics isMultipath];
-[NWURLSessionTaskTransactionMetrics networkProtocolName];
-[NWURLSessionTaskTransactionMetrics _interfaceName];
-[NWURLSessionTaskTransactionMetrics countOfResponseBodyBytesReceived];
-[NWURLSessionTaskTransactionMetrics remoteAddress];
-[NWURLSessionTaskTransactionMetrics remotePort];
-[NWURLSessionTaskTransactionMetrics localPort];
-[NWURLSessionTaskTransactionMetrics connectEndDate];
-[NWURLSessionTaskTransactionMetrics negotiatedTLSProtocolVersion];
-[NWURLSessionTaskTransactionMetrics _usedTFO];
-[NWURLSessionTaskTransactionMetrics encodeWithCoder:];
-[NWURLSessionTaskTransactionMetrics countOfResponseHeaderBytesReceived];
-[NWURLSessionTaskTransactionMetrics responseEndDate];
-[NWURLSessionTaskTransactionMetrics secureConnectionStartDate];
-[NWURLSessionTaskTransactionMetrics initWithCoder:];
-[NWURLSessionTaskTransactionMetrics resourceFetchType];
-[NWURLSessionTaskTransactionMetrics isProxyConnection];
-[NWURLSessionTaskTransactionMetrics requestEndDate];
-[NWURLSessionTaskTransactionMetrics _isUnlistedTracker];
-[NWURLSessionTaskTransactionMetrics localAddress];
-[NWURLSessionTaskTransactionMetrics countOfRequestHeaderBytesSent];
-[NWURLSessionTaskTransactionMetrics _connectionIdentifier];
-[NWURLSessionTaskTransactionMetrics _establishmentReport];
-[NWURLSessionTaskTransactionMetrics fetchStartDate];
-[NWURLSessionTaskTransactionMetrics domainResolutionProtocol];
-[NWURLSessionTaskTransactionMetrics response];
```
