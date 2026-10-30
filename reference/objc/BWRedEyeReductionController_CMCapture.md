# `BWRedEyeReductionController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorController`
- Protocols: `BWRedEyeReductionControllerInputDelegate`
- 4 instance variables, 4 properties, 7 instance methods, 2 class methods

## Instance variables

```
@"NSDictionary" _redEyeReductionParametersByPortType;
@"CIDualRedEyeRepairSession" _redEyeRepairSession;
^{opaqueCMFormatDescription=} _outputFormatDescription;
@"NSMutableArray" _requestQueue;
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
+[BWRedEyeReductionController prewarm];
+[BWRedEyeReductionController initialize];
```

## Instance methods

```
-[BWRedEyeReductionController dealloc];
-[BWRedEyeReductionController initWithConfiguration:];
-[BWRedEyeReductionController type];
-[BWRedEyeReductionController cancelProcessing];
-[BWRedEyeReductionController didReceiveAllFramesForInput:];
-[BWRedEyeReductionController didReceiveFrameForInput:];
-[BWRedEyeReductionController enqueueInputForProcessing:delegate:];
```
