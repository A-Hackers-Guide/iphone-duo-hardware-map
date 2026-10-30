# `NSHTTPURLResponse`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSURLResponse`
- 1 instance variables, 2 properties, 12 instance methods, 3 class methods

## Instance variables

```
@"NSHTTPURLResponseInternal" _httpInternal;
```

## Properties

```
@property (Tq,R) statusCode;
@property (T@"NSDictionary",R,C) allHeaderFields;
```

## Class methods

```
+[NSHTTPURLResponse supportsSecureCoding];
+[NSHTTPURLResponse isErrorStatusCode:];
+[NSHTTPURLResponse localizedStringForStatusCode:];
```

## Instance methods

```
-[NSHTTPURLResponse valueForHTTPHeaderField:];
-[NSHTTPURLResponse dealloc];
-[NSHTTPURLResponse statusCode];
-[NSHTTPURLResponse encodeWithCoder:];
-[NSHTTPURLResponse description];
-[NSHTTPURLResponse initWithCoder:];
-[NSHTTPURLResponse allHeaderFields];
-[NSHTTPURLResponse _allHTTPHeaderFieldsAsArrays];
-[NSHTTPURLResponse initWithURL:statusCode:HTTPVersion:headerFields:];
-[NSHTTPURLResponse _initWithCFURLResponse:];
-[NSHTTPURLResponse _peerCertificateChain];
-[NSHTTPURLResponse initWithURL:statusCode:headerFields:requestTime:];
```
