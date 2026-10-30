# `MLAppleWordTaggerParameters`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 22 instance methods, 0 class methods

## Instance variables

```
Q _revision;
@"NSString" _language;
@"NSString" _inputFeatureName;
@"NSString" _tokensOutputFeatureName;
@"NSString" _tokenTagsOutputFeatureName;
@"NSString" _tokenLocationsOutputFeatureName;
@"NSString" _tokenLengthsOutputFeatureName;
@"NSData" _modelParameterData;
@"NSArray" _tagNames;
@"NSDictionary" _metadata;
```

## Properties

```
@property (TQ,V_revision) revision;
@property (T@"NSString",&,V_language) language;
@property (T@"NSString",&,V_inputFeatureName) inputFeatureName;
@property (T@"NSString",&,V_tokensOutputFeatureName) tokensOutputFeatureName;
@property (T@"NSString",&,V_tokenTagsOutputFeatureName) tokenTagsOutputFeatureName;
@property (T@"NSString",&,V_tokenLocationsOutputFeatureName) tokenLocationsOutputFeatureName;
@property (T@"NSString",&,V_tokenLengthsOutputFeatureName) tokenLengthsOutputFeatureName;
@property (T@"NSData",&,V_modelParameterData) modelParameterData;
@property (T@"NSArray",&,V_tagNames) tagNames;
@property (T@"NSDictionary",&,V_metadata) metadata;
```

## Instance methods

```
-[MLAppleWordTaggerParameters language];
-[MLAppleWordTaggerParameters revision];
-[MLAppleWordTaggerParameters metadata];
-[MLAppleWordTaggerParameters setMetadata:];
-[MLAppleWordTaggerParameters setLanguage:];
-[MLAppleWordTaggerParameters setRevision:];
-[MLAppleWordTaggerParameters tokenLocationsOutputFeatureName];
-[MLAppleWordTaggerParameters initWithData:language:inputFeatureName:tokensFeatureName:tokenTagsFeatureName:tokenLocationsFeatureName:tokenLengthsFeatureName:modelData:tagNames:error:];
-[MLAppleWordTaggerParameters initWithData:language:inputFeatureName:tokensFeatureName:tokenTagsFeatureName:tokenLocationsFeatureName:tokenLengthsFeatureName:modelData:tagNames:metadata:error:];
-[MLAppleWordTaggerParameters inputFeatureName];
-[MLAppleWordTaggerParameters modelParameterData];
-[MLAppleWordTaggerParameters setInputFeatureName:];
-[MLAppleWordTaggerParameters setModelParameterData:];
-[MLAppleWordTaggerParameters setTagNames:];
-[MLAppleWordTaggerParameters setTokenLengthsOutputFeatureName:];
-[MLAppleWordTaggerParameters setTokenLocationsOutputFeatureName:];
-[MLAppleWordTaggerParameters setTokenTagsOutputFeatureName:];
-[MLAppleWordTaggerParameters setTokensOutputFeatureName:];
-[MLAppleWordTaggerParameters tagNames];
-[MLAppleWordTaggerParameters tokenLengthsOutputFeatureName];
-[MLAppleWordTaggerParameters tokenTagsOutputFeatureName];
-[MLAppleWordTaggerParameters tokensOutputFeatureName];
```
