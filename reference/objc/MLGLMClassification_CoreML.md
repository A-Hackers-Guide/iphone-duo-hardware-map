# `MLGLMClassification`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLClassifier`
- Protocols: `MLModelSpecificationLoader`
- 7 instance variables, 4 properties, 5 instance methods, 1 class methods

## Instance variables

```
{vector<double, std::allocator<double>>="__begin_"^d"__end_"^d""{?="__cap_"^d}} intercept;
{vector<std::vector<double>, std::allocator<std::vector<double>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} weights;
@"NSMutableArray" classLabels;
q classType;
i postEvalTransForm;
i classEncoding;
{shared_ptr<CoreML::Specification::Model>="__ptr_"^{Model}"__cntrl_"^{__shared_weak_count}} m_spec;
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
+[MLGLMClassification loadModelFromSpecification:configuration:error:];
```

## Instance methods

```
-[MLGLMClassification classify:options:error:];
-[MLGLMClassification classify:error:];
-[MLGLMClassification calculateClassProbability:input:error:];
-[MLGLMClassification classify:topK:error:];
-[MLGLMClassification initWithSpecification:configuration:error:];
```
