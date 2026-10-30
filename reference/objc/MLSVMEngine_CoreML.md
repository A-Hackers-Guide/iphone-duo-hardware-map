# `MLSVMEngine`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 6 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _freeModelOnDealloc;
B _isInputSizeLowerBoundOnly;
^{svm_model={svm_parameter=iiidddddi^i^dddii}ii^^{svm_node}^^d^d^d^d^i^i^ii} _model;
Q _inputSize;
@"NSArray" _classLabels;
```

## Properties

```
@property (T^{svm_model={svm_parameter=iiidddddi^i^dddii}ii^^{svm_node}^^d^d^d^d^i^i^ii},V_model) model;
@property (TB,V_freeModelOnDealloc) freeModelOnDealloc;
@property (TB,V_isInputSizeLowerBoundOnly) isInputSizeLowerBoundOnly;
@property (TQ,V_inputSize) inputSize;
@property (T@"NSArray",&,N,V_classLabels) classLabels;
@property (TQ,R,N) numberOfClasses;
```

## Instance methods

```
-[MLSVMEngine classLabels];
-[MLSVMEngine model];
-[MLSVMEngine setModel:];
-[MLSVMEngine dealloc];
-[MLSVMEngine setClassLabels:];
-[MLSVMEngine numberOfClasses];
-[MLSVMEngine fillSVMNodeVector:values:count:];
-[MLSVMEngine hasProbabilityPredictionEnabled];
-[MLSVMEngine initWithLibSVMFile:classLabels:];
-[MLSVMEngine allocSVMNodeVector:];
-[MLSVMEngine deallocSVMNodeVector:];
-[MLSVMEngine freeModelOnDealloc];
-[MLSVMEngine initWithSVMModel:freeOnDealloc:isInputSizeLowerBoundOnly:inputSize:classLabels:];
-[MLSVMEngine initWithSpecification:error:];
-[MLSVMEngine inputSize];
-[MLSVMEngine isInputSizeLowerBoundOnly];
-[MLSVMEngine predict:];
-[MLSVMEngine predictProbabilities:probabilities:];
-[MLSVMEngine setFreeModelOnDealloc:];
-[MLSVMEngine setInputSize:];
-[MLSVMEngine setIsInputSizeLowerBoundOnly:];
```
