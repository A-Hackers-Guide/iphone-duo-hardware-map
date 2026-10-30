# `CWFAsyncBlockOperation`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSBlockOperation`
- 2 instance variables, 2 properties, 9 instance methods, 1 class methods

## Instance variables

```
B _didStartOperation;
q _completionCounter;
```

## Properties

```
@property (TB,V_didStartOperation) didStartOperation;
@property (Tq,V_completionCounter) completionCounter;
```

## Class methods

```
+[CWFAsyncBlockOperation _removesDependenciesAfterFinish];
```

## Instance methods

```
-[CWFAsyncBlockOperation isFinished];
-[CWFAsyncBlockOperation main];
-[CWFAsyncBlockOperation isExecuting];
-[CWFAsyncBlockOperation completionCounter];
-[CWFAsyncBlockOperation decrementCompletionCounter];
-[CWFAsyncBlockOperation didStartOperation];
-[CWFAsyncBlockOperation incrementCompletionCounter];
-[CWFAsyncBlockOperation setCompletionCounter:];
-[CWFAsyncBlockOperation setDidStartOperation:];
```
