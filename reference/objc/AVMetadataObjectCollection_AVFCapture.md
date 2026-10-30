# `AVMetadataObjectCollection`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 6 instance methods, 1 class methods

## Instance variables

```
{?="value"q"timescale"i"flags"I"epoch"q} _time;
@"NSSet" _metadataObjectTypes;
@"NSSet" _handledMetadataObjectTypes;
@"NSArray" _metadataObjects;
```

## Properties

```
@property (T{?=qiIq},R,V_time) time;
@property (T@"NSSet",R,V_metadataObjectTypes) metadataObjectTypes;
@property (T@"NSSet",R,V_handledMetadataObjectTypes) handledMetadataObjectTypes;
@property (T@"NSArray",R,V_metadataObjects) metadataObjects;
```

## Class methods

```
+[AVMetadataObjectCollection collectionWithTime:metadataObjectTypes:handledMetadataObjectTypes:metadataObjects:];
```

## Instance methods

```
-[AVMetadataObjectCollection dealloc];
-[AVMetadataObjectCollection metadataObjectTypes];
-[AVMetadataObjectCollection time];
-[AVMetadataObjectCollection metadataObjects];
-[AVMetadataObjectCollection handledMetadataObjectTypes];
-[AVMetadataObjectCollection initWithTime:metadataObjectTypes:handledMetadataObjectTypes:metadataObjects:];
```
