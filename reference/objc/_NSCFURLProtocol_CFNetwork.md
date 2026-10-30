# `_NSCFURLProtocol`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSURLProtocol`
- 2 instance variables, 0 properties, 4 instance methods, 6 class methods

## Instance variables

```
^{_CFURLProtocol=} _prot;
^{NSCFURLProtocolClient=^^?^^?@@} _client;
```

## Class methods

```
+[_NSCFURLProtocol canonicalRequestForRequest:];
+[_NSCFURLProtocol _cf_internalImpl];
+[_NSCFURLProtocol canInitWithRequest:];
+[_NSCFURLProtocol canInitWithTask:];
+[_NSCFURLProtocol canonicalRequestForRequest:task:];
+[_NSCFURLProtocol requestIsCacheEquivalent:toRequest:];
```

## Instance methods

```
-[_NSCFURLProtocol stopLoading];
-[_NSCFURLProtocol dealloc];
-[_NSCFURLProtocol startLoading];
-[_NSCFURLProtocol initWithRequest:cachedResponse:client:];
```
