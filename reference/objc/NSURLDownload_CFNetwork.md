# `NSURLDownload`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSURLAuthenticationChallengeSender`
- 1 instance variables, 7 properties, 25 instance methods, 4 class methods

## Instance variables

```
@"NSURLDownloadInternal" _internal;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSURLRequest",R,C) request;
@property (T@"NSData",R,C) resumeData;
@property (TB) deletesFileUponFailure;
```

## Class methods

```
+[NSURLDownload _downloadWithLoadingConnection:request:response:delegate:proxy:];
+[NSURLDownload _downloadWithLoadingCFURLConnection:request:response:delegate:proxy:];
+[NSURLDownload _downloadWithRequest:delegate:directory:];
+[NSURLDownload canResumeDownloadDecodedWithEncodingMIMEType:];
```

## Instance methods

```
-[NSURLDownload _setDelegate:];
-[NSURLDownload init];
-[NSURLDownload dealloc];
-[NSURLDownload continueWithoutCredentialForAuthenticationChallenge:];
-[NSURLDownload request];
-[NSURLDownload useCredential:forAuthenticationChallenge:];
-[NSURLDownload cancelAuthenticationChallenge:];
-[NSURLDownload description];
-[NSURLDownload cancel];
-[NSURLDownload url];
-[NSURLDownload _directoryPath];
-[NSURLDownload _initWithLoadingCFURLConnection:request:response:delegate:proxy:];
-[NSURLDownload _initWithLoadingConnection:request:response:delegate:proxy:];
-[NSURLDownload _initWithRequest:delegate:directory:];
-[NSURLDownload _initWithResumeInformation:delegate:path:];
-[NSURLDownload _resumeInformation];
-[NSURLDownload _setDelegateQueue:];
-[NSURLDownload _setDirectoryPath:];
-[NSURLDownload deletesFileUponFailure];
-[NSURLDownload initWithRequest:delegate:];
-[NSURLDownload initWithResumeData:delegate:path:];
-[NSURLDownload resumeData];
-[NSURLDownload setDeletesFileUponFailure:];
-[NSURLDownload setDestination:allowOverwrite:];
-[NSURLDownload withDelegate:];
```
