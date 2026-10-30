# `MTLShaderValidationConfiguration`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 10 instance variables, 10 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _enableBoundsChecking;
B _enableThreadgroupMemoryChecks;
B _enableTextureChecks;
B _enableResourceUsageValidation;
B _enableStackOverflow;
B _enableAddressSpaceValidation;
B _enableTensorValidation;
B _enableNumericsChecks;
B _enableAccelerationStructureChecks;
B _enableYieldChecks;
```

## Properties

```
@property (TB,V_enableBoundsChecking) enableBoundsChecking;
@property (TB,V_enableThreadgroupMemoryChecks) enableThreadgroupMemoryChecks;
@property (TB,V_enableTextureChecks) enableTextureChecks;
@property (TB,V_enableResourceUsageValidation) enableResourceUsageValidation;
@property (TB,V_enableStackOverflow) enableStackOverflow;
@property (TB,V_enableAddressSpaceValidation) enableAddressSpaceValidation;
@property (TB,V_enableTensorValidation) enableTensorValidation;
@property (TB,V_enableNumericsChecks) enableNumericsChecks;
@property (TB,V_enableAccelerationStructureChecks) enableAccelerationStructureChecks;
@property (TB,V_enableYieldChecks) enableYieldChecks;
```

## Instance methods

```
-[MTLShaderValidationConfiguration init];
-[MTLShaderValidationConfiguration hash];
-[MTLShaderValidationConfiguration copyWithZone:];
-[MTLShaderValidationConfiguration isEqual:];
-[MTLShaderValidationConfiguration enableAccelerationStructureChecks];
-[MTLShaderValidationConfiguration enableAddressSpaceValidation];
-[MTLShaderValidationConfiguration enableBoundsChecking];
-[MTLShaderValidationConfiguration enableNumericsChecks];
-[MTLShaderValidationConfiguration enableResourceUsageValidation];
-[MTLShaderValidationConfiguration enableStackOverflow];
-[MTLShaderValidationConfiguration enableTensorValidation];
-[MTLShaderValidationConfiguration enableTextureChecks];
-[MTLShaderValidationConfiguration enableThreadgroupMemoryChecks];
-[MTLShaderValidationConfiguration enableYieldChecks];
-[MTLShaderValidationConfiguration isShaderValidationEnabled];
-[MTLShaderValidationConfiguration setEnableAccelerationStructureChecks:];
-[MTLShaderValidationConfiguration setEnableAddressSpaceValidation:];
-[MTLShaderValidationConfiguration setEnableBoundsChecking:];
-[MTLShaderValidationConfiguration setEnableNumericsChecks:];
-[MTLShaderValidationConfiguration setEnableResourceUsageValidation:];
-[MTLShaderValidationConfiguration setEnableStackOverflow:];
-[MTLShaderValidationConfiguration setEnableTensorValidation:];
-[MTLShaderValidationConfiguration setEnableTextureChecks:];
-[MTLShaderValidationConfiguration setEnableThreadgroupMemoryChecks:];
-[MTLShaderValidationConfiguration setEnableYieldChecks:];
```
