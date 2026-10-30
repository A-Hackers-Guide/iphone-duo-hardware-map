# `_OnDiskArchiveReader`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_ArchiveReader`
- 4 instance variables, 8 properties, 8 instance methods, 5 class methods

## Instance variables

```
@"NSArray" _layerInfos;
@"NSString" _modelPath;
@"NSDictionary" _netJson;
@"NSDictionary" _shapeJson;
```

## Properties

```
@property (T@"NSDictionary",R,C,N,V_netJson) netJson;
@property (T@"NSDictionary",R,C,N,V_shapeJson) shapeJson;
@property (T@"NSString",R,C,N,V_modelPath) modelPath;
@property (T@"NSArray",R,N,V_layerInfos) layerInfos;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_OnDiskArchiveReader modelName];
+[_OnDiskArchiveReader modelNetFileName];
+[_OnDiskArchiveReader modelShapeFileName];
+[_OnDiskArchiveReader parseCompiledNetworkBlobWithName:archive:error:];
+[_OnDiskArchiveReader readerFromArchiver:error:];
```

## Instance methods

```
-[_OnDiskArchiveReader shapeJson];
-[_OnDiskArchiveReader copyLayerShapesToContainer:];
-[_OnDiskArchiveReader modelPath];
-[_OnDiskArchiveReader netJson];
-[_OnDiskArchiveReader initWithNetJson:shapeJson:modelPath:];
-[_OnDiskArchiveReader loadUpdatableParams:];
-[_OnDiskArchiveReader layerInfos];
-[_OnDiskArchiveReader transformParams];
```
