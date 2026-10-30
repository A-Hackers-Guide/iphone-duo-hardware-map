# `_MTL4CommitFeedback`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MTL4CommitFeedbackGGDPrivate`
- 8 instance variables, 8 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"_MTL4CommandQueue" _queue;
@"_MTL4CommitFeedbackDispatch" _commitFeedbackDispatch;
@"NSError" _error;
Q _gpuStartTime;
Q _gpuEndTime;
@"NSMutableArray" _errors;
@? _internalFeedbackHandler;
@"NSArray" _logs;
```

## Properties

```
@property (T@"NSError",R,N) error;
@property (Td,R,N) GPUStartTime;
@property (Td,R,N) GPUEndTime;
@property (T@"<MTLLogContainer>",N) logs;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_MTL4CommitFeedback initialize];
```

## Instance methods

```
-[_MTL4CommitFeedback GPUEndTime];
-[_MTL4CommitFeedback setLogs:];
-[_MTL4CommitFeedback logs];
-[_MTL4CommitFeedback GPUStartTime];
-[_MTL4CommitFeedback dealloc];
-[_MTL4CommitFeedback error];
-[_MTL4CommitFeedback commandBufferComplete:completionTime:error:executeHandlers:];
-[_MTL4CommitFeedback initWithQueue:commitOptions:internalCompletionHandler:];
-[_MTL4CommitFeedback initWithQueue:commitOptions:internalFeedbackHandler:];
```
