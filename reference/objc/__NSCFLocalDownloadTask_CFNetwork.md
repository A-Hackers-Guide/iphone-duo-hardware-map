# `__NSCFLocalDownloadTask`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `__NSCFLocalSessionTask`
- Protocols: `NSURLSessionDownloadTaskSubclass`, `__NSCFLocalDownloadFileOpener`
- 17 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
@? _fileCompletion;
@"__NSCFLocalDownloadFile" _downloadFile;
@"NSObject<OS_dispatch_data>" _writeBuffer;
Q _ioSuspend;
q _totalWrote;
@? _resumeCallback;
q _initialResumeSize;
@"NSDictionary" _originalResumeInfo;
Q _transientWriteProgress;
@? _afterDidReportProgressOnQueue;
@? _dataAckCompletion;
i _seqNo;
B _canWrite;
B _suppressProgress;
B _needFinish;
B _didIssueNeedFinish;
B _extractorFinishedSuccessfully;
```

## Properties

```
@property (T@"__NSCFLocalDownloadFile",&,V_downloadFile) downloadFile;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[__NSCFLocalDownloadTask _expandResumeData:];
```

## Instance methods

```
-[__NSCFLocalDownloadTask _onqueue_didReceiveResponse:completion:];
-[__NSCFLocalDownloadTask set_keepDownloadTaskFile:];
-[__NSCFLocalDownloadTask _onqueue_willCacheResponse:withCompletion:];
-[__NSCFLocalDownloadTask _task_onqueue_didReceiveDispatchData:completionHandler:];
-[__NSCFLocalDownloadTask _task_onqueue_didFinish];
-[__NSCFLocalDownloadTask _onqueue_completeInitialization];
-[__NSCFLocalDownloadTask dealloc];
-[__NSCFLocalDownloadTask createResumeInformation:];
-[__NSCFLocalDownloadTask _keepDownloadTaskFile];
-[__NSCFLocalDownloadTask _onqueue_cancelByProducingResumeData:];
-[__NSCFLocalDownloadTask terminateExtractorWithError:completion:];
-[__NSCFLocalDownloadTask isKindOfClass:];
-[__NSCFLocalDownloadTask cancelByProducingResumeData:];
-[__NSCFLocalDownloadTask openItemForPath:mode:];
-[__NSCFLocalDownloadTask setDownloadFile:];
-[__NSCFLocalDownloadTask downloadFile];
-[__NSCFLocalDownloadTask _copySocketStreamProperties];
```
