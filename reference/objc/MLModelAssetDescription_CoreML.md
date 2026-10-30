# `MLModelAssetDescription`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _functionNames;
@"NSDictionary" _modelDescriptionsByFunctionName;
@"NSString" _defaultFunctionNameOrEmptyString;
```

## Properties

```
@property (T@"NSDictionary",R,C,N,V_modelDescriptionsByFunctionName) modelDescriptionsByFunctionName;
@property (T@"NSString",R,C,N,V_defaultFunctionNameOrEmptyString) defaultFunctionNameOrEmptyString;
@property (TB,R,N) usesMultiFunctionSyntax;
@property (T@"NSArray",R,C,N,V_functionNames) functionNames;
@property (T@"MLModelDescription",R,C,N) defaultModelDescription;
@property (T@"NSString",R,C,N) defaultFunctionName;
```

## Instance methods

```
-[MLModelAssetDescription defaultFunctionName];
-[MLModelAssetDescription initFromModelSpecification:];
-[MLModelAssetDescription initWithRawModelDescription:];
-[MLModelAssetDescription assetDescriptionBySettingClassLabels:];
-[MLModelAssetDescription assetDescriptionBySettingClassLabels:functionName:];
-[MLModelAssetDescription initWithModelDescriptionsByFunctionName:functionNames:defaultFunctionName:];
-[MLModelAssetDescription modelDescriptionsByFunctionName];
-[MLModelAssetDescription modelDescriptionOfFunctionNamed:];
-[MLModelAssetDescription initFromModelDescriptionSpecification:];
-[MLModelAssetDescription description];
-[MLModelAssetDescription defaultModelDescription];
-[MLModelAssetDescription defaultFunctionNameOrEmptyString];
-[MLModelAssetDescription functionNames];
-[MLModelAssetDescription usesMultiFunctionSyntax];
-[MLModelAssetDescription initWithModelDescription:];
-[MLModelAssetDescription initWithCompiledModelArchive:error:];
```
