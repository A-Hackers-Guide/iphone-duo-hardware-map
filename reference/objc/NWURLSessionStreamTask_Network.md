# `NWURLSessionStreamTask`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NWURLSessionTask`
- 5 instance variables, 0 properties, 12 instance methods, 1 class methods

## Instance variables

```
B _readClosed;
B _writeClosed;
B _becameStreams;
I _outstandingReadsWrites;
@"NSURLResponse" _storedResponse;
```

## Class methods

```
+[NWURLSessionStreamTask isSubclassOfClass:];
```

## Instance methods

```
-[NWURLSessionStreamTask error];
-[NWURLSessionStreamTask captureStreams];
-[NWURLSessionStreamTask isKindOfClass:];
-[NWURLSessionStreamTask response];
-[NWURLSessionStreamTask closeRead];
-[NWURLSessionStreamTask closeWrite];
-[NWURLSessionStreamTask loaderBetterPathAvailable];
-[NWURLSessionStreamTask loaderConnectedWithHTTPConnectionMetadata:CNAMEChain:unlistedTracker:];
-[NWURLSessionStreamTask readDataOfMinLength:maxLength:timeout:completionHandler:];
-[NWURLSessionStreamTask startNextLoad];
-[NWURLSessionStreamTask startSecureConnection];
-[NWURLSessionStreamTask writeData:timeout:completionHandler:];
```
