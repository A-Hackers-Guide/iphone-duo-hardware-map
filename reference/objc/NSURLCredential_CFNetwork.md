# `NSURLCredential`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_CFNWebKitSecureCoding`, `NSSecureCoding`, `NSCopying`
- 1 instance variables, 5 properties, 23 instance methods, 4 class methods

## Instance variables

```
@"NSURLCredentialInternal" _internal;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R) persistence;
```

## Class methods

```
+[NSURLCredential supportsSecureCoding];
+[NSURLCredential credentialWithUser:password:persistence:];
+[NSURLCredential credentialForTrust:];
+[NSURLCredential credentialWithIdentity:certificates:persistence:];
```

## Instance methods

```
-[NSURLCredential certificates];
-[NSURLCredential persistence];
-[NSURLCredential hasPassword];
-[NSURLCredential dealloc];
-[NSURLCredential initWithUser:password:persistence:];
-[NSURLCredential initWithIdentity:certificates:persistence:];
-[NSURLCredential _initWithCFURLCredential:];
-[NSURLCredential user];
-[NSURLCredential _webKitPropertyListData];
-[NSURLCredential _CFURLCredential];
-[NSURLCredential _removeSWCACreatorAttribute];
-[NSURLCredential encodeWithCoder:];
-[NSURLCredential initWithTrust:];
-[NSURLCredential _hasSWCACreatorAttribute];
-[NSURLCredential hash];
-[NSURLCredential identity];
-[NSURLCredential description];
-[NSURLCredential _cfurlcredential];
-[NSURLCredential initWithCoder:];
-[NSURLCredential _initWithWebKitPropertyListData:];
-[NSURLCredential copyWithZone:];
-[NSURLCredential isEqual:];
-[NSURLCredential password];
```
