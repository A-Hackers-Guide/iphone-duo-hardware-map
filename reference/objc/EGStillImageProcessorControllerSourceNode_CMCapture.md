# `EGStillImageProcessorControllerSourceNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGNode`
- 2 instance variables, 1 properties, 4 instance methods, 2 class methods

## Instance variables

```
Q _processorType;
@"EGStillImageOutput" _processorControllerOutput;
```

## Properties

```
@property (T@"EGOutput",R,N,V_processorControllerOutput) processorControllerOutput;
```

## Class methods

```
+[EGStillImageProcessorControllerSourceNode initialize];
+[EGStillImageProcessorControllerSourceNode enqueueProcessorControllersToGraph:fromResourceCoordinator:];
```

## Instance methods

```
-[EGStillImageProcessorControllerSourceNode initWithType:];
-[EGStillImageProcessorControllerSourceNode dealloc];
-[EGStillImageProcessorControllerSourceNode enqueueProcessorControllerFromResourceCoordinator:];
-[EGStillImageProcessorControllerSourceNode processorControllerOutput];
```
