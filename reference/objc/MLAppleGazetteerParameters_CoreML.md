# `MLAppleGazetteerParameters`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
Q _revision;
@"NSString" _language;
@"NSString" _inputFeatureName;
@"NSString" _outputFeatureName;
@"NSData" _modelParameterData;
@"NSArray" _labelNames;
@"NSDictionary" _metadata;
```

## Properties

```
@property (TQ,V_revision) revision;
@property (T@"NSString",&,V_language) language;
@property (T@"NSString",&,V_inputFeatureName) inputFeatureName;
@property (T@"NSString",&,V_outputFeatureName) outputFeatureName;
@property (T@"NSData",&,V_modelParameterData) modelParameterData;
@property (T@"NSArray",&,V_labelNames) labelNames;
@property (T@"NSDictionary",&,V_metadata) metadata;
```

## Instance methods

```
-[MLAppleGazetteerParameters language];
-[MLAppleGazetteerParameters revision];
-[MLAppleGazetteerParameters metadata];
-[MLAppleGazetteerParameters setMetadata:];
-[MLAppleGazetteerParameters setLanguage:];
-[MLAppleGazetteerParameters setRevision:];
-[MLAppleGazetteerParameters initWithData:language:inputFeatureName:outputFeatureName:modelData:labelNames:metadata:error:];
-[MLAppleGazetteerParameters inputFeatureName];
-[MLAppleGazetteerParameters labelNames];
-[MLAppleGazetteerParameters modelParameterData];
-[MLAppleGazetteerParameters outputFeatureName];
-[MLAppleGazetteerParameters setInputFeatureName:];
-[MLAppleGazetteerParameters setLabelNames:];
-[MLAppleGazetteerParameters setModelParameterData:];
-[MLAppleGazetteerParameters setOutputFeatureName:];
```
