# `MetalPackage`

- Image: [`/System/Library/Frameworks/MetalPerformanceShadersGraph.framework/MetalPerformanceShadersGraph`](../userland/System__Library__Frameworks__MetalPerformanceShadersGraph.framework__MetalPerformanceShadersGraph.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"NSURL" _packageURL;
@"NSURL" _temporaryPackageURL;
@"NSFileManager" _fileManager;
@"NSJSONSerialization" _jsonSerializer;
B _ml;
{unique_ptr<llvm::LockFileManager, std::default_delete<llvm::LockFileManager>>=""{?="__ptr_"^{LockFileManager}}} _temporaryPackageFileLock;
{unique_ptr<InProcessPackageWritingGuard::LockGuard, std::default_delete<InProcessPackageWritingGuard::LockGuard>>=""{?="__ptr_"^{LockGuard}}} _writingLockGuard;
```

## Instance methods

```
-[MetalPackage getJsonData];
-[MetalPackage initWithPackageURL:temporaryPackageURL:];
```
