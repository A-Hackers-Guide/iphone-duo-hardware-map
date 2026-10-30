# `EGStillImageGraph`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGGraph`
- Protocols: `EGStillImageGraphManager`, `BWStillImageProcessingCoordinator`
- 5 instance variables, 5 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"BWStillImageSettings" _stillImageSettings;
@"<BWStillImageProcessingCoordinatorDelegate>" _weakDelegate;
@"<EGStillImageGraphSampleBufferEntryPoint>" _sampleBufferEntryPoint;
AB _isProcessing;
@"NSObject<OS_dispatch_group>" _completionGroup;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,N) captureRequestIdentifier;
```

## Class methods

```
+[EGStillImageGraph initialize];
```

## Instance methods

```
-[EGStillImageGraph dealloc];
-[EGStillImageGraph enqueueSampleBuffer:];
-[EGStillImageGraph captureRequestIdentifier];
-[EGStillImageGraph captureComplete];
-[EGStillImageGraph _signalCompletion];
-[EGStillImageGraph didEncounterError:description:element:];
-[EGStillImageGraph didFinishProcessingSampleBuffer:description:];
-[EGStillImageGraph initWithName:stillImageSettings:delegate:];
-[EGStillImageGraph setSampleBufferEntryPoint:];
-[EGStillImageGraph waitForActiveProcessingToComplete];
```
