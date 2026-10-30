# `MLModelAsset`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 11 properties, 28 instance methods, 16 class methods

## Instance variables

```
@"MLModelAssetResourceFactory" _resourceFactory;
@"MLModelAssetDescriptionVendor" _descriptionVendor;
@"MLModelAssetModelVendor" _modelVendor;
@"MLModelAssetModelStructureVendor" _structureVendor;
@"MLModelConfiguration" _lastConfiguration;
@"NSDictionary" _archiveData;
```

## Properties

```
@property (T@"MLModelAssetResourceFactory",R,N,V_resourceFactory) resourceFactory;
@property (T@"MLModelAssetDescriptionVendor",R,N,V_descriptionVendor) descriptionVendor;
@property (T@"MLModelAssetModelVendor",R,N,V_modelVendor) modelVendor;
@property (T@"MLModelAssetModelStructureVendor",R,N,V_structureVendor) structureVendor;
@property (T@"MLModelConfiguration",C,N,V_lastConfiguration) lastConfiguration;
@property (T@"NSDictionary",&,N,V_archiveData) archiveData;
@property (T@"NSURL",R) compiledURL;
@property (T@"NSURL",R,C,N) compiledModelURL;
@property (T@"MLModel",R,N) model;
@property (T@"<MLRegressor>",R,N) regressor;
@property (T@"<MLClassifier>",R,N) classifier;
```

## Class methods

```
+[MLModelAsset _modelAssetWithSpecificationData:blobMapping:error:];
+[MLModelAsset fetchNetworkURLFromCompiledModelAtURL:error:];
+[MLModelAsset isANESupported];
+[MLModelAsset modelAssetDataByLoadingBlobFileReferencesInModelSpecificationAtURL:blobMapping:error:];
+[MLModelAsset modelAssetDataByResolvingBlobFileReferencesIntoInMemoryValuesInModelSpecificationAtURL:error:];
+[MLModelAsset modelAssetWithSpecification:compilerOptions:error:];
+[MLModelAsset modelAssetWithSpecification:error:];
+[MLModelAsset modelAssetWithSpecificationData:blobMapping:error:];
+[MLModelAsset modelAssetWithSpecificationData:error:];
+[MLModelAsset modelAssetWithSpecificationURL:compilerOptions:error:];
+[MLModelAsset modelAssetWithSpecificationURL:error:];
+[MLModelAsset modelAssetWithURL:configuration:error:];
+[MLModelAsset modelAssetWithURL:error:];
+[MLModelAsset needsANECompilationForModelAtURL:result:error:];
+[MLModelAsset purgeANEBinaryForModelAtURL:error:];
+[MLModelAsset purgeANEIRForModelAtURL:error:];
```

## Instance methods

```
-[MLModelAsset regressor];
-[MLModelAsset classifier];
-[MLModelAsset model];
-[MLModelAsset compiledModelURL];
-[MLModelAsset functionNamesWithCompletionHandler:];
-[MLModelAsset storageType];
-[MLModelAsset modelDescriptionOfFunctionNamed:completionHandler:];
-[MLModelAsset initWithArchiveData:];
-[MLModelAsset modelWithError:];
-[MLModelAsset initWithResourceFactory:configuration:];
-[MLModelAsset lastConfiguration];
-[MLModelAsset initWithURL:configuration:error:];
-[MLModelAsset compiledURL];
-[MLModelAsset setLastConfiguration:];
-[MLModelAsset regressorWithError:];
-[MLModelAsset initWithURL:error:];
-[MLModelAsset resourceFactory];
-[MLModelAsset load:];
-[MLModelAsset modelStructureWithCompletionHandler:];
-[MLModelAsset archiveData];
-[MLModelAsset description];
-[MLModelAsset modelVendor];
-[MLModelAsset setArchiveData:];
-[MLModelAsset descriptionVendor];
-[MLModelAsset classifierWithError:];
-[MLModelAsset modelDescriptionWithCompletionHandler:];
-[MLModelAsset structureVendor];
-[MLModelAsset modelWithConfiguration:error:];
```
