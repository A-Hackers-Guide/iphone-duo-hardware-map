# `MTLLegacySVDynamicLibrary`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsDynamicLibrary`
- Protocols: `MTLDynamicLibrarySPI`
- 1 instance variables, 21 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"MTLLegacySVImageData" _imageData;
```

## Properties

```
@property (T@"MTLLegacySVImageData",R,N,V_imageData) imageData;
@property (T@"NSObject<OS_dispatch_data>",R) binaryData;
@property (T@"NSObject<OS_dispatch_data>",R) reflectionData;
@property (T@"NSArray",R) exportedFunctions;
@property (T@"NSArray",R) exportedVariables;
@property (T@"NSArray",R) importedSymbols;
@property (T@"NSArray",R) importedLibraries;
@property (T@"NSString",R) libraryPath;
@property (Tr^{?=[32C]},R) libraryUUID;
@property (TQ,R) globalConstantsBase;
@property (TQ,R) globalConstantsSize;
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
-[MTLLegacySVDynamicLibrary imageData];
-[MTLLegacySVDynamicLibrary dealloc];
-[MTLLegacySVDynamicLibrary prepareForUsage];
-[MTLLegacySVDynamicLibrary initWithDynamicLibrary:device:];
```
