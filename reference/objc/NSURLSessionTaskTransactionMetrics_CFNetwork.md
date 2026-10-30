# `NSURLSessionTaskTransactionMetrics`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 65 properties, 71 instance methods, 2 class methods

## Instance variables

```
B __connectionTimingCached;
B __forCache;
@"__CFN_TransactionMetrics" __metrics;
{?="domainLookupBeginTime"d"connectBeginTime"d"domainLookupDuration"I"connectDuration"I"secureConnectionDuration"I"secure"B} __connectionTiming;
```

## Properties

```
@property (TB,R) _secureConnection;
@property (TB,R) _localCache;
@property (TB,R) _serverPush;
@property (TB,R) _connectionRace;
@property (TI,R) _redirected;
@property (T@"NSString",R,C) _localAddressAndPort;
@property (T@"NSString",R,C) _remoteAddressAndPort;
@property (T@"NSUUID",R,C) _connectionIdentifier;
@property (Tq,R) _requestHeaderBytesSent;
@property (Tq,R) _responseHeaderBytesReceived;
@property (Tq,R) _responseBodyBytesReceived;
@property (Tq,R) _responseBodyBytesDecoded;
@property (TB,R) _apsRelayAttempted;
@property (TB,R) _apsRelaySucceeded;
@property (Tq,R) _totalBytesSent;
@property (Tq,R) _totalBytesReceived;
@property (Ti,R) _negotiatedTLSProtocol;
@property (TS,R) _negotiatedTLSCipher;
@property (TB,R) _usesMultipath;
@property (T@"NSDate",R,C) _firstByteReceivedDate;
@property (T@"NSString",R,C) _interfaceName;
@property (Ti,R) _privacyStance;
@property (T@"NSObject<OS_nw_establishment_report>",R,&) _establishmentReport;
@property (T@"NSObject<OS_nw_data_transfer_report>",R,&) _dataTransferReport;
@property (T@"NSString",R,C) _proxyAddress;
@property (T@"NSNumber",R,C) _proxyPort;
@property (TB,R) _isUnlistedTracker;
@property (TB,R) _usedTFO;
@property (TI,R) _effectiveTrafficClass;
@property (T{?=ddIIIB},N,V__connectionTiming) _connectionTiming;
@property (TB,N,V__connectionTimingCached) _connectionTimingCached;
@property (T@"NSURLRequest",R,C) request;
@property (T@"NSURLResponse",R,C) response;
@property (T@"NSDate",R,C) fetchStartDate;
@property (T@"NSDate",R,C) domainLookupStartDate;
@property (T@"NSDate",R,C) domainLookupEndDate;
@property (T@"NSDate",R,C) connectStartDate;
@property (T@"NSDate",R,C) secureConnectionStartDate;
@property (T@"NSDate",R,C) secureConnectionEndDate;
@property (T@"NSDate",R,C) connectEndDate;
@property (T@"NSDate",R,C) requestStartDate;
@property (T@"NSDate",R,C) requestEndDate;
@property (T@"NSDate",R,C) responseStartDate;
@property (T@"NSDate",R,C) responseEndDate;
@property (T@"NSString",R,C) networkProtocolName;
@property (TB,R,GisProxyConnection) proxyConnection;
@property (TB,R,GisReusedConnection) reusedConnection;
@property (Tq,R) resourceFetchType;
@property (Tq,R) countOfRequestHeaderBytesSent;
@property (Tq,R) countOfRequestBodyBytesSent;
@property (Tq,R) countOfRequestBodyBytesBeforeEncoding;
@property (Tq,R) countOfResponseHeaderBytesReceived;
@property (Tq,R) countOfResponseBodyBytesReceived;
@property (Tq,R) countOfResponseBodyBytesAfterDecoding;
@property (T@"NSString",R,C) localAddress;
@property (T@"NSNumber",R,C) localPort;
@property (T@"NSString",R,C) remoteAddress;
@property (T@"NSNumber",R,C) remotePort;
@property (T@"NSNumber",R,C) negotiatedTLSProtocolVersion;
@property (T@"NSNumber",R,C) negotiatedTLSCipherSuite;
@property (TB,R,GisCellular) cellular;
@property (TB,R,GisExpensive) expensive;
@property (TB,R,GisConstrained) constrained;
@property (TB,R,GisMultipath) multipath;
@property (Tq,R) domainResolutionProtocol;
```

## Class methods

```
+[NSURLSessionTaskTransactionMetrics supportsSecureCoding];
+[NSURLSessionTaskTransactionMetrics new];
```

## Instance methods

```
-[NSURLSessionTaskTransactionMetrics isCellular];
-[NSURLSessionTaskTransactionMetrics isConstrained];
-[NSURLSessionTaskTransactionMetrics isExpensive];
-[NSURLSessionTaskTransactionMetrics _privacyStance];
-[NSURLSessionTaskTransactionMetrics responseStartDate];
-[NSURLSessionTaskTransactionMetrics domainLookupStartDate];
-[NSURLSessionTaskTransactionMetrics negotiatedTLSCipherSuite];
-[NSURLSessionTaskTransactionMetrics init];
-[NSURLSessionTaskTransactionMetrics domainLookupEndDate];
-[NSURLSessionTaskTransactionMetrics connectStartDate];
-[NSURLSessionTaskTransactionMetrics isReusedConnection];
-[NSURLSessionTaskTransactionMetrics _effectiveTrafficClass];
-[NSURLSessionTaskTransactionMetrics countOfRequestBodyBytesBeforeEncoding];
-[NSURLSessionTaskTransactionMetrics secureConnectionEndDate];
-[NSURLSessionTaskTransactionMetrics countOfResponseBodyBytesAfterDecoding];
-[NSURLSessionTaskTransactionMetrics request];
-[NSURLSessionTaskTransactionMetrics countOfRequestBodyBytesSent];
-[NSURLSessionTaskTransactionMetrics requestStartDate];
-[NSURLSessionTaskTransactionMetrics isMultipath];
-[NSURLSessionTaskTransactionMetrics networkProtocolName];
-[NSURLSessionTaskTransactionMetrics _interfaceName];
-[NSURLSessionTaskTransactionMetrics countOfResponseBodyBytesReceived];
-[NSURLSessionTaskTransactionMetrics remoteAddress];
-[NSURLSessionTaskTransactionMetrics remotePort];
-[NSURLSessionTaskTransactionMetrics localPort];
-[NSURLSessionTaskTransactionMetrics connectEndDate];
-[NSURLSessionTaskTransactionMetrics negotiatedTLSProtocolVersion];
-[NSURLSessionTaskTransactionMetrics _usedTFO];
-[NSURLSessionTaskTransactionMetrics encodeWithCoder:];
-[NSURLSessionTaskTransactionMetrics countOfResponseHeaderBytesReceived];
-[NSURLSessionTaskTransactionMetrics responseEndDate];
-[NSURLSessionTaskTransactionMetrics secureConnectionStartDate];
-[NSURLSessionTaskTransactionMetrics description];
-[NSURLSessionTaskTransactionMetrics initWithCoder:];
-[NSURLSessionTaskTransactionMetrics resourceFetchType];
-[NSURLSessionTaskTransactionMetrics isProxyConnection];
-[NSURLSessionTaskTransactionMetrics requestEndDate];
-[NSURLSessionTaskTransactionMetrics _isUnlistedTracker];
-[NSURLSessionTaskTransactionMetrics localAddress];
-[NSURLSessionTaskTransactionMetrics countOfRequestHeaderBytesSent];
-[NSURLSessionTaskTransactionMetrics _connectionIdentifier];
-[NSURLSessionTaskTransactionMetrics _establishmentReport];
-[NSURLSessionTaskTransactionMetrics fetchStartDate];
-[NSURLSessionTaskTransactionMetrics domainResolutionProtocol];
-[NSURLSessionTaskTransactionMetrics response];
-[NSURLSessionTaskTransactionMetrics _localCache];
-[NSURLSessionTaskTransactionMetrics _apsRelayAttempted];
-[NSURLSessionTaskTransactionMetrics _apsRelaySucceeded];
-[NSURLSessionTaskTransactionMetrics _dataTransferReport];
-[NSURLSessionTaskTransactionMetrics _connectionRace];
-[NSURLSessionTaskTransactionMetrics _totalBytesSent];
-[NSURLSessionTaskTransactionMetrics _connectionTiming];
-[NSURLSessionTaskTransactionMetrics _connectionTimingCached];
-[NSURLSessionTaskTransactionMetrics _firstByteReceivedDate];
-[NSURLSessionTaskTransactionMetrics _localAddressAndPort];
-[NSURLSessionTaskTransactionMetrics _negotiatedTLSCipher];
-[NSURLSessionTaskTransactionMetrics _negotiatedTLSProtocol];
-[NSURLSessionTaskTransactionMetrics _proxyAddress];
-[NSURLSessionTaskTransactionMetrics _proxyPort];
-[NSURLSessionTaskTransactionMetrics _redirected];
-[NSURLSessionTaskTransactionMetrics _remoteAddressAndPort];
-[NSURLSessionTaskTransactionMetrics _requestHeaderBytesSent];
-[NSURLSessionTaskTransactionMetrics _responseBodyBytesDecoded];
-[NSURLSessionTaskTransactionMetrics _responseBodyBytesReceived];
-[NSURLSessionTaskTransactionMetrics _responseHeaderBytesReceived];
-[NSURLSessionTaskTransactionMetrics _secureConnection];
-[NSURLSessionTaskTransactionMetrics _serverPush];
-[NSURLSessionTaskTransactionMetrics _totalBytesReceived];
-[NSURLSessionTaskTransactionMetrics _usesMultipath];
-[NSURLSessionTaskTransactionMetrics set_connectionTiming:];
-[NSURLSessionTaskTransactionMetrics set_connectionTimingCached:];
```
