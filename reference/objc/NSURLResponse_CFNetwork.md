# `NSURLResponse`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_CFNWebKitSecureCoding`, `NSSecureCoding`, `NSCopying`
- 2 instance variables, 12 properties, 31 instance methods, 3 class methods

## Instance variables

```
@"NSURLResponseInternal" _internal;
^{URLResponse=^^?^{__CFURL}^{__CFString}^{__CFString}qdd^{__CFDictionary}^{__CFDictionary}i^{__CFData}^{HTTPResponse}{os_unfair_lock_s=I}CC} __cf_resp_data;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T^{URLResponse=^^?^{__CFURL}^{__CFString}^{__CFString}qdd^{__CFDictionary}^{__CFDictionary}i^{__CFData}^{HTTPResponse}{os_unfair_lock_s=I}CC},V__cf_resp_data) _cf_resp_data;
@property (Tq,R) statusCode;
@property (T@"NSDictionary",R,C) allHeaderFields;
@property (T@"NSURL",R,C) URL;
@property (T@"NSString",R,C) MIMEType;
@property (Tq,R) expectedContentLength;
@property (T@"NSString",R,C) textEncodingName;
@property (T@"NSString",R,C) suggestedFilename;
```

## Class methods

```
+[NSURLResponse supportsSecureCoding];
+[NSURLResponse instancesRespondToSelector:];
+[NSURLResponse _responseWithCFURLResponse:];
```

## Instance methods

```
-[NSURLResponse MIMEType];
-[NSURLResponse init];
-[NSURLResponse _inner];
-[NSURLResponse dealloc];
-[NSURLResponse statusCode];
-[NSURLResponse _webKitPropertyListData];
-[NSURLResponse encodeWithCoder:];
-[NSURLResponse description];
-[NSURLResponse initWithCoder:];
-[NSURLResponse _initWithWebKitPropertyListData:];
-[NSURLResponse respondsToSelector:];
-[NSURLResponse copyWithZone:];
-[NSURLResponse URL];
-[NSURLResponse allHeaderFields];
-[NSURLResponse _lastModifiedDate];
-[NSURLResponse _setMIMEType:];
-[NSURLResponse _setSSLCertificateContext:];
-[NSURLResponse expectedContentLength];
-[NSURLResponse initWithURL:MIMEType:expectedContentLength:textEncodingName:];
-[NSURLResponse suggestedFilename];
-[NSURLResponse _CFURLResponse];
-[NSURLResponse _mustRevalidate];
-[NSURLResponse _calculatedExpiration];
-[NSURLResponse _cf_resp_data];
-[NSURLResponse _freshnessLifetime];
-[NSURLResponse _initWithCFURLResponse:];
-[NSURLResponse _initWithInternal:];
-[NSURLResponse _peerCertificateChain];
-[NSURLResponse _setExpectedContentLength:];
-[NSURLResponse set_cf_resp_data:];
-[NSURLResponse textEncodingName];
```
