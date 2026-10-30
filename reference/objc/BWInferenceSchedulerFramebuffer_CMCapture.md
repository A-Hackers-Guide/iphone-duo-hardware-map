# `BWInferenceSchedulerFramebuffer`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} framebufferLock;
Ai failedJobStatus;
@"BWInferenceSchedulerJobList" _jobs;
@"BWInferenceSchedulerJobList" _postProcessorJobs;
@"BWInferenceSchedulerGraph" _graph;
@"NSMutableDictionary" _dependentPostProcessorsBySourceInferenceJobs;
```

## Properties

```
@property (T@"BWInferenceSchedulerJobList",R,N,V_jobs) jobs;
@property (T@"BWInferenceSchedulerJobList",R,N,V_postProcessorJobs) postProcessorJobs;
@property (T@"BWInferenceSchedulerGraph",R,N,V_graph) graph;
@property (T@"NSMutableDictionary",R,N,V_dependentPostProcessorsBySourceInferenceJobs) dependentPostProcessorsBySourceInferenceJobs;
```

## Instance methods

```
-[BWInferenceSchedulerFramebuffer jobs];
-[BWInferenceSchedulerFramebuffer graph];
-[BWInferenceSchedulerFramebuffer dealloc];
-[BWInferenceSchedulerFramebuffer description];
-[BWInferenceSchedulerFramebuffer dependentPostProcessorsBySourceInferenceJobs];
-[BWInferenceSchedulerFramebuffer initWithGraph:jobList:postProcessorJobList:dependentPostProcessorsBySourceInferenceJobs:];
-[BWInferenceSchedulerFramebuffer postProcessorJobs];
-[BWInferenceSchedulerFramebuffer resetJobStatesWithPreventionBlock:];
```
