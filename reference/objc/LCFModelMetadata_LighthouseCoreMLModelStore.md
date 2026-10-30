# `LCFModelMetadata`

- Image: [`/System/Library/PrivateFrameworks/LighthouseCoreMLModelStore.framework/LighthouseCoreMLModelStore`](../userland/System__Library__PrivateFrameworks__LighthouseCoreMLModelStore.framework__LighthouseCoreMLModelStore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _isAvailable;
B _isOriginalEmptyModel;
B _isImported;
B _isLocal;
@"NSDate" _dateCreated;
@"NSDate" _dateTrained;
@"NSString" _sha256;
@"NSDictionary" _custom;
```

## Properties

```
@property (TB,N,V_isAvailable) isAvailable;
@property (TB,N,V_isOriginalEmptyModel) isOriginalEmptyModel;
@property (TB,N,V_isImported) isImported;
@property (TB,N,V_isLocal) isLocal;
@property (T@"NSDate",C,N,V_dateCreated) dateCreated;
@property (T@"NSDate",C,N,V_dateTrained) dateTrained;
@property (T@"NSString",C,N,V_sha256) sha256;
@property (T@"NSDictionary",C,N,V_custom) custom;
```

## Instance methods

```
-[LCFModelMetadata toDictionary];
-[LCFModelMetadata dateCreated];
-[LCFModelMetadata isAvailable];
-[LCFModelMetadata isImported];
-[LCFModelMetadata custom];
-[LCFModelMetadata setIsLocal:];
-[LCFModelMetadata sha256];
-[LCFModelMetadata isLocal];
-[LCFModelMetadata init:];
-[LCFModelMetadata setIsAvailable:];
-[LCFModelMetadata setDateCreated:];
-[LCFModelMetadata setCustom:];
-[LCFModelMetadata setSha256:];
-[LCFModelMetadata setDateTrained:];
-[LCFModelMetadata dateTrained];
-[LCFModelMetadata isOriginalEmptyModel];
-[LCFModelMetadata setIsImported:];
-[LCFModelMetadata setIsOriginalEmptyModel:];
```
