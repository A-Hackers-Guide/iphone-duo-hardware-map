# `BWDeferredProcessingAnalyticsPayload`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWCoreAnalyticsPayload`
- 12 instance variables, 16 properties, 29 instance methods, 0 class methods

## Instance variables

```
i _error;
@"NSString" _processingResult;
i _processingType;
B _fileBacked;
I _containerAgeInSeconds;
Q _containerSizeInBytes;
B _interactiveQoS;
I _graphPrepareDurationInMilliseconds;
I _jobDurationInMilliseconds;
i _containerProcessingCount;
i _memoryStatusLevel;
i _thermalLevel;
```

## Properties

```
@property (Ti,N,V_error) error;
@property (T@"NSString",C,N,V_processingResult) processingResult;
@property (Ti,N,V_processingType) processingType;
@property (TB,N,V_fileBacked) fileBacked;
@property (TI,N,V_containerAgeInSeconds) containerAgeInSeconds;
@property (TQ,N,V_containerSizeInBytes) containerSizeInBytes;
@property (TB,N,V_interactiveQoS) interactiveQoS;
@property (TI,N,V_graphPrepareDurationInMilliseconds) graphPrepareDurationInMilliseconds;
@property (TI,N,V_jobDurationInMilliseconds) jobDurationInMilliseconds;
@property (Ti,N,V_containerProcessingCount) containerProcessingCount;
@property (Ti,N,V_memoryStatusLevel) memoryStatusLevel;
@property (Ti,N,V_thermalLevel) thermalLevel;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BWDeferredProcessingAnalyticsPayload setError:];
-[BWDeferredProcessingAnalyticsPayload eventDictionary];
-[BWDeferredProcessingAnalyticsPayload init];
-[BWDeferredProcessingAnalyticsPayload dealloc];
-[BWDeferredProcessingAnalyticsPayload reset];
-[BWDeferredProcessingAnalyticsPayload error];
-[BWDeferredProcessingAnalyticsPayload eventName];
-[BWDeferredProcessingAnalyticsPayload setThermalLevel:];
-[BWDeferredProcessingAnalyticsPayload thermalLevel];
-[BWDeferredProcessingAnalyticsPayload containerAgeInSeconds];
-[BWDeferredProcessingAnalyticsPayload containerProcessingCount];
-[BWDeferredProcessingAnalyticsPayload containerSizeInBytes];
-[BWDeferredProcessingAnalyticsPayload fileBacked];
-[BWDeferredProcessingAnalyticsPayload graphPrepareDurationInMilliseconds];
-[BWDeferredProcessingAnalyticsPayload interactiveQoS];
-[BWDeferredProcessingAnalyticsPayload jobDurationInMilliseconds];
-[BWDeferredProcessingAnalyticsPayload memoryStatusLevel];
-[BWDeferredProcessingAnalyticsPayload processingResult];
-[BWDeferredProcessingAnalyticsPayload processingType];
-[BWDeferredProcessingAnalyticsPayload setContainerAgeInSeconds:];
-[BWDeferredProcessingAnalyticsPayload setContainerProcessingCount:];
-[BWDeferredProcessingAnalyticsPayload setContainerSizeInBytes:];
-[BWDeferredProcessingAnalyticsPayload setFileBacked:];
-[BWDeferredProcessingAnalyticsPayload setGraphPrepareDurationInMilliseconds:];
-[BWDeferredProcessingAnalyticsPayload setInteractiveQoS:];
-[BWDeferredProcessingAnalyticsPayload setJobDurationInMilliseconds:];
-[BWDeferredProcessingAnalyticsPayload setMemoryStatusLevel:];
-[BWDeferredProcessingAnalyticsPayload setProcessingResult:];
-[BWDeferredProcessingAnalyticsPayload setProcessingType:];
```
