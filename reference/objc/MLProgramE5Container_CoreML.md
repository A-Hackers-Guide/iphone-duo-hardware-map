# `MLProgramE5Container`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 10 instance methods, 2 class methods

## Instance variables

```
@"MLModelAssetDescription" _modelAssetDescription;
@"MLCompilerNeuralNetworkOutput" _compilerOutput;
@"NSURL" _URLOfMILText;
@"MLVersionInfo" _compilerVersionInfo;
@"MLVersionInfo" _modelVersionInfo;
@"NSArray" _functionInfoArray;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_functionInfoArray) functionInfoArray;
@property (T@"MLModelAssetDescription",R,C,N,V_modelAssetDescription) modelAssetDescription;
@property (T@"MLCompilerNeuralNetworkOutput",R,N,V_compilerOutput) compilerOutput;
@property (T@"NSURL",R,C,N,V_URLOfMILText) URLOfMILText;
@property (T@"MLVersionInfo",R,N,V_compilerVersionInfo) compilerVersionInfo;
@property (T@"MLVersionInfo",R,N,V_modelVersionInfo) modelVersionInfo;
```

## Class methods

```
+[MLProgramE5Container _getDefaultFunctionName:modelDescription:fromModelAssetDescription:];
+[MLProgramE5Container deduceFunctionNameToCompute:modelDescription:fromConfiguration:modelAssetDescription:error:];
```

## Instance methods

```
-[MLProgramE5Container findPrecompiledE5BundleAndReturnError:];
-[MLProgramE5Container compilerOutput];
-[MLProgramE5Container modelAssetDescription];
-[MLProgramE5Container URLOfMILText];
-[MLProgramE5Container optionalInputDefaultValuesForFunctionNamed:];
-[MLProgramE5Container functionInfoArray];
-[MLProgramE5Container modelVersionInfo];
-[MLProgramE5Container compilerVersionInfo];
-[MLProgramE5Container initWithCompiledArchive:modelVersionInfo:compilerVersionInfo:error:];
-[MLProgramE5Container classScoreVectorNameOfFunctionNamed:];
```
