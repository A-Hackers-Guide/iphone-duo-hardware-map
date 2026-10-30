# `_ANEVirtualModel`

- Image: [`/System/Library/PrivateFrameworks/ParavirtualizedANE.framework/ParavirtualizedANE`](../userland/System__Library__PrivateFrameworks__ParavirtualizedANE.framework__ParavirtualizedANE.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 19 instance methods, 5 class methods

## Instance variables

```
@"_ANEModel" _model;
@"NSString" _tmpModelFilesPath;
@"NSString" _tmpWeightFilesPath;
@"NSURL" _modelURLFromGuest;
@"NSMutableDictionary" _mutableWeightsMappings;
@"_ANEProgramForEvaluation" _baseKeeperProgram;
q _refcount;
```

## Properties

```
@property (Tq,N,V_refcount) refcount;
@property (T@"_ANEModel",&,N,V_model) model;
@property (T@"NSString",&,N,V_tmpModelFilesPath) tmpModelFilesPath;
@property (T@"NSString",&,N,V_tmpWeightFilesPath) tmpWeightFilesPath;
@property (T@"NSURL",&,N,V_modelURLFromGuest) modelURLFromGuest;
@property (T@"NSMutableDictionary",&,N,V_mutableWeightsMappings) mutableWeightsMappings;
@property (T@"_ANEProgramForEvaluation",&,N,V_baseKeeperProgram) baseKeeperProgram;
```

## Class methods

```
+[_ANEVirtualModel initialize];
+[_ANEVirtualModel new];
+[_ANEVirtualModel objectWithModel:];
+[_ANEVirtualModel objectWithModel:tmpModelFilesPath:tmpWeightFilesPath:];
+[_ANEVirtualModel objectWithModel:tmpModelFilesPath:tmpWeightFilesPath:modelURLFromGuest:];
```

## Instance methods

```
-[_ANEVirtualModel model];
-[_ANEVirtualModel setModel:];
-[_ANEVirtualModel init];
-[_ANEVirtualModel addCachedReference];
-[_ANEVirtualModel baseKeeperProgram];
-[_ANEVirtualModel initWithModel:tmpModelFilesPath:tmpWeightFilesPath:modelURLFromGuest:];
-[_ANEVirtualModel modelURLFromGuest];
-[_ANEVirtualModel mutableWeightsMappings];
-[_ANEVirtualModel refcount];
-[_ANEVirtualModel removeCachedReference];
-[_ANEVirtualModel setBaseKeeperProgram:];
-[_ANEVirtualModel setModelURLFromGuest:];
-[_ANEVirtualModel setMutableWeightsMappings:];
-[_ANEVirtualModel setRefcount:];
-[_ANEVirtualModel setTmpModelFilesPath:];
-[_ANEVirtualModel setTmpWeightFilesPath:];
-[_ANEVirtualModel tmpModelFilesPath];
-[_ANEVirtualModel tmpWeightFilesPath];
-[_ANEVirtualModel updateTmpWeightFilesPath:];
```
