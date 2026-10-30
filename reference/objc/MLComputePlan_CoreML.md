# `MLComputePlan`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 10 instance methods, 3 class methods

## Instance variables

```
@"MLModelStructure" _modelStructure;
@"NSDictionary" _computeDevicesBySupportedComputeUnits;
@"NSDictionary" _executionScheduleByModelStructurePath;
q _modelAssetStorageType;
@"MLModelDescription" _modelDescription;
@"MLModelConfiguration" _configuration;
```

## Properties

```
@property (T@"NSDictionary",R,C,N,V_computeDevicesBySupportedComputeUnits) computeDevicesBySupportedComputeUnits;
@property (T@"NSDictionary",R,C,N,V_executionScheduleByModelStructurePath) executionScheduleByModelStructurePath;
@property (Tq,R,N,V_modelAssetStorageType) modelAssetStorageType;
@property (T@"MLModelDescription",R,N,V_modelDescription) modelDescription;
@property (T@"MLModelConfiguration",R,N,V_configuration) configuration;
@property (T@"MLModelStructure",R,N,V_modelStructure) modelStructure;
```

## Class methods

```
+[MLComputePlan computePlanOfModelStructure:modelAsset:configuration:error:];
+[MLComputePlan loadContentsOfURL:configuration:completionHandler:];
+[MLComputePlan loadModelAsset:configuration:completionHandler:];
```

## Instance methods

```
-[MLComputePlan modelStructure];
-[MLComputePlan configuration];
-[MLComputePlan modelDescription];
-[MLComputePlan computeDeviceUsageForMLProgramOperation:];
-[MLComputePlan computeDeviceUsageForNeuralNetworkLayer:];
-[MLComputePlan computeDevicesBySupportedComputeUnits];
-[MLComputePlan estimatedCostOfMLProgramOperation:];
-[MLComputePlan executionScheduleByModelStructurePath];
-[MLComputePlan initWithModelStructure:modelDescription:modelAssetStorageType:executionSchedule:configuration:];
-[MLComputePlan modelAssetStorageType];
```
