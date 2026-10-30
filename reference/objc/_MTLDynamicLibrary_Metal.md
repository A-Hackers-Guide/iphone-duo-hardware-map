# `_MTLDynamicLibrary`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_MTLObjectWithLabel`
- Protocols: `MTLDynamicLibrarySPI`
- 4 instance variables, 20 properties, 25 instance methods, 1 class methods

## Instance variables

```
@"NSString" _libraryPath;
@"MTLDynamicLibraryContainer" _container;
@"NSArray" _relocations;
B _shaderValidationEnabled;
```

## Properties

```
@property (T@"NSArray",C,N,V_relocations) relocations;
@property (T@"MTLDebugInstrumentationData",&,N) debugInstrumentationData;
@property (TB,R,N,V_shaderValidationEnabled) shaderValidationEnabled;
@property (T@"NSObject<OS_dispatch_data>",R) binaryData;
@property (T@"NSObject<OS_dispatch_data>",R) reflectionData;
@property (T@"NSArray",R) exportedFunctions;
@property (T@"NSArray",R) exportedVariables;
@property (T@"NSArray",R) importedSymbols;
@property (T@"NSArray",R) importedLibraries;
@property (T@"NSString",R,V_libraryPath) libraryPath;
@property (Tr^{?=[32C]},R) libraryUUID;
@property (TQ,R) globalConstantsBase;
@property (TQ,R) globalConstantsSize;
@property (T@"NSString",C) label;
@property (T@"<MTLDevice>",R) device;
@property (T@"NSString",R) installName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_MTLDynamicLibrary dynamicLibraryTypeAtURL:device:error:];
```

## Instance methods

```
-[_MTLDynamicLibrary setRelocations:];
-[_MTLDynamicLibrary formattedDescription:];
-[_MTLDynamicLibrary device];
-[_MTLDynamicLibrary importedLibraries];
-[_MTLDynamicLibrary dealloc];
-[_MTLDynamicLibrary setDebugInstrumentationData:];
-[_MTLDynamicLibrary libraryPath];
-[_MTLDynamicLibrary installName];
-[_MTLDynamicLibrary reflectionData];
-[_MTLDynamicLibrary shaderValidationEnabled];
-[_MTLDynamicLibrary description];
-[_MTLDynamicLibrary serializeToURL:error:];
-[_MTLDynamicLibrary debugInstrumentationData];
-[_MTLDynamicLibrary relocations];
-[_MTLDynamicLibrary importedSymbols];
-[_MTLDynamicLibrary serializeToURL:options:error:];
-[_MTLDynamicLibrary container];
-[_MTLDynamicLibrary binaryData];
-[_MTLDynamicLibrary airData];
-[_MTLDynamicLibrary exportedFunctions];
-[_MTLDynamicLibrary exportedVariables];
-[_MTLDynamicLibrary initWithLibrary:binaryData:device:error:];
-[_MTLDynamicLibrary initWithURL:device:error:];
-[_MTLDynamicLibrary initWithURL:device:options:error:];
-[_MTLDynamicLibrary libraryUUID];
```
