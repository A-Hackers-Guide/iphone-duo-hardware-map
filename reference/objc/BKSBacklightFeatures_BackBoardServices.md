# `BKSBacklightFeatures`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSProtobufSerializable`
- 3 instance variables, 7 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _disableFeatures;
f _fixedBrightnessNitsWhileDisabled;
f _fixedBrightnessLevelWhileDisabled;
```

## Properties

```
@property (TB,N,V_disableFeatures) disableFeatures;
@property (Tf,N,V_fixedBrightnessNitsWhileDisabled) fixedBrightnessNitsWhileDisabled;
@property (Tf,N,V_fixedBrightnessLevelWhileDisabled) fixedBrightnessLevelWhileDisabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSBacklightFeatures protobufSchema];
```

## Instance methods

```
-[BKSBacklightFeatures didFinishProtobufDecodingWithError:];
-[BKSBacklightFeatures succinctDescriptionBuilder];
-[BKSBacklightFeatures init];
-[BKSBacklightFeatures descriptionWithMultilinePrefix:];
-[BKSBacklightFeatures succinctDescription];
-[BKSBacklightFeatures description];
-[BKSBacklightFeatures descriptionBuilderWithMultilinePrefix:];
-[BKSBacklightFeatures disableFeatures];
-[BKSBacklightFeatures fixedBrightnessLevelWhileDisabled];
-[BKSBacklightFeatures fixedBrightnessNitsWhileDisabled];
-[BKSBacklightFeatures setDisableFeatures:];
-[BKSBacklightFeatures setFixedBrightnessLevelWhileDisabled:];
-[BKSBacklightFeatures setFixedBrightnessNitsWhileDisabled:];
```
