# `_InMemoryArchiveReader`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_ArchiveReader`
- 2 instance variables, 6 properties, 6 instance methods, 2 class methods

## Instance variables

```
{shared_ptr<Espresso::net>="__ptr_"^{net}"__cntrl_"^{__shared_weak_count}} _network;
@"NSArray" _layerInfos;
```

## Properties

```
@property (T@"NSString",R,C,N) modelPath;
@property (T@"NSArray",R,N,V_layerInfos) layerInfos;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_InMemoryArchiveReader modelName];
+[_InMemoryArchiveReader readerFromArchiver:error:];
```

## Instance methods

```
-[_InMemoryArchiveReader copyLayerShapesToContainer:];
-[_InMemoryArchiveReader modelPath];
-[_InMemoryArchiveReader loadUpdatableParams:];
-[_InMemoryArchiveReader initWithNetwork:];
-[_InMemoryArchiveReader layerInfos];
-[_InMemoryArchiveReader transformParams];
```
