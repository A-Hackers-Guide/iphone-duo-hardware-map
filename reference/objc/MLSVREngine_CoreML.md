# `MLSVREngine`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
B _isInputSizeLowerBoundOnly;
B _freeModelOnDealloc;
Q _inputSize;
^{svm_model={svm_parameter=iiidddddi^i^dddii}ii^^{svm_node}^^d^d^d^d^i^i^ii} _model;
```

## Properties

```
@property (T^{svm_model={svm_parameter=iiidddddi^i^dddii}ii^^{svm_node}^^d^d^d^d^i^i^ii},V_model) model;
@property (TB,V_freeModelOnDealloc) freeModelOnDealloc;
@property (TB,R,V_isInputSizeLowerBoundOnly) isInputSizeLowerBoundOnly;
@property (TQ,R,V_inputSize) inputSize;
```

## Instance methods

```
-[MLSVREngine model];
-[MLSVREngine setModel:];
-[MLSVREngine dealloc];
-[MLSVREngine fillSVMNodeVector:values:count:];
-[MLSVREngine allocSVMNodeVector:];
-[MLSVREngine deallocSVMNodeVector:];
-[MLSVREngine freeModelOnDealloc];
-[MLSVREngine initWithLibSVMFile:];
-[MLSVREngine initWithSVMModel:freeOnDealloc:isInputSizeLowerBoundOnly:inputSize:];
-[MLSVREngine initWithSpecification:error:];
-[MLSVREngine inputSize];
-[MLSVREngine isInputSizeLowerBoundOnly];
-[MLSVREngine predict:];
-[MLSVREngine setFreeModelOnDealloc:];
```
