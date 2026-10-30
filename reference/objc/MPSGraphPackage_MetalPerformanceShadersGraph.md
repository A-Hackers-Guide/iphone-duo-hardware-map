# `MPSGraphPackage`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `MPSGraphObject`
- 7 instance variables, 0 properties, 16 instance methods, 2 class methods

## Instance variables

```
@"NSURL" _packageURL;
@"NSURL" _temporaryPackageURL;
@"NSFileManager" _fileManager;
@"NSMutableDictionary" _plistRoot;
@"NSMutableDictionary" _perExtensionFileCounts;
{unique_ptr<llvm::LockFileManager, std::default_delete<llvm::LockFileManager>>=""{?="__ptr_"^{LockFileManager}}} _temporaryPackageFileLock;
{unique_ptr<InProcessPackageWritingGuard::LockGuard, std::default_delete<InProcessPackageWritingGuard::LockGuard>>=""{?="__ptr_"^{LockGuard}}} _writingLockGuard;
```

## Class methods

```
+[MPSGraphPackage getResourceFileName];
+[MPSGraphPackage readResources:fromURL:error:usingAllocator:];
```

## Instance methods

```
-[MPSGraphPackage commonInit];
-[MPSGraphPackage initWithSourcePackageURL:error:];
-[MPSGraphPackage writeResources:];
-[MPSGraphPackage addBinaryResourceFile:withFileType:toBinaryResourceFileDict:];
-[MPSGraphPackage copyDataFiles:currentBasePath:location:];
-[MPSGraphPackage createBytecodeFromMlirModule:fileHandle:resourceStorageMode:];
-[MPSGraphPackage createMLIRFileHandle:];
-[MPSGraphPackage createVersionedBytecodeFromMlirModule:packageKey:fileHandle:resourceStorageMode:downgradedModuleCallback:];
-[MPSGraphPackage findLatestPackage];
-[MPSGraphPackage findLatestPackageKey];
-[MPSGraphPackage getMLIRLibrary];
-[MPSGraphPackage getPackageKeyForPlatform:andMinimumDeploymentTarget:];
-[MPSGraphPackage getPlistData];
-[MPSGraphPackage initWithPackageURL:temporaryPackageURL:append:];
-[MPSGraphPackage initWithSourcePackageURL:];
-[MPSGraphPackage setMLIRLibrary:withPackageKey:];
```
