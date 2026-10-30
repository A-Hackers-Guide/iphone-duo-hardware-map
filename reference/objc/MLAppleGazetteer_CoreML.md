# `MLAppleGazetteer`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModel`
- Protocols: `MLModelSpecificationLoader`
- 2 instance variables, 5 properties, 4 instance methods, 2 class methods

## Instance variables

```
^v gazetteerModel;
@"MLAppleGazetteerParameters" _parameters;
```

## Properties

```
@property (T@"MLAppleGazetteerParameters",R,V_parameters) parameters;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLAppleGazetteer loadModelFromSpecification:configuration:error:];
+[MLAppleGazetteer saveAppleGazetteerModelToURL:gazetteerParameters:error:];
```

## Instance methods

```
-[MLAppleGazetteer parameters];
-[MLAppleGazetteer dealloc];
-[MLAppleGazetteer predictionFromFeatures:options:error:];
-[MLAppleGazetteer initWithParameters:modelDescription:nlpHandle:configuration:error:];
```
