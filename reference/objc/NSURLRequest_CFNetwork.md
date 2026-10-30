# `NSURLRequest`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_CFNWebKitSecureCoding`, `NSSecureCoding`, `NSCopying`, `NSMutableCopying`
- 2 instance variables, 25 properties, 93 instance methods, 9 class methods

## Instance variables

```
@"NSURLRequestInternal" _internal;
@"NSString" _cookiePartitionIdentifier;
```

## Properties

```
@property (T@"NSString",R,C) HTTPMethod;
@property (T@"NSDictionary",R,C) allHTTPHeaderFields;
@property (T@"NSData",R,C) HTTPBody;
@property (T@"NSInputStream",R,&) HTTPBodyStream;
@property (TB,R) HTTPShouldHandleCookies;
@property (TB,R) HTTPShouldUsePipelining;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T^v,R) _inner;
@property (T@"NSURL",R,C) URL;
@property (TQ,R) cachePolicy;
@property (Td,R) timeoutInterval;
@property (T@"NSURL",R,C) mainDocumentURL;
@property (TQ,R) networkServiceType;
@property (TB,R) allowsCellularAccess;
@property (TB,R) allowsExpensiveNetworkAccess;
@property (TB,R) allowsConstrainedNetworkAccess;
@property (TB,R) allowsUltraConstrainedNetworkAccess;
@property (TB,R) assumesHTTP3Capable;
@property (TQ,R) attribution;
@property (TB,R) requiresDNSSECValidation;
@property (TB,R) allowsPersistentDNS;
@property (T@"NSString",R,C,V_cookiePartitionIdentifier) cookiePartitionIdentifier;
```

## Class methods

```
+[NSURLRequest supportsSecureCoding];
+[NSURLRequest requestWithURL:];
+[NSURLRequest requestWithURL:cachePolicy:timeoutInterval:];
+[NSURLRequest allowsAnyHTTPSCertificateForHost:];
+[NSURLRequest allowsSpecificHTTPSCertificateForHost:];
+[NSURLRequest defaultTimeoutInterval];
+[NSURLRequest setAllowsAnyHTTPSCertificate:forHost:];
+[NSURLRequest setAllowsSpecificHTTPSCertificate:forHost:];
+[NSURLRequest setDefaultTimeoutInterval:];
```

## Instance methods

```
-[NSURLRequest cachePolicy];
-[NSURLRequest allowsExpensiveNetworkAccess];
-[NSURLRequest networkServiceType];
-[NSURLRequest mutableCopyWithZone:];
-[NSURLRequest HTTPBody];
-[NSURLRequest _timeWindowDelay];
-[NSURLRequest _setProperty:forKey:];
-[NSURLRequest allowsCellularAccess];
-[NSURLRequest _allowedProtocolTypes];
-[NSURLRequest init];
-[NSURLRequest _inner];
-[NSURLRequest mainDocumentURL];
-[NSURLRequest _privacyProxyFailClosed];
-[NSURLRequest valueForHTTPHeaderField:];
-[NSURLRequest _initWithCFURLRequest:];
-[NSURLRequest _timeWindowDuration];
-[NSURLRequest dealloc];
-[NSURLRequest allowsConstrainedNetworkAccess];
-[NSURLRequest _privacyProxyStrictFailClosed];
-[NSURLRequest _privacyProxyFailClosedForUnreachableNonMainHosts];
-[NSURLRequest _privacyProxyFailClosedForUnreachableHosts];
-[NSURLRequest attribution];
-[NSURLRequest _blockTrackers];
-[NSURLRequest HTTPMethod];
-[NSURLRequest _webKitPropertyListData];
-[NSURLRequest encodeWithCoder:];
-[NSURLRequest initWithURL:cachePolicy:timeoutInterval:];
-[NSURLRequest hash];
-[NSURLRequest description];
-[NSURLRequest _failInsecureLoadWithHTTPSDNSRecord];
-[NSURLRequest initWithCoder:];
-[NSURLRequest _prohibitPrivacyProxy];
-[NSURLRequest _useEnhancedPrivacyMode];
-[NSURLRequest _isKnownTracker];
-[NSURLRequest _initWithWebKitPropertyListData:];
-[NSURLRequest timeoutInterval];
-[NSURLRequest _trackerContext];
-[NSURLRequest _isWebSearchContent];
-[NSURLRequest copyWithZone:];
-[NSURLRequest isEqual:];
-[NSURLRequest initWithURL:];
-[NSURLRequest URL];
-[NSURLRequest HTTPBodyStream];
-[NSURLRequest HTTPShouldHandleCookies];
-[NSURLRequest HTTPShouldUsePipelining];
-[NSURLRequest allHTTPHeaderFields];
-[NSURLRequest allowsPersistentDNS];
-[NSURLRequest allowsUltraConstrainedNetworkAccess];
-[NSURLRequest assumesHTTP3Capable];
-[NSURLRequest cookiePartitionIdentifier];
-[NSURLRequest cookiePartitionIdentifier];
-[NSURLRequest requiresDNSSECValidation];
-[NSURLRequest _needsNetworkTrackingPrevention];
-[NSURLRequest _allHTTPHeaderFieldsAsArrays];
-[NSURLRequest _allowOnlyPartitionedCookies];
-[NSURLRequest _allowPrivateAccessTokensForThirdParty];
-[NSURLRequest _allowsUCA];
-[NSURLRequest _explicitlySetAllowsCellularAccess];
-[NSURLRequest _explicitlySetAllowsConstrainedNetworkAccess];
-[NSURLRequest _explicitlySetAllowsExpensiveNetworkAccess];
-[NSURLRequest _explicitlySetAllowsUCA];
-[NSURLRequest _explicitlySetCachePolicy];
-[NSURLRequest _explicitlySetNetworkServiceType];
-[NSURLRequest _explicitlySetRequiresDNSSECValidation];
-[NSURLRequest _explicitlySetShouldHandleCookies];
-[NSURLRequest _explicitlySetTimeoutInterval];
-[NSURLRequest _ignoreHSTS];
-[NSURLRequest _payloadTransmissionTimeout];
-[NSURLRequest _propertyForKey:];
-[NSURLRequest _startTimeoutDate];
-[NSURLRequest _unsafeAllowedInEarlyData];
-[NSURLRequest boundInterfaceIdentifier];
-[NSURLRequest contentDispositionEncodingFallbackArray];
-[NSURLRequest _CFURLRequest];
-[NSURLRequest HTTPExtraCookies];
-[NSURLRequest HTTPReferrer];
-[NSURLRequest HTTPContentType];
-[NSURLRequest HTTPUserAgent];
-[NSURLRequest _requiresShortConnectionTimeout];
-[NSURLRequest _URLHasScheme:];
-[NSURLRequest _allProtocolProperties];
-[NSURLRequest _copyReplacingURLWithURL:];
-[NSURLRequest _explicitlySetPreventsIdleSystemSleep];
-[NSURLRequest _explicitlySetProxySettings];
-[NSURLRequest _explicitlySetSSLProperties];
-[NSURLRequest _initWithInternal:];
-[NSURLRequest _isIdempotent];
-[NSURLRequest _isNonAppInitiated];
-[NSURLRequest _preventHSTSStorage];
-[NSURLRequest _removePropertyForKey:];
-[NSURLRequest _schemeWasUpgradedDueToDynamicHSTS];
-[NSURLRequest cfURL];
-[NSURLRequest expectedWorkload];
```
