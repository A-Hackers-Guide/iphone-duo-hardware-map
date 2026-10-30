# `BWDeferredCaptureController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorController`
- Protocols: `BWDeferredCaptureControllerInputUpdatesDelegate`
- 1 instance variables, 4 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"BWDeferredCaptureContainer" _captureContainer;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWDeferredCaptureController usesCustomProcessingFlow];
```

## Instance methods

```
-[BWDeferredCaptureController process];
-[BWDeferredCaptureController reset];
-[BWDeferredCaptureController initWithConfiguration:];
-[BWDeferredCaptureController prepare];
-[BWDeferredCaptureController requestForInput:delegate:errOut:];
-[BWDeferredCaptureController cancelProcessing];
-[BWDeferredCaptureController _addInferences];
-[BWDeferredCaptureController input:encounteredProcessingError:];
-[BWDeferredCaptureController inputReceivedIntermediate:];
```
