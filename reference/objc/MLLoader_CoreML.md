# `MLLoader`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 0 instance variables, 0 properties, 0 instance methods, 21 class methods

## Class methods

```
+[MLLoader loadModelFromArchive:error:];
+[MLLoader checkAssetPath:error:];
+[MLLoader loadUpdatableModelFromArchive:configuration:error:];
+[MLLoader _findCodedObjectURLInModelArchive:];
+[MLLoader loadModelAssetDescriptionFromArchive:error:];
+[MLLoader _loadUpdatableModelWithClass:fromArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
+[MLLoader _createDecryptSessionForModelAtURL:configuration:decryptSession:loaderEvent:error:];
+[MLLoader _loadModelWithClass:fromArchive:modelVersionInfo:compilerVersionInfo:configuration:error:];
+[MLLoader loadModelFromAssetAtURL:configuration:error:];
+[MLLoader _loadModelAssetDescriptionFromArchive:configuration:modelVersion:compilerVersion:loadingClasses:error:];
+[MLLoader _loadModelFromArchive:configuration:modelVersion:compilerVersion:loaderEvent:useUpdatableModelLoaders:loadingClasses:error:];
+[MLLoader _conformConfiguration:usingModelArchive:];
+[MLLoader _loadWithModelLoaderFromArchive:configuration:loaderEvent:useUpdatableModelLoaders:error:];
+[MLLoader loadUpdatableModelFromAssetAtURL:configuration:error:];
+[MLLoader loadModelAssetDescriptionFromAssetAtURL:error:];
+[MLLoader _populateLoaderAndPredictionEvent:model:configuration:loadTimeDuration:];
+[MLLoader loadModelFromAssetAtURL:error:];
+[MLLoader loadModelFromArchive:configuration:error:];
+[MLLoader _loadModelFromAssetAtURL:configuration:loaderEvent:error:];
+[MLLoader _unarchiveCodedModelObjectAtURL:error:];
+[MLLoader _loadModelFromArchive:configuration:loaderEvent:useUpdatableModelLoaders:error:];
```
