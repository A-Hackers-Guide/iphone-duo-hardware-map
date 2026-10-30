# `CAMSubjectGroupResult`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMMetadataObjectResult`
- 3 instance variables, 10 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"NSString" _uniqueIdentifier;
@"NSArray" _metadataObjects;
q __groupID;
```

## Properties

```
@property (Tq,N,V__groupID) _groupID;
@property (T@"NSArray",R,C,N,V_metadataObjects) metadataObjects;
@property (T@"NSString",R,C,N) metadataType;
@property (T@"NSString",R,C,N,V_uniqueIdentifier) uniqueIdentifier;
@property (T@"AVMetadataObject",R,N) underlyingMetadataObject;
@property (TQ,?,R,N) syntheticFocusMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMSubjectGroupResult _groupID];
-[CAMSubjectGroupResult metadataType];
-[CAMSubjectGroupResult syntheticFocusMode];
-[CAMSubjectGroupResult uniqueIdentifier];
-[CAMSubjectGroupResult description];
-[CAMSubjectGroupResult metadataObjects];
-[CAMSubjectGroupResult initWithMetadataObjects:groupID:];
-[CAMSubjectGroupResult set_groupID:];
-[CAMSubjectGroupResult underlyingMetadataObject];
```
