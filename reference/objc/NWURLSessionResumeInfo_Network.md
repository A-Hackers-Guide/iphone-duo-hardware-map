# `NWURLSessionResumeInfo`

- Image: [`/System/Library/Frameworks/Network.framework/Network`](../userland/System__Library__Frameworks__Network.framework__Network.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 11 instance variables, 11 properties, 24 instance methods, 1 class methods

## Instance variables

```
B _prefersIncrementalDelivery;
f _priority;
I _taskIdentifier;
@"NSURLRequest" _originalRequest;
@"NSURLRequest" _currentRequest;
@"NSHTTPURLResponse" _response;
@"NSDate" _earliestBeginDate;
q _countOfBytesClientExpectsToSend;
q _countOfBytesClientExpectsToReceive;
@"NSString" _taskDescription;
d _startTime;
```

## Properties

```
@property (T@"NSURLRequest",&,N,V_originalRequest) originalRequest;
@property (T@"NSURLRequest",&,N,V_currentRequest) currentRequest;
@property (T@"NSHTTPURLResponse",&,N,V_response) response;
@property (T@"NSDate",&,N,V_earliestBeginDate) earliestBeginDate;
@property (Tq,N,V_countOfBytesClientExpectsToSend) countOfBytesClientExpectsToSend;
@property (Tq,N,V_countOfBytesClientExpectsToReceive) countOfBytesClientExpectsToReceive;
@property (T@"NSString",&,N,V_taskDescription) taskDescription;
@property (Tf,N,V_priority) priority;
@property (TB,N,V_prefersIncrementalDelivery) prefersIncrementalDelivery;
@property (TI,N,V_taskIdentifier) taskIdentifier;
@property (Td,N,V_startTime) startTime;
```

## Class methods

```
+[NWURLSessionResumeInfo supportsSecureCoding];
```

## Instance methods

```
-[NWURLSessionResumeInfo currentRequest];
-[NWURLSessionResumeInfo taskIdentifier];
-[NWURLSessionResumeInfo priority];
-[NWURLSessionResumeInfo setResponse:];
-[NWURLSessionResumeInfo startTime];
-[NWURLSessionResumeInfo setPriority:];
-[NWURLSessionResumeInfo originalRequest];
-[NWURLSessionResumeInfo prefersIncrementalDelivery];
-[NWURLSessionResumeInfo setStartTime:];
-[NWURLSessionResumeInfo setCurrentRequest:];
-[NWURLSessionResumeInfo encodeWithCoder:];
-[NWURLSessionResumeInfo initWithCoder:];
-[NWURLSessionResumeInfo taskDescription];
-[NWURLSessionResumeInfo response];
-[NWURLSessionResumeInfo countOfBytesClientExpectsToSend];
-[NWURLSessionResumeInfo countOfBytesClientExpectsToReceive];
-[NWURLSessionResumeInfo earliestBeginDate];
-[NWURLSessionResumeInfo setCountOfBytesClientExpectsToReceive:];
-[NWURLSessionResumeInfo setCountOfBytesClientExpectsToSend:];
-[NWURLSessionResumeInfo setEarliestBeginDate:];
-[NWURLSessionResumeInfo setOriginalRequest:];
-[NWURLSessionResumeInfo setPrefersIncrementalDelivery:];
-[NWURLSessionResumeInfo setTaskDescription:];
-[NWURLSessionResumeInfo setTaskIdentifier:];
```
