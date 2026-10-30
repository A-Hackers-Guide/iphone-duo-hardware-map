# `BWInferenceSchedulerJobList`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSFastEnumeration`
- 4 instance variables, 1 properties, 5 instance methods, 0 class methods

## Instance variables

```
Q _jobCount;
Q _mutations;
^{?=@@ICCACAC} _orderedJobs;
@"NSMapTable" _jobIndexByProvider;
```

## Properties

```
@property (TQ,R) count;
```

## Instance methods

```
-[BWInferenceSchedulerJobList dealloc];
-[BWInferenceSchedulerJobList count];
-[BWInferenceSchedulerJobList countByEnumeratingWithState:objects:count:];
-[BWInferenceSchedulerJobList initWithCapacity:];
-[BWInferenceSchedulerJobList jobAtIndex:];
```
