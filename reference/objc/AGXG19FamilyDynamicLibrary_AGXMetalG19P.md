# `AGXG19FamilyDynamicLibrary`

- Image: [`/System/Library/Extensions/AGXMetalG19P.bundle/AGXMetalG19P`](../userland/System__Library__Extensions__AGXMetalG19P.bundle__AGXMetalG19P.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLDynamicLibrary`
- Protocols: `MTLDynamicLibrarySPI`
- 1 instance variables, 20 properties, 10 instance methods, 0 class methods

## Instance variables

```
{shared_ptr<AGX::HAL400::DynamicLibrary>="__ptr_"^{DynamicLibrary}"__cntrl_"^{__shared_weak_count}} _impl;
```

## Properties

```
@property (TQ,R) globalConstantsBase;
@property (TQ,R) globalConstantsSize;
@property (T@"NSObject<OS_dispatch_data>",R) binaryData;
@property (T@"NSObject<OS_dispatch_data>",R) reflectionData;
@property (T@"NSArray",R) exportedFunctions;
@property (T@"NSArray",R) exportedVariables;
@property (T@"NSArray",R) importedSymbols;
@property (T@"NSArray",R) importedLibraries;
@property (T@"NSString",R) libraryPath;
@property (Tr^{?=[32C]},R) libraryUUID;
@property (T@"NSArray",C,N) relocations;
@property (T@"MTLDebugInstrumentationData",&,N) debugInstrumentationData;
@property (TB,R,N) shaderValidationEnabled;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",R) installName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AGXG19FamilyDynamicLibrary binaryUniqueId];
-[AGXG19FamilyDynamicLibrary globalConstantsBase];
-[AGXG19FamilyDynamicLibrary globalConstantsSize];
-[AGXG19FamilyDynamicLibrary initWithLibrary:binaryData:device:error:];
-[AGXG19FamilyDynamicLibrary initWithURL:device:error:];
-[AGXG19FamilyDynamicLibrary initWithURL:device:options:error:];
-[AGXG19FamilyDynamicLibrary initWithBinaryData:name:device:];
-[AGXG19FamilyDynamicLibrary initWithCompilerReply:name:device:];
-[AGXG19FamilyDynamicLibrary initWithLibrary:binaryData:device:globalConstantsTag:error:];
-[AGXG19FamilyDynamicLibrary initWithURL:device:options:globalConstantsTag:error:];
```
