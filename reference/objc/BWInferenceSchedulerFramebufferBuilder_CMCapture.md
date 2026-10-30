# `BWInferenceSchedulerFramebufferBuilder`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 3 instance methods, 1 class methods

## Instance variables

```
I _framebufferPriority;
@"BWInferenceSchedulerGraph" _graph;
@"BWInferenceSchedulerJobList" _prototypeJobList;
@"BWInferenceSchedulerJobList" _prototypePostProcessorJobList;
@"NSString" _engineDescription;
Q _jobCount;
@"NSMapTable" _directedEdgesByNode;
@"NSMutableDictionary" _prototypeDependentPostProcessorsBySourceInferenceJobs;
B _didVendFramebuffer;
```

## Class methods

```
+[BWInferenceSchedulerFramebufferBuilder initialize];
```

## Instance methods

```
-[BWInferenceSchedulerFramebufferBuilder dealloc];
-[BWInferenceSchedulerFramebufferBuilder initWithInferenceRequirements:dependencyProvider:formatProvider:processingConfiguration:postProcessors:framebufferPriority:engineDescription:];
-[BWInferenceSchedulerFramebufferBuilder newFramebuffer];
```
