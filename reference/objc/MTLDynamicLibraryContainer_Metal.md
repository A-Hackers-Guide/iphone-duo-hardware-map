# `MTLDynamicLibraryContainer`

- Image: [`/System/Library/Frameworks/Metal.framework/Metal`](../userland/System__Library__Frameworks__Metal.framework__Metal.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"MTLLoadedFile" _fileMapping;
@"<MTLDevice>" _device;
@"NSObject<OS_dispatch_data>" _vendorData;
@"NSObject<OS_dispatch_data>" _reflectionData;
@"NSArray" _exportedFunctions;
@"NSArray" _exportedVariables;
@"NSArray" _importedSymbols;
@"NSArray" _importedLibraries;
@"NSString" _installName;
@"NSData" _airData;
Q _bitcodeOffset;
Q _bitcodeSize;
Q _airOffset;
Q _airSize;
Q _reflectionOffset;
I _reflectionSize;
I _uncompressedReflectionSize;
i _airVersion;
{?="key"[32C]} _libraryUUID;
@"MTLDebugInstrumentationData" _debugInstrumentationData;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _reflectionDataLock;
```

## Instance methods

```
-[MTLDynamicLibraryContainer dealloc];
-[MTLDynamicLibraryContainer release];
-[MTLDynamicLibraryContainer reflectionData];
-[MTLDynamicLibraryContainer serializeToURL:options:error:];
-[MTLDynamicLibraryContainer airData];
-[MTLDynamicLibraryContainer initReflectionData];
-[MTLDynamicLibraryContainer initWithLibrary:binaryData:device:error:];
-[MTLDynamicLibraryContainer initWithURL:device:options:error:];
```
