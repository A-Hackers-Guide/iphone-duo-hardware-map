# `NSURLProtocol`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 10 instance methods, 13 class methods

## Instance variables

```
@"NSURLProtocolInternal" _internal;
@"NSURLSessionTask" _task;
B _inInitWithTask;
```

## Properties

```
@property (T@"<NSURLProtocolClient>",R,&) client;
@property (T@"NSURLRequest",R,C) request;
@property (T@"NSCachedURLResponse",R,C) cachedResponse;
```

## Class methods

```
+[NSURLProtocol canonicalRequestForRequest:];
+[NSURLProtocol registerClass:];
+[NSURLProtocol canInitWithRequest:];
+[NSURLProtocol canInitWithTask:];
+[NSURLProtocol propertyForKey:inRequest:];
+[NSURLProtocol removePropertyForKey:inRequest:];
+[NSURLProtocol _makeRequestCanonicalByMakingRequestURLCanonical:];
+[NSURLProtocol _protocolClassForRequest:];
+[NSURLProtocol _protocolClassForRequest:skipAppSSO:];
+[NSURLProtocol canonicalRequestForRequest:task:];
+[NSURLProtocol requestIsCacheEquivalent:toRequest:];
+[NSURLProtocol setProperty:forKey:inRequest:];
+[NSURLProtocol unregisterClass:];
```

## Instance methods

```
-[NSURLProtocol init];
-[NSURLProtocol stopLoading];
-[NSURLProtocol dealloc];
-[NSURLProtocol request];
-[NSURLProtocol cachedResponse];
-[NSURLProtocol task];
-[NSURLProtocol startLoading];
-[NSURLProtocol client];
-[NSURLProtocol initWithTask:cachedResponse:client:];
-[NSURLProtocol initWithRequest:cachedResponse:client:];
```
