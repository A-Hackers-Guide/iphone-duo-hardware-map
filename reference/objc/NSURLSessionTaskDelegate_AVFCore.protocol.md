# `NSURLSessionTaskDelegate` (protocol)

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSURLSessionDelegate`
- 0 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance methods

```
-[NSURLSessionTaskDelegate URLSession:task:needNewBodyStream:];
-[NSURLSessionTaskDelegate URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:];
-[NSURLSessionTaskDelegate URLSession:task:didFinishCollectingMetrics:];
-[NSURLSessionTaskDelegate URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:];
-[NSURLSessionTaskDelegate URLSession:task:didReceiveChallenge:completionHandler:];
-[NSURLSessionTaskDelegate URLSession:task:didCompleteWithError:];
-[NSURLSessionTaskDelegate URLSession:didCreateTask:];
-[NSURLSessionTaskDelegate URLSession:task:didReceiveInformationalResponse:];
-[NSURLSessionTaskDelegate URLSession:task:needNewBodyStreamFromOffset:completionHandler:];
-[NSURLSessionTaskDelegate URLSession:task:willBeginDelayedRequest:completionHandler:];
-[NSURLSessionTaskDelegate URLSession:taskIsWaitingForConnectivity:];
```
