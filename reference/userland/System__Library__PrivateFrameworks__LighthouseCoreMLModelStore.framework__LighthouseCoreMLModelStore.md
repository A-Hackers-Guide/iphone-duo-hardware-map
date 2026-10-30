# `/System/Library/PrivateFrameworks/LighthouseCoreMLModelStore.framework/LighthouseCoreMLModelStore`

iOS 27.2 dyld shared cache image. Version `3.0.0.0.0`. **[DSC]**

## Linked libraries (5)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/CoreML.framework/CoreML`

## Objective-C: 5 classes, 0 protocols, 56 methods, 16 properties

### Class pages

Every class and protocol, with its methods: [`LCFModelMetadata`](../objc/LCFModelMetadata_LighthouseCoreMLModelStore.md), [`LCFModelStore`](../objc/LCFModelStore_LighthouseCoreMLModelStore.md), [`LCFModelStoreModelMetadataProvider`](../objc/LCFModelStoreModelMetadataProvider_LighthouseCoreMLModelStore.md), [`LCFModelStoreUserDefaults`](../objc/LCFModelStoreUserDefaults_LighthouseCoreMLModelStore.md), [`LCFModelStoreUtils`](../objc/LCFModelStoreUtils_LighthouseCoreMLModelStore.md)

### Classes

`LCFModelMetadata`, `LCFModelStore`, `LCFModelStoreModelMetadataProvider`, `LCFModelStoreUserDefaults`, `LCFModelStoreUtils`

### Properties

```
@property (TB,N,V_isAvailable) isAvailable;
@property (TB,N,V_isOriginalEmptyModel) isOriginalEmptyModel;
@property (TB,N,V_isImported) isImported;
@property (TB,N,V_isLocal) isLocal;
@property (T@"NSDate",C,N,V_dateCreated) dateCreated;
@property (T@"NSDate",C,N,V_dateTrained) dateTrained;
@property (T@"NSString",C,N,V_sha256) sha256;
@property (T@"NSDictionary",C,N,V_custom) custom;
@property (T@"NSURL",R,N,V_originalEmptyModelURL) originalEmptyModelURL;
@property (T@"NSURL",R,N,V_modelStoreRootWithKeyURL) modelStoreRootWithKeyURL;
@property (T@"NSString",R,N,V_key) key;
@property (T@"NSURL",R,N,V_modelStoreRootURL) modelStoreRootURL;
@property (T@"NSURL",R,N,V_emptyModelURL) emptyModelURL;
@property (T@"LCFModelStoreModelMetadataProvider",R,N,V_modelMetadataProvider) modelMetadataProvider;
@property (T@"NSURL",R,N,V_modelStoreRootWithKeyURL) modelStoreRootWithKeyURL;
@property (T@"NSURL",R,N,V_metadataPlistFileURL) metadataPlistFileURL;
```

## Strings (40)

```
modelconfig
seteuid to mobile failed.
ModelStoreModelMetadata
custom
/private/var/mobile/Library/Application Support/com.apple.LighthouseCoreMLModelStore
%02x
ModelStore
v8@?0
isOriginalEmptyModel
dateCreated
dateTrained
metadata.plist
com.apple.LighthouseCoreMLModelStore
isAvailable
i
sha256
mobile
/com.apple.LighthouseCoreMLModelStore/
lastTrained
isImported
isLocal
failed to create store directory %@
emptyModel exists in %@
copied model from %@ to %@
a model already exist %@ %@
model config file doesn't exist
failed to delete model url directory %@
failed to copy emptyModel from %@ to %@
copied emptyModel from %@ to %@
sourceModelURL %@ already exists.
get model config to %@
a model does not exist %@ %@
failed to get metadata.
created store directory %@
failed to copy model from %@ to %@
failed to delete store directory %@
failed to write metadata %@
succeeded to write metadata %@
the model name already exists %@ %@
save model config to %@
```
