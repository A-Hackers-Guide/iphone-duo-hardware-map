# `CONNECTION_SessionTask`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 18 instance variables, 2 properties, 147 instance methods, 0 class methods

## Instance variables

```
^{_CFURLRequest=} _originalRequest;
^{_CFURLRequest=} _currentRequest;
d _startTime;
^{__CFDictionary=} _connectionProperties;
^{__CFDictionary=} _socketProperties;
@"NSMutableURLRequest" _nsCurrentRequest;
@"NSURLRequest" _nsOriginalRequest;
@"NSURLSession" _session_ivar;
@"NSURLSessionConfiguration" _effectiveConfiguration;
@"NSUUID" _uniqueIdentifier;
B _is_cellular;
# _my_protocolForTask;
B __shouldSkipPreferredClientCertificateLookup;
^{__CFDictionary=} _atsStateCache;
B _preventsAppSSO;
B _appSSOFallback;
B _appleIDContextRedirect;
@"NSURLSessionTaskMetrics" _metrics;
```

## Properties

```
@property (T@"NSURLSessionTaskMetrics",&,N,V_metrics) _metrics;
@property (TB,R,N) _isAVAssetTask;
```

## Instance methods

```
-[CONNECTION_SessionTask _requiresPowerPluggedIn];
-[CONNECTION_SessionTask currentRequest];
-[CONNECTION_SessionTask _cachePolicy];
-[CONNECTION_SessionTask taskIdentifier];
-[CONNECTION_SessionTask priority];
-[CONNECTION_SessionTask _resolvedCNAMEChain];
-[CONNECTION_SessionTask set_TLSMaximumSupportedProtocolVersion:];
-[CONNECTION_SessionTask _discretionaryOverrride];
-[CONNECTION_SessionTask _withXURLCache:];
-[CONNECTION_SessionTask _description];
-[CONNECTION_SessionTask _preventsAppSSO];
-[CONNECTION_SessionTask _strictContentLength];
-[CONNECTION_SessionTask _disallowCellular];
-[CONNECTION_SessionTask _setConnectionCacheKey:];
-[CONNECTION_SessionTask currentRequest_URL];
-[CONNECTION_SessionTask _incompleteCurrentTaskTransactionMetrics];
-[CONNECTION_SessionTask set_TLSMinimumSupportedProtocolVersion:];
-[CONNECTION_SessionTask _suspensionThreshhold];
-[CONNECTION_SessionTask _isTopLevelNavigation];
-[CONNECTION_SessionTask updateCurrentRequest:];
-[CONNECTION_SessionTask _allowsQUIC];
-[CONNECTION_SessionTask _timeWindowDelay];
-[CONNECTION_SessionTask _allowedProtocolTypes];
-[CONNECTION_SessionTask _httpConnectionInfoCompletionBlock];
-[CONNECTION_SessionTask _DuetActivityProperties];
-[CONNECTION_SessionTask shouldHandleCookiesAndSchemeIsAppropriate];
-[CONNECTION_SessionTask _backtrace];
-[CONNECTION_SessionTask startTime];
-[CONNECTION_SessionTask _takePreventIdleSleepAssertionIfAppropriate];
-[CONNECTION_SessionTask _allowsCellularOverride];
-[CONNECTION_SessionTask _privacyProxyFailClosed];
-[CONNECTION_SessionTask _requiresSecureHTTPSProxyConnection];
-[CONNECTION_SessionTask countOfBytesReceived];
-[CONNECTION_SessionTask _attribution];
-[CONNECTION_SessionTask _cookieTransformCallback];
-[CONNECTION_SessionTask _copyATSState];
-[CONNECTION_SessionTask _atsTrustPolicy];
-[CONNECTION_SessionTask _cfCache];
-[CONNECTION_SessionTask _setAppleIDContext:];
-[CONNECTION_SessionTask _private_nw_activity];
-[CONNECTION_SessionTask _releasePreventIdleSleepAssertionIfAppropriate];
-[CONNECTION_SessionTask _protocolForTask];
-[CONNECTION_SessionTask _connectionPropertyDuet];
-[CONNECTION_SessionTask _proxyHandshakePending];
-[CONNECTION_SessionTask workQueue];
-[CONNECTION_SessionTask _timeWindowDuration];
-[CONNECTION_SessionTask _createXCookieStorage];
-[CONNECTION_SessionTask _incompleteTaskMetrics];
-[CONNECTION_SessionTask dealloc];
-[CONNECTION_SessionTask originalRequest];
-[CONNECTION_SessionTask _adoptEffectiveConfiguration:];
-[CONNECTION_SessionTask _privacyProxyStrictFailClosed];
-[CONNECTION_SessionTask set_metrics:];
-[CONNECTION_SessionTask _allowsExpensiveOverride];
-[CONNECTION_SessionTask countOfBytesExpectedToSend];
-[CONNECTION_SessionTask _privacyProxyFailClosedForUnreachableNonMainHosts];
-[CONNECTION_SessionTask _APSRelayTopic];
-[CONNECTION_SessionTask _privacyProxyFailClosedForUnreachableHosts];
-[CONNECTION_SessionTask set_proxyHandshakePending:];
-[CONNECTION_SessionTask _preconnect];
-[CONNECTION_SessionTask _preventsIdleSystemSleep];
-[CONNECTION_SessionTask set_allowsQUIC:];
-[CONNECTION_SessionTask _setConnectionIsCellular:];
-[CONNECTION_SessionTask set_expectedProgressTarget:];
-[CONNECTION_SessionTask _cfHSTS];
-[CONNECTION_SessionTask _loggableDescription];
-[CONNECTION_SessionTask _metrics];
-[CONNECTION_SessionTask _uniqueIdentifier];
-[CONNECTION_SessionTask _shouldPipelineHTTP];
-[CONNECTION_SessionTask hasExtractor];
-[CONNECTION_SessionTask _storagePartitionIdentifier];
-[CONNECTION_SessionTask error];
-[CONNECTION_SessionTask prefersIncrementalDelivery];
-[CONNECTION_SessionTask _requestPriority];
-[CONNECTION_SessionTask _setSocketProperties:connectionProperties:];
-[CONNECTION_SessionTask _TCPConnectionMetadata];
-[CONNECTION_SessionTask _connectionIsCompanionLink];
-[CONNECTION_SessionTask _shouldSkipPipelineProbe];
-[CONNECTION_SessionTask _createXCredentialStorage];
-[CONNECTION_SessionTask _priorityValue];
-[CONNECTION_SessionTask _blockTrackers];
-[CONNECTION_SessionTask set_protocolForTask:];
-[CONNECTION_SessionTask _cacheOnly];
-[CONNECTION_SessionTask countOfBytesSent];
-[CONNECTION_SessionTask _appSSOFallback];
-[CONNECTION_SessionTask _shouldHandleCookies];
-[CONNECTION_SessionTask set_connectionIsCompanionLink:];
-[CONNECTION_SessionTask _countOfBytesReceivedEncoded];
-[CONNECTION_SessionTask _allowsCellular];
-[CONNECTION_SessionTask _timeoutInterval];
-[CONNECTION_SessionTask _TLSNegotiatedCipherSuite];
-[CONNECTION_SessionTask _hostOverride];
-[CONNECTION_SessionTask _getAuthenticatorStatusCodes];
-[CONNECTION_SessionTask _cfCookies];
-[CONNECTION_SessionTask set_TCPConnectionMetadata:];
-[CONNECTION_SessionTask currentRequest_mainDocumentURL];
-[CONNECTION_SessionTask _logUnlistedTracker:];
-[CONNECTION_SessionTask _networkServiceType];
-[CONNECTION_SessionTask set_preconnect:];
-[CONNECTION_SessionTask _consumePendingBytesReceivedEncoded];
-[CONNECTION_SessionTask set_resolvedCNAMEChain:];
-[CONNECTION_SessionTask _TLSMaximumSupportedProtocolVersion];
-[CONNECTION_SessionTask _failInsecureLoadWithHTTPSDNSRecord];
-[CONNECTION_SessionTask _cookieAcceptPolicy];
-[CONNECTION_SessionTask _expectedProgressTarget];
-[CONNECTION_SessionTask _getAuthenticationHeadersForResponse:completionHandler:];
-[CONNECTION_SessionTask _prohibitPrivacyProxy];
-[CONNECTION_SessionTask _useEnhancedPrivacyMode];
-[CONNECTION_SessionTask _proxySettings];
-[CONNECTION_SessionTask set_discretionaryOverride:];
-[CONNECTION_SessionTask _isKnownTracker];
-[CONNECTION_SessionTask _appleIDContextRedirect];
-[CONNECTION_SessionTask _sslSettings];
-[CONNECTION_SessionTask _shouldSkipPreferredClientCertificateLookup];
-[CONNECTION_SessionTask _appendCountOfPendingBytesReceivedEncoded:];
-[CONNECTION_SessionTask _isAVAssetTask];
-[CONNECTION_SessionTask set_TLSNegotiatedCipherSuite:];
-[CONNECTION_SessionTask session];
-[CONNECTION_SessionTask countOfBytesExpectedToReceive];
-[CONNECTION_SessionTask _boundInterfaceIdentifier];
-[CONNECTION_SessionTask initWithRequest:mutableCurrent:connProps:sockProps:session:];
-[CONNECTION_SessionTask _trackerContext];
-[CONNECTION_SessionTask _isWebSearchContent];
-[CONNECTION_SessionTask _trailers];
-[CONNECTION_SessionTask resumableUploadState];
-[CONNECTION_SessionTask _copyHSTSPolicy];
-[CONNECTION_SessionTask _prohibitAuthUI];
-[CONNECTION_SessionTask _preventsSystemHTTPProxyAuthentication];
-[CONNECTION_SessionTask set_preventsAppSSO:];
-[CONNECTION_SessionTask _requiresDNSSECValidation];
-[CONNECTION_SessionTask _assumesHTTP3Capable];
-[CONNECTION_SessionTask set_appSSOFallback:];
-[CONNECTION_SessionTask set_trailers:];
-[CONNECTION_SessionTask _processConnectionProperties];
-[CONNECTION_SessionTask _shouldUsePipelineHeuristics];
-[CONNECTION_SessionTask _allowsUltraConstrainedOverride];
-[CONNECTION_SessionTask _backgroundTransactionMetrics];
-[CONNECTION_SessionTask _cfCreds];
-[CONNECTION_SessionTask _effectiveConfiguration];
-[CONNECTION_SessionTask _allowsConstrainedOverride];
-[CONNECTION_SessionTask _TLSMinimumSupportedProtocolVersion];
-[CONNECTION_SessionTask _siteForCookies];
-[CONNECTION_SessionTask _bytesPerSecondLimit];
-[CONNECTION_SessionTask state];
-[CONNECTION_SessionTask _allowsPersistentDNS];
-[CONNECTION_SessionTask _countOfPendingBytesReceivedEncoded];
-[CONNECTION_SessionTask _copySocketStreamProperties];
```
