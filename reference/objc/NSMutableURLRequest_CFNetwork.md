# `NSMutableURLRequest`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSURLRequest`
- 0 instance variables, 20 properties, 58 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",C) HTTPMethod;
@property (T@"NSDictionary",C) allHTTPHeaderFields;
@property (T@"NSData",C) HTTPBody;
@property (T@"NSInputStream",&) HTTPBodyStream;
@property (TB) HTTPShouldHandleCookies;
@property (TB) HTTPShouldUsePipelining;
@property (T@"NSURL",C,D) URL;
@property (TQ,D) cachePolicy;
@property (Td,D) timeoutInterval;
@property (T@"NSURL",C,D) mainDocumentURL;
@property (TQ,D) networkServiceType;
@property (TB,D) allowsCellularAccess;
@property (TB,D) allowsExpensiveNetworkAccess;
@property (TB,D) allowsConstrainedNetworkAccess;
@property (TB) allowsUltraConstrainedNetworkAccess;
@property (TB,D) assumesHTTP3Capable;
@property (TQ,D) attribution;
@property (TB,D) requiresDNSSECValidation;
@property (TB,D) allowsPersistentDNS;
@property (T@"NSString",C) cookiePartitionIdentifier;
```

## Instance methods

```
-[NSMutableURLRequest setCachePolicy:];
-[NSMutableURLRequest setAllowsExpensiveNetworkAccess:];
-[NSMutableURLRequest setHTTPBody:];
-[NSMutableURLRequest requestPriority];
-[NSMutableURLRequest setNetworkServiceType:];
-[NSMutableURLRequest setMainDocumentURL:];
-[NSMutableURLRequest setAllowsCellularAccess:];
-[NSMutableURLRequest setAttribution:];
-[NSMutableURLRequest setRequestPriority:];
-[NSMutableURLRequest setAllowsConstrainedNetworkAccess:];
-[NSMutableURLRequest setTimeoutInterval:];
-[NSMutableURLRequest setValue:forHTTPHeaderField:];
-[NSMutableURLRequest setURL:];
-[NSMutableURLRequest setHTTPMethod:];
-[NSMutableURLRequest setHTTPBodyStream:];
-[NSMutableURLRequest copyWithZone:];
-[NSMutableURLRequest addValue:forHTTPHeaderField:];
-[NSMutableURLRequest setAllHTTPHeaderFields:];
-[NSMutableURLRequest setAllowsPersistentDNS:];
-[NSMutableURLRequest setAllowsUltraConstrainedNetworkAccess:];
-[NSMutableURLRequest setAssumesHTTP3Capable:];
-[NSMutableURLRequest setCookiePartitionIdentifier:];
-[NSMutableURLRequest setHTTPShouldHandleCookies:];
-[NSMutableURLRequest setHTTPShouldUsePipelining:];
-[NSMutableURLRequest setRequiresDNSSECValidation:];
-[NSMutableURLRequest _setSchemeWasUpgradedDueToDynamicHSTS:];
-[NSMutableURLRequest setHTTPContentType:];
-[NSMutableURLRequest _setPayloadTransmissionTimeout:];
-[NSMutableURLRequest _setIgnoreHSTS:];
-[NSMutableURLRequest _removeAllProtocolProperties];
-[NSMutableURLRequest _setAllowOnlyPartitionedCookies:];
-[NSMutableURLRequest _setAllowPrivateAccessTokensForThirdParty:];
-[NSMutableURLRequest _setAllowsUCA:];
-[NSMutableURLRequest _setBlockTrackers:];
-[NSMutableURLRequest _setFailInsecureLoadWithHTTPSDNSRecord:];
-[NSMutableURLRequest _setKnownTracker:];
-[NSMutableURLRequest _setNeedsNetworkTrackingPrevention:];
-[NSMutableURLRequest _setNonAppInitiated:];
-[NSMutableURLRequest _setPreventHSTSStorage:];
-[NSMutableURLRequest _setPrivacyProxyFailClosed:];
-[NSMutableURLRequest _setPrivacyProxyFailClosedForUnreachableHosts:];
-[NSMutableURLRequest _setPrivacyProxyFailClosedForUnreachableNonMainHosts:];
-[NSMutableURLRequest _setPrivacyProxyStrictFailClosed:];
-[NSMutableURLRequest _setProhibitPrivacyProxy:];
-[NSMutableURLRequest _setRequiresShortConnectionTimeout:];
-[NSMutableURLRequest _setStartTimeoutDate:];
-[NSMutableURLRequest _setTimeWindowDelay:];
-[NSMutableURLRequest _setTimeWindowDuration:];
-[NSMutableURLRequest _setUnsafeAllowedInEarlyData:];
-[NSMutableURLRequest _setUseEnhancedPrivacyMode:];
-[NSMutableURLRequest _setWebSearchContent:];
-[NSMutableURLRequest setBoundInterfaceIdentifier:];
-[NSMutableURLRequest setContentDispositionEncodingFallbackArray:];
-[NSMutableURLRequest setExpectedWorkload:];
-[NSMutableURLRequest setHTTPExtraCookies:];
-[NSMutableURLRequest setHTTPReferrer:];
-[NSMutableURLRequest setHTTPUserAgent:];
-[NSMutableURLRequest set_trackerContext:];
```
