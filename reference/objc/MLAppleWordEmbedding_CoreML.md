# `MLAppleWordEmbedding`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModel`
- Protocols: `MLModelSpecificationLoader`
- 2 instance variables, 5 properties, 4 instance methods, 2 class methods

## Instance variables

```
^v wordEmbeddingModel;
@"MLAppleWordEmbeddingParameters" _parameters;
```

## Properties

```
@property (T@"MLAppleWordEmbeddingParameters",R,V_parameters) parameters;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLAppleWordEmbedding saveAppleWordEmbeddingModelToURL:wordEmbeddingParameters:error:];
+[MLAppleWordEmbedding loadModelFromSpecification:configuration:error:];
```

## Instance methods

```
-[MLAppleWordEmbedding parameters];
-[MLAppleWordEmbedding dealloc];
-[MLAppleWordEmbedding predictionFromFeatures:options:error:];
-[MLAppleWordEmbedding initWithParameters:modelDescription:nlpHandle:configuration:error:];
```
