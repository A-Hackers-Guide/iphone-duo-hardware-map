# `__NSCFURLSessionConnectionDelegate` (protocol)

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`, `NSCopying`
- 0 instance variables, 0 properties, 17 instance methods, 0 class methods

## Instance methods

```
-[__NSCFURLSessionConnectionDelegate connection:willCacheResponse:responseCallback:];
-[__NSCFURLSessionConnectionDelegate connection:didReceiveInformationalResponse:];
-[__NSCFURLSessionConnectionDelegate connectionWillFinishLoading:];
-[__NSCFURLSessionConnectionDelegate connection:request:needsNewBodyStreamFromOffset:callback:];
-[__NSCFURLSessionConnectionDelegate connection:alternatePathAvailable:];
-[__NSCFURLSessionConnectionDelegate connection:didFinishLoadingWithError:];
-[__NSCFURLSessionConnectionDelegate connection:_willSendRequestForEstablishedConnection:completion:];
-[__NSCFURLSessionConnectionDelegate connection:didReceiveResponse:completion:];
-[__NSCFURLSessionConnectionDelegate connection:_conditionalRequirementsChanged:];
-[__NSCFURLSessionConnectionDelegate connection:wasRedirected:newRequest:responseCallback:];
-[__NSCFURLSessionConnectionDelegate connection:didReceiveSocketInputStream:outputStream:];
-[__NSCFURLSessionConnectionDelegate connection:didReceiveData:completion:];
-[__NSCFURLSessionConnectionDelegate connection:request:needsNewBodyStreamCallback:];
-[__NSCFURLSessionConnectionDelegate connection:challenged:authCallback:];
-[__NSCFURLSessionConnectionDelegate connection:didReceiveTCPConnection:extraBytes:];
-[__NSCFURLSessionConnectionDelegate connection:waitingWithReason:];
-[__NSCFURLSessionConnectionDelegate connection:sentBodyBytes:totalBytes:expectedBytes:];
```
