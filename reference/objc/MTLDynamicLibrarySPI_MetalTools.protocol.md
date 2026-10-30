# `MTLDynamicLibrarySPI` (protocol)

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `MTLDynamicLibrary`
- 0 instance variables, 13 properties, 17 instance methods, 0 class methods

## Properties

```
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
```

## Instance methods

```
-[MTLDynamicLibrarySPI setRelocations:];
-[MTLDynamicLibrarySPI formattedDescription:];
-[MTLDynamicLibrarySPI importedLibraries];
-[MTLDynamicLibrarySPI setDebugInstrumentationData:];
-[MTLDynamicLibrarySPI libraryPath];
-[MTLDynamicLibrarySPI reflectionData];
-[MTLDynamicLibrarySPI shaderValidationEnabled];
-[MTLDynamicLibrarySPI debugInstrumentationData];
-[MTLDynamicLibrarySPI relocations];
-[MTLDynamicLibrarySPI importedSymbols];
-[MTLDynamicLibrarySPI serializeToURL:options:error:];
-[MTLDynamicLibrarySPI binaryData];
-[MTLDynamicLibrarySPI exportedFunctions];
-[MTLDynamicLibrarySPI exportedVariables];
-[MTLDynamicLibrarySPI globalConstantsBase];
-[MTLDynamicLibrarySPI globalConstantsSize];
-[MTLDynamicLibrarySPI libraryUUID];
```
