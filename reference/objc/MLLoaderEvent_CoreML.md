# `MLLoaderEvent`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUTCoreAnalyticsMetric`
- 21 instance variables, 27 properties, 46 instance methods, 0 class methods

## Instance variables

```
@"NSNumber" _modelType;
@"NSNumber" _modelLoadTime;
@"NSString" _modelVersion;
@"NSString" _compilerVersion;
@"NSNumber" _computeUnits;
@"NSNumber" _modelOrigin;
@"NSNumber" _modelLoadError;
@"NSString" _bundleIdentifier;
@"NSString" _modelName;
@"NSNumber" _firstPartyExecutable;
@"NSNumber" _modelIsEncrypted;
@"NSNumber" _modelProgramValidationError;
@"NSNumber" _modelProgramParsingError;
@"NSNumber" _modelEngineType;
@"NSString" _processName;
@"NSNumber" _containsCustomLayer;
@"NSString" _modelHash;
@"NSString" _nnModelNetHash;
@"NSString" _nnModelShapeHash;
@"NSString" _nnModelWeightsHash;
@"NSNumber" _modelDimension;
```

## Properties

```
@property (T@"NSString",C,N,V_modelHash) modelHash;
@property (T@"NSString",C,N,V_nnModelNetHash) nnModelNetHash;
@property (T@"NSString",C,N,V_nnModelShapeHash) nnModelShapeHash;
@property (T@"NSString",C,N,V_nnModelWeightsHash) nnModelWeightsHash;
@property (T@"NSNumber",C,N,V_modelDimension) modelDimension;
@property (T@"NSNumber",C,N,V_modelType) modelType;
@property (T@"NSNumber",C,N,V_modelLoadTime) modelLoadTime;
@property (T@"NSString",C,N,V_modelVersion) modelVersion;
@property (T@"NSString",C,N,V_compilerVersion) compilerVersion;
@property (T@"NSNumber",C,N,V_computeUnits) computeUnits;
@property (T@"NSNumber",C,N,V_modelOrigin) modelOrigin;
@property (T@"NSNumber",C,N,V_modelLoadError) modelLoadError;
@property (T@"NSString",C,N,V_bundleIdentifier) bundleIdentifier;
@property (T@"NSString",C,N,V_modelName) modelName;
@property (T@"NSNumber",C,N,V_firstPartyExecutable) firstPartyExecutable;
@property (T@"NSNumber",C,N,V_modelIsEncrypted) modelIsEncrypted;
@property (T@"NSNumber",C,N,V_modelProgramValidationError) modelProgramValidationError;
@property (T@"NSNumber",C,N,V_modelProgramParsingError) modelProgramParsingError;
@property (T@"NSNumber",C,N,V_modelEngineType) modelEngineType;
@property (T@"NSString",C,N,V_processName) processName;
@property (T@"NSNumber",C,N,V_containsCustomLayer) containsCustomLayer;
@property (T@"NSDictionary",R) dictionaryRepresentation;
@property (T@"NSString",R) name;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MLLoaderEvent setProcessName:];
-[MLLoaderEvent modelVersion];
-[MLLoaderEvent setModelIsEncrypted:];
-[MLLoaderEvent computeUnits];
-[MLLoaderEvent firstPartyExecutable];
-[MLLoaderEvent modelDimension];
-[MLLoaderEvent extractAndSetModelDetailsFromArchive:];
-[MLLoaderEvent setComputeUnits:];
-[MLLoaderEvent modelHash];
-[MLLoaderEvent modelOrigin];
-[MLLoaderEvent setContainsCustomLayer:];
-[MLLoaderEvent modelProgramValidationError];
-[MLLoaderEvent compilerVersion];
-[MLLoaderEvent modelEngineType];
-[MLLoaderEvent nnModelNetHash];
-[MLLoaderEvent setModelLoadTime:];
-[MLLoaderEvent setModelDimension:];
-[MLLoaderEvent setCompilerVersion:];
-[MLLoaderEvent setFirstPartyExecutable:];
-[MLLoaderEvent setNnModelShapeHash:];
-[MLLoaderEvent bundleIdentifier];
-[MLLoaderEvent containsCustomLayer];
-[MLLoaderEvent setModelVersion:];
-[MLLoaderEvent modelLoadTime];
-[MLLoaderEvent setModelEngineType:];
-[MLLoaderEvent setModelOrigin:];
-[MLLoaderEvent setModelHash:];
-[MLLoaderEvent setModelProgramValidationError:];
-[MLLoaderEvent setNnModelNetHash:];
-[MLLoaderEvent modelLoadError];
-[MLLoaderEvent setModelProgramParsingError:];
-[MLLoaderEvent processName];
-[MLLoaderEvent setModelName:];
-[MLLoaderEvent nnModelWeightsHash];
-[MLLoaderEvent nnModelShapeHash];
-[MLLoaderEvent modelType];
-[MLLoaderEvent modelIsEncrypted];
-[MLLoaderEvent numberFromCString:];
-[MLLoaderEvent setBundleIdentifier:];
-[MLLoaderEvent setModelLoadError:];
-[MLLoaderEvent name];
-[MLLoaderEvent setNnModelWeightsHash:];
-[MLLoaderEvent modelProgramParsingError];
-[MLLoaderEvent modelName];
-[MLLoaderEvent dictionaryRepresentation];
-[MLLoaderEvent setModelType:];
```
