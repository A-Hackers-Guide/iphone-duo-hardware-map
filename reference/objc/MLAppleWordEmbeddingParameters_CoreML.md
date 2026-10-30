# `MLAppleWordEmbeddingParameters`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 14 instance methods, 0 class methods

## Instance variables

```
Q _revision;
@"NSString" _language;
@"NSString" _inputFeatureName;
@"NSString" _outputFeatureName;
@"NSData" _modelParameterData;
@"NSDictionary" _metadata;
```

## Properties

```
@property (TQ,V_revision) revision;
@property (T@"NSString",&,V_language) language;
@property (T@"NSString",&,V_inputFeatureName) inputFeatureName;
@property (T@"NSString",&,V_outputFeatureName) outputFeatureName;
@property (T@"NSData",&,V_modelParameterData) modelParameterData;
@property (T@"NSDictionary",&,V_metadata) metadata;
```

## Instance methods

```
-[MLAppleWordEmbeddingParameters language];
-[MLAppleWordEmbeddingParameters revision];
-[MLAppleWordEmbeddingParameters metadata];
-[MLAppleWordEmbeddingParameters setMetadata:];
-[MLAppleWordEmbeddingParameters setLanguage:];
-[MLAppleWordEmbeddingParameters setRevision:];
-[MLAppleWordEmbeddingParameters initWithData:language:inputFeatureName:outputFeatureName:modelData:error:];
-[MLAppleWordEmbeddingParameters initWithData:language:inputFeatureName:outputFeatureName:modelData:metadata:error:];
-[MLAppleWordEmbeddingParameters inputFeatureName];
-[MLAppleWordEmbeddingParameters modelParameterData];
-[MLAppleWordEmbeddingParameters outputFeatureName];
-[MLAppleWordEmbeddingParameters setInputFeatureName:];
-[MLAppleWordEmbeddingParameters setModelParameterData:];
-[MLAppleWordEmbeddingParameters setOutputFeatureName:];
```
