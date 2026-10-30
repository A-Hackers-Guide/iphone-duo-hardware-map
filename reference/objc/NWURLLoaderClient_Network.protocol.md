# `NWURLLoaderClient` (protocol)

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 9 properties, 25 instance methods, 0 class methods

## Properties

```
@property (T{nw_http_task_log_description=[16C]I},R,N) logDescription;
@property (T@"NSURLSessionTask",R,N) loaderTask;
@property (T@"NSURLSessionDataTask",R,N) loaderDataTask;
@property (T@"NSObject<OS_nw_protocol_metadata>",R,N) clientMetadata;
@property (T^v,R,N) joiningContext;
@property (T@"NSObject<OS_nw_context>",R,N) networkContext;
@property (TB,R,N) supportsResumableUpload;
@property (T@"NSURL",R,N) uploadResumeURL;
@property (TB,R,N) isWebSocket;
```

## Instance methods

```
-[NWURLLoaderClient joiningContext];
-[NWURLLoaderClient clientMetadata];
-[NWURLLoaderClient uploadResumeURL];
-[NWURLLoaderClient supportsResumableUpload];
-[NWURLLoaderClient loaderDataTask];
-[NWURLLoaderClient logDescription];
-[NWURLLoaderClient isWebSocket];
-[NWURLLoaderClient loaderBetterPathAvailable];
-[NWURLLoaderClient loaderCallCustomURLProtocol:];
-[NWURLLoaderClient loaderConnectedWithHTTPConnectionMetadata:CNAMEChain:unlistedTracker:];
-[NWURLLoaderClient loaderDidReceiveChallenge:completionHandler:];
-[NWURLLoaderClient loaderDidReceiveClientCertificateChallenge:completionHandler:];
-[NWURLLoaderClient loaderDidReceiveInformationalResponse:];
-[NWURLLoaderClient loaderDidReceiveServerTrustChallenge:secProtocolMetadata:completionHandler:];
-[NWURLLoaderClient loaderDidSendBodyData:totalBytesSent:totalBytesExpectedToSend:completionHandler:];
-[NWURLLoaderClient loaderFailedToConnect:];
-[NWURLLoaderClient loaderNeedsBodyProviderFromOffset:completionHandler:];
-[NWURLLoaderClient loaderNeedsEarlyData:];
-[NWURLLoaderClient loaderRunDelegateBlock:];
-[NWURLLoaderClient loaderTask];
-[NWURLLoaderClient loaderToggleRequestTimeoutTimer:];
-[NWURLLoaderClient loaderWaitingForConnectivity];
-[NWURLLoaderClient loaderWillPerformHSTSUpgradeToURL:preload:completionHandler:];
-[NWURLLoaderClient loaderWillPerformHTTPRedirection:newRequest:completionHandler:];
-[NWURLLoaderClient networkContext];
```
