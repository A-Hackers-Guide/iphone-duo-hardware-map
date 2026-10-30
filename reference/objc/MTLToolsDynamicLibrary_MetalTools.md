# `MTLToolsDynamicLibrary`

- Image: [`/System/Library/PrivateFrameworks/MetalTools.framework/MetalTools`](../userland/System__Library__PrivateFrameworks__MetalTools.framework__MetalTools.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MTLToolsObject`
- Protocols: `MTLDynamicLibrarySPI`
- 1 instance variables, 20 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _relocations;
```

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
-[MTLToolsDynamicLibrary setRelocations:];
-[MTLToolsDynamicLibrary formattedDescription:];
-[MTLToolsDynamicLibrary device];
-[MTLToolsDynamicLibrary label];
-[MTLToolsDynamicLibrary importedLibraries];
-[MTLToolsDynamicLibrary setLabel:];
-[MTLToolsDynamicLibrary dealloc];
-[MTLToolsDynamicLibrary setDebugInstrumentationData:];
-[MTLToolsDynamicLibrary libraryPath];
-[MTLToolsDynamicLibrary installName];
-[MTLToolsDynamicLibrary reflectionData];
-[MTLToolsDynamicLibrary shaderValidationEnabled];
-[MTLToolsDynamicLibrary serializeToURL:error:];
-[MTLToolsDynamicLibrary debugInstrumentationData];
-[MTLToolsDynamicLibrary relocations];
-[MTLToolsDynamicLibrary importedSymbols];
-[MTLToolsDynamicLibrary serializeToURL:options:error:];
-[MTLToolsDynamicLibrary binaryData];
-[MTLToolsDynamicLibrary exportedFunctions];
-[MTLToolsDynamicLibrary exportedVariables];
-[MTLToolsDynamicLibrary globalConstantsBase];
-[MTLToolsDynamicLibrary globalConstantsSize];
-[MTLToolsDynamicLibrary libraryUUID];
```
