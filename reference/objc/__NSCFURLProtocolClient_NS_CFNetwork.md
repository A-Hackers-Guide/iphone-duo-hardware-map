# `__NSCFURLProtocolClient_NS`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSURLProtocolClient`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
^{URLProtocolClient=^^?} _cf;
^v _prot;
@"NSURLAuthenticationChallenge" _challenge;
^{_CFURLAuthChallenge=} _cfChallenge;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[__NSCFURLProtocolClient_NS dealloc];
-[__NSCFURLProtocolClient_NS URLProtocol:cachedResponseIsValid:];
-[__NSCFURLProtocolClient_NS URLProtocol:didFailWithError:];
-[__NSCFURLProtocolClient_NS URLProtocol:didReceiveAuthenticationChallenge:];
-[__NSCFURLProtocolClient_NS URLProtocol:wasRedirectedToRequest:redirectResponse:];
-[__NSCFURLProtocolClient_NS URLProtocol:didCancelAuthenticationChallenge:];
-[__NSCFURLProtocolClient_NS URLProtocol:didLoadData:];
-[__NSCFURLProtocolClient_NS URLProtocol:didReceiveResponse:cacheStoragePolicy:];
-[__NSCFURLProtocolClient_NS URLProtocolDidFinishLoading:];
```
