# `BKSDisplayTraits`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`, `NSSecureCoding`, `BSDescriptionStreamable`, `BSProtobufSerializable`, `BKSDisplayTraitsProviding`
- 1 instance variables, 5 properties, 11 instance methods, 5 class methods

## Instance variables

```
i _surfaceType;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Ti,R,N) surfaceType;
```

## Class methods

```
+[BKSDisplayTraits build:];
+[BKSDisplayTraits supportsSecureCoding];
+[BKSDisplayTraits protobufSchema];
+[BKSDisplayTraits new];
+[BKSDisplayTraits _classesRequiredToDecode];
```

## Instance methods

```
-[BKSDisplayTraits mutableCopyWithZone:];
-[BKSDisplayTraits surfaceType];
-[BKSDisplayTraits initForProtobufDecoding];
-[BKSDisplayTraits init];
-[BKSDisplayTraits appendDescriptionToFormatter:];
-[BKSDisplayTraits encodeWithCoder:];
-[BKSDisplayTraits hash];
-[BKSDisplayTraits description];
-[BKSDisplayTraits initWithCoder:];
-[BKSDisplayTraits copyWithZone:];
-[BKSDisplayTraits isEqual:];
```
