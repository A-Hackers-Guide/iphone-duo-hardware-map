# `BWDeferredProcessingContainerManager`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWDeferredContainerManagerBase`
- 1 instance variables, 0 properties, 7 instance methods, 1 class methods

## Instance variables

```
^{OpaqueFigCaptureDeferredContainerManager=} _xpcContainerManager;
```

## Class methods

```
+[BWDeferredProcessingContainerManager sharedInstance];
```

## Instance methods

```
-[BWDeferredProcessingContainerManager init];
-[BWDeferredProcessingContainerManager createProcessingContainerWithApplicationID:captureRequestIdentifier:openForPeeking:err:];
-[BWDeferredProcessingContainerManager createTransientContainerWithApplicationID:resolvedSettings:unresolvedSettings:pipelineParameters:intermediates:photoDescriptors:];
-[BWDeferredProcessingContainerManager deleteContainerForApplicationID:captureRequestIdentifier:];
-[BWDeferredProcessingContainerManager manifestsForApplicationID:err:];
-[BWDeferredProcessingContainerManager releaseProcessingContainer:];
-[BWDeferredProcessingContainerManager waitForShaderCompilation];
```
