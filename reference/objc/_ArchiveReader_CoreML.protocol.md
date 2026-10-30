# `_ArchiveReader` (protocol)

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 5 instance methods, 1 class methods

## Properties

```
@property (T@"NSString",R,C,N) modelPath;
@property (T@"NSArray",R,N) layerInfos;
```

## Class methods

```
+[_ArchiveReader modelName];
```

## Instance methods

```
-[_ArchiveReader copyLayerShapesToContainer:];
-[_ArchiveReader modelPath];
-[_ArchiveReader loadUpdatableParams:];
-[_ArchiveReader layerInfos];
-[_ArchiveReader transformParams];
```
