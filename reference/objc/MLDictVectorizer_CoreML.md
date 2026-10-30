# `MLDictVectorizer`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MLModelEngine`
- Protocols: `MLModelSpecificationLoader`
- 1 instance variables, 5 properties, 5 instance methods, 3 class methods

## Instance variables

```
@"NSOrderedSet" _categoryName;
```

## Properties

```
@property (T@"NSOrderedSet",R,N,V_categoryName) categoryName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[MLDictVectorizer categoryName:dataTransformerName:inputDescription:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:error:];
+[MLDictVectorizer categoryName:inputDescription:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:error:];
+[MLDictVectorizer loadModelFromSpecification:configuration:error:];
```

## Instance methods

```
-[MLDictVectorizer predictionTypeForKTrace];
-[MLDictVectorizer categoryName];
-[MLDictVectorizer predictionFromFeatures:options:error:];
-[MLDictVectorizer constructDictionary:error:];
-[MLDictVectorizer initWith:dataTransformerName:inputDescription:outputDescription:orderedInputFeatureNames:orderedOutputFeatureNames:configuration:error:];
```
