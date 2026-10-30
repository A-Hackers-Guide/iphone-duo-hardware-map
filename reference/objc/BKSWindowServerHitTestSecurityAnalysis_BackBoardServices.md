# `BKSWindowServerHitTestSecurityAnalysis`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreamable`, `BSProtobufSerializable`, `NSCopying`, `NSMutableCopying`
- 7 instance variables, 11 properties, 15 instance methods, 4 class methods

## Instance variables

```
{CATransform3D="m11"d"m12"d"m13"d"m14"d"m21"d"m22"d"m23"d"m24"d"m31"d"m32"d"m33"d"m34"d"m41"d"m42"d"m43"d"m44"d} _cumulativeLayerTransform;
f _cumulativeOpacity;
B _hasInsecureFilter;
B _parentsHaveInsecureLayerProperties;
I _occlusionMask;
f _occlusionPercentage;
q _occlusionType;
```

## Properties

```
@property (T{CATransform3D=dddddddddddddddd},R,N) cumulativeLayerTransform;
@property (Tf,R,N) cumulativeOpacity;
@property (TB,R,N) hasInsecureFilter;
@property (TB,R,N) parentsHaveInsecureLayerProperties;
@property (TI,R,N) occlusionMask;
@property (Tf,R,N) occlusionPercentage;
@property (Tq,R,N) occlusionType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSWindowServerHitTestSecurityAnalysis build:];
+[BKSWindowServerHitTestSecurityAnalysis protobufSchema];
+[BKSWindowServerHitTestSecurityAnalysis new];
+[BKSWindowServerHitTestSecurityAnalysis securityAnalysisFromCAHitTestDictionary:errorString:];
```

## Instance methods

```
-[BKSWindowServerHitTestSecurityAnalysis mutableCopyWithZone:];
-[BKSWindowServerHitTestSecurityAnalysis initForProtobufDecoding];
-[BKSWindowServerHitTestSecurityAnalysis init];
-[BKSWindowServerHitTestSecurityAnalysis appendDescriptionToFormatter:];
-[BKSWindowServerHitTestSecurityAnalysis occlusionType];
-[BKSWindowServerHitTestSecurityAnalysis occlusionMask];
-[BKSWindowServerHitTestSecurityAnalysis cumulativeOpacity];
-[BKSWindowServerHitTestSecurityAnalysis hash];
-[BKSWindowServerHitTestSecurityAnalysis hasInsecureFilter];
-[BKSWindowServerHitTestSecurityAnalysis description];
-[BKSWindowServerHitTestSecurityAnalysis occlusionPercentage];
-[BKSWindowServerHitTestSecurityAnalysis parentsHaveInsecureLayerProperties];
-[BKSWindowServerHitTestSecurityAnalysis copyWithZone:];
-[BKSWindowServerHitTestSecurityAnalysis isEqual:];
-[BKSWindowServerHitTestSecurityAnalysis cumulativeLayerTransform];
```
