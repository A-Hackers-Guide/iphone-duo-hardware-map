# `MLGLMRegression`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLRegressor`
- Protocols: `MLModelSpecificationLoader`
- 4 instance variables, 4 properties, 3 instance methods, 1 class methods

## Instance variables

```
{vector<double, std::allocator<double>>="__begin_"^d"__end_"^d""{?="__cap_"^d}} intercept;
{vector<std::vector<double>, std::allocator<std::vector<double>>>="__begin_"^v"__end_"^v""{?="__cap_"^v}} weights;
i postEvalTransForm;
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
+[MLGLMRegression loadModelFromSpecification:configuration:error:];
```

## Instance methods

```
-[MLGLMRegression regress:options:error:];
-[MLGLMRegression initWithLRSpec:configuration:error:];
-[MLGLMRegression initWithSpecification:configuration:error:];
```
