# `FigCaptureDeferredProcessingJob`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 9 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"FigWeakReference" _weakDelegateReference;
@"BWDeferredProcessingContainer" _container;
@"FigCaptureDeferredPhotoProcessorRequest" _processorRequest;
q _startNS;
q _durationNS;
@"NSString" _primaryPortType;
B _interactiveQoS;
i _numberOfPhotosDelivered;
i _memoryStatusLevel;
i _thermalLevel;
q _prepareGraphNS;
```

## Properties

```
@property (T@"FigCaptureDeferredPhotoProcessorRequest",R,N,V_processorRequest) processorRequest;
@property (Tq,N,V_startNS) startNS;
@property (Tq,N,V_durationNS) durationNS;
@property (T@"NSString",R,N,V_primaryPortType) primaryPortType;
@property (Ti,N,V_memoryStatusLevel) memoryStatusLevel;
@property (Ti,N,V_thermalLevel) thermalLevel;
@property (Ti,V_numberOfPhotosDelivered) numberOfPhotosDelivered;
@property (TB,N,GisInteractiveQoS,V_interactiveQoS) interactiveQoS;
@property (Tq,N,V_prepareGraphNS) prepareGraphNS;
```

## Class methods

```
+[FigCaptureDeferredProcessingJob isPotentiallyRecoverableError:];
```

## Instance methods

```
-[FigCaptureDeferredProcessingJob dealloc];
-[FigCaptureDeferredProcessingJob setThermalLevel:];
-[FigCaptureDeferredProcessingJob thermalLevel];
-[FigCaptureDeferredProcessingJob primaryPortType];
-[FigCaptureDeferredProcessingJob container];
-[FigCaptureDeferredProcessingJob startNS];
-[FigCaptureDeferredProcessingJob durationNS];
-[FigCaptureDeferredProcessingJob initWithProcessorRequest:delegate:error:];
-[FigCaptureDeferredProcessingJob isInteractiveQoS];
-[FigCaptureDeferredProcessingJob memoryStatusLevel];
-[FigCaptureDeferredProcessingJob numberOfPhotosDelivered];
-[FigCaptureDeferredProcessingJob prepareGraphNS];
-[FigCaptureDeferredProcessingJob processorRequest];
-[FigCaptureDeferredProcessingJob setDurationNS:];
-[FigCaptureDeferredProcessingJob setInteractiveQoS:];
-[FigCaptureDeferredProcessingJob setMemoryStatusLevel:];
-[FigCaptureDeferredProcessingJob setNumberOfPhotosDelivered:];
-[FigCaptureDeferredProcessingJob setPrepareGraphNS:];
-[FigCaptureDeferredProcessingJob setStartNS:];
```
