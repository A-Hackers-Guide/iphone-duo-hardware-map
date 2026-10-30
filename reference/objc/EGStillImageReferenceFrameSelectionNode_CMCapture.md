# `EGStillImageReferenceFrameSelectionNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `EGNode`
- 3 instance variables, 3 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _sampleBufferInputs;
@"EGInput" _fusionModeInput;
@"EGStillImageOutput" _referenceFrameOutput;
```

## Properties

```
@property (T@"NSArray",R,N,V_sampleBufferInputs) sampleBufferInputs;
@property (T@"EGInput",R,N,V_fusionModeInput) fusionModeInput;
@property (T@"EGOutput",R,N,V_referenceFrameOutput) referenceFrameOutput;
```

## Class methods

```
+[EGStillImageReferenceFrameSelectionNode initialize];
```

## Instance methods

```
-[EGStillImageReferenceFrameSelectionNode dealloc];
-[EGStillImageReferenceFrameSelectionNode fusionModeInput];
-[EGStillImageReferenceFrameSelectionNode initWithName:numSampleBufferInputs:];
-[EGStillImageReferenceFrameSelectionNode receiveData:fromInputGroup:];
-[EGStillImageReferenceFrameSelectionNode referenceFrameOutput];
-[EGStillImageReferenceFrameSelectionNode sampleBufferInputs];
```
