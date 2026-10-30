# `BWRedEyeReductionControllerInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerInput`
- 6 instance variables, 6 properties, 11 instance methods, 1 class methods

## Instance variables

```
@"<BWRedEyeReductionControllerInputDelegate>" _inputDelegate;
@"<BWStillImageProcessorControllerDelegate>" _processorControllerDelegate;
^{opaqueCMSampleBuffer=} _primaryImage;
^{opaqueCMSampleBuffer=} _auxImage;
@"NSArray" _faceObservations;
B _requiresSensorInterfaceRawPropagation;
```

## Properties

```
@property (T@"<BWRedEyeReductionControllerInputDelegate>",&,N,V_inputDelegate) inputDelegate;
@property (T@"<BWStillImageProcessorControllerDelegate>",&,N,V_processorControllerDelegate) processorControllerDelegate;
@property (TB,N,V_requiresSensorInterfaceRawPropagation) requiresSensorInterfaceRawPropagation;
@property (T^{opaqueCMSampleBuffer=},R,N,V_primaryImage) primaryImage;
@property (T^{opaqueCMSampleBuffer=},R,N,V_auxImage) auxImage;
@property (T@"NSArray",R,N,V_faceObservations) faceObservations;
```

## Class methods

```
+[BWRedEyeReductionControllerInput requiresInferencesFromFrame:];
```

## Instance methods

```
-[BWRedEyeReductionControllerInput setInputDelegate:];
-[BWRedEyeReductionControllerInput inputDelegate];
-[BWRedEyeReductionControllerInput dealloc];
-[BWRedEyeReductionControllerInput faceObservations];
-[BWRedEyeReductionControllerInput primaryImage];
-[BWRedEyeReductionControllerInput auxImage];
-[BWRedEyeReductionControllerInput setProcessorControllerDelegate:];
-[BWRedEyeReductionControllerInput addFrame:faceObservations:];
-[BWRedEyeReductionControllerInput processorControllerDelegate];
-[BWRedEyeReductionControllerInput requiresSensorInterfaceRawPropagation];
-[BWRedEyeReductionControllerInput setRequiresSensorInterfaceRawPropagation:];
```
