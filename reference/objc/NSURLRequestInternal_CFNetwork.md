# `NSURLRequestInternal`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 1 properties, 7 instance methods, 0 class methods

## Instance variables

```
{URLRequest="_vptr$CoreLoggable"^^?"fURL"^{__CFURL}"fCachePolicy"Q"fTimeout"d"fMainDocumentURL"^{__CFURL}"fProtocolProperties"^{__CFDictionary}"fProxyDict"^{__CFDictionary}"fHTTPRequest"^{HTTPRequest}"fFlags"{Flags="_flag_SHOULD_HANDLE_HTTP_COOKIES"b1"_flag_IS_MUTABLE"b1"_flag_SHOULD_START_SYNCHRONOUSLY"b1"_flag_ALLOW_CELLULAR"b1"_flag_PREVENTSIDLESYSTEMSLEEP"b1"_flag_SET_EXPLICIT_SHOULD_HANDLE_COOKIES"b1"_flag_SET_EXPLICIT_NETWORK_SERVICE_TYPE"b1"_flag_SET_EXPLICIT_ALLOWS_CELLULAR"b1"_flag_SET_EXPLICIT_PREVENTS_IDLE_SYSTEM_SLEEP"b1"_flag_SET_EXPLICIT_SHOULD_PIPELINE"b1"_flag_SET_EXPLICIT_CACHE_POLICY"b1"_flag_SET_EXPLICIT_TIMEOUT"b1"_flag_SET_EXPLICIT_PROXY_DICT"b1"_flag_SET_EXPLICIT_SSL_PROPERTIES"b1"_flag_SET_EXPLICIT_SHOULD_START_SYNCHRONOUSLY"b1}"fSSLProps"^{__CFDictionary}"fContentDispositionHeaderEncodingFallbackArray"^{__CFArray}"fRequestPriority"q"fAllowedProtocolTypes"Q"fNetworkServiceType"i"fBoundInterfaceIdentifier"^{__CFString}"fTrackerContext"^{__CFString}"fCookiePartitionIdentifier"^{__CFString}"fTimeWindowDelay"d"fTimeWindowDuration"d"fStartTimeoutTime"d"fRequiresShortConnectionTimeout"C"fPreventHSTSStorage"C"fIgnoreHSTS"C"fSchemeWasUpgradedDueToDynamicHSTS"C"fAssumesHTTP3Capable"C"fKnownTracker"C"fPrivacyProxyFailClosed"C"fPrivacyProxyStrictFailClosed"C"fPrivacyProxyFailClosedForUnreachableNonMainHosts"C"fPrivacyProxyFailClosedForUnreachableHosts"C"fProhibitPrivacyProxy"C"fAllowPrivateAccessTokensForThirdParty"C"fUseEnhancedPrivacyMode"C"fBlockTrackers"C"fFailInsecureLoadWithHTTPSDNSRecord"C"fIsWebSearchContent"C"fAllowOnlyPartitionedCookies"C"fUnsafeAllowedInEarlyData"C"fRequiresDNSSECValidation"C"fAllowsPersistentDNS"C"fAttribution"Q"fPayloadTransmissionTimeout"d"fATSOverrides"^{__CFDictionary}"fHSTSPolicy"{unique_ptr<_CFHSTSPolicy, Deleter_CFRelease>=""{?="__ptr_"^{_CFHSTSPolicy}}}"fAllowsExpensiveNetworkAccess"C"fAllowsConstrainedNetworkAccess"C"fAllowsUltraConstrainedNetworkAccess"C"_explicitStorageSession"^{__CFURLStorageSession}} _request;
```

## Properties

```
@property (T^v,R,D) _inner;
```

## Instance methods

```
-[NSURLRequestInternal init];
-[NSURLRequestInternal _inner];
-[NSURLRequestInternal dealloc];
-[NSURLRequestInternal _initWithMessage:bodyParts:cachePolicy:timeout:mainDocumentURL:mutable:];
-[NSURLRequestInternal hash];
-[NSURLRequestInternal copyWithZone:];
-[NSURLRequestInternal isEqual:];
```
