# `MTLFunctionDescriptor`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 5 properties, 26 instance methods, 3 class methods

## Instance variables

```
{MTLFunctionDescriptorPrivate="name"@"NSString""specializedName"@"NSString""options"Q"constantValues"@"MTLFunctionConstantValues""binaryArchives"@"NSArray""applyFunctionConstants"B"privateFunctions"@"NSArray"} _private;
Q _pipelineOptions;
@"NSDictionary" _pluginData;
```

## Properties

```
@property (T@"NSString",C,D,N) name;
@property (T@"NSString",C,D,N) specializedName;
@property (T@"MTLFunctionConstantValues",C,D,N) constantValues;
@property (TQ,D,N) options;
@property (T@"NSArray",C,N) binaryArchives;
```

## Class methods

```
+[MTLFunctionDescriptor allocWithZone:];
+[MTLFunctionDescriptor alloc];
+[MTLFunctionDescriptor functionDescriptor];
```

## Instance methods

```
-[MTLFunctionDescriptor setPluginData:];
-[MTLFunctionDescriptor binaryArchives];
-[MTLFunctionDescriptor applyFunctionConstants];
-[MTLFunctionDescriptor setPipelineOptions:];
-[MTLFunctionDescriptor pluginData];
-[MTLFunctionDescriptor setOptions:];
-[MTLFunctionDescriptor formattedDescription:];
-[MTLFunctionDescriptor init];
-[MTLFunctionDescriptor dealloc];
-[MTLFunctionDescriptor setPrivateFunctions:];
-[MTLFunctionDescriptor pipelineOptions];
-[MTLFunctionDescriptor hashStableWithFunction:];
-[MTLFunctionDescriptor setBinaryArchives:];
-[MTLFunctionDescriptor setApplyFunctionConstants:];
-[MTLFunctionDescriptor hash];
-[MTLFunctionDescriptor description];
-[MTLFunctionDescriptor setName:];
-[MTLFunctionDescriptor options];
-[MTLFunctionDescriptor privateFunctions];
-[MTLFunctionDescriptor copyWithZone:];
-[MTLFunctionDescriptor constantValues];
-[MTLFunctionDescriptor setConstantValues:];
-[MTLFunctionDescriptor isEqual:];
-[MTLFunctionDescriptor name];
-[MTLFunctionDescriptor setSpecializedName:];
-[MTLFunctionDescriptor specializedName];
```
