# `MLCompiler`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 26 class methods

## Class methods

```
+[MLCompiler contentsOfDirectoryAtURL:error:];
+[MLCompiler encryptFileAtURL:options:error:];
+[MLCompiler _compileSpecification:blobMapping:toArchive:options:error:];
+[MLCompiler _compileSpecificationAtURL:toURL:compiledModelName:overridingModelDescription:options:error:];
+[MLCompiler _loadSpecificationAtURL:to:error:];
+[MLCompiler _updateFeatures:withFeatures:];
+[MLCompiler _updateMetadata:withMetadata:];
+[MLCompiler _updateSpecification:withModelDescription:];
+[MLCompiler addMLProgramToCompiledModelAtURL:error:];
+[MLCompiler addMLProgramToCompiledModelAtURL:withCompilationMode:dryRun:oarchiveForModelCompilation:compilerEvent:error:];
+[MLCompiler canAddMLProgramToCompiledModelAtURL:];
+[MLCompiler compileModelAtURL:toURL:options:error:];
+[MLCompiler compileSpecification:blobMapping:compilerClass:toArchive:options:error:];
+[MLCompiler compileSpecification:blobMapping:toArchive:options:compilerEvent:error:];
+[MLCompiler compileSpecification:blobMapping:toArchive:options:error:];
+[MLCompiler compileSpecification:toArchive:options:error:];
+[MLCompiler compileSpecificationAtURL:toURL:options:error:];
+[MLCompiler compiledVersionForModelAtURL:options:error:];
+[MLCompiler compiledVersionForSpecification:options:error:];
+[MLCompiler compiledVersionForSpecificationAtURL:options:error:];
+[MLCompiler encryptCompiledModelAtURL:options:error:];
+[MLCompiler fillCompilerEvent:withMetadataFromModelAt:error:];
+[MLCompiler fingerprintSpecificationAtURL:toArchive:hash:error:];
+[MLCompiler hashSpecificationAtURL:];
+[MLCompiler storeEncryptionInfoInCompiledArchive:options:error:];
+[MLCompiler versionInfo];
```
