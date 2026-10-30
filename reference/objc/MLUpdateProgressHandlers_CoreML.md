# `MLUpdateProgressHandlers`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 14 instance methods, 0 class methods

## Instance variables

```
q _interestedEvents;
@? _progressHandler;
@? _completionHandler;
```

## Properties

```
@property (Tq,V_interestedEvents) interestedEvents;
@property (T@?,C,V_progressHandler) progressHandler;
@property (T@?,C,V_completionHandler) completionHandler;
```

## Instance methods

```
-[MLUpdateProgressHandlers setProgressHandler:];
-[MLUpdateProgressHandlers progressHandler];
-[MLUpdateProgressHandlers setCompletionHandler:];
-[MLUpdateProgressHandlers completionHandler];
-[MLUpdateProgressHandlers description];
-[MLUpdateProgressHandlers _dispatchUpdateProgressHandlerForEvent:metrics:parameters:error:onQueue:];
-[MLUpdateProgressHandlers dispatchEpochEndProgressHandlerWithMetrics:parameters:onQueue:];
-[MLUpdateProgressHandlers dispatchMiniBatchEndProgressHandlerWithMetrics:parameters:onQueue:];
-[MLUpdateProgressHandlers dispatchTrainingBeginProgressHandlerWithMetrics:parameters:onQueue:];
-[MLUpdateProgressHandlers dispatchTrainingCompletionHandlerWithError:onQueue:];
-[MLUpdateProgressHandlers dispatchTrainingCompletionHandlerWithMetrics:parameters:onQueue:];
-[MLUpdateProgressHandlers initForEvents:progressHandler:completionHandler:];
-[MLUpdateProgressHandlers interestedEvents];
-[MLUpdateProgressHandlers setInterestedEvents:];
```
