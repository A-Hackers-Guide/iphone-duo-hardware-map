# `NSURLProtectionSpace`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_CFNWebKitSecureCoding`, `NSSecureCoding`, `NSCopying`
- 1 instance variables, 12 properties, 27 instance methods, 1 class methods

## Instance variables

```
@"NSURLProtectionSpaceInternal" _internal;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C) realm;
@property (TB,R) receivesCredentialSecurely;
@property (TB,R) isProxy;
@property (T@"NSString",R,C) host;
@property (Tq,R) port;
@property (T@"NSString",R,C) proxyType;
@property (T@"NSString",R,C) protocol;
@property (T@"NSString",R,C) authenticationMethod;
```

## Class methods

```
+[NSURLProtectionSpace supportsSecureCoding];
```

## Instance methods

```
-[NSURLProtectionSpace isProxy];
-[NSURLProtectionSpace protocol];
-[NSURLProtectionSpace init];
-[NSURLProtectionSpace dealloc];
-[NSURLProtectionSpace port];
-[NSURLProtectionSpace _webKitPropertyListData];
-[NSURLProtectionSpace realm];
-[NSURLProtectionSpace encodeWithCoder:];
-[NSURLProtectionSpace hash];
-[NSURLProtectionSpace description];
-[NSURLProtectionSpace initWithCoder:];
-[NSURLProtectionSpace _initWithWebKitPropertyListData:];
-[NSURLProtectionSpace copyWithZone:];
-[NSURLProtectionSpace isEqual:];
-[NSURLProtectionSpace host];
-[NSURLProtectionSpace _initWithCFURLProtectionSpace:];
-[NSURLProtectionSpace _setDistinguishedNames:];
-[NSURLProtectionSpace _setServerTrust:];
-[NSURLProtectionSpace authenticationMethod];
-[NSURLProtectionSpace initWithHost:port:protocol:realm:authenticationMethod:];
-[NSURLProtectionSpace serverTrust];
-[NSURLProtectionSpace _CFURLProtectionSpace];
-[NSURLProtectionSpace _cfurlprtotectionspace];
-[NSURLProtectionSpace distinguishedNames];
-[NSURLProtectionSpace initWithProxyHost:port:type:realm:authenticationMethod:];
-[NSURLProtectionSpace proxyType];
-[NSURLProtectionSpace receivesCredentialSecurely];
```
