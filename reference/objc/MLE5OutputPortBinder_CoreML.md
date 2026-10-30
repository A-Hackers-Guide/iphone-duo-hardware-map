# `MLE5OutputPortBinder`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLE5PortBinder`
- 9 instance variables, 12 properties, 26 instance methods, 0 class methods

## Instance variables

```
^{__CVBuffer=} _temporarilyBoundPixelBuffer;
@"MLFeatureValue" _featureValue;
B _outputBackingWasDirectlyBound;
B _boundFeatureDirectly;
@"MLPixelBufferPool" _pixelBufferPool;
@ _outputBacking;
^{e5rt_io_port=} _portHandle;
@"MLFeatureDescription" _featureDescription;
@"NSObject<OS_dispatch_queue>" _serialQueue;
```

## Properties

```
@property (T^{e5rt_io_port=},R,V_portHandle) portHandle;
@property (T@"MLFeatureDescription",R,V_featureDescription) featureDescription;
@property (T@"NSObject<OS_dispatch_queue>",R,V_serialQueue) serialQueue;
@property (TB,N,V_outputBackingWasDirectlyBound) outputBackingWasDirectlyBound;
@property (TB,N,V_boundFeatureDirectly) boundFeatureDirectly;
@property (T@,&,V_outputBacking) outputBacking;
@property (T@"MLFeatureValue",R) featureValue;
@property (T@"MLPixelBufferPool",&,N,V_pixelBufferPool) pixelBufferPool;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MLE5OutputPortBinder setPixelBufferPool:];
-[MLE5OutputPortBinder portHandle];
-[MLE5OutputPortBinder serialQueue];
-[MLE5OutputPortBinder outputBackingWasDirectlyBound];
-[MLE5OutputPortBinder setOutputBacking:];
-[MLE5OutputPortBinder pixelBufferPool];
-[MLE5OutputPortBinder _makeFeatureValueFromOutputBacking:error:];
-[MLE5OutputPortBinder featureDescription];
-[MLE5OutputPortBinder _directModeForOutputBacking:error:];
-[MLE5OutputPortBinder dealloc];
-[MLE5OutputPortBinder featureValue];
-[MLE5OutputPortBinder _reusableForCopyBoundOutputBacking];
-[MLE5OutputPortBinder reset];
-[MLE5OutputPortBinder bindAndReturnError:];
-[MLE5OutputPortBinder _makeFeatureValueAndReturnError:];
-[MLE5OutputPortBinder _copyOutputFromPort:toOutputBacking:featureDescription:error:];
-[MLE5OutputPortBinder setOutputBackingWasDirectlyBound:];
-[MLE5OutputPortBinder _reusableForDirectlyBoundOutputBacking:];
-[MLE5OutputPortBinder initWithPort:featureDescription:];
-[MLE5OutputPortBinder _outputModeForOutputBacking:error:];
-[MLE5OutputPortBinder reusableForOutputBacking:willBindDirectly:];
-[MLE5OutputPortBinder _directlyBindOutputBacking:error:];
-[MLE5OutputPortBinder boundFeatureDirectly];
-[MLE5OutputPortBinder _makeFeatureValueFromPort:featureDescription:error:];
-[MLE5OutputPortBinder setBoundFeatureDirectly:];
-[MLE5OutputPortBinder outputBacking];
```
