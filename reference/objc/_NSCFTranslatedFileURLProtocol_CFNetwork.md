# `_NSCFTranslatedFileURLProtocol`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSURLProtocol`
- 3 instance variables, 0 properties, 4 instance methods, 4 class methods

## Instance variables

```
r^{CFURLProtocolInstanceCallbacks=q^?^?^?^?^?^?^?^?^?^?^?^?^v} _callbacks;
{CFURLProtocolClient="version"q"client"^v"retain"^?"release"^?"copyDescription"^?"wasRedirected"^?"cacheResponseIsValid"^?"didReceiveResponse"^?"didLoadData"^?"didFinishLoading"^?"didFail"^?"didReceiveAuthenticationChallenge"^?} _cfurlClient;
r^v _info;
```

## Class methods

```
+[_NSCFTranslatedFileURLProtocol canonicalRequestForRequest:];
+[_NSCFTranslatedFileURLProtocol canInitWithRequest:];
+[_NSCFTranslatedFileURLProtocol pimpl];
+[_NSCFTranslatedFileURLProtocol requestIsCacheEquivalent:toRequest:];
```

## Instance methods

```
-[_NSCFTranslatedFileURLProtocol stopLoading];
-[_NSCFTranslatedFileURLProtocol dealloc];
-[_NSCFTranslatedFileURLProtocol startLoading];
-[_NSCFTranslatedFileURLProtocol initWithRequest:cachedResponse:client:];
```
