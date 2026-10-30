# `MPSGraphExecutableSerializationDescriptor`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 9 instance variables, 8 properties, 20 instance methods, 1 class methods

## Instance variables

```
B _userSetMinimumDeploymentTarget;
@"NSString" _minimumDeploymentTarget;
B _disableNDX;
B _append;
B _serializeOriginalModule;
B _applyGenericThinning;
B _serializeResourcesBin;
B _serializeReflectionFb;
Q _deploymentPlatform;
```

## Properties

```
@property (TB,V_disableNDX) disableNDX;
@property (TB,V_serializeOriginalModule) serializeOriginalModule;
@property (TB,V_applyGenericThinning) applyGenericThinning;
@property (TB,V_serializeResourcesBin) serializeResourcesBin;
@property (TB,V_serializeReflectionFb) serializeReflectionFb;
@property (TB,V_append) append;
@property (TQ,V_deploymentPlatform) deploymentPlatform;
@property (T@"NSString",C) minimumDeploymentTarget;
```

## Class methods

```
+[MPSGraphExecutableSerializationDescriptor validateMinimumDeploymentTargetVersion:forPlatform:];
```

## Instance methods

```
-[MPSGraphExecutableSerializationDescriptor deploymentPlatform];
-[MPSGraphExecutableSerializationDescriptor init];
-[MPSGraphExecutableSerializationDescriptor setDeploymentPlatform:];
-[MPSGraphExecutableSerializationDescriptor append];
-[MPSGraphExecutableSerializationDescriptor applyGenericThinning];
-[MPSGraphExecutableSerializationDescriptor disableNDX];
-[MPSGraphExecutableSerializationDescriptor getDeploymentTargetAsOSVersion];
-[MPSGraphExecutableSerializationDescriptor getPackageVersionString];
-[MPSGraphExecutableSerializationDescriptor getUserSetMinimumDeploymentTarget];
-[MPSGraphExecutableSerializationDescriptor minimumDeploymentTarget];
-[MPSGraphExecutableSerializationDescriptor serializeOriginalModule];
-[MPSGraphExecutableSerializationDescriptor serializeReflectionFb];
-[MPSGraphExecutableSerializationDescriptor serializeResourcesBin];
-[MPSGraphExecutableSerializationDescriptor setAppend:];
-[MPSGraphExecutableSerializationDescriptor setApplyGenericThinning:];
-[MPSGraphExecutableSerializationDescriptor setDisableNDX:];
-[MPSGraphExecutableSerializationDescriptor setMinimumDeploymentTarget:];
-[MPSGraphExecutableSerializationDescriptor setSerializeOriginalModule:];
-[MPSGraphExecutableSerializationDescriptor setSerializeReflectionFb:];
-[MPSGraphExecutableSerializationDescriptor setSerializeResourcesBin:];
```
