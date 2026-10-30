# `NSURLSessionTaskHTTPAuthenticator`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 1 instance variables, 1 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSSet" _statusCodes;
```

## Properties

```
@property (T@"NSSet",C,V_statusCodes) statusCodes;
```

## Class methods

```
+[NSURLSessionTaskHTTPAuthenticator sessionTaskHTTPAuthenticatorWithContext:statusCodes:];
```

## Instance methods

```
-[NSURLSessionTaskHTTPAuthenticator dealloc];
-[NSURLSessionTaskHTTPAuthenticator getAuthenticationHeadersForTask:task:response:completionHandler:];
-[NSURLSessionTaskHTTPAuthenticator copyWithZone:];
-[NSURLSessionTaskHTTPAuthenticator setStatusCodes:];
-[NSURLSessionTaskHTTPAuthenticator initWithStatusCodes:];
-[NSURLSessionTaskHTTPAuthenticator statusCodes];
```
