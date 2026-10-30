# `__NSCFLocalUploadTask`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `__NSCFLocalDataTask`
- Protocols: `NSURLSessionUploadTaskSubclass`
- 2 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
B _startedProducingResumeData;
@? _resumeCallback;
```

## Properties

```
@property (T@?,C,V_resumeCallback) resumeCallback;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[__NSCFLocalUploadTask setResumeCallback:];
-[__NSCFLocalUploadTask _task_onqueue_didFinish];
-[__NSCFLocalUploadTask dealloc];
-[__NSCFLocalUploadTask initWithResumeData:ident:taskGroup:];
-[__NSCFLocalUploadTask _onqueue_cancelByProducingResumeData:];
-[__NSCFLocalUploadTask resumeCallback];
-[__NSCFLocalUploadTask isKindOfClass:];
-[__NSCFLocalUploadTask cancelByProducingResumeData:];
```
